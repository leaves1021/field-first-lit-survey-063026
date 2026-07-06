# AGENTS.md

## Authority map

| document | purpose |
|---|---|
| `AGENTS.md` | repo-level agent rules (this file) |
| `docs/workflow_quickstart.md` | detailed batch workflow: stages, inputs, outputs, human gates |
| `docs/status_vocabulary.md` | authoritative status and label definitions |
| `docs/file_retention_policy.md` | file retention, archive, and cleanup rules |
| `templates/*.csv` | CSV schema source of truth |
| `docs/research_context.md` | current research framing and field axes |

When in doubt about current research scope or field axes, read `docs/research_context.md` before acting.

## Project purpose

This project builds a reproducible literature-review workflow for a field-first survey in systems neuroscience and computational neuroscience. The goal is to build a structured evidence base that helps evaluate broad research axes, representative experimental papers, candidate research questions, and feasible computational methods.

For current research framing, field axes, and topic constraints, see `docs/research_context.md`.

## Citation and evidence rules

1. Never invent citations.
2. Every candidate paper should include at least one stable identifier when available:
   - DOI
   - PMID
   - PMCID
   - arXiv ID
   - Semantic Scholar ID
3. Separate clearly:
   - paper claims
   - experimental evidence
   - model or agent inference
   - user's interpretation
4. Do not treat review-paper summaries as primary experimental evidence.
5. For core papers, do not rely on abstracts alone. Use the full PDF text when available.
6. For each key finding, identify the relevant figure, result section, table, or supplementary figure when possible.
7. Mark uncertainty explicitly instead of filling gaps with plausible-sounding claims.

## File organization

Use the existing project structure:

- `references.bib`: Zotero / Better BibTeX export. Treat it as the confirmed citation database.
- `papers/raw_pdf/`: original PDF files.
- `papers/extracted_text/`: extracted text from PDFs.
- `papers/supplementary/`: supplementary files.
- `notes/`: paper-level notes.
- `tables/`: CSV / Markdown evidence matrices.
- `synthesis/`: higher-level summaries and drafts.
- `scripts/`: reproducible scripts.
- `templates/`: reusable templates.
- `logs/`: logs of searches, extraction, and workflow decisions.
- `data/raw/`: raw API outputs or downloaded metadata.
- `data/processed/`: cleaned metadata and derived tables.

## Output conventions

1. Use Markdown for notes and synthesis.
2. Use CSV for tabular data intended for later analysis.
3. Use clear filenames:
   - `YYYYMMDD_search_<source>_<topic>.csv`
   - `<first_author>_<year>_<short_title>.md`
   - `candidate_papers.csv`
   - `confirmed_papers.csv`
   - `paper_matrix.csv`
   - `figure_evidence_table.csv`
4. Do not overwrite existing non-empty files unless explicitly asked.
5. If a file already exists and changes are needed, summarize the planned changes before editing.

## Language and documentation conventions

1. Use Simplified Chinese by default for user-facing communication, including task summaries, explanations, progress reports, error explanations, and final responses.
2. Use Simplified Chinese by default for human-facing documentation, including `README.md`, usage notes, workflow explanations, and project-level guides.
3. Keep standard technical terms in English when they are standard in the field, especially for systems neuroscience, computational neuroscience, machine learning, programming, APIs, and command-line workflows.
4. Do not translate variable names, function names, class names, filenames, directory names, command-line arguments, package names, API names, environment variables, or code identifiers.
5. Preserve the original language of direct quotations, paper titles, code snippets, command outputs, error messages, and citation metadata unless the user explicitly asks for translation.
6. If the user explicitly requests English, bilingual output, or another language, follow the user's request.

## Literature-survey workflow

The full workflow is documented in `docs/workflow_quickstart.md`. Default stage sequence:

1. Define the field axis or search scope (see `docs/research_context.md` for current axes).
2. Search reliable sources such as PubMed, Semantic Scholar, arXiv, Crossref, or Zotero exports.
3. Save raw metadata before cleaning.
4. Deduplicate by DOI, PMID, arXiv ID, Semantic Scholar ID, title, and year.
5. Classify papers into: field-level review / perspective, representative experimental landmark, theoretical / computational method, case-study paper, optional / borderline.
6. Extract structured fields (see `templates/*.csv` for exact schemas).
7. Produce tables first, then synthesis.

## Safety and execution

1. Ask before installing packages, deleting files, moving large folders, or running long batch jobs.
2. Do not upload private files or local paths to external services unless explicitly instructed.
3. Do not store API keys in tracked files.
4. Prefer local scripts and transparent outputs over opaque automated workflows.
5. Log major automated searches or extraction runs in `logs/`.

## Python environment and validation commands

1. Prefer the project-local virtual environment under `.venv`.
2. On this project, prefer `.\.venv\Scripts\python.exe` over `py`, bare `python`, or other launcher-based commands when running scripts or validators from Windows PowerShell.
3. Prefer validation commands in this form:

   ```powershell
   & .\.venv\Scripts\python.exe .\scripts\validate_tables.py
   & .\.venv\Scripts\python.exe .\scripts\validate_notes.py
   & .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
   ```

4. If the project `.venv` is unavailable, stop and report the issue rather than using an unverified interpreter.

## Interaction style

When reporting progress:

1. State what was changed.
2. State where the output was saved.
3. State what remains uncertain or incomplete.
4. Suggest the next concrete step.
