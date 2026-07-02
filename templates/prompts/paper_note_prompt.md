# Paper Note Generation Prompt

## Task

Create exactly one full-text paper note for `{batch_id}`.

Target paper:

- citekey: `{citekey}`
- title: `{paper_title}`
- output note path: `{output_note_path}`

Use:

- confirmed paper metadata from `{confirmed_papers_csv_path}`
- extracted full text from `{extracted_text_path}`
- PDF path for reference only: `{pdf_path}`
- optional prior note schema reference: `{prior_note_schema_reference}`
- special cautions: `{special_cautions}`

The prior note schema reference is only for formatting and section style. Do not use it as scientific evidence for this paper.

Language and terminology:
- Use Simplified Chinese for explanations.
- Keep technical filenames, field names, code identifiers, commands, and standard technical terms in English.

## Do Not

- Do not create notes other than `{output_note_path}`.
- Do not modify CSV files.
- Do not update `tables/paper_matrix.csv`.
- Do not update `tables/figure_evidence_table.csv`.
- Do not modify scripts.
- Do not modify `references.bib`.
- Do not run searches.
- Do not download PDFs.
- Do not extract text.
- Do not copy long verbatim passages from the paper or extracted text.
- Do not infer figure-level claims from abstract alone.

## Required Note Sections

The note must contain these exact top-level headings:

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

## Required Content Rules

In `# Citation metadata`, include title, authors, year, venue, DOI, PMID, PMCID, arXiv ID, Semantic Scholar ID, citekey, PDF path, and extracted text path when available from `{confirmed_papers_csv_path}`.

In `# One-paragraph summary`, write a concise paraphrased summary. Do not copy long passages.

In `# Main findings`, use bullet points. Each finding should point to a figure, table, result section, or page when available. If the anchor is unclear, write `unclear`.

In `# Figure-by-figure evidence map`, separate:

- paper claim
- extracted evidence
- model / agent interpretation
- user-facing survey interpretation

Mark uncertainty explicitly. Keep model-based evidence separate from biological evidence. Keep `causal_status` conservative, using terms such as `correlational`, `observational`, `methodological`, `simulation-based`, `model-based`, `biological data + model comparison`, `conceptual`, `speculative`, `learning contrast`, `geometric analysis`, or `methodological support`.

List which figures, panels, tables, or supplementary figures require manual PDF inspection before promotion to `tables/figure_evidence_table.csv`.

## Candidate `paper_matrix.csv` Section

The candidate table header must exactly match:

```markdown
| paper | citekey | year | category | field_axis | species | brain_area_or_scale | task_or_behavior | neural_measurement | neural_object | computation | causal_status | key_finding_short | modeling_opportunity | identifiers | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Provide proposed rows only. Do not update `tables/paper_matrix.csv`.

## Candidate `figure_evidence_table.csv` Section

The candidate table header must exactly match:

```markdown
| paper | citekey | figure_or_table | result_section | page | claim | evidence_summary | variable_or_neural_object | analysis_method | causal_status | relevance_to_research_question | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Provide proposed rows only. Do not update `tables/figure_evidence_table.csv`.

## Evidence Safety Rules

- Do not treat Introduction or Discussion framing as direct figure-level evidence unless supported by Results or figures.
- Do not treat review-level statements as primary experimental evidence.
- Do not promote extracted-text-only claims as confirmed figure evidence.
- If extracted text lacks captions, panels, formulas, supplementary mapping, or page anchors, state that manual PDF inspection is required.
- Preserve uncertainty instead of filling gaps with plausible claims.

## After Creating The Note

Run these read-only validators and report stdout / stderr summaries:

```powershell
py -3 scripts\validate_notes.py
py -3 scripts\validate_tables.py
py -3 scripts\check_no_leaked_paths.py
```

If `py -3` is unavailable in the current environment, use the project virtual environment Python interpreter if available. Do not install packages or modify files just to make validators run.

Do not modify any files based on validator output unless explicitly asked in a later step.
