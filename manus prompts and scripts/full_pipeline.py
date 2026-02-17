#!/usr/bin/env python3
"""
Full pipeline:
1. Read Congress.gov CSV
2. Filter to substantive floor actions
3. Parse party breakdowns and flag cross-party breaks
4. Fetch House Clerk XML for bill numbers and titles
5. Output final table as markdown and CSV
"""

import csv
import json
import re
import time
import xml.etree.ElementTree as ET
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

CSV_PATH = '/home/ubuntu/upload/search_results_2026-02-16_0524pm.csv'

# Substantive floor action keywords
SUBSTANTIVE_ACTIONS = [
    'On passage',
    'On agreeing to the resolution',
    'On motion to suspend the rules and pass',
]

# Map congress-session to year for Clerk URLs
SESSION_TO_YEAR = {
    '119-2': '2026',
    '119-1': '2025',
    '118-2': '2024',
    '118-1': '2023',
}

def read_csv():
    """Read the Congress.gov CSV, skipping header rows."""
    rows = []
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        # Skip the first two metadata rows
        next(reader)  # "Downloaded on" row
        next(reader)  # "Search URL" row
        # Third row is the header
        header = next(reader)
        for row in reader:
            if len(row) >= 7:
                rows.append({
                    'url': row[0],
                    'roll_call': row[1],
                    'date': row[2],
                    'description': row[3],
                    'result': row[4],
                    'congress': row[5],
                    'member_vote': row[6],
                })
    return rows

def is_substantive(description):
    """Check if the vote is a substantive floor action."""
    for action in SUBSTANTIVE_ACTIONS:
        if action.lower() in description.lower():
            return True
    return False

def get_floor_action(description):
    """Extract the floor action type."""
    desc_lower = description.lower()
    if 'on passage' in desc_lower:
        return 'On Passage'
    elif 'on agreeing to the resolution' in desc_lower:
        return 'On Agreeing to Resolution'
    elif 'on motion to suspend the rules and pass' in desc_lower:
        return 'Suspension Vote'
    return 'Other'

def parse_party_breakdown(result_text):
    """Extract D and R vote breakdowns."""
    d_match = re.search(r'D\s+(\d+)-(\d+)', result_text)
    r_match = re.search(r'R\s+(\d+)-(\d+)', result_text)
    d_yea = int(d_match.group(1)) if d_match else 0
    d_nay = int(d_match.group(2)) if d_match else 0
    r_yea = int(r_match.group(1)) if r_match else 0
    r_nay = int(r_match.group(2)) if r_match else 0
    return d_yea, d_nay, r_yea, r_nay

def is_cross_party(member_vote, d_yea, d_nay):
    """Check if the member broke from the Democratic majority."""
    if member_vote == 'Yea' and d_nay > d_yea:
        return 'Yes'
    elif member_vote == 'Nay' and d_yea > d_nay:
        return 'Yes'
    elif member_vote in ('Not Voting', 'Present'):
        return ''
    return 'No'

def parse_congress_url(url):
    """Extract congress-session and roll call number from URL."""
    match = re.search(r'/votes/house/(\d+-\d+)/(\d+)', url)
    if match:
        return match.group(1), int(match.group(2))
    return None, None

def build_clerk_url(session, roll_num):
    """Build the House Clerk XML URL."""
    year = SESSION_TO_YEAR.get(session)
    if not year:
        return None
    return f"https://clerk.house.gov/evs/{year}/roll{roll_num:03d}.xml"

def fetch_clerk_data(clerk_url, congress_url):
    """Fetch and parse the Clerk XML."""
    result = {
        'congress_url': congress_url,
        'legis_num': '',
        'vote_question': '',
        'vote_desc': '',
        'action_date': '',
        'error': ''
    }
    try:
        resp = requests.get(clerk_url, timeout=15)
        if resp.status_code != 200:
            result['error'] = f"HTTP {resp.status_code}"
            return result
        root = ET.fromstring(resp.content)
        
        for tag, key in [('legis-num', 'legis_num'), ('vote-question', 'vote_question'),
                         ('vote-desc', 'vote_desc'), ('action-date', 'action_date')]:
            elem = root.find(f'.//{tag}')
            if elem is not None and elem.text:
                result[key] = elem.text.strip()
    except Exception as e:
        result['error'] = str(e)
    return result

def normalize_bill_number(legis_num):
    """Convert Clerk format 'H R 2189' to standard 'H.R. 2189'."""
    if not legis_num:
        return ''
    s = legis_num.strip()
    # Common patterns from Clerk XML
    replacements = [
        (r'^H R\s+', 'H.R. '),
        (r'^S\s+', 'S. '),
        (r'^H RES\s+', 'H.Res. '),
        (r'^S RES\s+', 'S.Res. '),
        (r'^H J RES\s+', 'H.J.Res. '),
        (r'^S J RES\s+', 'S.J.Res. '),
        (r'^H CON RES\s+', 'H.Con.Res. '),
        (r'^S CON RES\s+', 'S.Con.Res. '),
    ]
    for pattern, repl in replacements:
        s, count = re.subn(pattern, repl, s, flags=re.IGNORECASE)
        if count:
            return s
    return s

def main():
    # Step 1: Read CSV
    print("Reading CSV...")
    all_votes = read_csv()
    print(f"  Total rows: {len(all_votes)}")
    
    # Step 2: Filter to substantive actions
    print("Filtering to substantive floor actions...")
    filtered = [v for v in all_votes if is_substantive(v['description'])]
    print(f"  Substantive votes: {len(filtered)}")
    
    # Step 3: Parse party breakdowns and flag cross-party breaks
    print("Parsing party breakdowns...")
    for v in filtered:
        d_yea, d_nay, r_yea, r_nay = parse_party_breakdown(v['result'])
        v['d_yea_nay'] = f"{d_yea}-{d_nay}"
        v['r_yea_nay'] = f"{r_yea}-{r_nay}"
        v['floor_action'] = get_floor_action(v['description'])
        v['cross_party_break'] = is_cross_party(v['member_vote'], d_yea, d_nay)
    
    cross_party_count = sum(1 for v in filtered if v['cross_party_break'] == 'Yes')
    print(f"  Cross-party breaks: {cross_party_count}")
    
    # Step 4: Build Clerk URLs and fetch
    print("Building Clerk URLs...")
    tasks = []
    for v in filtered:
        session, roll_num = parse_congress_url(v['url'])
        if session and roll_num:
            clerk_url = build_clerk_url(session, roll_num)
            if clerk_url:
                tasks.append((clerk_url, v['url']))
    
    print(f"  Clerk URLs to fetch: {len(tasks)}")
    print("Fetching House Clerk XML (10 concurrent)...")
    
    clerk_results = {}
    success = 0
    errors = 0
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_clerk_data, cu, cong_u): cong_u 
                   for cu, cong_u in tasks}
        for i, future in enumerate(as_completed(futures)):
            result = future.result()
            clerk_results[result['congress_url']] = result
            if result['error']:
                errors += 1
            else:
                success += 1
            if (i + 1) % 100 == 0:
                print(f"    Processed {i+1}/{len(tasks)} (success: {success}, errors: {errors})")
    
    print(f"  Done! Success: {success}, Errors: {errors}")
    
    has_bill = sum(1 for r in clerk_results.values() if r['legis_num'])
    has_desc = sum(1 for r in clerk_results.values() if r['vote_desc'])
    print(f"  Have bill number: {has_bill}, Have vote description: {has_desc}")
    
    # Step 5: Merge clerk data into filtered votes
    print("Merging clerk data...")
    for v in filtered:
        clerk = clerk_results.get(v['url'], {})
        v['bill_number'] = normalize_bill_number(clerk.get('legis_num', ''))
        v['bill_title'] = clerk.get('vote_desc', '')
        v['clerk_action_date'] = clerk.get('action_date', '')
        v['clerk_vote_question'] = clerk.get('vote_question', '')
    
    # Sort by date (newest first)
    filtered.sort(key=lambda x: x['date'], reverse=True)
    
    # Stats
    total = len(filtered)
    missing_bill = sum(1 for v in filtered if not v['bill_number'])
    cross_party_missing = sum(1 for v in filtered if v['cross_party_break'] == 'Yes' and not v['bill_number'])
    
    is_119 = lambda v: '119' in v['congress']
    is_118 = lambda v: '118' in v['congress']
    c119_total = sum(1 for v in filtered if is_119(v))
    c119_cross = sum(1 for v in filtered if is_119(v) and v['cross_party_break'] == 'Yes')
    c118_total = sum(1 for v in filtered if is_118(v))
    c118_cross = sum(1 for v in filtered if is_118(v) and v['cross_party_break'] == 'Yes')
    
    print(f"\n=== FINAL STATS ===")
    print(f"Total substantive votes: {total}")
    print(f"Cross-party breaks: {cross_party_count} ({cross_party_count*100//total}%)")
    print(f"119th: {c119_total} votes, {c119_cross} cross-party")
    print(f"118th: {c118_total} votes, {c118_cross} cross-party")
    print(f"Missing bill numbers: {missing_bill} (of which {cross_party_missing} are cross-party)")
    
    # Step 6: Write markdown table
    print("\nWriting markdown table...")
    with open('/home/ubuntu/gonzalez_voting_record_table.md', 'w') as f:
        f.write("# Vicente Gonzalez (TX-34) — Substantive Voting Record\n\n")
        f.write("**Source:** Congress.gov House Roll Call Votes + House Clerk XML, 118th & 119th Congress\n\n")
        f.write(f"**Total substantive votes:** {total} | **Cross-party breaks:** {cross_party_count} ({cross_party_count*100//total}%)\n\n")
        f.write("**Filter:** On Passage, On Agreeing to Resolution, and Suspension Votes only (procedural votes excluded)\n\n")
        f.write("**Cross-Party Break** = Gonzalez voted opposite to the majority of House Democrats\n\n")
        f.write("---\n\n")
        
        # 119th Congress
        f.write(f"## 119th Congress (2025-2026) — {c119_total} votes, {c119_cross} cross-party breaks\n\n")
        f.write("| Date | Bill | Title | Floor Action | Vote | Cross-Party | D (Y-N) | R (Y-N) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: |\n")
        for v in filtered:
            if is_119(v):
                title = (v['bill_title'][:80] + '...') if len(v['bill_title']) > 80 else v['bill_title']
                title = title.replace('|', '\\|')
                bill = v['bill_number'].replace('|', '\\|') if v['bill_number'] else '—'
                f.write(f"| {v['date']} | {bill} | {title} | {v['floor_action']} | {v['member_vote']} | {v['cross_party_break']} | {v['d_yea_nay']} | {v['r_yea_nay']} |\n")
        
        f.write("\n---\n\n")
        
        # 118th Congress
        f.write(f"## 118th Congress (2023-2024) — {c118_total} votes, {c118_cross} cross-party breaks\n\n")
        f.write("| Date | Bill | Title | Floor Action | Vote | Cross-Party | D (Y-N) | R (Y-N) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: |\n")
        for v in filtered:
            if is_118(v):
                title = (v['bill_title'][:80] + '...') if len(v['bill_title']) > 80 else v['bill_title']
                title = title.replace('|', '\\|')
                bill = v['bill_number'].replace('|', '\\|') if v['bill_number'] else '—'
                f.write(f"| {v['date']} | {bill} | {title} | {v['floor_action']} | {v['member_vote']} | {v['cross_party_break']} | {v['d_yea_nay']} | {v['r_yea_nay']} |\n")
    
    print("  Written to gonzalez_voting_record_table.md")
    
    # Step 7: Write CSV
    with open('/home/ubuntu/gonzalez_voting_record_table.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Congress', 'Bill Number', 'Bill Title', 'Floor Action', 
                         'Gonzalez Vote', 'Cross-Party Break', 'D (Yea-Nay)', 'R (Yea-Nay)', 'Vote URL'])
        for v in filtered:
            writer.writerow([v['date'], v['congress'], v['bill_number'], v['bill_title'],
                            v['floor_action'], v['member_vote'], v['cross_party_break'],
                            v['d_yea_nay'], v['r_yea_nay'], v['url']])
    
    print("  Written to gonzalez_voting_record_table.csv")
    
    # Save filtered JSON for reference
    with open('/home/ubuntu/gonzalez_filtered.json', 'w') as f:
        json.dump(filtered, f, indent=2)
    print("  Written to gonzalez_filtered.json")

if __name__ == '__main__':
    main()
