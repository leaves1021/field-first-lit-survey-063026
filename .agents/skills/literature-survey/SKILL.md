---
name: literature-survey
description: Use this skill for field-first systems/computational neuroscience literature surveys, including paper search, metadata cleanup, evidence matrices, PDF-based notes, and synthesis. Use it when the task involves literature review automation, candidate paper screening, figure-level evidence extraction, or research-question mapping.
---

# Literature Survey Skill

## Purpose

Use this skill to perform structured, reproducible literature-review work for systems neuroscience and computational neuroscience.

The survey should be field-first: start from broad research axes and evidence structure before narrowing to any specific topic such as PFC, working memory, sequence tasks, subspaces, or low-rank RNNs.

## Core rules

1. Never invent citations.
2. Prefer stable identifiers:
   - DOI
   - PMID
   - PMCID
   - arXiv ID
   - Semantic Scholar ID
3. Separate:
   - paper claim
   - experimental evidence
   - model or agent inference
   - user's interpretation
4. Do not rely on abstracts alone for core papers.
5. For each key finding, identify the figure, result section, table, or supplementary item when available.
6. Mark uncertainty explicitly.
7. Prefer structured tables before narrative synthesis.

## Standard workflow

### Step 1: Define scope

Identify the current survey axis or task type:

- brain-wide / distributed computation
- population dynamics and neural manifolds
- flexible behavior and cognitive control
- multi-area communication and routing
- causal perturbation and model-based intervention
- NeuroAI and interpretable trained models
- PFC / frontal working-memory case study
- computational methods and modeling

If the user asks for a predefined topic, keep the topic but avoid assuming it is the project center.

### Step 2: Search and save raw metadata

Use reliable sources when available. Prefer using standard project scripts under `scripts/` when they exist:

- `scripts/search_pubmed.py`
- `scripts/search_semantic_scholar.py`
- `scripts/search_arxiv.py`

If the required script does not exist, do not invent a different workflow; report that the script needs to be created.

Save raw outputs under `data/raw/` or `tables/` before cleaning. Use the file naming convention: `YYYYMMDD_search_<source>_<topic>.csv`.

### Step 3: Clean and deduplicate

Deduplicate using:

- DOI
- PMID
- arXiv ID
- Semantic Scholar ID
- normalized title
- year
- first author

Do not merge records if uncertainty remains. Instead, flag them for manual review.

### Step 4: Classify papers

Use these categories:

- field-level review / perspective
- representative experimental landmark
- theoretical / computational method
- case-study paper
- optional / borderline
- excluded

For excluded papers, provide a short reason.

### Step 5: Extract structured fields

For each paper, extract:

- paper
- year
- species / model system
- brain area or recording scale
- task / behavior
- neural measurement
- main neural object
- main computation
- key finding
- causal status
- modeling opportunity
- identifiers
- notes / uncertainty

### Step 6: Read core PDFs

For core papers:

1. Use PDF text from `papers/extracted_text/` when available.
2. If extracted text is missing, prefer `scripts/extract_pdf_text.py` to extract text from `papers/raw_pdf/` to `papers/extracted_text/` using PyMuPDF as the default backend. If the script is missing, report that it needs to be created instead of choosing another PDF library ad hoc.
3. Build a figure-level evidence table.
4. Do not treat claims from Introduction or Discussion as direct evidence unless supported by Results or figures.

### Step 7: Produce outputs

Use these standard outputs:

- `tables/candidate_papers.csv`
- `tables/confirmed_papers.csv`
- `tables/paper_matrix.csv`
- `tables/figure_evidence_table.csv`
- `notes/<first_author>_<year>_<short_title>.md`
- `synthesis/field_axis_map.md`
- `synthesis/candidate_research_questions.md`

## Table schemas

### candidate_papers.csv

Recommended columns:

- source
- title
- authors
- year
- venue
- doi
- pmid
- pmcid
- arxiv_id
- semantic_scholar_id
- url
- abstract
- search_query
- initial_relevance
- notes

### paper_matrix.csv

Recommended columns:

- paper
- year
- category
- field_axis
- species
- brain_area_or_scale
- task_or_behavior
- neural_measurement
- neural_object
- computation
- causal_status
- key_finding_short
- modeling_opportunity
- identifiers
- uncertainty

### figure_evidence_table.csv

Recommended columns:

- paper
- figure_or_table
- result_section
- claim
- evidence_summary
- variable_or_neural_object
- analysis_method
- causal_status
- relevance_to_research_question
- uncertainty

## Notes format

Each paper note should contain:

1. Bibliographic metadata
2. Why this paper is included
3. Task / behavior
4. Neural data and scale
5. Key findings
6. Figure-level evidence
7. Limitations
8. Relation to field axes
9. Modeling opportunity
10. Open questions

## When to stop

Stop and ask for guidance if:

1. The search scope becomes too broad.
2. More than 30 candidate papers are found for a single small task.
3. A paper lacks stable identifiers and cannot be verified.
4. The task requires paid access, credentials, or external upload.
5. A script would modify or delete many files.

## Reporting format

When finishing a task, report:

1. What was done.
2. Files created or modified.
3. Number of records or papers processed.
4. Main uncertainties.
5. Recommended next step.
