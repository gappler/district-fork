# Top Articles Recommendation Process

---
version: 1.1
date: 2026-02-17
purpose: After all research is complete, identify the 3 best long-format articles for the writer to read before drafting
tool: Claude (Cowork or Claude Code)
---

## When to Run

Run this after all Manus research is complete and indexed (baseline, media research, candidate profiles, voting record if applicable) — before starting the briefing draft.

## What It Does

1. Scans the media research file for all article URLs already collected
2. Searches premium outlets for additional long-format coverage not already in the research
3. Recommends the top 3 articles most likely to inform the briefing angle
4. Flags paywalled articles the writer has subscription access to

## Premium Outlet Scan List

Three tiers, searched in order. Stop when you have 3 strong recommendations — don't grind through every outlet.

### Tier 1: Always Search

These outlets most consistently produce the long-format, structural analysis that informs briefing angles.

| Outlet | Paywall | Why it's here |
|:-------|:--------|:------|
| The Atlantic | Yes — writer has access | Best at "what does this race mean" framing |
| New York Times | Yes — writer has access | National framing, trend pieces, Ezra Klein podcast/essays |
| ProPublica | Free | Investigative deep-dives: dark money, financial conflicts, gerrymandering mechanics |
| Politico | Partial paywall | Campaign dynamics, insider reporting |
| Cook Political Report | Yes — writer has access | Race ratings, handicapping essays |
| Sabato's Crystal Ball | Free | Race previews, historical context essays |
| Inside Elections | Yes — writer has access | Detailed race analysis |
| The Downballot (Daily Kos) | Free | Granular competitive-race coverage, closest to what Early Returns does |

### Tier 2: Search If Tier 1 Doesn't Fill 3 Slots

| Outlet | Paywall | Why it's here |
|:-------|:--------|:------|
| Wall Street Journal | Yes — writer has access | Economic angles, business-side framing |
| Vox | Free | Policy-context pieces, structural explanations |
| The Intercept | Free | Adversarial accountability journalism, financial/voting record vulnerabilities |
| Mother Jones | Free | Investigative features, especially on money in politics |
| The New Yorker | Yes — writer has access | Extraordinary long profiles when they exist (rare but worth checking) |
| Bolts Magazine | Free | Down-ballot power, local-shapes-national framing — very aligned with Early Returns |
| FiveThirtyEight (ABC) | Free | Data-driven structural analysis |

### Tier 3: Regional / State-Level

**Dynamically populated based on district location.** These often produce the single best piece on a given race because they have reporters on the ground.

| Region | Outlets |
|:-------|:--------|
| Texas | Texas Tribune |
| California | CalMatters, Los Angeles Times (writer has access) |
| North Carolina | NC Newsline |
| Ohio | Ohio Capital Journal |
| Michigan | Bridge Michigan |
| Virginia | Virginia Mercury |
| Minnesota | Minnesota Reformer |
| Oregon | Oregon Capital Chronicle |
| Wisconsin | Wisconsin Examiner |
| Arizona | Arizona Mirror |
| Nevada | Nevada Current |
| Pennsylvania | Pennsylvania Capital-Star |
| Georgia | Georgia Recorder |
| Florida | Florida Phoenix |
| National hub | States Newsroom (may surface affiliate stories) |

For states not listed, search `site:statesnewsroom.com "{STATE}"` to find the local affiliate, and check for independent state-level outlets (e.g., Colorado Sun, Iowa Capital Dispatch, Maine Monitor).

### Not Included

These were considered but deprioritized. The media research prompt already catches most of their output, or their long-format coverage is too inconsistent to justify a dedicated search:

Rolling Stone, Wired, Salon, The Nation, The Hill, Real Clear Politics, Roll Call. If any of these surface in the media research file, they'll be considered — but they're not worth a separate scan pass.

## Search Strategy

For each outlet, search:
- `site:[outlet.com] "{DISTRICT_ID}"` or `"{STATE} [district number]"`
- `site:[outlet.com] "{CANDIDATE_NAME}"` (for major candidates)
- `site:[outlet.com] "{STATE}" congressional 2026` (for state-level trend pieces)

Prioritize:
- **Long-format analysis** over news briefs (1,000+ words preferred)
- **Structural or thematic framing** over horse-race coverage
- **Pieces that challenge conventional wisdom** or offer a non-obvious angle
- **Recent pieces** (last 6 months) unless an older piece is foundational

## Output Format

```
## Top 3 Articles for {DISTRICT_ID}

### 1. [Headline] — [Outlet]
**URL:** [link]
**Date:** [date]
**Paywall:** Yes/No (you have access)
**Why read this:** [1-2 sentences on what this piece offers that the research doesn't already cover — a framing angle, a data point, a quote, a counterargument]

### 2. [Headline] — [Outlet]
**URL:** [link]
**Date:** [date]
**Paywall:** Yes/No (you have access)
**Why read this:** [1-2 sentences]

### 3. [Headline] — [Outlet]
**URL:** [link]
**Date:** [date]
**Paywall:** Yes/No (you have access)
**Why read this:** [1-2 sentences]

### Also Notable
- [Headline] — [Outlet] — [Paywall: Y/N] — [One line on why]
- [Headline] — [Outlet] — [Paywall: Y/N] — [One line on why]
```

## Rules

1. Do not duplicate articles already in the media research file. Check the Sources Appendix first.
2. Prioritize depth over breadth — one great long-read beats three thin news hits.
3. "Why read this" must be specific. Not "good overview of the race" — instead: "frames Gonzalez's district-switching as part of a broader pattern of South Texas Democratic realignment anxiety."
4. Flag all paywalled articles clearly. The writer has subscriptions to NYT, WSJ, LAT, The Atlantic, The New Yorker, Economist, Cook, and Inside Elections.
5. If fewer than 3 strong articles exist beyond what's already in the research, say so. Do not pad with weak recommendations.
6. The "Also Notable" section is optional — only include if there are genuinely useful additional pieces.

## How to Run

Ask Claude: "Run the top-articles process for {DISTRICT_ID}."

Claude will:
1. Read the media research file's Sources Appendix to know what's already collected
2. Search the premium outlet list for additional coverage
3. Return the top 3 recommendations in the format above

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-17 | Initial version. Premium outlet scan list, search strategy, output format, paywall flagging. |
| 1.1 | 2026-02-17 | Expanded to three-tier outlet system: Tier 1 (always search — 8 outlets), Tier 2 (if needed — 7 outlets), Tier 3 (regional, dynamically populated by state). Added The Atlantic, ProPublica, Vox, The Intercept, Mother Jones, The New Yorker, Bolts Magazine, FiveThirtyEight. Added 15 state-level outlets with States Newsroom fallback. Deprioritized Rolling Stone, Wired, Salon, The Nation, The Hill, RCP, Roll Call. |
