# Figure PDF Check Prompt

## Task

Create exactly one manual PDF figure-inspection results document for `{batch_id}`.

Output path:

- `{output_results_path}`

Use:

- PDF check plan: `{pdf_check_plan_path}`
- note paths: `{note_paths}`
- PDF paths: `{pdf_paths}`
- `figure_evidence_table.csv` path: `{figure_evidence_table_csv_path}`
- special cautions: `{special_cautions}`

This is a results-recording step for manual PDF inspection. Use extracted text and notes as candidate-claim sources, but do not treat extracted text alone as visual confirmation.

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
- Do not force a note claim to fit the PDF if visual inspection contradicts it.

## Scope

Use `{pdf_check_plan_path}` as the primary inspection agenda and `{note_paths}` as the source of candidate claims that need visual confirmation.

For each inspected figure, table, panel, or caption, record:

- `paper`
- `citekey`
- `figure_or_table`
- `panel or caption inspected`
- `candidate claim from the note or PDF-check plan`
- `visual confirmation result`
- `final claim wording`
- `final evidence_summary wording`
- `final causal_status`
- `final uncertainty`
- `proposed notes wording for future figure_evidence_table.csv`
- `ready for promotion`

Allowed `visual confirmation result` values:

- `confirmed`
- `revised`
- `rejected`
- `hold`

Allowed `ready for promotion` values:

- `ready_for_figure_evidence_table`
- `revise_before_promotion`
- `hold_until_methods_checked`
- `do_not_promote`

## Promotion Rules

- Only promote figure claims after panel-to-claim mapping is visually confirmed in the PDF.
- Keep conceptual or schematic figures separate from empirical evidence.
- Keep model-based evidence separate from biological evidence.
- Keep `causal_status` conservative.
- If visual inspection contradicts the note, revise or reject the candidate claim rather than forcing it to fit.
- If caption wording is weaker than the note wording, shrink the claim to match the PDF.
- If figure meaning depends on methods details, supplementary controls, or panel mapping that remain unclear, use `hold` or `hold_until_methods_checked`.

## Required Output Structure

The results document must contain these sections:

```markdown
# Batch scope
# Inspection summary
# Per-figure inspection results
# Claims ready for promotion
# Claims requiring revision
# Claims rejected or held
# Final recommendation
```

## Per-Figure Recording Rules

Within `# Per-figure inspection results`, include one structured entry per inspected figure, table, or panel.

Each entry should clearly state:

- which panel, caption, or figure region was inspected
- whether the candidate claim is confirmed, revised, rejected, or held
- the final wording that should be used later if the claim is promoted
- the final `evidence_summary` wording for future `figure_evidence_table.csv`
- the final `causal_status`
- the final uncertainty statement
- whether the claim is ready for later promotion

Keep final wording concise and promotion-safe. Do not treat this step as the append itself.

## Evidence Safety Rules

- Do not use extracted-text-only claims as confirmed figure-level evidence.
- Do not upgrade correlational or model-comparison evidence into causal wording.
- Keep model-only figures explicitly labeled as model-based evidence.
- Keep robustness controls, ablations, and supplementary comparisons explicitly labeled as controls when appropriate.
- If a figure is mostly schematic, do not promote it as empirical evidence.

## Future Append Boundary

This results file does not update `figure_evidence_table.csv`.

A separate `figure_evidence_table_append_plan` must be created after user approval. The append step should use only claims that are clearly marked `ready_for_figure_evidence_table`.

## Final Recommendation Rules

In `# Final recommendation`, explain:

- which claims are safe to carry forward into a later append plan
- which claims need rewording first
- which claims must stay on hold until methods, captions, or supplementary controls are checked
- whether the next step should be a separate append-plan document rather than direct CSV modification

## After Creating The Results Document

Run these read-only validators and report stdout / stderr summaries:

```powershell
py -3 scripts\validate_notes.py
py -3 scripts\validate_tables.py
py -3 scripts\check_no_leaked_paths.py
```

Do not modify any files based on validator output unless explicitly requested in a later step.
