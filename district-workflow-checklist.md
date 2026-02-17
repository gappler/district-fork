# [DISTRICT] Workflow Checklist

**District:** [DISTRICT]
**Date Started:** [DATE]
**Target Publish:** [DATE]
**Publish Day:** Tuesday or Thursday (Sunday if third post in a week)

## Stage 1: Pre-flight (You)

- [ ] Created `~/early-returns/projects/{DISTRICT_ID}/data/` folder
- [ ] Downloaded Census CSV from My Congressional District → `data/census.csv`
- [ ] Looked up Cook PVI, Cook rating, Sabato rating, Inside Elections rating
- [ ] Downloaded FEC candidate totals CSV → `data/fec-candidates.csv`
- [ ] Downloaded FEC IE 2024 CSV → `data/fec-ie-2024.csv`
- [ ] Downloaded FEC IE 2026 CSV → `data/fec-ie-2026.csv`
- [ ] If redistricted: verified DRA map against county list
- [ ] If redistricted: confirmed Kondik crossover CSV has district data

## Stage 2: Baseline (Manus)

- [ ] Ran `district-baseline-prompt.md` via Manus
- [ ] Attached: census CSV, Downballot CSV, Kondik CSV (if redistricted)
- [ ] Provided: district ID, state, all four ratings
- [ ] QA: candidates and fundraising match FEC CSV
- [ ] QA: IE spending matches FEC IE CSVs
- [ ] QA: ratings match what you typed in
- [ ] QA: presidential performance matches Downballot/Kondik CSVs
- [ ] QA: counties match DRA map (redistricted states)
- [ ] Saved to `projects/{DISTRICT_ID}/research/{district-id}-baseline.md`
- [ ] Pushed to GitHub, reindexed

## Stage 3: Media Research (Manus)

- [ ] Ran `district-media-research-prompt.md` via Manus
- [ ] Spot-checked article URLs (do they load? do quotes match?)
- [ ] Saved to `projects/{DISTRICT_ID}/research/{district-id}-media-research.md`
- [ ] Pushed to GitHub, reindexed

## Stage 4: Candidate Profiles (Manus)

- [ ] Ran `district-candidate-profile-prompt.md` for each contender:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- [ ] Spot-checked FEC numbers against baseline
- [ ] Spot-checked vulnerability claims against cited sources
- [ ] Saved to `projects/{DISTRICT_ID}/research/{district-id}-candidate-{name}.md`
- [ ] Pushed to GitHub, reindexed

## Stage 5: Voting Record (Manus) — Incumbents Only

- [ ] Downloaded Congress.gov roll call CSV (118th + 119th, all bill types, no other filters) → `data/congress-rollcall-{first-last}.csv`
- [ ] Downloaded OpenSecrets industry CSV (optional, for donor overlay) → `data/opensecrets-industries-{first-last}.csv`
- [ ] Ran `district-voting-record-prompt.md` via Manus
- [ ] Attached: Congress.gov roll call CSV
- [ ] Provided: district ID, candidate name, party, Congress.gov member ID
- [ ] QA: missing bill numbers = 0
- [ ] QA: vote count plausible (300-500 substantive per Congress)
- [ ] QA: cross-party break rate plausible (5% safe seat, 20%+ moderate)
- [ ] QA: spot-checked 3-5 rows against Congress.gov vote URLs
- [ ] QA: no motion-to-table votes slipped through with reversed meaning
- [ ] Saved to `projects/{DISTRICT_ID}/research/{district-id}-voting-record-{first-last}.md`
- [ ] Saved CSV to `projects/{DISTRICT_ID}/research/{district-id}-voting-record-{first-last}.csv`
- [ ] Pushed to GitHub, reindexed

## Stage 6: Briefing Draft (Claude)

- [ ] All research files indexed and accessible via MCP
- [ ] Drafted using `district-briefing-prompt.md`
- [ ] Working draft has inline citations for every factual claim
- [ ] Clean draft stripped of citation brackets

## Stage 7: Fact-Check (NotebookLM)

- [ ] Compiled source URL list for NotebookLM (all research files, CSVs, polling PDFs, and external sources cited in working draft)
- [ ] Uploaded working draft with citations to NotebookLM
- [ ] Uploaded all source documents (baseline, media research, candidate profiles, voting record, Equis/polling if cited)
- [ ] Asked NotebookLM to verify each cited claim against sources
- [ ] Resolved any flagged discrepancies
- [ ] Verified any polling claims against actual toplines (not summaries or memos)

## Stage 8: Editorial Review (Claude + You)

- [ ] Fresh read for rhythm and voice
- [ ] Opening paragraph frames structure, dynamics, and what to watch
- [ ] Closing paragraph returns to opening question
- [ ] Em dashes consistent (no spaces)
- [ ] No unnecessary burn rates or redundant numbers
- [ ] Every number earns its place
- [ ] Overnight review before publishing

## Stage 9: Publish

- [ ] Schedule for Tuesday or Thursday morning
- [ ] Clean version (no citations) → Substack
- [ ] Working version (with citations) → `projects/{DISTRICT_ID}/` for reference

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-05 | Initial version (old prompt structure) |
| 2.0 | 2026-02-14 | Rewritten to match current workflow: baseline → media → candidates → briefing → NotebookLM fact-check → editorial review. Added DRA map verification, polling topline verification, publishing cadence. |
| 3.0 | 2026-02-16 | Added Stage 5: Voting Record (incumbents only). Congress.gov roll call CSV + House Clerk XML pipeline. Includes cross-party break analysis, OpenSecrets donor overlay. Bumped all subsequent stages. Added voting record to NotebookLM source list. |
