# district-baseline-prompt

---
version: 3.3
date: 2026-02-12
purpose: Build structural foundation for Early Returns district articles
tool: Manus AI 1.6 max
replaces: district-baseline-prompt v3.2
---

## Naming Convention

**REQUIRED:** Before generating output, load and apply all conventions from `district-naming-prompt.md`. This file governs output filenames, H1 headers, and YAML metadata blocks.

Output filename pattern: `[district]-baseline.md`

Example: `tx-34-baseline.md`

---

## Input

- **District:** {DISTRICT_ID} (e.g., TX-28, WA-03, OH-09)
- **State:** {STATE} (e.g., Texas, Washington, Ohio)

---

## Pre-flight (manual, before running this prompt)

Complete these steps before starting. Attach the files where noted.

1. **Census CSV:** Download from https://www.census.gov/mycd/application/?st={STATE_FIPS}&cd={DISTRICT_NUMBER} — Click the download/export button. Attach the CSV to this prompt.
2. **Downballot presidential results CSV:** From your data folder (one-time download from https://docs.google.com/spreadsheets/d/1ng1i_Dm_RMDnEvauH44pgE6JCUsapcuu8F2pCfeLWFo — export "Percentages" tab as CSV). Attach to this prompt.
3. **Kondik crossover CSV (if redistricted):** From your data folder (`data/reference/kondik-crossover-presidential-2026-lines.csv`). Attach to this prompt ONLY if the district is in a state that redistricted for 2026 (California, Missouri, North Carolina, Ohio, Texas, Utah). If the district is not in a redistricted state, skip this attachment.
4. **Ratings:** Look up {DISTRICT_ID} at each source and note the values below.
   - Cook PVI: {COOK_PVI} — https://www.cookpolitical.com/ratings/house-race-ratings (requires login)
   - Cook rating: {COOK_RATING} — same page
   - Sabato: {SABATO_RATING} — https://centerforpolitics.org/crystalball/2026-house/
   - Inside Elections: {IE_RATING} — https://insideelections.com/ratings/house
5. **FEC Candidate Totals (QA):** Download from https://www.fec.gov/data/candidates/house/?election_year=2026&election_full=True&state={STATE_ABBREV}&district={DISTRICT_NUMBER}&is_active_candidate=true — Export CSV. Use to verify Manus output for Section 2.
6. **FEC Independent Expenditures — 2024 cycle (QA):** Download from https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2024&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER} — Export CSV. Use to verify Manus output for Section 3.
7. **FEC Independent Expenditures — 2026 cycle (QA):** Download from https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2026&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER} — Export CSV. Use to verify Manus output for Section 3.

---

## Task

Build the structural foundation for an Early Returns district article. Collect fixed data about the district and the current race from specified sources. Follow the sections below IN ORDER. Use ONLY the sources specified in each section. If a data point is not available from the specified source, flag it under "Manual Input Needed" at the end — do not guess or search elsewhere.

**Source URL tracking:** In every section, record the exact URL(s) you visited. These will be collected in a Sources appendix for citation use.

---

## Section 1: Redistricting Status

**Source:** Ballotpedia redistricting tracker
**URL:** https://ballotpedia.org/Redistricting_ahead_of_the_2026_elections

Go to the URL above. Is {STATE} listed as having new congressional maps or pending redistricting activity?

- If NO → write "No change — same lines as 2022." Skip to Section 2.
- If YES → click through to the {STATE}-specific redistricting page. Find any information specific to {DISTRICT_ID}. Extract:
  - Geographic changes (counties/areas added or removed)
  - Partisan impact described by Ballotpedia or its cited sources
  - Litigation status (is the new map in effect, stayed, or under challenge?)
  - Which map will be used for the 2026 elections

Then search for: "{DISTRICT_ID} redistricting 2025" and find ONE article from a state-level news outlet (prefer state tribunes, States Newsroom affiliates, AP, local papers of record). Extract source name, date, URL, and 2-3 sentences about what changed for this district.

**Do not search further. One article is sufficient.**

**Output:**
```
### Redistricting Status
- Status: [No change / Redrawn]
- Map in effect for 2026: [Specify which map]
- What changed: [2-3 sentences from Ballotpedia]
- Confirming source: [Name, date, URL, 2-3 sentence summary]
- Litigation: [Current status]
- URLs visited: [list all URLs accessed for this section]
```

---

## Section 2: Candidates & Fundraising

**Source:** FEC candidate search
**URL:** https://www.fec.gov/data/candidates/?office=H&state={STATE_ABBREV}&district={DISTRICT_NUMBER}&election_year=2026

Go to the URL above (substitute the correct two-letter state abbreviation and two-digit district number, e.g., state=TX&district=34). List all candidates who have filed for this race.

The search results page displays candidate name, party, status, and summary fundraising data (total raised, total spent, cash on hand). Record all of this from the results page. Do not click through to individual candidate pages.

**Output:**
```
### Candidates & Fundraising (FEC)
| Candidate | Party | Status | Total Raised | Total Spent | Cash on Hand | FEC ID |
|:----------|:------|:-------|:-------------|:------------|:-------------|:-------|
| | | | | | | |

Coverage period: [through date shown on page]
URLs visited: [list all URLs accessed for this section]
```

---

## Section 3: Independent Expenditures (Prior Cycle)

**Source:** FEC independent expenditures
**URL:** https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2024&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER}

Go to the URL above. This returns all independent expenditures for this district in the 2024 cycle, filtered to current (non-superseded) filings only.

**Critical:** Use this exact URL. The `most_recent=true` parameter filters out amended filings. If you use the FEC API or construct a different query, you will double-count amended filings and inflate the totals.

Record:
- Total IE spending in the district (all spenders, all candidates)
- Top 3 spenders by amount
- Spending broken down by: support/oppose for each candidate

Note: The same candidate may appear under slightly different name variants (e.g., "FLORES, MAYRA" and "FLORES, MAYRA NOHEMI"). Consolidate these into one candidate total.

**Output:**
```
### Independent Expenditures — 2024 Cycle
- Total outside spending: $[X]
- Breakdown:
  - Supporting [Candidate A]: $[X] (top spenders: [list])
  - Opposing [Candidate A]: $[X] (top spenders: [list])
  - Supporting [Candidate B]: $[X] (top spenders: [list])
  - Opposing [Candidate B]: $[X] (top spenders: [list])
- Note: [any data quality flags]
- URLs visited: [list all URLs accessed for this section]
```

**Also check current cycle (2025-2026).** If any IE spending has been reported for the 2026 cycle, note it. If none, write "No 2026 cycle IE spending reported as of [date]."

---

## Section 4: Electoral History

**Source:** Ballotpedia district page
**URL:** https://ballotpedia.org/{STATE}'s_{DISTRICT_NUMBER}th_Congressional_District

Go to the Ballotpedia page for this district. Find the election results section. Record results for the last three cycles (2024, 2022, 2020). For each cycle:
- All candidates, their party, vote total, and percentage
- Margin of victory
- Whether the race was a general election, top-two general, or runoff

Also record:
- Primary results for the most recent cycle (2024) if available
- Any special elections in this district in the last three cycles

**Output:**
```
### Electoral History (Ballotpedia)

**2024 General:**
| Candidate | Party | Votes | % | Margin |
|:----------|:------|:------|:--|:-------|
| | | | | |

**2022 General:**
| Candidate | Party | Votes | % | Margin |
|:----------|:------|:------|:--|:-------|
| | | | | |

**2020 General:**
| Candidate | Party | Votes | % | Margin |
|:----------|:------|:------|:--|:-------|
| | | | | |

**2024 Primary (if available):**
[Results or "Not available on Ballotpedia"]

**Special elections:** [None / Details]

URLs visited: [list all URLs accessed for this section]
```

---

## Section 5: Presidential Performance

**Source:** Attached CSV files — use the three-tier logic below.

### Three-Tier Presidential Data Logic

**Tier 1 — No redistricting:** If Section 1 found "No change — same lines as 2022," use the attached Downballot presidential results CSV. Find the row where the District column = {DISTRICT_ID}.

**Tier 2 — Redistricted, Kondik data available:** If Section 1 found the district was redrawn AND the attached Kondik crossover CSV contains a row for {DISTRICT_ID}, use the Kondik CSV for the 2026-lines numbers. Also report the old-lines numbers from the Downballot CSV for comparison.

**Tier 3 — Redistricted, no Kondik data:** If Section 1 found the district was redrawn BUT the Kondik CSV does not contain {DISTRICT_ID} (or was not attached), use the Downballot CSV and flag that these numbers reflect OLD district boundaries. Add to "Manual Input Needed" that new-lines presidential numbers require manual lookup on Dave's Redistricting App.

### Extract (all tiers):
- 2024: Harris %, Trump %, Margin
- 2020: Biden %, Trump %, Margin (Downballot CSV only — Kondik does not include 2020)
- Calculate the swing (change in margin from 2020 to 2024)

### Additional for Tier 2:
- Report both old-lines and new-lines 2024 numbers
- Calculate the redistricting shift (difference between old and new margin)

**Output:**
```
### Presidential Performance
- Data tier: [1 — unchanged lines / 2 — redistricted, Kondik data / 3 — redistricted, old lines only]

**2024 (new lines):** Harris [X]% — Trump [X]% (Margin: [D/R]+[X])  [Tier 2 only]
**2024 (old lines):** Harris [X]% — Trump [X]% (Margin: [D/R]+[X])
**2020 (old lines):** Biden [X]% — Trump [X]% (Margin: [D/R]+[X])
- Swing (2020→2024, old lines): [X] points toward [Democrats/Republicans]
- Redistricting shift: [X] points toward [Democrats/Republicans]  [Tier 2 only]

Sources:
- Old lines: The Downballot (Singer, Donner, Nir), 2025
- New lines: Sabato's Crystal Ball (Kondik), Feb 5 2026 — via Dave's Redistricting App  [Tier 2 only]
- ⚠️ Numbers reflect old district boundaries — new-lines data not available. Manual DRA lookup needed.  [Tier 3 only]
```

---

## Section 6: Demographics

**Source:** Attached Census CSV file (downloaded from My Congressional District tool in pre-flight step)

Extract the following from the attached CSV. The CSV has columns: Topic, Subject, Title, District Estimate, District MOE.

- **Total population:** Row where Subject = "Sex and Age" and Title = "Total population"
- **Median household income:** Row where Subject = "Income and Benefits" and Title contains "Median household income" — round to nearest $1,000
- **White (non-Hispanic):** Row where Subject = "Hispanic or Latino and Race" and Title = "Not Hispanic or Latino" — calculate as percentage of total population, one decimal
- **Hispanic or Latino:** Row where Subject = "Hispanic or Latino and Race" and Title = "Hispanic or Latino (of any race)" — calculate as percentage of total population, one decimal
- **BA+:** Row where Subject = "Educational Attainment" and Title = "Percent bachelor's degree or higher"
- **Veterans:** Row where Subject = "Veteran Status" and Title = "Civilian veterans" — calculate as percentage of "Civilian population 18 years and over" (same section), one decimal
- **Owner-occupied housing:** Row where Subject = "Housing Tenure" and Title = "Owner-occupied" — calculate as percentage of "Occupied housing units" (same section), round to nearest whole number
- **Key employment sectors:** From the Business section, rows under "Paid employees for pay period including March 12" — list the top 3 sectors by employee count (exclude "Total for all sectors")
- **Median home value:** Row where Subject = "Value" and Title = "Median (dollars)"
- **Poverty rate:** Row where Subject contains "Poverty" and Title = "All people"

**Output:**
```
### Demographics (Census — My Congressional District)
- Population: [X]
- Median household income: $[X]K
- Hispanic or Latino: [X]%
- White (non-Hispanic): [X]%
- BA+: [X]%
- Veterans: [X]%
- Owner-occupied housing: [X]%
- Key employment sectors: [1st, 2nd, 3rd by employee count]
- Median home value: $[X]
- Poverty rate: [X]%
- Source: [Year] American Community Survey, Census My Congressional District
- Source URL: https://www.census.gov/mycd/application/?st={STATE_FIPS}&cd={DISTRICT_NUMBER}
```

---

## Section 7: District Geography

**Source:** Ballotpedia district page (same URL as Section 4)

Record:
- Counties fully or partially in the district
- Largest city
- Any notable geographic features (border area, coastal, metro spillover, rural)
- Primary type (open primary, top-two, partisan primary)
- Primary date for 2026
- Filing deadline for 2026

**Output:**
```
### Geography & Election Info
- Counties: [list]
- Largest city: [X]
- Character: [brief description — e.g., "Portland metro spillover + rural timber counties"]
- Primary type: [open / top-two / partisan]
- Primary date: [date]
- Filing deadline: [date]
- URLs visited: [list all URLs accessed for this section]
```

---

## Section 8: Ratings

**All ratings are provided in the pre-flight input.** Include them in the output exactly as given.

**Output:**
```
### Ratings
- Cook PVI: {COOK_PVI}
- Cook rating: {COOK_RATING}
- Sabato: {SABATO_RATING}
- Inside Elections: {IE_RATING}
- Source URLs:
  - https://www.cookpolitical.com/ratings/house-race-ratings
  - https://centerforpolitics.org/crystalball/2026-house/
  - https://insideelections.com/ratings/house
```

---

## Section 9: Polling

**Source:** Search for "{DISTRICT_ID} poll 2026" on the web.

Check if any public polls exist for this district. Credible polling sources include university polls, partisan pollsters with disclosed methodology, and nonpartisan firms.

If no polls are found, write "No public polling available."

**Note:** The FiveThirtyEight polling database (projects.fivethirtyeight.com) now redirects to ABC News and may not be functional. Do not rely on it.

**Output:**
```
### Polling
[Pollster, date, sample size, result] or "No public polling available"
URLs visited: [list all URLs accessed for this section]
```

---

## Final Output: Assemble Baseline

Combine all sections above into a single document.

### Document Header

The document's **H1 must match the output filename** (without the `.md` extension).

**Example H1:** `# tx-34-baseline`

Include YAML metadata block immediately after the H1:

```yaml
---
district: TX-34
type: baseline
date: 2026-02-11
prompt: district-baseline-prompt.md
prompt_version: 3.3
---
```

Note: The `district:` field uses conventional uppercase (`TX-34`) for interoperability with external sources. The H1 and filename are all lowercase with hyphens.

| Field | Required | Notes |
|:------|:---------|:------|
| district | Yes | Standard code, uppercase (TX-28, NC-01) |
| type | Yes | Always `baseline` for this prompt |
| date | Yes | YYYY-MM-DD |
| prompt | Yes | Filename of prompt that created this |
| prompt_version | Yes | Version of prompt that created this |

### Manual Input Needed

At the end of the document, include:

```
## Manual Input Needed
[List every data point that was not available from the specified sources, with a note on why — paywall, not on page, tool did not reflect current boundaries, etc.]
```

### Sources Appendix

After "Manual Input Needed," include a consolidated list of all URLs visited during research, organized by section. This is used for citation lookup during article writing.

```
## Sources

### Section 1: Redistricting Status
- [URL 1]
- [URL 2]

### Section 2: Candidates & Fundraising
- [URL]

### Section 3: Independent Expenditures
- [URL 1]
- [URL 2]

### Section 4: Electoral History
- [URL]

### Section 5: Presidential Performance
- Source: [Downballot CSV / Kondik crossover CSV / both]

### Section 6: Demographics
- Source: Census My Congressional District CSV
- https://www.census.gov/mycd/application/?st={STATE_FIPS}&cd={DISTRICT_NUMBER}

### Section 7: District Geography
- [URL]

### Section 8: Ratings
- https://www.cookpolitical.com/ratings/house-race-ratings
- https://centerforpolitics.org/crystalball/2026-house/
- https://insideelections.com/ratings/house

### Section 9: Polling
- [URLs searched]
```

---

## Naming Convention

Save this file as: `{district-id}-baseline.md`
Example: `tx-34-baseline.md`

Use lowercase with hyphens for the filename and H1. Use uppercase for the `district:` field in YAML.

---

## Rules

1. Follow sections 1-9 in order. Do not skip or reorder.
2. Use ONLY the sources specified in each section. Do not freelance.
3. If a data point is not available from the specified source, do not search elsewhere. Add it to "Manual Input Needed."
4. Do not editorialize or interpret the data. Report what the sources say.
5. Every factual claim must be attributable to its source.
6. If you find conflicting numbers between sources, report both with attribution. Do not reconcile them.
7. If a URL returns an error or is behind a paywall, note the error and add the data point to "Manual Input Needed."
8. Record every URL visited. The Sources appendix must be complete.
9. Report all percentages to one decimal place (e.g., 47.4%, not 47%). Do not round before calculating margins or swings.
10. Use the web URLs specified in each section. Do not substitute FEC API endpoints, Ballotpedia API, or other programmatic interfaces. The web URLs include specific filters (e.g., `most_recent=true`) that affect data accuracy.

---

## QA Checklist

Before delivering the final document, verify each item:

**Structure:**
- [ ] H1 matches filename (lowercase, hyphens, no `.md`)
- [ ] YAML block immediately after H1, inside code fence
- [ ] YAML contains all required fields: district, type, date, prompt, prompt_version
- [ ] `district:` field uses uppercase (TX-34); H1 and filename use lowercase (tx-34)
- [ ] Sections 1-9 present in order
- [ ] "Manual Input Needed" section present (even if empty — write "None")
- [ ] Sources Appendix present, organized by section

**Content:**
- [ ] All percentages reported to one decimal place
- [ ] All data sourced from specified sources only — no freelanced sources
- [ ] Conflicting numbers between sources reported with both values and attribution
- [ ] Every "not available" or "Manual Input Needed" entry explains why
- [ ] Census CSV data used for demographics (not web navigation)
- [ ] Presidential data uses correct tier for district (standard / Kondik crossover / both)

**Sources:**
- [ ] Every URL visited is recorded in the Sources Appendix
- [ ] Sources Appendix has entries for all 9 sections

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-10 | Initial version with 9 sections |
| 2.0 | 2026-02-11 | Census data from attached CSV instead of navigation. Presidential data from Downballot CSV. Ratings as manual input. FEC QA downloads added. 538 URL removed. |
| 3.0 | 2026-02-11 | Aligned with naming conventions (YAML header, H1 = filename, version in YAML not filename). Added three-tier presidential data logic for redistricted districts (Kondik crossover CSV). Added source URL tracking in all sections plus Sources appendix. |
| 3.1 | 2026-02-11 | Hyphens replace underscores as universal separator per naming convention v1.4. |
| 3.2 | 2026-02-11 | Fixed Section 3 IE URL to use correct FEC web interface with most_recent=true filter. Split pre-flight IE download into 2024 and 2026 cycles. Added candidate name consolidation note. Added rules: one-decimal precision (rule 9), use specified web URLs not API endpoints (rule 10). |
| 3.3 | 2026-02-12 | Added QA Checklist section for pre-delivery format and content verification. |
