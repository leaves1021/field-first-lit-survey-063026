# Figure Evidence Table Promotion Prompt

## Task

Create exactly one `figure_evidence_table.csv` append-plan document for `{batch_id}`.

Output path:

- `{output_append_plan_path}`

Use:

- PDF-check results: `{pdf_check_results_path}`
- note paths: `{note_paths}`
- `figure_evidence_table.csv` path: `{figure_evidence_table_csv_path}`
- special cautions: `{special_cautions}`

This is an append-planning step based on already inspected PDF evidence. It does not modify `figure_evidence_table.csv`, and it must not convert unresolved or excluded claims into append rows.

Language and terminology:
- Use Simplified Chinese for explanations.
- Keep technical filenames, field names, code identifiers, commands, and standard technical terms in English.

## Do Not

- Do not modify notes.
- Do not modify CSV files.
- Do not update `figure_evidence_table.csv`.
- Do not update `paper_matrix.csv`.
- Do not create new paper notes.
- Do not modify scripts.
- Do not modify `references.bib`.
- Do not run searches.
- Do not download PDFs.
- Do not extract text.
- Do not copy long verbatim text from papers.
- Do not include claims marked `hold_until_methods_checked`.
- Do not include claims marked `do_not_promote`.
- Do not turn `revise_before_promotion` claims into append rows in this step.

## Scope

Use `{pdf_check_results_path}` as the primary source of promotion-ready figure claims, and `{note_paths}` only as supporting context if needed to clarify wording or identifiers.

Only claims marked:

- `ready_for_figure_evidence_table`

may be converted into proposed append rows.

Claims marked:

- `revise_before_promotion`
- `hold_until_methods_checked`
- `do_not_promote`

must not be converted into proposed rows in this step.

## Required Output Structure

The append-plan document must contain these sections:

```markdown
# Batch scope
# Source PDF-check results
# Proposed figure_evidence_table.csv append rows
# Duplicate / conflict check
# Claims excluded from this append plan
# Field normalization notes
# Final recommendation
```

## Exact Target Header

All proposed rows must use this exact `figure_evidence_table.csv` header:

```text
paper,citekey,figure_or_table,result_section,page,claim,evidence_summary,variable_or_neural_object,analysis_method,causal_status,relevance_to_research_question,uncertainty,notes
```

Do not invent alternative field names.

## Proposed Row Rules

Within `# Proposed figure_evidence_table.csv append rows`, include only rows derived from claims marked `ready_for_figure_evidence_table`.

For each proposed row, check and state whether the row has:

- non-empty `paper`
- non-empty `citekey`
- non-empty `figure_or_table`
- non-empty `claim`
- non-empty `evidence_summary`
- non-empty `causal_status`
- non-empty `uncertainty`

Also check:

- duplicate `paper + citekey + figure_or_table` against existing `{figure_evidence_table_csv_path}`
- whether `causal_status` remains conservative

If a row fails these checks, do not place it under proposed append rows. Move it to `# Claims excluded from this append plan` and explain why.

## Duplicate / Conflict Rules

Within `# Duplicate / conflict check`, explicitly review:

- exact duplicate `paper + citekey + figure_or_table`
- obvious near-duplicate entries that describe the same figure with only minor wording differences
- conflicts between the planned row wording and any existing row already present in `{figure_evidence_table_csv_path}`

If a duplicate or conflict is found, do not silently merge it. Describe the issue and keep the plan conservative.

## Excluded Claims Rules

Within `# Claims excluded from this append plan`, include:

- all `revise_before_promotion` claims, with a short note that they require a later revision pass before inclusion
- all `hold_until_methods_checked` claims, with a short note that they must not be promoted yet
- any `do_not_promote` claims if they exist
- any would-be row that failed required-field or duplicate/conflict checks

Do not convert excluded claims into row previews.

## Field Normalization Rules

Within `# Field normalization notes`, explain any minimal normalization applied while planning rows, such as:

- keeping `figure_or_table` wording consistent with the PDF-check results
- keeping `causal_status` conservative
- keeping robustness / control figures clearly labeled as control evidence
- keeping model-based figures clearly labeled as model-based evidence
- keeping uncertainty wording explicit rather than implied

Do not normalize by strengthening claims.

## Final Recommendation Rules

The document must end with exactly one of:

- `ready_for_user_approval`
- `needs_revision`
- `hold`

Use:

- `ready_for_user_approval` if the proposed rows are complete, conservative, and conflict-free
- `needs_revision` if only excluded/revision items block a clean append plan
- `hold` if duplicate/conflict or evidence-boundary issues make even the ready claims unsafe to plan

In `# Final recommendation`, explain:

- how many rows are proposed
- whether any duplicate/conflict issues were found
- which excluded claims need a later revision or methods-check pass
- that a separate later step is still required to append approved rows into `figure_evidence_table.csv`

## After Creating The Append-Plan Document

Run these read-only validators and report stdout / stderr summaries:

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

If the project `.venv` is unavailable, stop and report the issue rather than using an unverified interpreter.

Do not modify any files based on validator output unless explicitly requested in a later step.
