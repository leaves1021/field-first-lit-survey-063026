import argparse
import os
import time
import xml.etree.ElementTree as ET
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
    parser = argparse.ArgumentParser(description="Search PubMed and save results.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--topic", required=True, help="Topic for output filenames")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum results to fetch")
    parser.add_argument("--email", help="NCBI email")
    parser.add_argument("--api-key", help="NCBI API key")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()

def main():
    load_project_dotenv()
    args = parse_args()
    
    email = args.email or os.environ.get("NCBI_EMAIL")
    api_key = args.api_key or os.environ.get("NCBI_API_KEY")
    print(f"NCBI_EMAIL loaded: {'yes' if email else 'no'}")
    print(f"NCBI_API_KEY loaded: {'yes' if api_key else 'no'}")
    
    date_str = datetime.now().strftime("%Y%m%d")
    raw_path = f"data/raw/{date_str}_search_pubmed_{args.topic}_raw.xml"
    csv_path = f"tables/{date_str}_search_pubmed_{args.topic}.csv"
    
    if not args.overwrite:
        if os.path.exists(raw_path) or os.path.exists(csv_path):
            print(f"Error: Output files exist. Use --overwrite to overwrite.")
            return

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("tables", exist_ok=True)

    tool = "literature-survey"
    
    # ESearch
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": args.query,
        "retmax": args.max_results,
        "retmode": "json",
        "tool": tool,
        "email": email
    }
    if api_key: 
        search_params["api_key"] = api_key
    
    print(f"Searching PubMed for: '{args.query}'...")
    time.sleep(0.4)
    
    res = requests.get(search_url, params=search_params)
    res.raise_for_status()
    pmids = res.json().get("esearchresult", {}).get("idlist", [])
    
    if not pmids:
        print("No results found.")
        return
        
    print(f"Found {len(pmids)} PMIDs. Fetching details...")
    
    # EFetch
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "tool": tool,
        "email": email
    }
    if api_key: 
        fetch_params["api_key"] = api_key
    
    time.sleep(0.4)
    res = requests.get(fetch_url, params=fetch_params)
    res.raise_for_status()
    
    with open(raw_path, "wb") as f:
        f.write(res.content)
    print(f"Saved raw XML to {raw_path}")
    
    # Parse XML
    root = ET.fromstring(res.content)
    records = []
    
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or ""
        title = article.findtext(".//ArticleTitle") or ""
        
        abstract_elem = article.find(".//Abstract")
        abstract = ""
        if abstract_elem is not None:
            abstract_texts = [text.text for text in abstract_elem.findall(".//AbstractText") if text.text]
            abstract = " ".join(abstract_texts)
            
        authors = []
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            initials = author.findtext("Initials") or ""
            if last: authors.append(f"{last} {initials}".strip())
        authors_str = ", ".join(authors)
        
        journal = article.findtext(".//Journal/Title") or ""
        pub_year = article.findtext(".//JournalIssue/PubDate/Year") or ""
        
        doi = ""
        pmcid = ""
        for el in article.findall(".//ArticleId"):
            id_type = el.get("IdType")
            if id_type == "doi": doi = el.text
            elif id_type == "pmc": pmcid = el.text
            
        records.append({
            "source": "PubMed",
            "title": title,
            "authors": authors_str,
            "year": pub_year,
            "venue": journal,
            "doi": doi,
            "pmid": pmid,
            "pmcid": pmcid,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
            "abstract": abstract,
            "publication_date": pub_year,
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
