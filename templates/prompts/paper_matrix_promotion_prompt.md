# Paper Matrix Promotion Prompt

## Task

Create exactly one `paper_matrix.csv` append-plan document for `{batch_id}`.

Output path:

- `{output_append_plan_path}`

Use:

- note paths: `{note_paths}`
- note QC path: `{note_qc_path}`
- `paper_matrix.csv` path: `{paper_matrix_csv_path}`
- `confirmed_papers.csv` path: `{confirmed_papers_csv_path}`
- special cautions: `{special_cautions}`

Language and terminology:
- Use Simplified Chinese for explanations.
- Keep technical filenames, field names, code identifiers, commands, and standard technical terms in English.

## Do Not

- Do not modify notes.
- Do not modify CSV files.
- Do not update `paper_matrix.csv`.
- Do not update `figure_evidence_table.csv`.
- Do not create new paper notes.
- Do not modify scripts.
- Do not modify `references.bib`.
- Do not run searches.
- Do not download PDFs.
- Do not extract text.
- Do not copy long verbatim text from papers or extracted text.
- Do not promote figure-level evidence.

## Scope

Use `{note_paths}` as the source of candidate `paper_matrix.csv` rows and `{note_qc_path}` as the QC basis for deciding which rows are ready for a later append.

This step creates an append-plan document only. It does not append rows and does not modify `paper_matrix.csv`.

## Required Append-Plan Structure

The append plan must include these sections:

```markdown
# Batch scope
# Source notes
# QC basis
# Proposed paper_matrix.csv append rows
# Duplicate / conflict check
# Field normalization notes
# Rows not ready for append
# Final recommendation
```

## Required `paper_matrix.csv` Header

Proposed append rows must use the exact `paper_matrix.csv` header:

```text
paper,citekey,year,category,field_axis,species,brain_area_or_scale,task_or_behavior,neural_measurement,neural_object,computation,causal_status,key_finding_short,modeling_opportunity,identifiers,uncertainty,notes
```

When presenting proposed rows in Markdown-table form, preserve the exact column order implied by this header.

## Required Checks For Each Proposed Row

Check whether each proposed row has:

- non-empty `paper`
- non-empty `citekey`
- non-empty `year`
- non-empty `category`
- non-empty `field_axis`
- non-empty `causal_status`

Also check:

- duplicate `citekey` against existing `{paper_matrix_csv_path}`
- obvious duplicate `paper` / `year` conflict against existing `{paper_matrix_csv_path}`
- whether `category`, `field_axis`, and `causal_status` are conservative and consistent with current vocabulary

If a row fails one of these checks, move it to `# Rows not ready for append` instead of forcing it into the proposed append block.

## Proposed Append Rows

Within `# Proposed paper_matrix.csv append rows`:

- include only rows that are supported by validated notes and QC
- keep wording concise and promotion-safe
- keep figure-level details out of this section
- use note-level findings only

Do not include candidate rows that depend on unresolved PDF figure inspection for their core validity.

## Duplicate / Conflict Check

Within `# Duplicate / conflict check`, explicitly record:

- duplicate `citekey` checks against `{paper_matrix_csv_path}`
- possible title or year conflicts
- rows that may overlap conceptually but are still distinct papers
- rows that should be held because normalization is not stable yet

## Field Normalization Notes

Within `# Field normalization notes`, explain any conservative cleanup applied to:

- `category`
- `field_axis`
- `causal_status`
- `brain_area_or_scale`
- `computation`

Keep normalization conservative. Do not invent stronger claims than the notes support.

## Separation From Figure Evidence

- This append plan must not include figure-level rows.
- `figure_evidence_table.csv` remains separate.
- Figure evidence promotion requires PDF inspection and a separate append plan.

## Final Recommendation

End the plan with exactly one of:

- `ready_for_user_approval`
- `needs_note_cleanup`
- `hold`

Choose conservatively based on note quality, QC status, duplicate risk, and vocabulary stability.

## After Creating The Append-Plan Document

Run these read-only validators and report stdout / stderr summaries:

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

If the project `.venv` is unavailable, stop and report the issue rather than using an unverified interpreter.

Do not modify any files based on validator output unless explicitly requested in a later step.
