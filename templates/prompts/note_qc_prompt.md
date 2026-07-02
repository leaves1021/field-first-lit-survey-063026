# Note QC Prompt

## Task

Create exactly one QC review document for `{batch_id}`.

Output path:

- `{output_qc_path}`

Use:

- note paths: `{note_paths}`
- `paper_matrix.csv` path: `{paper_matrix_csv_path}`
- `figure_evidence_table.csv` path: `{figure_evidence_table_csv_path}`
- `confirmed_papers.csv` path: `{confirmed_papers_csv_path}`
- special cautions: `{special_cautions}`

Existing Run001 notes may be used only as schema and formatting examples. Do not use them as scientific evidence for the current batch unless they are explicitly included in `{note_paths}`.

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

## QC Scope

For each note in `{note_paths}`, review the note before any candidate entries are promoted into `paper_matrix.csv` or `figure_evidence_table.csv`.

Check:

- schema completeness
- whether all required sections exist
- whether candidate `paper_matrix.csv` rows use the exact expected header
- whether candidate `figure_evidence_table.csv` rows use the exact expected header
- whether main findings have figure / page / result-section anchors
- whether paper claim, extracted evidence, model interpretation, and survey interpretation are separated
- whether biological evidence, model evidence, methodological evidence, and review-level evidence are separated
- whether `causal_status` is conservative
- whether uncertainty is explicitly marked

## Required Note Schema Reference

Treat the following top-level headings as the new-schema reference:

```markdown
# Citation metadata
# One-paragraph summary
# Research question
# Task / behavior
# Species / brain area / recording method
# Neural object analyzed
# Main findings
# Figure-by-figure evidence map
# Modeling relevance
# Relation to field-first survey axes
# Uncertainty / caveats
# Candidate entries for future `paper_matrix.csv`
# Candidate entries for future `figure_evidence_table.csv`
```

## Candidate Header Checks

Compare candidate rows against the real CSV headers from `{paper_matrix_csv_path}` and `{figure_evidence_table_csv_path}`.

The candidate `paper_matrix.csv` header must exactly match:

```markdown
| paper | citekey | year | category | field_axis | species | brain_area_or_scale | task_or_behavior | neural_measurement | neural_object | computation | causal_status | key_finding_short | modeling_opportunity | identifiers | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

The candidate `figure_evidence_table.csv` header must exactly match:

```markdown
| paper | citekey | figure_or_table | result_section | page | claim | evidence_summary | variable_or_neural_object | analysis_method | causal_status | relevance_to_research_question | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Identify missing fields such as `citekey`, `notes`, or any non-standard header names.

## Promotion Readiness Labels

For each note, assign one or more readiness labels as appropriate:

- `paper_matrix_ready`
- `paper_matrix_ready_after_minor_cleanup`
- `figure_evidence_ready_after_pdf_check`
- `figure_evidence_not_ready`
- `hold`

Default to conservative readiness labels when evidence anchors, table headers, or PDF-inspection status are uncertain.

Use these labels conservatively. A note can be structurally complete but still require PDF inspection before figure-level promotion.

## Manual PDF Inspection Needs

For each note, list exact manual PDF inspection needs, including:

- exact figure or table
- panel or caption if available
- what must be visually checked
- whether the candidate row should be promoted, revised, downgraded, or held

If a figure-level claim depends on caption wording, panel mapping, supplementary control, or geometry that is not secure from extracted text alone, say so explicitly.

## Evidence Rules

- Keep paper claim, extracted evidence, model / agent interpretation, and user-facing survey interpretation clearly separated.
- Keep biological evidence separate from model evidence, methodological evidence, and review-level evidence.
- Keep `causal_status` conservative. Prefer terms such as `correlational`, `observational`, `methodological`, `simulation-based`, `model-based`, `biological data + model comparison`, `conceptual`, `speculative`, `learning contrast`, `geometric analysis`, or `methodological support`.
- Mark uncertainty explicitly instead of filling gaps with plausible claims.

## Required QC Output Structure

The QC document should include at least these sections:

```markdown
# Batch scope
# Overall judgment
# Per-note QC
# Candidate table consistency
# Manual PDF inspection needs
# Final recommendation
```

Within `# Per-note QC`, include for each note:

- schema completeness
- evidence quality
- promotion readiness
- candidate table consistency
- suggested cleanup before promotion

Within `# Final recommendation`, recommend one of:

- revise notes first
- create paper_matrix append plan
- create figure_evidence PDF-check plan
- proceed to append only after user approval

## After Creating The QC Document

Run these read-only validators and report stdout / stderr summaries:

```powershell
py -3 scripts\validate_notes.py
py -3 scripts\validate_tables.py
py -3 scripts\check_no_leaked_paths.py
```

If `py -3` is unavailable in the current environment, use the project virtual environment Python interpreter if available. Do not install packages or modify files just to make validators run.

Do not modify any files based on validator output unless explicitly requested in a later step.
