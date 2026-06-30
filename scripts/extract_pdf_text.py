import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
import logging

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        print("Error: PyMuPDF is required. Install it with `pip install pymupdf`", file=sys.stderr)
        sys.exit(1)

def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d")
    log_file = log_dir / f"{timestamp}_extract_pdf_text.log"
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return log_file

def sanitize_filename(filename):
    """Return a safe filename string by replacing unsafe characters with underscores."""
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in filename)

def process_pdf(pdf_path, output_dir, overwrite, sort_text, min_chars_per_page, logger):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    
    stem = sanitize_filename(pdf_path.stem)
    output_file = output_dir / f"{stem}.md"
    
    if output_file.exists() and not overwrite:
        logger.info(f"Skipping {pdf_path.name}: Output file {output_file.name} already exists.")
        print(f"Skipping {pdf_path.name}: {output_file.name} already exists. Use --overwrite to overwrite.")
        return "skipped"
        
    try:
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
    except Exception as e:
        logger.error(f"Failed to open {pdf_path.name}: {e}")
        print(f"Error opening {pdf_path.name}: {e}")
        return "error"
        
    total_chars = 0
    pages_text = []
    sparse_pages = 0
    
    for i in range(num_pages):
        page = doc[i]
        try:
            # In recent versions, get_text("text", sort=True) is valid.
            text = page.get_text("text", sort=sort_text)
        except TypeError:
            # Fallback if sort argument is not accepted
            text = page.get_text("text")
            
        pages_text.append(text)
        total_chars += len(text)
        if len(text.strip()) < min_chars_per_page:
            sparse_pages += 1
            
    is_sparse = (sparse_pages > num_pages / 2) if num_pages > 0 else True
    
    timestamp = datetime.now().isoformat()
    pymupdf_version = fitz.VersionBind if hasattr(fitz, "VersionBind") else (fitz.version[0] if hasattr(fitz, "version") else "unknown")
    
    md_content = []
    md_content.append("---")
    md_content.append(f"original_file: {pdf_path.name}")
    md_content.append(f"extraction_time: {timestamp}")
    md_content.append(f"num_pages: {num_pages}")
    md_content.append(f"pymupdf_version: {pymupdf_version}")
    md_content.append("---")
    md_content.append("")
    
    if is_sparse:
        md_content.append("> **Warning**: This document appears to have very little text per page.")
        md_content.append("> It might be a scanned document or image-based PDF requiring OCR.")
        md_content.append("")
        
    for i, text in enumerate(pages_text):
        page_num = i + 1
        md_content.append(f"## Page {page_num}")
        md_content.append("")
        md_content.append(f"<!-- PAGE_{page_num}_START -->")
        if text.strip():
            md_content.append(text)
        else:
            md_content.append("*[No text extracted from this page]*")
        md_content.append("")
        
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))
        
    logger.info(f"Successfully extracted {pdf_path.name} to {output_file.name}")
    return "flagged" if is_sparse else "extracted"

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files using PyMuPDF.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", type=str, help="Path to a single PDF file")
    group.add_argument("--input-dir", type=str, help="Directory containing PDF files")
    
    parser.add_argument("--output-dir", type=str, default="papers/extracted_text", help="Output directory for extracted Markdown files")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing extracted Markdown files")
    parser.add_argument("--no-sort", action="store_false", dest="sort", help="Disable sorted text extraction (enabled by default)")
    parser.add_argument("--min-chars-per-page", type=int, default=50, help="Minimum characters per page to flag likely scanned PDFs (default: 50)")
    
    args = parser.parse_args()
    
    log_file = setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting PDF extraction. Arguments: {vars(args)}")
    
    pdfs_to_process = []
    if args.input:
        pdf_path = Path(args.input)
        if pdf_path.is_file() and pdf_path.suffix.lower() == ".pdf":
            pdfs_to_process.append(pdf_path)
        else:
            print(f"Error: {args.input} is not a valid PDF file.", file=sys.stderr)
            sys.exit(1)
    elif args.input_dir:
        dir_path = Path(args.input_dir)
        if dir_path.is_dir():
            pdfs_to_process = list(dir_path.glob("*.pdf"))
        else:
            print(f"Error: {args.input_dir} is not a valid directory.", file=sys.stderr)
            sys.exit(1)
            
    stats = {"found": len(pdfs_to_process), "extracted": 0, "skipped": 0, "flagged": 0, "error": 0}
    
    for pdf_path in pdfs_to_process:
        status = process_pdf(
            pdf_path=pdf_path,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
            sort_text=args.sort,
            min_chars_per_page=args.min_chars_per_page,
            logger=logger
        )
        if status in stats:
            stats[status] += 1
        
    print("\n--- Extraction Summary ---")
    print(f"PDFs found:         {stats['found']}")
    print(f"Extracted:          {stats['extracted']}")
    print(f"Skipped:            {stats['skipped']}")
    print(f"Flagged (low text): {stats['flagged']}")
    if stats['error'] > 0:
        print(f"Errors:             {stats['error']}")
    print(f"Log written to:     {log_file}")
    
if __name__ == "__main__":
    main()
