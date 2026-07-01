# Search Run 001

## 1. Purpose
This document defines the first formal but small search run for the literature survey to validate query quality, script execution, and screening workflows. 

## 2. Scope of run 001
This run focuses strictly on two field axes:
1. population dynamics / neural manifolds
2. brain-wide / distributed computation

## 3. Commands to run later
*(Note: API keys are loaded from `.env` and must not be committed. Semantic Scholar may still return 429 or 5xx transient errors, and the script now retries them.)*

### Axis 1: population dynamics / neural manifolds
**PubMed:**
```bash
python scripts/search_pubmed.py --query "(\"neural population dynamics\" OR \"population dynamics\") AND (neuroscience OR cortex OR \"neural manifolds\")" --topic "pop_dynamics" --max-results 20
```

**Semantic Scholar:**
```bash
python scripts/search_semantic_scholar.py --query "\"neural population dynamics\" \"neural manifolds\" computation dynamics" --topic "pop_dynamics" --max-results 20
```

**arXiv:**
```bash
python scripts/search_arxiv.py --query "all:\"neural population dynamics\" AND all:\"neural manifolds\"" --topic "pop_dynamics" --max-results 20
```

### Axis 2: brain-wide / distributed computation
**PubMed:**
```bash
python scripts/search_pubmed.py --query "(\"brain-wide\" OR \"whole-brain\" OR \"distributed computation\") AND (neural activity OR neural dynamics OR systems neuroscience)" --topic "brain_wide" --max-results 20
```

**Semantic Scholar:**
```bash
python scripts/search_semantic_scholar.py --query "\"brain-wide\" \"distributed computation\" neural dynamics" --topic "brain_wide" --max-results 20
```

**arXiv:**
*(Deferred: Use arXiv only for the population dynamics / computational-methods side if appropriate; otherwise mark arXiv as deferred.)*

## 4. Expected outputs
- **Raw output filename pattern:** `data/raw/YYYYMMDD_search_<source>_<topic>.[json|csv]`
- **CSV output filename pattern:** Cleaned and deduplicated candidates will be appended to `tables/candidate_papers.csv` for human screening.
- **Expected paper types:** Field-level reviews / perspectives; representative experimental landmarks; theoretical and computational methods.

## 5. Screening questions
- Does the paper represent a field-level review, a representative experimental landmark, or a theoretical/computational method?
- Does it explicitly connect neural dynamics, brain-wide coordination, population geometry, causal perturbation, or interpretable models?
- Is it merely a weak neuroscience paper, a pure clinical study without mechanistic population analysis, or a pure machine learning paper without clear neuroscience relevance? (If yes, exclude).
- Can the paper be tracked with a stable identifier (DOI, PMID, arXiv ID, or Semantic Scholar ID)?

## 6. Stop criteria
- **Size Limit:** Stop fetching if 20 results per source per topic are reached (`max-results 20`).
- **Quality Check:** Stop execution and adjust queries if the returned results visibly drift away from systems and computational neuroscience.
- **API Limits:** Stop if transient API errors (e.g., 429/5xx on Semantic Scholar) persist despite the built-in script retries.
- Do not process more than 10 candidate papers deeply in this first pass before reviewing search quality.

## 7. What not to do in this run
- Do not run searches yet.
- Do not modify CSV files.
- Do not modify scripts.
- Do not modify `search_plan_v1.md`.

## 8. How to record results
- Save search metadata in `data/raw/`.
- Append deduplicated results to `tables/candidate_papers.csv`.
- Record any search execution notes, API issues, or manual decisions in `logs/` (e.g., `logs/search_run_001_log.md`).
