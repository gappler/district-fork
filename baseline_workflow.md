# Baseline Research Workflow

## Overview

This is your checklist for running the district baseline prompt on Manus. Three phases: pre-flight downloads, prompt run, QA verification.

**Time estimate:** ~15 minutes per district (5 min pre-flight, 5 min Manus runs, 5 min QA)

---

## Phase 1: Pre-flight Downloads

Do these before opening Manus.

### One-time setup (first run only)

- [ ] Create `data/reference/` folder in early-returns repo
- [ ] Download Downballot presidential results CSV → save as `data/reference/downballot_presidential.csv`
  - Source: https://docs.google.com/spreadsheets/d/1ng1i_Dm_RMDnEvauH44pgE6JCUsapcuu8F2pCfeLWFo
  - Export the "Percentages" tab as CSV

### Per-district downloads

For each new district, replace {STATE_FIPS}, {STATE_ABBREV}, {DISTRICT_NUMBER} as needed.

**1. Census CSV** (attached to prompt — Manus reads this)
- Download from: https://www.census.gov/mycd/application/?st={STATE_FIPS}&cd={DISTRICT_NUMBER}
- Click the download/export button
- Save as: `projects/{DISTRICT_ID}/census.csv`

**2. Cook PVI & Rating** (typed into prompt)
- Look up at: https://www.cookpolitical.com/ratings/house-race-ratings
- Note both values — you'll paste them into the prompt input

**3. FEC Candidate Totals** (QA reference — not attached to prompt)
- Download from: https://www.fec.gov/data/candidates/house/?election_year=2026&election_full=True&state={STATE_ABBREV}&district={DISTRICT_NUMBER}&is_active_candidate=true
- Export CSV
- Save as: `projects/{DISTRICT_ID}/fec-candidates.csv`

**4. FEC Independent Expenditures** (QA reference — not attached to prompt)
- Download from: https://www.fec.gov/data/independent-expenditures/?data_type=processed&most_recent=true&cycle=2026&is_notice=false&candidate_office=H&candidate_office_state={STATE_ABBREV}&candidate_office_district={DISTRICT_NUMBER}
- Export CSV (version filter: "Current version" only — `most_recent=true` is already in the URL)
- Save as: `projects/{DISTRICT_ID}/fec-ie.csv`

### State FIPS codes (common)

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

---

## Phase 2: Run the Prompt

1. Open Manus 1.6 max
2. Attach two files:
   - `projects/{DISTRICT_ID}/census.csv`
   - `data/reference/downballot_presidential.csv`
3. Paste the baseline prompt (`district_baseline_prompt_v2.md`)
4. Fill in the variables:
   - {DISTRICT_ID} → e.g., TX-34
   - {STATE} → e.g., Texas
   - {COOK_PVI} → from your pre-flight lookup
   - {COOK_RATING} → from your pre-flight lookup
5. Run

---

## Phase 3: QA Verification

Check Manus output against your pre-flight downloads.

### Must verify (high error risk)

- [ ] **Candidates & Fundraising (Section 2):** Compare candidate count, top-line receipts/disbursements/cash-on-hand against `fec-candidates.csv`
- [ ] **IE Spending (Section 3):** Compare total amounts and top spenders against `fec-ie.csv`. Watch for deduplication issues — if Manus total is significantly higher than your CSV, it may have counted amended filings
- [ ] **Ratings (Section 8):** Verify Sabato and Inside Elections ratings match what's on their actual pages. In TX-34 test, Manus contradicted itself between activity log and final output

### Spot check (medium risk)

- [ ] **Demographics (Section 6):** Confirm population and median income against Census CSV. These are simple extractions so errors are rare but worth a glance
- [ ] **Presidential Performance (Section 5):** Confirm against Downballot CSV. Should be exact match since Manus is reading the file directly
- [ ] **Redistricting (Section 1):** Does the redistricting status match what you know? If the state has new maps, does the description make sense?

### Low risk (scan for obvious errors)

- [ ] **Electoral History (Section 4):** Do the last 3 cycles look right? Any missing elections?
- [ ] **Geography (Section 7):** Do the counties listed match the district?
- [ ] **Polling (Section 9):** If polls are reported, are they from credible firms?

---

## File Locations

```
early-returns/
├── data/
│   ├── reference/
│   │   └── downballot_presidential.csv    ← one-time download
│   ├── sample_data.sql
│   └── schema.sql
├── projects/
│   └── {DISTRICT_ID}/
│       ├── census.csv                     ← per-district pre-flight
│       ├── fec-candidates.csv             ← per-district QA
│       └── fec-ie.csv                     ← per-district QA
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
