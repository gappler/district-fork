# District Fork Naming Convention v1.0

Standard naming for all prompts and outputs in District Fork. Attach this file to prompts or load into project files.

---

## Prompt File Naming

**Pattern:** `district_[function]_prompt_v[version].md`

| Prompt | Filename |
|:---|:---|
| District Research | `district_research_prompt_v1.0.md` |
| Opposition Research | `district_opposition_prompt_v1.0.md` |
| Affirmative Research | `district_affirmative_prompt_v1.0.md` |
| Media Discovery | `district_media_discovery_prompt_v1.0.md` |
| Media Triage | `district_media_triage_prompt_v1.0.md` |
| Writing | `district_writing_prompt_v1.0.md` |

---

## Output File Naming

**Pattern:** `[district]_[type]_[candidate if applicable]_v[prompt version].md`

| Output Type | Code | Example |
|:---|:---|:---|
| District Research | `overview` | `TX-28_overview_v1.0.md` |
| Opposition Research | `opposition` | `TX-28_opposition_henry_cuellar_v1.0.md` |
| Affirmative Research | `affirmative` | `TX-28_affirmative_henry_cuellar_v1.0.md` |
| Media Discovery | `media_discovery` | `TX-28_media_discovery_v1.0.md` |
| Media Triage | `media_triage` | `TX-28_media_triage_v1.0.md` |

**Candidate names:** lowercase, underscore between first and last: `henry_cuellar`

---

## Output Header

**CRITICAL:** The document's first heading (H1) must match the output filename (without the `.md` extension). This ensures consistent file naming when the document is saved.

**Example H1:** `# TX-28_opposition_henry_cuellar_v1.0`

Include YAML metadata block immediately after the H1:

```yaml
---
district: TX-28
type: opposition
candidate: henry_cuellar
date: 2026-01-19
prompt: district_opposition_prompt_v1.0.md
prompt_version: 1.0
---
```

| Field | Required | Notes |
|:---|:---|:---|
| district | Yes | Standard code (TX-28, NC-01) |
| type | Yes | overview, opposition, affirmative, media_discovery, media_triage |
| candidate | If applicable | For opposition/affirmative only |
| date | Yes | YYYY-MM-DD |
| prompt | Yes | Filename of prompt that created this |
| prompt_version | Yes | Version of prompt that created this |

---

## Versioning

**Prompts:** Update version when you change the prompt.
- Patch (minor tweak): v1.0 → v1.0.1
- Minor (new section or capability): v1.0.1 → v1.1
- Major (significant restructure): v1.1 → v2.0

**Outputs:** Inherit prompt version. The version in the filename reflects the prompt version, not output iterations.

If you rerun the same prompt on the same district/candidate:
- `TX-28_opposition_henry_cuellar_v1.0.md` (first run)
- `TX-28_opposition_henry_cuellar_v1.0_run2.md` (second run)
- `TX-28_opposition_henry_cuellar_v1.0_run3.md` (third run)

The `_run#` suffix tracks iterations. The `v1.0` stays constant unless the prompt itself changes.

---

## Integration

Add this line to each prompt:

> **Naming:** Follow the conventions in the attached `district_fork_naming_convention_v1.0.md` file.

---

## Quick Reference

```
PROMPTS:  district_[function]_prompt_v[version].md
OUTPUTS:  [district]_[type]_[candidate]_v[prompt version].md

TYPES:    overview, opposition, affirmative, media_discovery, media_triage
NAMES:    first_last (lowercase, underscore)
HEADER:   YAML with district, type, candidate, date, prompt, prompt_version
```

---

*Version 1.0 | 2026-01-19*
