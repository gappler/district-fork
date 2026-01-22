# district_workflow

---
version: 1.2
date: 2026-01-21
purpose: One-page reference for the Early Returns article production workflow
---

## The Principle

**Order matters.** AI reads media *after* you've made editorial decisions, not before.

- AI reading media before you decide = AI's interpretation becomes invisible in your work
- AI reading media after you decide = AI matches your claims to sources

---

## The Five Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 1: FOUNDATIONAL RESEARCH                                      │
│ Tool: Manus                                                         │
│ Prompts: district_research_prompt                                   │
│          district_opposition_prompt                                 │
│          district_affirmative_prompt                                │
│ Outputs: [district]_overview.md                                     │
│          [district]_opposition_[candidate].md                       │
│          [district]_affirmative_[candidate].md                      │
│ Your role: Verify numbers, spot-check facts                         │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 2: MEDIA DISCOVERY                                            │
│ Tool: Manus                                                         │
│ Prompt: district_media_discovery_prompt                             │
│ Output: [district]_media_discovery.md                               │
│ Your role: Scan list, select 3-5 priority articles to read          │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 3: YOUR READING                                               │
│ Tool: You                                                           │
│ Input: Priority articles from Stage 2                               │
│ Output: Your notes on what's editorially significant                │
│ This is where YOUR interpretation happens                           │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 4: DRAFTING                                                   │
│ Tool: Claude                                                        │
│ Prompt: district_writing_prompt                                     │
│ Inputs: Research reports + YOUR notes                               │
│ NOT available: Full media articles, media triage                    │
│ Output: Draft article                                               │
│ AI role: Collaborative partner—challenges, sharpens, flags risks    │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 5: CITATION PASS                                              │
│ Tool: Claude                                                        │
│ Trigger: After you've reviewed draft and locked editorial frame     │
│ Input: Locked draft + full media articles                           │
│ Output: Cited version with references                               │
│ AI role: Match claims to sources. Do NOT reinterpret or add.        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## What Each Tool Sees

| Stage | Manus | Claude | You |
|-------|-------|--------|-----|
| 1. Foundational Research | Primary sources | — | Verify |
| 2. Media Discovery | Web search | — | Select priorities |
| 3. Your Reading | — | — | Read, take notes |
| 4. Drafting | — | Research + your notes | Collaborate |
| 5. Citation Pass | — | Draft + full media | Review |

**Critical:** Claude does NOT see full media until Stage 5, after editorial decisions are locked.

---

## The Guardrail Test

Before any claim implying intent, motive, or causation:

> "What's the factual basis for this inference? Can you defend it if challenged?"

| Claim Type | Required Evidence |
|------------|------------------|
| Factual statement | Primary source |
| Pattern claim | Multiple instances |
| Characterization | Observable behavior + context |
| Intent/motive | Explicit statement OR overwhelming evidence |

**Donations alone ≠ corrupt intent**
**Votes alone ≠ betrayal**
**Association alone ≠ endorsement of views**

---

## Prompts by Stage

| Stage | Prompt | Tool |
|-------|--------|------|
| 1 | `district_research_prompt.md` | Manus |
| 1 | `district_opposition_prompt.md` | Manus |
| 1 | `district_affirmative_prompt.md` | Manus |
| 2 | `district_media_discovery_prompt.md` | Manus |
| 2-3 | `district_media_triage_prompt.md` (optional) | Manus |
| 4-5 | `district_writing_prompt.md` | Claude |

**For operational details** (what to attach, what to provide, what to say), see `district_fork_readme.md`.

---

## Common Mistakes to Avoid

1. **Skipping Stage 3** — If you don't read priority articles yourself, AI's interpretation controls your piece
2. **Giving Claude media in Stage 4** — Editorial decisions get made by AI, not you
3. **Reinterpreting during Stage 5** — Citation pass is mechanical; don't change the frame
4. **Inferring intent from donations** — High bar; need explicit evidence
5. **Letting AI soften your digs** — If you earned it, keep it

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-01-19 | Initial District Fork version. Converted from legacy `field_report_workflow_v1.0.md`. Updated all prompt references to v1.0. Added output filenames. Added reference to README for operational details. |
| 1.1 | 2026-01-21 | Updated naming convention references. Removed versions from filenames per `district_naming_prompt.md` v1.1. |
| 1.2 | 2026-01-21 | Renamed publication from "Field Report" to "Early Returns". |
