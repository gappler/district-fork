# Baseline Research Workflow (v4.0)

## Overview

Checklist for running the district research prompts via Manus. Four phases per prompt: pre-flight downloads, prompt run, QA verification, publish to GitHub.

**Time estimate:** ~60-75 minutes per district across all four prompts

**Prompts location:** `https://raw.githubusercontent.com/gappler/district-fork/main/`

---

## Research Workflow

The baseline is step 1 of a four-prompt research workflow:

1. **Baseline** → structural data foundation. Prompt: `district-baseline-prompt.md`
2. **Media Research** → press coverage + social extraction. Prompt: `district-media-research-prompt.md`
3. **Candidate Profiles** → per-candidate deep dive (opposition + affirmative merged). Prompt: `district-candidate-profile-prompt.md`
4. **Voting Record** → incumbent voting record with cross-party breaks and thematic analysis. Prompt: `district-voting-record-prompt.md`

After all four are complete, push everything to GitHub, reindex, and start a writing session with Claude.

---

## Prompt 1: Baseline

### Phase 1: Pre-flight Downloads

Do these before opening Manus.

#### One-time setup (first run only)

- [ ] Create `data/reference/` folder in early-returns repo
- [ ] Download Downballot presidential results CSV → save as `data/reference/downballot-presidential.csv`
  - Source: https://docs.google.com/spreadsheets/d/1ng1i_Dm_RMDnEvauH44pgE6JCUsapcuu8F2pCfeLWFo
  - Export the "Percentages" tab as CSV
- [ ] Download Kondik crossover CSV → save as `data/reference/kondik-crossover-presidential-2026-lines.csv`
  - Source: Sabato's Crystal Ball (Kondik), Feb 5, 2026 — via Dave's Redistricting App
  - Only needed for redistricted states: California, Missouri, North Carolina, Ohio, Texas, Utah

#### Per-district downloads

For each new district, replace {STATE_FIPS}, {STATE_ABBREV}, {DISTRICT_NUMBER} as needed.

**1. Census CSV** (attached to prompt — Manus reads this)
- Download from: https://www.census.gov/mycd/application/?st={STATE_FIPS}&cd={DISTRICT_NUMBER}
- Click the download/export button
- Save to: `~/early-returns/projects/{DISTRICT_ID}/data/census.csv`

**2. DRA Map Verification (redistricted states only)**
- Go to Dave's Redistricting App: https://davesredistricting.org/
- Find the enacted 2026 map for {STATE}
- Verify which counties are fully or partially in {DISTRICT_ID}
- Record the correct county list — Manus may use old boundary data
- In TX-34, Manus listed only 2 of 5 counties because Ballotpedia hadn't updated
- You will provide this as {COUNTIES} when running the prompt

**3. Ratings** (typed into prompt — all four required)
- Cook PVI: https://www.cookpolitical.com/ratings/house-race-ratings (requires login)
- Cook rating: same page
- Sabato: https://centerforpolitics.org/crystalball/2026-house/
- Inside Elections: https://insideelections.com/ratings/house
- Note all four values — you'll type them into the prompt input

**4. FEC Candidate Totals** (QA reference — not attached to prompt)
- Download from: https://www.fec.gov/data/candidates/house/?election_year=2026&election_full=True&state={STATE_ABBREV}&district={DISTRICT_NUMBER}&is_active_candidate=true
- Export CSV
- Save to: `~/early-returns/projects/{DISTRICT_ID}/data/fec-candidates.csv`

**5. FEC Independent Expenditures — 2024 cycle** (QA reference — not attached to prompt)
- Download from: https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2024&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER}
- Export CSV
- Save to: `~/early-returns/projects/{DISTRICT_ID}/data/fec-ie-2024.csv`

**6. FEC Independent Expenditures — 2026 cycle** (QA reference — not attached to prompt)
- Download from: https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2026&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER}
- Export CSV
- Save to: `~/early-returns/projects/{DISTRICT_ID}/data/fec-ie-2026.csv`

#### State FIPS codes (common)

| State | FIPS | State | FIPS |
|-------|------|-------|------|
| AZ | 04 | NJ | 34 |
| CA | 06 | NC | 37 |
| FL | 12 | OH | 39 |
| GA | 13 | OR | 41 |
| MI | 26 | PA | 42 |
| MN | 27 | TX | 48 |
| NV | 32 | VA | 51 |
| NH | 33 | WA | 53 |

Full list: https://www.census.gov/library/reference/code-lists/ansi/ansi-codes-for-states.html

### Phase 2: Run the Prompt

1. Open Manus 1.6 max
2. Tell Manus: "Fetch and follow the prompt at `https://raw.githubusercontent.com/gappler/district-fork/main/district-baseline-prompt.md`"
3. Attach files:
   - `~/early-returns/projects/{DISTRICT_ID}/data/census.csv`
   - `~/early-returns/data/reference/downballot-presidential.csv`
   - `~/early-returns/data/reference/kondik-crossover-presidential-2026-lines.csv` (only if redistricted state)
4. Provide the variables Manus needs:
   - {DISTRICT_ID} → e.g., TX-34
   - {STATE} → e.g., Texas
   - {COOK_PVI} → from your pre-flight lookup
   - {COOK_RATING} → from your pre-flight lookup
   - {SABATO_RATING} → from your pre-flight lookup
   - {IE_RATING} → from your pre-flight lookup
5. Run

#### Three-tier presidential data logic

The prompt handles this automatically based on Section 1 (redistricting status), but know which tier applies:

- **Tier 1 — No redistricting:** Uses Downballot CSV only. Reports 2024 and 2020 on old lines.
- **Tier 2 — Redistricted, Kondik data available:** Uses both CSVs. Reports 2024 on new lines (Kondik) and old lines (Downballot), plus 2020 on old lines. Calculates redistricting shift.
- **Tier 3 — Redistricted, no Kondik data:** Uses Downballot CSV only, flags that numbers reflect old boundaries. Adds manual DRA lookup to "Manual Input Needed."

### Phase 3: QA Verification

Check Manus output against your pre-flight downloads.

#### Must verify (high error risk)

- [ ] **Candidates & Fundraising (Section 2):** Compare candidate count, top-line receipts/disbursements/cash-on-hand against `fec-candidates.csv`
- [ ] **IE Spending (Section 3):** Compare total amounts and top spenders against `fec-ie-2024.csv` and `fec-ie-2026.csv`. Watch for deduplication issues — if Manus total is significantly higher than your CSV, it may have counted amended filings
- [ ] **Ratings (Section 8):** Verify all four ratings match what you typed in. In TX-34 test, Manus contradicted itself between activity log and final output
- [ ] **Geography (Section 7):** For redistricted states, verify county list against your pre-flight DRA lookup. For non-redistricted states, spot-check is sufficient.

#### Spot check (medium risk)

- [ ] **Demographics (Section 6):** Confirm population and median income against Census CSV. Simple extractions, errors are rare
- [ ] **Presidential Performance (Section 5):** Confirm against Downballot CSV (and Kondik CSV if Tier 2). Should be exact match since Manus is reading the files directly
- [ ] **Redistricting (Section 1):** Does the redistricting status match what you know? If the state has new maps, does the description make sense?

#### Low risk (scan for obvious errors)

- [ ] **Electoral History (Section 4):** Do the last 3 cycles look right? Any missing elections?
- [ ] **Polling (Section 9):** If polls are reported, are they from credible firms?

#### Structure check

- [ ] H1 matches filename (lowercase, hyphens, no `.md`)
- [ ] YAML block present with all required fields: district, type, date, prompt, prompt_version
- [ ] `district:` field uses uppercase (TX-34); H1 and filename use lowercase (tx-34)
- [ ] All 9 sections present in order
- [ ] "Manual Input Needed" section present (even if empty)
- [ ] Sources Appendix present, organized by section

### Phase 4: Publish

Save Manus output to `~/early-returns/projects/{DISTRICT_ID}/research/{district-id}-baseline.md`

---

## Prompt 2: Media Research

Prompt: `district-media-research-prompt.md`

Run after Baseline is published. Standard four-phase process (pre-flight, run, QA, publish).

Output: `~/early-returns/projects/{DISTRICT_ID}/research/{district-id}-media-research.md`

---

## Prompt 3: Candidate Profiles

Prompt: `district-candidate-profile-prompt.md`

Run after Media Research is published. One prompt run per candidate.

Output: `~/early-returns/projects/{DISTRICT_ID}/research/{candidate}-profile.md`

---

## Prompt 4: Voting Record

**Only for incumbents.** Skip for open-seat races.

Prompt: `district-voting-record-prompt.md`

**Time estimate:** ~20 minutes (5 min pre-flight, 10 min pipeline run, 5 min QA)

### Phase 1: Pre-flight Downloads

**1. Congress.gov Roll Call CSV** (attached to prompt — Manus reads this)

1. Go to `https://www.congress.gov/member/{name}/{MEMBER_ID}`
2. Navigate to the House Roll Call Votes view. URL parameter: `?q={"sponsorship":"houseRollCallVoteFacet"}`
3. Apply filters:
   - **Congress:** Check 119 (2025-2026) and 118 (2023-2024)
   - **Bill Type:** Check ALL four types (Bills, Resolutions, Concurrent Resolutions, Joint Resolutions)
   - **All other filters:** Leave unselected/unfiltered
4. Click **Download Results** → **OK**
5. Save to: `~/early-returns/projects/{DISTRICT_ID}/data/congress-rollcall-{first-last}.csv`

**Why these filters:**
- All bill types because Joint Resolutions include CRA rollback votes. Resolutions include messaging votes.
- No subject filter because CRS tags are too narrow. In testing, Congress.gov tagged 4 immigration votes for Gonzalez; VoteSmart tagged 62.
- No committee, status, or member activity filters — these all restrict the result set in ways that lose data.

**2. OpenSecrets Industry Data** (optional — for donor overlay analysis)

- Download from: `https://www.opensecrets.org/members-of-congress/{name}/industries?cid={CID}&cycle=2024`
- Use the download CSV link on the page
- Save to: `~/early-returns/projects/{DISTRICT_ID}/data/opensecrets-industries-{first-last}.csv`
- Note: OpenSecrets runs one cycle behind. 2024 is the most recent as of February 2026. For incumbents, industry relationships are generally stable across cycles.

**3. Find the member's Congress.gov ID**

- On the member page URL: `congress.gov/member/{name}/{MEMBER_ID}`
- The ID is the last segment (e.g., G000581 for Gonzalez, S001222 for Sorensen)

### Phase 2: Run the Pipeline

1. Open Manus 1.6 max
2. Tell Manus: "Fetch and follow the prompt at `https://raw.githubusercontent.com/gappler/district-fork/main/district-voting-record-prompt.md`"
3. Attach: `~/early-returns/projects/{DISTRICT_ID}/data/congress-rollcall-{first-last}.csv`
4. Provide variables:
   - {DISTRICT_ID} → e.g., TX-34
   - {CANDIDATE_NAME} → e.g., Vicente Gonzalez
   - {PARTY} → Democrat or Republican (determines cross-party break logic)
   - {MEMBER_ID} → e.g., G000581
5. Manus runs `full_pipeline.py` which:
   - Filters to substantive floor actions (On Passage, On Agreeing to Resolution, Suspension Votes)
   - Parses party breakdowns from result field
   - Flags cross-party breaks (member voted opposite to majority of their party)
   - Fetches House Clerk XML for each vote to get bill numbers and titles
   - Outputs markdown table, CSV, and JSON

**If Republican member:** Manus updates `is_cross_party()` to compare against Republican majority instead of Democratic majority. The prompt includes the code swap.

### Phase 3: QA Verification

- [ ] **Vote count plausible:** Expect 300-500 substantive votes per Congress for an active member
- [ ] **Missing bill numbers = 0:** Clerk XML should resolve all votes
- [ ] **Cross-party break rate plausible:** 5% for safe-seat members, 20%+ for Blue Dogs or moderates
- [ ] **Spot-check 3-5 rows:** Click the Congress.gov vote URL to confirm bill number and member vote match
- [ ] **Check for "motion to table" errors:** A "Yea" on a motion to table means the opposite of a "Yea" on passage. The pipeline filters these, but verify if any slip through.
- [ ] **Verify thematic categorization uses bill titles only** — no AI-generated descriptions

#### Structure check

- [ ] H1 matches filename
- [ ] YAML block present with all required fields: district, type, candidate, party, date, prompt, prompt_version, source_csv, congresses
- [ ] Summary statistics present
- [ ] Thematic categorization present
- [ ] Lone wolf analysis present
- [ ] Full voting record tables present (one per Congress)
- [ ] Sources section present

### Phase 4: Publish

Save output files:
- `~/early-returns/projects/{DISTRICT_ID}/research/{district-id}-voting-record-{first-last}.md`
- `~/early-returns/projects/{DISTRICT_ID}/research/{district-id}-voting-record-{first-last}.csv`

---

## Final Steps

After all prompts are complete:

```bash
cd ~/early-returns
git add -A
git commit -m "{DISTRICT_ID} research complete"
git push
reindex
```

Claude now has access to all research for writing sessions — no upload needed.

---

## File Locations

```
~/early-returns/
├── data/
│   ├── reference/
│   │   ├── downballot-presidential.csv         ← one-time download
│   │   └── kondik-crossover-presidential-2026-lines.csv  ← one-time (redistricted states)
│   ├── sample_data.sql
│   └── schema.sql
├── projects/
│   └── {DISTRICT_ID}/
│       ├── data/
│       │   ├── census.csv                      ← per-district pre-flight
│       │   ├── fec-candidates.csv              ← per-district QA
│       │   ├── fec-ie-2024.csv                 ← per-district QA
│       │   ├── fec-ie-2026.csv                 ← per-district QA
│       │   ├── congress-rollcall-{first-last}.csv  ← voting record pre-flight
│       │   └── opensecrets-industries-{first-last}.csv  ← voting record pre-flight (optional)
│       └── research/
│           ├── {district-id}-baseline.md       ← Manus output (after QA)
│           ├── {district-id}-media-research.md ← media research output
│           ├── {candidate}-profile.md          ← candidate profile outputs
│           ├── {district-id}-voting-record-{first-last}.md  ← voting record output
│           └── {district-id}-voting-record-{first-last}.csv ← voting record CSV
```

---

## Known Issues & Workarounds

| Issue | Workaround |
|-------|-----------|
| Census tool is JavaScript-heavy, Manus can't navigate it | Manual CSV download, attached to prompt |
| Cook PVI/ratings behind paywall | Manual lookup, typed into prompt |
| FiveThirtyEight polling URL redirects to ABC News | Prompt uses web search instead |
| Manus sometimes contradicts itself on ratings | Always verify Section 8 against source pages |
| FEC IE data can include amended filings | URL includes `most_recent=true`; verify totals against your download |
| Manus may use Wikipedia when Ballotpedia lacks data | Presidential data now comes from attached CSV; redistricting section has source-lock guardrails |
| Prompt pasting errors | Manus now fetches prompt from GitHub — no pasting needed |
| Congress.gov CSV lacks bill names | Pipeline fetches House Clerk XML to fill in bill numbers and titles |
| CRS subject tags too narrow for topic filtering | Never filter by Subject/Policy Area before download. Topic analysis happens after download. |
| OpenSecrets data runs one cycle behind | 2024 cycle is the most recent as of February 2026. Industry relationships are stable for incumbents. |
| "On Agreeing to Resolution" includes procedural rules resolutions | Titles starting with "Providing for consideration of..." are nearly always party-line. Note but don't weight in thematic analysis. |
| Motion to table reverses vote meaning | Pipeline filters these out, but verify during spot-check. A "Yea" on a motion to table kills the underlying measure. |

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-11 | Initial workflow matching baseline prompt v2.0 |
| 2.0 | 2026-02-12 | Updated for baseline prompt v3.3: three-tier presidential logic, Kondik CSV, hyphen convention, data/ subfolder structure |
| 3.0 | 2026-02-13 | Manus fetches prompt from GitHub (no more pasting). Added Phase 4 (push to GitHub + reindex). Split FEC IE into 2024/2026 downloads. Added all four ratings to pre-flight. Added structure check to QA. Added three-prompt workflow context. |
| 4.0 | 2026-02-16 | Added Prompt 4: Voting Record pipeline. Four-prompt workflow. Congress.gov CSV + House Clerk XML + full_pipeline.py. Includes cross-party break analysis, thematic categorization, donor overlay. Updated file locations and known issues. |
