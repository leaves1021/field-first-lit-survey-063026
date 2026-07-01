import argparse
import os
import time
import json
from datetime import datetime
from pathlib import Path
import pandas as pd
import requests

def load_project_dotenv():
    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / ".env"
    if not env_path.exists():
        return

    try:
        from dotenv import load_dotenv
    except ImportError:
        print("python-dotenv is not installed; continuing with system environment variables.")
        return

    load_dotenv(dotenv_path=env_path, override=False)

def parse_args():
    parser = argparse.ArgumentParser(description="Search Semantic Scholar and save results.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--topic", required=True, help="Topic for output filenames")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum results to fetch")
    parser.add_argument("--api-key", help="Semantic Scholar API key")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()

def main():
    load_project_dotenv()
    args = parse_args()
    api_key = args.api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    print(f"SEMANTIC_SCHOLAR_API_KEY loaded: {'yes' if api_key else 'no'}")
    
    date_str = datetime.now().strftime("%Y%m%d")
    raw_path = f"data/raw/{date_str}_search_semanticscholar_{args.topic}_raw.json"
    csv_path = f"tables/{date_str}_search_semanticscholar_{args.topic}.csv"
    
    if not args.overwrite:
        if os.path.exists(raw_path) or os.path.exists(csv_path):
            print(f"Error: Output files exist. Use --overwrite to overwrite.")
            return

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("tables", exist_ok=True)
    
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    fields = "title,year,authors,venue,publicationDate,citationCount,externalIds,abstract,url,isOpenAccess,openAccessPdf"
    params = {
        "query": args.query,
        "limit": args.max_results,
        "fields": fields
    }
    
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key
        
    print(f"Searching Semantic Scholar for: '{args.query}'...")

    retryable_status_codes = {429, 500, 502, 503, 504}
    max_retries = 3
    backoff_times = [10, 30, 60]

    res = None
    for attempt in range(max_retries + 1):
        time.sleep(1.1)

        res = requests.get(url, params=params, headers=headers)

        if res.ok:
            break

        if res.status_code in retryable_status_codes and attempt < max_retries:
            retry_after = res.headers.get("Retry-After")
            if retry_after:
                try:
                    wait_time = int(retry_after)
                except ValueError:
                    wait_time = backoff_times[attempt]
            else:
                wait_time = backoff_times[attempt]

            print(
                f"HTTP {res.status_code} from Semantic Scholar API. "
                f"Retrying in {wait_time} seconds (attempt {attempt + 1}/{max_retries})..."
            )
            time.sleep(wait_time)
            continue

        break

    if res is None or not res.ok:
        status_code = res.status_code if res is not None else "unknown"
        error_msg = (
            f"Error: Semantic Scholar API request failed after retries "
            f"(HTTP {status_code}). No output files were written."
        )
        print(error_msg)

        body_snippet = ""
        if res is not None:
            body_snippet = res.text[:500]
            if len(res.text) > 500:
                body_snippet += "..."

        os.makedirs("logs", exist_ok=True)
        with open("logs/semanticscholar_api_error.log", "a", encoding="utf-8") as f:
            f.write(
                f"timestamp: {datetime.now().isoformat()}\n"
                f"status_code: {status_code}\n"
                f"query: {args.query}\n"
                f"url: {res.url if res is not None else url}\n"
                f"response_body_snippet: {body_snippet}\n"
                f"---\n"
            )
        return

    data = res.json()
    
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved raw JSON to {raw_path}")
    
    papers = data.get("data", [])
    records = []
    
    for p in papers:
        ext = p.get("externalIds", {})
        authors = p.get("authors", [])
        authors_str = ", ".join([a.get("name", "") for a in authors])
        oa_pdf = p.get("openAccessPdf")
        oa_url = oa_pdf.get("url", "") if oa_pdf else ""
        
        records.append({
            "source": "Semantic Scholar",
            "title": p.get("title", ""),
            "authors": authors_str,
            "year": p.get("year", ""),
            "venue": p.get("venue", ""),
            "doi": ext.get("DOI", ""),
            "pmid": ext.get("PubMed", ""),
            "pmcid": ext.get("PubMedCentral", ""),
            "arxiv_id": ext.get("ArXiv", ""),
            "semantic_scholar_id": p.get("paperId", ""),
            "url": p.get("url", ""),
            "abstract": p.get("abstract", ""),
            "publication_date": p.get("publicationDate", ""),
            "citation_count": p.get("citationCount", ""),
            "is_open_access": p.get("isOpenAccess", False),
            "open_access_pdf": oa_url,
            "search_query": args.query,
            "retrieved_at": datetime.now().isoformat(),
            "raw_file": raw_path,
            "notes": ""
        })
        
    df = pd.DataFrame(records)
    df.to_csv(csv_path, index=False)
    print(f"Saved {len(records)} records to {csv_path}")

if __name__ == "__main__":
    main()
