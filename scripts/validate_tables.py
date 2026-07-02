#!/usr/bin/env python3
"""Read-only validators for the literature-survey workflow CSV tables."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TABLES = {
    "candidate_papers.csv": ROOT / "tables" / "candidate_papers.csv",
    "confirmed_papers.csv": ROOT / "tables" / "confirmed_papers.csv",
    "paper_matrix.csv": ROOT / "tables" / "paper_matrix.csv",
    "figure_evidence_table.csv": ROOT / "tables" / "figure_evidence_table.csv",
}

EXPECTED_HEADERS = {
    "candidate_papers.csv": [
        "source",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "pmid",
        "pmcid",
        "arxiv_id",
        "semantic_scholar_id",
        "url",
        "abstract",
        "search_query",
        "search_topic",
        "retrieved_at",
        "raw_file",
        "initial_relevance",
        "status",
        "notes",
    ],
    "confirmed_papers.csv": [
        "citekey",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "pmid",
        "pmcid",
        "arxiv_id",
        "semantic_scholar_id",
        "zotero_key",
        "zotero_collection",
        "pdf_path",
        "extracted_text_path",
        "status",
        "confirmed_by",
        "confirmed_at",
        "notes",
    ],
    "paper_matrix.csv": [
        "paper",
        "citekey",
        "year",
        "category",
        "field_axis",
        "species",
        "brain_area_or_scale",
        "task_or_behavior",
        "neural_measurement",
        "neural_object",
        "computation",
        "causal_status",
        "key_finding_short",
        "modeling_opportunity",
        "identifiers",
        "uncertainty",
        "notes",
    ],
    "figure_evidence_table.csv": [
        "paper",
        "citekey",
        "figure_or_table",
        "result_section",
        "page",
        "claim",
        "evidence_summary",
        "variable_or_neural_object",
        "analysis_method",
        "causal_status",
        "relevance_to_research_question",
        "uncertainty",
        "notes",
    ],
}

ALLOWED_STATUS = {
    "candidate_papers.csv": {
        "candidate_title_level",
        "candidate_metadata_verified",
        "candidate_needs_manual_review",
        "candidate_rejected",
        "candidate_hold",
    },
    "confirmed_papers.csv": {
        "confirmed",
        "confirmed_metadata_only",
        "ready_for_pdf_download",
        "ready_for_reading",
        "note_drafted",
        "matrix_ready",
        "hold",
    },
}

CANDIDATE_DUPLICATE_FIELDS = (
    "doi",
    "pmid",
    "pmcid",
    "arxiv_id",
    "semantic_scholar_id",
)
CONFIRMED_DUPLICATE_FIELDS = (
    "citekey",
    "doi",
    "pmid",
    "pmcid",
    "arxiv_id",
    "semantic_scholar_id",
)

CONFIRMED_REQUIRED = {
    "citekey",
    "title",
    "doi",
    "pdf_path",
    "extracted_text_path",
    "status",
}
PAPER_MATRIX_REQUIRED = {
    "paper",
    "citekey",
    "year",
    "category",
    "field_axis",
    "causal_status",
}
FIGURE_EVIDENCE_REQUIRED = {
    "paper",
    "citekey",
    "figure_or_table",
    "claim",
    "evidence_summary",
    "causal_status",
    "uncertainty",
    "notes",
}

NON_IDENTIFIER_VALUES = {"", "unclear", "not_available"}


def normalize(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip()


def is_missing(value: str | None) -> bool:
    return normalize(value) == ""


def is_duplicate_candidate_value(value: str | None) -> bool:
    return normalize(value).lower() not in NON_IDENTIFIER_VALUES


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], list[str]]:
    warnings: list[str] = []
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        header = reader.fieldnames or []
        if reader.line_num == 0:
            warnings.append(f"{path.name}: file appears to be empty")
    return header, rows, warnings


def validate_header(
    filename: str,
    actual: list[str],
    expected: list[str],
    errors: list[str],
) -> None:
    if actual == expected:
        return
    errors.append(
        f"{filename}: header mismatch\n"
        f"  expected: {','.join(expected)}\n"
        f"  actual:   {','.join(actual)}"
    )


def check_duplicates(
    filename: str,
    rows: list[dict[str, str]],
    fields: tuple[str, ...],
    errors: list[str],
) -> None:
    seen: dict[tuple[str, str], list[int]] = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        for field in fields:
            value = normalize(row.get(field))
            if not is_duplicate_candidate_value(value):
                continue
            seen[(field, value)].append(row_number)

    for (field, value), row_numbers in sorted(seen.items()):
        if len(row_numbers) > 1:
            rows_text = ", ".join(str(row_number) for row_number in row_numbers)
            errors.append(
                f"{filename}: duplicate {field} value {value!r} at rows {rows_text}"
            )


def validate_status(
    filename: str,
    rows: list[dict[str, str]],
    allowed_values: set[str],
    errors: list[str],
) -> None:
    for row_number, row in enumerate(rows, start=2):
        status = normalize(row.get("status"))
        if status == "":
            errors.append(f"{filename}: row {row_number}: missing required field status")
        elif status not in allowed_values:
            errors.append(
                f"{filename}: row {row_number}: unknown status value {status!r}"
            )


def validate_required_fields(
    filename: str,
    rows: list[dict[str, str]],
    required_fields: set[str],
    errors: list[str],
) -> None:
    for row_number, row in enumerate(rows, start=2):
        for field in sorted(required_fields):
            if is_missing(row.get(field)):
                errors.append(
                    f"{filename}: row {row_number}: missing required field {field}"
                )


def validate_confirmed_path_status(
    rows: list[dict[str, str]],
    errors: list[str],
) -> None:
    filename = "confirmed_papers.csv"
    for row_number, row in enumerate(rows, start=2):
        status = normalize(row.get("status"))
        pdf_path = normalize(row.get("pdf_path"))
        extracted_text_path = normalize(row.get("extracted_text_path"))

        if status == "ready_for_pdf_download":
            if pdf_path != "not_downloaded_yet":
                errors.append(
                    f"{filename}: row {row_number}: status ready_for_pdf_download "
                    f"requires pdf_path='not_downloaded_yet', found {pdf_path!r}"
                )
            if extracted_text_path != "not_extracted_yet":
                errors.append(
                    f"{filename}: row {row_number}: status ready_for_pdf_download "
                    "requires extracted_text_path='not_extracted_yet', "
                    f"found {extracted_text_path!r}"
                )

        if status == "ready_for_reading":
            if not pdf_path.startswith("papers/raw_pdf/"):
                errors.append(
                    f"{filename}: row {row_number}: status ready_for_reading "
                    "requires pdf_path to start with 'papers/raw_pdf/', "
                    f"found {pdf_path!r}"
                )
            if not extracted_text_path.startswith("papers/extracted_text/"):
                errors.append(
                    f"{filename}: row {row_number}: status ready_for_reading "
                    "requires extracted_text_path to start with "
                    f"'papers/extracted_text/', found {extracted_text_path!r}"
                )


def print_section(title: str, lines: list[str]) -> None:
    print(f"{title}:")
    if lines:
        for line in lines:
            print(f"- {line}")
    else:
        print("- none")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    loaded: dict[str, tuple[list[str], list[dict[str, str]]]] = {}

    for filename, path in TABLES.items():
        try:
            header, rows, file_warnings = read_csv(path)
        except FileNotFoundError:
            errors.append(f"{filename}: file not found at {path}")
            loaded[filename] = ([], [])
            continue

        warnings.extend(file_warnings)
        loaded[filename] = (header, rows)

    for filename, (header, rows) in loaded.items():
        validate_header(filename, header, EXPECTED_HEADERS[filename], errors)

        if filename in ALLOWED_STATUS:
            validate_status(filename, rows, ALLOWED_STATUS[filename], errors)

    candidate_rows = loaded["candidate_papers.csv"][1]
    confirmed_rows = loaded["confirmed_papers.csv"][1]
    paper_matrix_rows = loaded["paper_matrix.csv"][1]
    figure_evidence_rows = loaded["figure_evidence_table.csv"][1]

    check_duplicates(
        "candidate_papers.csv",
        candidate_rows,
        CANDIDATE_DUPLICATE_FIELDS,
        errors,
    )
    check_duplicates(
        "confirmed_papers.csv",
        confirmed_rows,
        CONFIRMED_DUPLICATE_FIELDS,
        errors,
    )

    validate_required_fields(
        "confirmed_papers.csv",
        confirmed_rows,
        CONFIRMED_REQUIRED,
        errors,
    )
    validate_required_fields(
        "paper_matrix.csv",
        paper_matrix_rows,
        PAPER_MATRIX_REQUIRED,
        errors,
    )
    validate_required_fields(
        "figure_evidence_table.csv",
        figure_evidence_rows,
        FIGURE_EVIDENCE_REQUIRED,
        errors,
    )
    validate_confirmed_path_status(confirmed_rows, errors)

    files_checked = [
        str(path.relative_to(ROOT)).replace("\\", "/") for path in TABLES.values()
    ]
    row_counts = [
        f"{filename}: {len(rows)} data row(s)"
        for filename, (_header, rows) in loaded.items()
    ]

    print_section("Files checked", files_checked)
    print_section("Row counts", row_counts)
    print_section("Warnings", warnings)
    print_section("Errors", errors)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
