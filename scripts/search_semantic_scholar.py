import argparse
import os
import time
import json
from datetime import datetime
import pandas as pd
import requests

def parse_args():
    parser = argparse.ArgumentParser(description="Search Semantic Scholar and save results.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--topic", required=True, help="Topic for output filenames")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum results to fetch")
    parser.add_argument("--api-key", help="Semantic Scholar API key")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()

def main():
    args = parse_args()
    api_key = args.api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    
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
    
    max_retries = 3
    backoff_times = [10, 30, 60]
    
    for attempt in range(max_retries + 1):
        if attempt == 0:
            time.sleep(1.1)
            
        res = requests.get(url, params=params, headers=headers)
        
        if res.status_code == 429:
            if attempt < max_retries:
                retry_after = res.headers.get("Retry-After")
                if retry_after and retry_after.isdigit():
                    wait_time = int(retry_after)
                else:
                    wait_time = backoff_times[attempt]
                
                print(f"HTTP 429 Too Many Requests. Retrying in {wait_time} seconds (attempt {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
                continue
            else:
                error_msg = "Error: Semantic Scholar API rate limit exceeded after all retries.\nConsider setting the SEMANTIC_SCHOLAR_API_KEY environment variable to increase your rate limits."
                print(error_msg)
                os.makedirs("logs", exist_ok=True)
                with open("logs/semanticscholar_429_error.log", "a") as f:
                    f.write(f"{datetime.now().isoformat()} - {error_msg}\nURL: {res.url}\n")
                return
                
        res.raise_for_status()
        break
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
