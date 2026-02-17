# Voting Record Pipeline

A repeatable process for downloading, parsing, and analyzing voting records for U.S. House members. Developed for TX-34 (Vicente Gonzalez) analysis in February 2026.

## Overview

The pipeline produces a clean, substantive voting record (bill numbers, titles, floor actions, cross-party breaks) from Congress.gov data. The output is a markdown table and CSV suitable for pattern analysis without requiring bill text review for every vote.

## Pipeline Steps

### Step 1: Download from Congress.gov

1. Navigate to the member's page: `congress.gov/member/[first-name]-[last-name]/[ID]`
   - Example: `congress.gov/member/vicente-gonzalez/G000581`

2. Click the "House Roll Call Votes" tab or add `?q={"sponsorship":"houseRollCallVoteFacet"}` to the URL.

3. Apply filters:
   - **Congress:** Select the current Congress and prior Congress (e.g., 118th + 119th)
   - **Bill Type:** Check ALL boxes—Bills, Resolutions, Concurrent Resolutions, Joint Resolutions
     - Joint Resolutions capture CRA rollback votes, which are substantive law
     - Resolutions include messaging votes that show positioning
   - **Status of Legislation:** Leave unfiltered
   - **Subject/Policy Area:** Leave unfiltered
     - Congress.gov's CRS tags are too narrow (e.g., only 4 immigration votes for Gonzalez vs. VoteSmart's 62)
     - Topic grouping is better done post-download using bill titles
   - **Committee:** Leave unfiltered
   - **Chamber of Origin:** Leave unfiltered
   - **Member Activity:** Do NOT check Sponsored/Cosponsored
     - Checking these switches to legislative activity, not voting records

4. Click "Download Results" to get the CSV.

**CSV Contents:** URL, Roll Call Vote Number, Date Voted, Description (procedural summary only), Roll Call Result (party breakdown), Congress, Member Vote.

### Step 2: Run full_pipeline.py

The script performs four operations:

**1. Filter to Substantive Floor Actions**

Keeps only:
- "On Passage" votes
- "On Agreeing to Resolution" votes
- "Suspension Votes"

Removes procedural votes:
- Motions to recommit
- Motions to table
- Ordering the previous question
- Other procedural roll calls

Procedural votes are typically party-line whip votes and add noise to break analysis.

**2. Parse Party Breakdowns**

Extracts Democratic and Republican vote totals from the Result field using regex.

Example format in CSV: `R 211-1 Pres=0 NV=5, D 22-184 Pres=0 NV=8`

Output: Separate columns for D (Yea-Nay) and R (Yea-Nay).

**3. Flag Cross-Party Breaks**

Compares the member's vote to the Democratic (or Republican) majority:
- If the member voted Yea and more of their party voted Nay → flagged as break
- If the member voted Nay and more of their party voted Yea → flagged as break
- "Not Voting" and "Present" votes are unflagged

**4. Fetch Bill Numbers and Titles from House Clerk XML**

Congress.gov CSV descriptions are procedural ("On passage Passed by the Yeas and Nays: 233-185"); they don't identify the bill.

The House Clerk publishes XML for every roll call at:
```
https://clerk.house.gov/evs/{year}/roll{number padded to 3 digits}.xml
```

The script fetches and extracts:
- `legis-num` (bill number, e.g., H.R. 1234)
- `vote-desc` (bill title)
- `vote-question` (floor action type)
- `action-date` (vote date)

Requests are made in parallel (10 concurrent) to minimize runtime.

**Inputs:** Congress.gov CSV
**Outputs:**
- Markdown table: `[member]_voting_record_table.md`
- CSV: `[member]_voting_record_table.csv`

**Table Columns:** Date, Bill Number, Bill Title, Floor Action, Member Vote, Cross-Party Break, D (Yea-Nay), R (Yea-Nay)

**To run for a different member:** Change the CSV_PATH variable in the script. The pipeline is member-agnostic.

### Step 3: Pattern Analysis

The output table supports quantitative analysis without additional data:

**Cross-party break rate**
- Count breaks as a percentage of total substantive votes
- Compare rates across Congresses to identify trends toward independence or party alignment
- Example: Vicente Gonzalez, 14% breaks in 118th Congress → 23% in 119th Congress

**Categorize breaks by bill title**
- Group breaks by subject area (energy, healthcare, immigration, defense, etc.)
- Look for clusters in the member's break patterns
- Identify which issue areas diverge from party positions

**Lone wolf vs. crowd breaks**
- Use the D (Yea-Nay) column to check how many Democrats crossed over on each break
- A break where 3 Democrats crossed signals an outlier position
- A break where 80 Democrats crossed signals a broader coalition
- Filter to ≤5 or ≤10 Democratic crossovers for the member's most distinctive votes

**Absences in break patterns**
- Which issue areas show NO breaks?
- A member who breaks on energy but never on healthcare reveals priorities

### Step 4: Selective Deep Dive

For 5-10 votes that anchor the story:

1. **Verify the floor action** — Click the vote URL on Congress.gov
   - A "Yea" on a motion to table kills the bill (opposite polarity of "Yea" on passage)
   - The pipeline removes motions to table, but verify for high-stakes votes

2. **Read the bill text or summary** if the title is ambiguous
   - Congress.gov bill pages: `congress.gov/bill/[congress]/[bill-type]/[number]`
   - House Clerk provides titles; bill text requires additional lookup

3. **Cross-reference with OpenSecrets** by donor industry
   - See Step 5 below

### Step 5: OpenSecrets Donor Overlay

Pull the member's top donor industries and sector totals:
```
opensecrets.org/members-of-congress/[name]/industries?cid=[ID]&cycle=2024
```

Compare to voting break categories:
- Does the member break on votes affecting major donor industries?
- Check the PAC vs. individual split
  - High PAC percentage: industry investment
  - High individual percentage: grassroots support

## Known Limitations

**Congress.gov CSV descriptions are procedural, not substantive**
- "On passage Passed by the Yeas and Nays: 233-185" does not identify the bill
- The pipeline solves this by fetching bill numbers from House Clerk XML

**CRS subject tags are too narrow for filtering**
- Don't filter by Subject/Policy Area on Congress.gov
- Do topic analysis post-download using bill titles

**Motions to table reverse vote polarity**
- A "Yea" on a motion to table kills the bill
- The pipeline filters these out; verify them in manual research

**Resolution numbers reset each Congress**
- H.Res.939 in the 119th ≠ H.Res.939 in any other Congress
- Always include the Congress number when citing

**VoteSmart issue categories are broader than CRS**
- VoteSmart tagged 62 immigration votes for Gonzalez vs. Congress.gov's 4
- VoteSmart is useful for issue-specific deep dives but requires manual web pulls
- (API appears to be shut down)

**House members only**
- Senate roll calls use a different voting system

## Requirements

- Python 3
- `requests` library

## Files

- `full_pipeline.py` — The pipeline script
- Input: Congress.gov member roll call CSV
- Output: `[member]_voting_record_table.md` and `[member]_voting_record_table.csv`

## First Developed

TX-34 (Vicente Gonzalez), February 2026.
Tested on 1,673 roll call votes → 723 substantive votes with 0 missing bill numbers.
