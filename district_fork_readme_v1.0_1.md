# District Fork

**A modular system for political intelligence on U.S. House races.**

District Fork produces standardized research and analysis for Field Report. The system uses AI tools for research and discovery, with human editorial judgment controlling the narrative.

---

## Current Components

### Prompts

| Prompt | Filename | Description |
|:-------|:---------|:------------|
| District Research | `district_research_prompt_v1.0.md` | District-level structural analysis |
| Opposition Research | `district_opposition_prompt_v1.0.md` | Vulnerability dossier on a candidate |
| Affirmative Research | `district_affirmative_prompt_v1.0.md` | Candidate performance record |
| Media Discovery | `district_media_discovery_prompt_v1.0.md` | Find relevant media coverage |
| Media Triage | `district_media_triage_prompt_v1.0.md` | Index media without interpreting |
| Writing | `district_writing_prompt_v1.0.md` | Draft the final article |

### Modules

| Module | Filename | Description |
|:-------|:---------|:------------|
| Naming Convention | `district_fork_naming_convention_v1.0.md` | File naming, YAML headers, versioning |
| Research Checklist | `district_research_checklist_v1.0.md` | QA checklist for district research reports |

### Reference Documents

| Document | Filename | Description |
|:---------|:---------|:------------|
| Workflow | `district_workflow_v1.0.md` | One-page reference for the 5-stage production workflow |

---

## How to Run a Prompt

### Setup

1. **Attach the prompt file** (e.g., `district_opposition_prompt_v1.0.md`)
2. **Attach the naming convention** (`district_fork_naming_convention_v1.0.md`)
3. **Provide the required inputs** (see table below)
4. **Tell Manus what to do** (see example phrases)

### Quick Reference

| Prompt | Attach | Provide | Say |
|:-------|:-------|:--------|:----|
| District Research | `district_research_prompt_v1.0.md` + naming convention | District code | "Run district research on TX-28" |
| Opposition Research | `district_opposition_prompt_v1.0.md` + naming convention | District, candidate name | "Run opposition research on Henry Cuellar, TX-28" |
| Affirmative Research | `district_affirmative_prompt_v1.0.md` + naming convention | District, candidate name | "Run affirmative research on Henry Cuellar, TX-28" |
| Media Discovery | `district_media_discovery_prompt_v1.0.md` + naming convention | District, all candidate names, primary date | "Run media discovery for TX-28. Candidates: Cuellar, Tijerina. Primary: March 3, 2026" |
| Media Triage | `district_media_triage_prompt_v1.0.md` + naming convention | District, attach media discovery output | "Triage the media for TX-28" |
| Writing | `district_writing_prompt_v1.0.md` | Research reports + writer's notes | "Draft Field Report article for TX-28" (use with Claude, not Manus) |

---

## Output Naming

All outputs follow this pattern:

**Filename:** `[district]_[type]_[candidate]_v[prompt version].md`

| Output Type | Code | Example |
|:------------|:-----|:--------|
| District Research | `overview` | `TX-28_overview_v1.0.md` |
| Opposition Research | `opposition` | `TX-28_opposition_henry_cuellar_v1.0.md` |
| Affirmative Research | `affirmative` | `TX-28_affirmative_henry_cuellar_v1.0.md` |
| Media Discovery | `media_discovery` | `TX-28_media_discovery_v1.0.md` |
| Media Triage | `media_triage` | `TX-28_media_triage_v1.0.md` |

**Critical:** The document's H1 header must match the filename (without `.md`). This is how Manus names the output file.

```markdown
# TX-28_opposition_henry_cuellar_v1.0

---
district: TX-28
type: opposition
candidate: henry_cuellar
date: 2026-01-19
prompt: district_opposition_prompt_v1.0.md
prompt_version: 1.0
---

[Content follows]
```

---

## Workflow

The full workflow for producing a Field Report article:

```
Stage 1: Foundational Research (Manus)
        ↓
Stage 2: Media Discovery (Manus)
        ↓
Stage 3: Writer's Reading (You)
        ↓
Stage 4: Drafting (Claude)
        ↓
Stage 5: Citation Pass (Claude)
```

| Stage | Tool | Prompt | Output |
|:------|:-----|:-------|:-------|
| 1 | Manus | `district_research_prompt_v1.0.md` | `[district]_overview_v1.0.md` |
| 1 | Manus | `district_opposition_prompt_v1.0.md` | `[district]_opposition_[candidate]_v1.0.md` |
| 1 | Manus | `district_affirmative_prompt_v1.0.md` | `[district]_affirmative_[candidate]_v1.0.md` |
| 2 | Manus | `district_media_discovery_prompt_v1.0.md` | `[district]_media_discovery_v1.0.md` |
| 2-3 | Manus (optional) | `district_media_triage_prompt_v1.0.md` | `[district]_media_triage_v1.0.md` |
| 3 | You | — | Your notes |
| 4-5 | Claude | `district_writing_prompt_v1.0.md` | Article draft |

**Key principle:** AI reads media *after* you've made editorial decisions, not before.

---

## Versioning

**Prompts and modules:**
- Patch (minor tweak): v1.0 → v1.0.1
- Minor (new capability): v1.0.1 → v1.1
- Major (restructure): v1.1 → v2.0

**Output re-runs:**
- First run: `TX-28_opposition_henry_cuellar_v1.0.md`
- Second run: `TX-28_opposition_henry_cuellar_v1.0_run2.md`

---

## Tips and Gotchas

- **Always attach the naming convention** with every prompt (except writing)
- **H1 must match filename** — Manus uses the H1 to name the output file
- **Check YAML header** — Ensure all fields are filled correctly
- **Re-runs get `_run#` suffix** — Don't overwrite previous outputs
- **Writing prompt uses Claude** — Not Manus; different tool, different workflow stage

---

## Quality Assurance

After generating a district research report, run the **Research Checklist** (`district_research_checklist_v1.0.md`) to verify completeness.

---

*Version 1.0 | January 19, 2026*
