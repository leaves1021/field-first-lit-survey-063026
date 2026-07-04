---
name: literature-survey
description: Use this skill for field-first systems/computational neuroscience literature surveys, including paper search, metadata cleanup, evidence matrices, PDF-based notes, and synthesis. Use it when the task involves literature review automation, candidate paper screening, figure-level evidence extraction, or research-question mapping.
---

# Literature Survey Skill

## Purpose

Use this skill to perform structured, reproducible literature-review work for systems neuroscience and computational neuroscience.

The survey is field-first: start from broad research axes and evidence structure before narrowing to any specific topic. For the current field axes, topic constraints, and the rationale for the field-first approach, read `docs/research_context.md` before beginning any search or classification task.

## Core rules

Follow the citation and evidence rules, language conventions, file organization, output conventions, and safety rules defined in `AGENTS.md`. Key points:

1. Never invent citations.
2. Prefer stable identifiers: DOI, PMID, PMCID, arXiv ID, Semantic Scholar ID.
3. Separate paper claims, experimental evidence, model/agent inference, and user interpretation.
4. Do not rely on abstracts alone for core papers.
5. For each key finding, identify the figure, result section, table, or supplementary item when available.
6. Mark uncertainty explicitly.
7. Prefer structured tables before narrative synthesis.

For the full set of rules, refer to `AGENTS.md`.

## Standard workflow

The detailed 10-stage batch workflow is documented in `docs/workflow_quickstart.md`. Summary:

1. **Define scope** — identify the current survey axis or task type.
2. **Search and save raw metadata** — use `scripts/search_pubmed.py`, `scripts/search_semantic_scholar.py`, `scripts/search_arxiv.py`. Save raw outputs under `data/raw/` and per-search CSVs under `tables/`. If a required script does not exist, report it instead of inventing a workflow.
3. **Clean and deduplicate** — by DOI, PMID, arXiv ID, Semantic Scholar ID, normalized title, year, first author. Flag uncertain matches for manual review.
4. **Classify papers** — field-level review/perspective, representative experimental landmark, theoretical/computational method, case-study paper, optional/borderline, excluded.
5. **Extract structured fields** — see table schemas below.
6. **Read core PDFs** — use extracted text from `papers/extracted_text/`. If missing, use `scripts/extract_pdf_text.py`. Build figure-level evidence. Do not treat Introduction/Discussion as direct evidence unless supported by Results or figures.
7. **Produce outputs** — populate the tables and notes listed below.

For stage-by-stage inputs, outputs, human gates, validators, and failure modes, see `docs/workflow_quickstart.md`.

## Standard outputs

- `tables/candidate_papers.csv`
- `tables/confirmed_papers.csv`
- `tables/paper_matrix.csv`
- `tables/figure_evidence_table.csv`
- `notes/<first_author>_<year>_<short_title>.md`

## Table schemas

All schemas below match the authoritative CSV templates under `templates/`. Agents must use these exact column sets.

### candidate_papers.csv

Columns (in order):

```
source,title,authors,year,venue,doi,pmid,pmcid,arxiv_id,semantic_scholar_id,url,abstract,search_query,search_topic,retrieved_at,raw_file,initial_relevance,status,notes
```

### confirmed_papers.csv

Columns (in order):

```
citekey,title,authors,year,venue,doi,pmid,pmcid,arxiv_id,semantic_scholar_id,zotero_key,zotero_collection,pdf_path,extracted_text_path,status,confirmed_by,confirmed_at,notes
```

### paper_matrix.csv

Columns (in order):

```
paper,citekey,year,category,field_axis,species,brain_area_or_scale,task_or_behavior,neural_measurement,neural_object,computation,causal_status,key_finding_short,modeling_opportunity,identifiers,uncertainty,notes
```

### figure_evidence_table.csv

Columns (in order):

```
paper,citekey,figure_or_table,result_section,page,claim,evidence_summary,variable_or_neural_object,analysis_method,causal_status,relevance_to_research_question,uncertainty,notes
```

## Notes format

Each paper note must contain these exact top-level headings (checked by `scripts/validate_notes.py`):

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
