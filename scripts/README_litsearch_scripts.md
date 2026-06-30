# Literature Search Scripts

This directory contains standalone, portable Python scripts for performing reproducible literature searches against standard academic databases. These scripts fetch metadata, handle basic rate-limiting, and save both raw outputs (JSON/XML) and cleaned tabular summaries (CSV).

## Required Python Packages

Before running the scripts, ensure you have the following packages installed:

```bash
pip install requests pandas feedparser
```

## Configuration & Environment Variables

To respect database usage policies and obtain higher rate limits, you should provide optional API keys and contact information via environment variables:

- **`NCBI_API_KEY`**: (Optional) API key for PubMed/NCBI. Increases limit from 3 req/sec to 10 req/sec.
- **`NCBI_EMAIL`**: (Recommended) Contact email for NCBI, required by their terms of service.
- **`SEMANTIC_SCHOLAR_API_KEY`**: (Optional) API key for Semantic Scholar Academic Graph.

Alternatively, you can pass these directly to the scripts using `--api-key` and `--email` arguments.

## File Output Locations

All scripts enforce the project's output file conventions:

- **Raw metadata** is saved to `data/raw/` in the format:
  `YYYYMMDD_search_<source>_<topic>_raw.<json/xml>`
- **Cleaned data** is saved to `tables/` in the format:
  `YYYYMMDD_search_<source>_<topic>.csv`

To prevent accidental data loss, the scripts **will not overwrite existing files** unless explicitly told to do so via the `--overwrite` flag.

## Example Commands

### 1. PubMed Search
```bash
python scripts/search_pubmed.py --query "prefrontal cortex working memory" --topic "pfc_wm" --max-results 50
```

### 2. Semantic Scholar Search
```bash
python scripts/search_semantic_scholar.py --query "low rank rnn" --topic "lowrank_rnn" --max-results 20
```

### 3. arXiv Search
```bash
python scripts/search_arxiv.py --query "neural manifold" --topic "manifolds" --max-results 100 --overwrite
```

## Rate-Limit Assumptions

The scripts implement conservative defaults to ensure compliance with API terms:
- **PubMed**: 0.4 second delay between requests.
- **Semantic Scholar**: 1.1 second delay between requests.
- **arXiv**: 3.1 second delay per request to respect their strict 3-second limit.

Always prefer using API keys if performing large or concurrent queries.
