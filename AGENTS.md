# AGENTS.md

## Project purpose

This project builds a reproducible literature-review workflow for a field-first survey in systems neuroscience and computational neuroscience.

The immediate goal is not to confirm a predefined PFC / working-memory / subspace direction. The goal is to build a structured evidence base that helps evaluate broad research axes, representative experimental papers, candidate research questions, and feasible computational methods.

## Working principles

1. Do not assume that PFC, working memory, sequence tasks, subspaces, or low-rank RNNs are the center of the project.
2. Start from field-level axes first:
   - brain-wide / distributed computation
   - population dynamics and neural manifolds
   - flexible behavior and cognitive control
   - multi-area communication and routing
   - causal perturbation and model-based intervention
   - NeuroAI and interpretable trained models
3. Treat PFC / frontal working-memory studies as a possible case study, not as the default center.
4. Prefer structured tables over long narrative summaries during early survey stages.
5. Keep all intermediate outputs reproducible, inspectable, and easy to revise.

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
   - `field_axis_matrix.csv`
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

Default workflow:

1. Define the field axis or search scope.
2. Search reliable sources such as PubMed, Semantic Scholar, arXiv, Crossref, or Zotero exports.
3. Save raw metadata before cleaning.
4. Deduplicate by DOI, PMID, arXiv ID, Semantic Scholar ID, title, and year.
5. Classify papers into:
   - field-level review / perspective
   - representative experimental landmark
   - theoretical / computational method
   - case-study paper
   - optional / borderline
6. Extract structured fields:
   - behavior / task
   - scale: single-area, multi-area, brain-wide, connectomics, whole-brain imaging
   - neural object: spikes, firing rates, population state, latent state, manifold, subspace, connectivity, oscillation
   - computation: memory, decision, routing, selection, planning, prediction, control
   - causal status: correlational, perturbational, closed-loop, model-based
   - modeling opportunity
7. Produce tables first, then synthesis.

## Safety and execution

1. Ask before installing packages, deleting files, moving large folders, or running long batch jobs.
2. Do not upload private files or local paths to external services unless explicitly instructed.
3. Do not store API keys in tracked files.
4. Prefer local scripts and transparent outputs over opaque automated workflows.
5. Log major automated searches or extraction runs in `logs/`.

## Interaction style

When reporting progress:

1. State what was changed.
2. State where the output was saved.
3. State what remains uncertain or incomplete.
4. Suggest the next concrete step.
