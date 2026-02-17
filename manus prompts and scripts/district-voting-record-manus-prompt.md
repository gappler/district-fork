# district-voting-record-prompt

---
version: 1.0
date: 2026-02-16
purpose: Produce a clean, verified voting record table for any U.S. House incumbent
tool: Manus AI 1.6 max + full_pipeline.py
---

## Naming Convention

**REQUIRED:** Before generating output, load and apply all conventions from `district-naming-prompt.md`. This file governs output filenames, H1 headers, and YAML metadata blocks.

Output filename pattern: `[district]-voting-record-[first-last].md` (markdown table) and `[district]-voting-record-[first-last].csv` (spreadsheet)

Example: `tx-34-voting-record-vicente-gonzalez.md`

---

## Input

- **District:** {DISTRICT_ID} (e.g., TX-34)
- **Incumbent name:** {CANDIDATE_NAME} (e.g., Vicente Gonzalez)
- **Party:** {PARTY} (Democrat or Republican — determines cross-party break logic)
- **Congress.gov member ID:** {MEMBER_ID} (e.g., G000581)
- **Congress.gov CSV:** Attached (downloaded in pre-flight)

---

## Pre-flight (manual, before running this prompt)

Complete these steps before starting. Attach the CSV where noted.

### 1. Download Congress.gov Roll Call CSV

1. Go to `https://www.congress.gov/member/{name}/{MEMBER_ID}`
2. Navigate to the House Roll Call Votes view. URL parameter: `?q={"sponsorship":"houseRollCallVoteFacet"}`
3. Apply filters:
   - **Congress:** Check 119 (2025-2026) and 118 (2023-2024)
   - **Bill Type:** Check ALL four types (Bills, Resolutions, Concurrent Resolutions, Joint Resolutions)
   - **All other filters:** Leave unselected/unfiltered
4. Click **Download Results** → **OK**
5. Save to: `~/early-returns/projects/{DISTRICT_ID}/data/congress-rollcall-{first-last}.csv`
6. Attach the CSV to this prompt

**Why these filters:**
- **All bill types:** Joint Resolutions include CRA rollback votes (substantive law). Resolutions include messaging votes that show positioning. Excluding any type loses data.
- **No subject filter:** Congress.gov CRS tags are too narrow. In testing, Congress.gov tagged 4 immigration votes for Gonzalez; VoteSmart tagged 62 for the same member. Topic analysis happens after download, not before.
- **No committee filter:** Would limit to votes on bills from specific committees, not all floor votes.
- **No status filter:** A vote on a bill that failed is equally revealing about positioning.
- **No member activity filter:** Checking Sponsored/Cosponsored switches to legislative activity. Leave unchecked to get votes.

### 2. (Optional) Download OpenSecrets Industry Data

For the donor overlay analysis, pull the member's top industries:
`https://www.opensecrets.org/members-of-congress/{name}/industries?cid={CID}&cycle=2024`

Note: OpenSecrets runs one cycle behind. 2024 cycle data is the most recent available as of February 2026. For incumbents, industry relationships are generally stable across cycles.

Save to: `~/early-returns/projects/{DISTRICT_ID}/data/opensecrets-industries-{first-last}.csv` (use the download CSV link on the page)

---

## Task

Run `full_pipeline.py` on the attached Congress.gov CSV to produce a verified voting record table. Then analyze the output for patterns relevant to the district article.

The pipeline script handles steps 1-4 automatically. Steps 5-6 require analytical judgment.

---

## Step 1: Run the Pipeline Script

1. Place the attached CSV in a known location
2. Update `CSV_PATH` in `full_pipeline.py` to point to the CSV
3. If the member is **Republican**, update the `is_cross_party` function to compare against Republican majority:
   ```python
   def is_cross_party(member_vote, r_yea, r_nay):
       if member_vote == 'Yea' and r_nay > r_yea:
           return 'Yes'
       elif member_vote == 'Nay' and r_yea > r_nay:
           return 'Yes'
       elif member_vote in ('Not Voting', 'Present'):
           return ''
       return 'No'
   ```
4. Update `SESSION_TO_YEAR` if sessions differ from default:
   ```python
   SESSION_TO_YEAR = {
       '119-2': '2026',
       '119-1': '2025',
       '118-2': '2024',
       '118-1': '2023',
   }
   ```
5. Run: `python3 full_pipeline.py`
6. Rename output files per naming convention

**Script location:** `full_pipeline.py` (in the project tools folder)

**Output:** Three files — markdown table, CSV, and JSON. The markdown and CSV contain: Date, Bill Number, Bill Title, Floor Action, Member Vote, Cross-Party Break (Yes/No), D (Yea-Nay), R (Yea-Nay).

---

## Step 2: Verify Output Quality

Before analysis, confirm:

- [ ] Total substantive votes is plausible (expect 300-500 per Congress for an active member)
- [ ] Missing bill numbers = 0 (Clerk XML should resolve all)
- [ ] Cross-party break count is plausible (varies widely — 5% for a safe-seat member, 20%+ for a Blue Dog or moderate Republican)
- [ ] Spot-check 3-5 rows: click the Congress.gov vote URL to confirm the bill number and member vote match

---

## Step 3: Aggregate Analysis

From the output table, calculate and report:

### Summary Statistics
```
Total substantive votes: [X]
Cross-party breaks: [X] ([X]%)

By Congress:
  119th: [X] votes, [X] breaks ([X]%)
  118th: [X] votes, [X] breaks ([X]%)

Break rate trend: [increasing / decreasing / stable] ([X]% → [X]%)
```

### Categorization by Theme

Using bill titles only (no AI-generated descriptions), group all cross-party breaks into thematic categories. Common categories include but are not limited to:

- Energy / Fossil Fuels / Climate
- Immigration / Border
- Social Issues (anti-trans, abortion, etc.)
- Law Enforcement / Crime
- Anti-China / Foreign Adversaries
- Deregulation / CRA Rollbacks
- Appropriations (Defense/DHS/Interior)
- Financial Services / Crypto
- Middle East / Anti-Iran
- DC Governance

Report each category with:
- Count of breaks
- Split by Congress (119th vs 118th)
- Count of solo/near-solo breaks (≤10 same-party crossovers)

### Lone Wolf Analysis

List all votes where ≤5 members of the incumbent's party crossed over. These are the most distinctive positions — where the member is genuinely out of step with their caucus, not joining a bipartisan crowd.

### Crowd Vote Identification

Flag cross-party breaks where 40+ same-party members crossed over. These are bipartisan votes where the member joined a large coalition. Still worth noting but less distinctive than lone wolf votes.

---

## Step 4: Donor Overlay (if OpenSecrets data available)

If the OpenSecrets industry CSV was downloaded in pre-flight, compare the top donor sectors against the thematic categories from Step 3.

Report:
- Top 5 donor industries with dollar amounts
- Top 3 donor sectors with dollar amounts and PAC vs. individual split
- Any alignment between high-donation sectors and high-break voting categories
- Note the cycle (OpenSecrets data is one cycle behind)

**Do not allege causation.** Report the alignment. The analysis is: here's where the money comes from, here's where the votes break. The reader draws conclusions.

---

## Step 5: Findings for Article

Identify 3-5 findings most relevant to the district article. Prioritize:

1. **The dominant break category** — what issue area has the most cross-party breaks? Is it what you'd expect from the district, or surprising?
2. **Break rate trend** — is the member becoming more or less independent of their party?
3. **Lone wolf positions** — what votes is this member nearly alone on?
4. **Money-vote connections** — does donor sector data align with voting breaks?
5. **What they DON'T break on** — if a member breaks on energy but not healthcare, that's a signal about priorities.

Format as a brief (under 500 words) summary of findings with specific data points. This is the handoff to the writer.

---

## Output Structure

### Document Header

H1 must match the output filename (without `.md`).

**Example H1:** `# tx-34-voting-record-vicente-gonzalez`

Include YAML metadata block immediately after H1:

```yaml
---
district: TX-34
type: voting-record
candidate: vicente_gonzalez
party: Democrat
date: 2026-02-16
prompt: district-voting-record-prompt.md
prompt_version: 1.0
source_csv: congress-rollcall-vicente-gonzalez.csv
congresses: 118, 119
---
```

| Field | Required | Notes |
|:------|:---------|:------|
| district | Yes | Standard code, uppercase (TX-34) |
| type | Yes | Always `voting-record` for this prompt |
| candidate | Yes | first_last format |
| party | Yes | Democrat or Republican |
| date | Yes | YYYY-MM-DD |
| prompt | Yes | Filename of prompt that created this |
| prompt_version | Yes | Version of prompt used |
| source_csv | Yes | Filename of Congress.gov CSV input |
| congresses | Yes | Which congresses are included |

### Document Body

1. Summary Statistics (from Step 3)
2. Categorization by Theme (from Step 3)
3. Lone Wolf Votes table (from Step 3)
4. Donor Overlay (from Step 4, if available)
5. Findings for Article (from Step 5)
6. Full Voting Record Table — 119th Congress (from pipeline output)
7. Full Voting Record Table — 118th Congress (from pipeline output)

### Sources

```
## Sources
- Congress.gov Roll Call Votes: https://www.congress.gov/member/{name}/{MEMBER_ID}
- House Clerk XML: https://clerk.house.gov/evs/{year}/roll{nnn}.xml
- OpenSecrets Industries: https://www.opensecrets.org/members-of-congress/{name}/industries?cid={CID}&cycle=2024
```

---

## Rules

1. Use ONLY data from the Congress.gov CSV and House Clerk XML for voting record data. Do not supplement with VoteSmart, GovTrack, or other sources.
2. Do not generate descriptions of what bills do. Report bill titles from the Clerk XML only. The writer researches individual bills as needed.
3. Cross-party break is defined mechanically: member voted opposite to the majority of their party. No editorial judgment about whether a vote "counts."
4. Report all break rates as percentages rounded to nearest whole number.
5. When categorizing by theme, use bill titles only. If a title is ambiguous, place it in "Other" — do not guess.
6. The "Providing for consideration of..." resolutions are procedural rules votes that passed the substantive filter. Note their presence but do not count them as thematic breaks. They are almost always party-line.
7. A "Yea" on a motion to table means the opposite of a "Yea" on passage. The pipeline filters these out, but if encountered in manual verification, be aware.
8. Do not editorialize or interpret findings beyond what the data shows. Report patterns. The writer decides what matters.
9. Record every URL visited in the Sources section.

---

## Known Limitations

- **Clerk XML `vote-desc` is a short title, not a summary.** "Laken Riley Act" doesn't explain what the act does. The writer looks up individual bills as needed.
- **CRS subject tags are too narrow for topic filtering.** Do not filter by Subject/Policy Area on Congress.gov before download.
- **OpenSecrets data runs one cycle behind.** 2024 cycle is the most recent as of February 2026.
- **Resolution numbers reset each Congress.** Always include the Congress number when citing (e.g., "H.Res.939, 119th Congress").
- **The pipeline is House-only.** Senate roll calls use a different system.
- **"On Agreeing to Resolution" includes procedural rules resolutions** (titles starting with "Providing for consideration of..."). These are nearly always party-line and should be noted but not weighted in thematic analysis.

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-16 | Initial version. Developed from TX-34 (Gonzalez) analysis. Pipeline: Congress.gov CSV → full_pipeline.py → House Clerk XML → verified table with cross-party breaks. |
