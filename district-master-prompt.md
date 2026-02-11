# district_master_prompt

**Version:** 1.0  
**Date:** February 5, 2026  
**Purpose:** Orchestrate the complete District Fork research workflow for a single congressional district, executing all AI-automatable prompts in sequence and producing all research outputs.

---

## Overview

This master prompt chains together all District Fork research prompts for a single district. When executed, it will:

1. Load the baseline file and naming conventions
2. Execute all Stage 2 research prompts (electoral history, context, opposition, affirmative)
3. Execute all Stage 3 media prompts (discovery, notes)
4. Produce a complete research package ready for human review

---

## Prerequisites (Required Before Running)

Before executing this master prompt, you must have:

| Prerequisite | File | How to Obtain |
|:-------------|:-----|:--------------|
| Completed baseline | `[district]_baseline.md` | Fill out `baseline_template` manually |
| Census data (optional) | `[district]_census.md` | Download CSV from Census.gov, run `district_census_prompt.md` |
| GitHub prompts | All `district_*_prompt.md` files | Clone from `github.com/gappler/district-fork` |

---

## Input Required

Provide the following information to begin:

```yaml
district: [e.g., TX-28]
baseline_file: [path to completed baseline file]
census_file: [path to census file, or "skip" if not available]
candidates:
  - name: [Full Name]
    party: [D/R/I]
  - name: [Full Name]
    party: [D/R/I]
```

---

## Execution Sequence

### Phase 1: Load Dependencies

1. Load `district_naming_prompt.md` (apply to all outputs)
2. Load the provided baseline file
3. Load census file (if provided)

### Phase 2: Research Execution

Execute the following prompts in order. Each prompt produces a separate output file.

| Step | Prompt | Output File | Dependencies |
|:-----|:-------|:------------|:-------------|
| 2.1 | `district_electoral_history_prompt.md` | `[district]_electoral_history.md` | Baseline |
| 2.2 | `district_context_prompt.md` | `[district]_context.md` | Baseline, Census |
| 2.3 | `district_opposition_prompt.md` | `[district]_opposition_[candidate].md` | Baseline (per candidate) |
| 2.4 | `district_affirmative_prompt.md` | `[district]_affirmative_[candidate].md` | Baseline (per candidate) |

**Note:** Steps 2.3 and 2.4 repeat for each candidate listed in the input.

### Phase 3: Media Discovery

| Step | Prompt | Output File | Dependencies |
|:-----|:-------|:------------|:-------------|
| 3.1 | `district_media_discovery_prompt.md` | `[district]_media_discovery.md` | Candidate list |
| 3.2 | `district_media_notes_prompt.md` | `[district]_media_notes.md` | Media discovery output |

---

## Output Package

Upon completion, the following files will be produced:

```
[district]_electoral_history.md
[district]_context.md
[district]_census.md (if provided)
[district]_opposition_[candidate1].md
[district]_opposition_[candidate2].md
[district]_affirmative_[candidate1].md
[district]_affirmative_[candidate2].md
[district]_media_discovery.md
[district]_media_notes.md
```

---

## Execution Instructions

When running this master prompt:

1. **Clone the repository** to access all prompt files:
   ```
   git clone https://github.com/gappler/district-fork.git
   ```

2. **Provide the input YAML** with district, baseline path, and candidate list

3. **Execute each prompt in sequence**, using the output from previous steps as input where required

4. **Save all outputs** to a single directory using the naming conventions

5. **Report completion** with a summary of all files produced

---

## Error Handling

If a prompt fails or produces incomplete output:

1. Note the failure in the execution log
2. Continue with remaining prompts that don't depend on the failed output
3. Report all failures at the end with suggested remediation

---

## Completion Checklist

Before marking the master prompt complete, verify:

- [ ] Electoral history file produced
- [ ] Context file produced
- [ ] Opposition file produced for each candidate
- [ ] Affirmative file produced for each candidate
- [ ] Media discovery file produced
- [ ] Media notes file produced (if articles were found)
- [ ] All files follow naming conventions
- [ ] All files include YAML metadata blocks

---

## What Happens Next (Human Steps)

After this master prompt completes, the human workflow continues:

1. **Stage 4:** Read priority articles from media discovery
2. **Stage 5:** Interview/drafting with Claude
3. **Stage 6:** Citation pass
4. **Stage 7:** Publish to Substack

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-05 | Initial version. Orchestrates Stages 2-3 of District Fork workflow. |
