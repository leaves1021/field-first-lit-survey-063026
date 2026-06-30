import argparse
import os
import time
from datetime import datetime
import pandas as pd
import requests

try:
    import feedparser
except ImportError:
    print("Error: 'feedparser' is required for arXiv search. Install with 'pip install feedparser'.")
    exit(1)

def parse_args():
    parser = argparse.ArgumentParser(description="Search arXiv and save results.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--topic", required=True, help="Topic for output filenames")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum results to fetch")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()

def main():
    args = parse_args()
    
    date_str = datetime.now().strftime("%Y%m%d")
    raw_path = f"data/raw/{date_str}_search_arxiv_{args.topic}_raw.xml"
    csv_path = f"tables/{date_str}_search_arxiv_{args.topic}.csv"
    
    if not args.overwrite:
        if os.path.exists(raw_path) or os.path.exists(csv_path):
            print(f"Error: Output files exist. Use --overwrite to overwrite.")
            return

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("tables", exist_ok=True)
    
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": args.query,
        "start": 0,
        "max_results": args.max_results
    }
    
    print(f"Searching arXiv for: '{args.query}'...")
    time.sleep(3.1)
    
    res = requests.get(url, params=params)
    res.raise_for_status()
    
    with open(raw_path, "wb") as f:
        f.write(res.content)
    print(f"Saved raw XML to {raw_path}")
    
    feed = feedparser.parse(res.content)
    records = []
    
    for entry in feed.entries:
        authors = [a.get("name", "") for a in entry.get("authors", [])]
        authors_str = ", ".join(authors)
        
        arxiv_id = entry.id.split("/abs/")[-1] if "/abs/" in entry.id else ""
        
        pub_date = entry.get("published", "")
        year = pub_date[:4] if pub_date else ""
        
        doi = entry.get("arxiv_doi", "")
        
        records.append({
            "source": "arXiv",
            "title": entry.get("title", "").replace('\n', ' '),
            "authors": authors_str,
            "year": year,
            "venue": "arXiv",
            "doi": doi,
            "arxiv_id": arxiv_id,
            "url": entry.get("link", ""),
            "abstract": entry.get("summary", "").replace('\n', ' '),
            "publication_date": pub_date,
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
