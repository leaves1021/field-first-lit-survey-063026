#!/usr/bin/env python3
"""Read-only validator for literature-workflow Markdown notes."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "notes"

REQUIRED_SECTIONS = [
    "# Citation metadata",
    "# One-paragraph summary",
    "# Research question",
    "# Task / behavior",
    "# Species / brain area / recording method",
    "# Neural object analyzed",
    "# Main findings",
    "# Figure-by-figure evidence map",
    "# Modeling relevance",
    "# Relation to field-first survey axes",
    "# Uncertainty / caveats",
    "# Candidate entries for future `paper_matrix.csv`",
    "# Candidate entries for future `figure_evidence_table.csv`",
]

PAPER_MATRIX_SECTION = "# Candidate entries for future `paper_matrix.csv`"
FIGURE_EVIDENCE_SECTION = "# Candidate entries for future `figure_evidence_table.csv`"

PAPER_MATRIX_HEADER = (
    "| paper | citekey | year | category | field_axis | species | "
    "brain_area_or_scale | task_or_behavior | neural_measurement | neural_object | "
    "computation | causal_status | key_finding_short | modeling_opportunity | "
    "identifiers | uncertainty | notes |"
)
FIGURE_EVIDENCE_HEADER = (
    "| paper | citekey | figure_or_table | result_section | page | claim | "
    "evidence_summary | variable_or_neural_object | analysis_method | causal_status | "
    "relevance_to_research_question | uncertainty | notes |"
)

RISKY_PHRASES = [
    "confirmed figure-level evidence",
    "proves that",
    "causal proof",
    "directly proves",
    "fully explains",
    "establishes causality",
]

ALLOWED_CAUSAL_STATUS_SUBSTRINGS = [
    "correlational",
    "observational",
    "methodological",
    "simulation-based",
    "model-based",
    "biological data + model comparison",
    "conceptual",
    "speculative",
    "learning contrast",
    "geometric analysis",
    "methodological support",
]

TOP_LEVEL_HEADING_RE = re.compile(r"^# ")
TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$")
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_notes() -> list[Path]:
    if not NOTES_DIR.exists():
        return []
    return sorted(NOTES_DIR.glob("*.md"), key=relative_path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def format_issue(path: Path, line_number: int | None, reason: str) -> str:
    location = relative_path(path)
    if line_number is not None:
        location = f"{location}:{line_number}"
    return f"{location}: {reason}"


def find_heading_line(lines: list[str], heading: str) -> int | None:
    for index, line in enumerate(lines, start=1):
        if line.strip() == heading:
            return index
    return None


def section_bounds(lines: list[str], heading: str) -> tuple[int, int] | None:
    start = find_heading_line(lines, heading)
    if start is None:
        return None

    end = len(lines) + 1
    for index in range(start + 1, len(lines) + 1):
        if TOP_LEVEL_HEADING_RE.match(lines[index - 1]):
            end = index
            break
    return start, end


def validate_required_sections(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    lines = text.splitlines()
    for heading in REQUIRED_SECTIONS:
        if find_heading_line(lines, heading) is None:
            errors.append(format_issue(path, None, f"missing required section {heading!r}"))
    return errors


def validate_candidate_headers(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    lines = text.splitlines()
    expected = [
        (PAPER_MATRIX_SECTION, PAPER_MATRIX_HEADER, "candidate paper_matrix.csv table header"),
        (
            FIGURE_EVIDENCE_SECTION,
            FIGURE_EVIDENCE_HEADER,
            "candidate figure_evidence_table.csv table header",
        ),
    ]

    for heading, header, description in expected:
        bounds = section_bounds(lines, heading)
        if bounds is None:
            continue
        start, end = bounds
        section_lines = [line.strip() for line in lines[start:end - 1]]
        if header not in section_lines:
            errors.append(format_issue(path, start, f"missing {description}"))

    return errors


def validate_risky_phrasing(path: Path, text: str) -> list[str]:
    warnings: list[str] = []
    lower_phrases = [(phrase, phrase.lower()) for phrase in RISKY_PHRASES]

    for line_number, line in enumerate(text.splitlines(), start=1):
        normalized = line.lower()
        for phrase, lower_phrase in lower_phrases:
            if lower_phrase in normalized:
                warnings.append(
                    format_issue(path, line_number, f"risky evidence-boundary phrase {phrase!r}")
                )
    return warnings


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(SEPARATOR_CELL_RE.match(cell) for cell in cells)


def validate_candidate_causal_status(path: Path, text: str) -> list[str]:
    warnings: list[str] = []
    lines = text.splitlines()
    bounds = section_bounds(lines, FIGURE_EVIDENCE_SECTION)
    if bounds is None:
        return warnings

    start, end = bounds
    header_seen = False
    allowed = [item.lower() for item in ALLOWED_CAUSAL_STATUS_SUBSTRINGS]

    for line_number in range(start + 1, end):
        line = lines[line_number - 1].strip()
        if line == FIGURE_EVIDENCE_HEADER:
            header_seen = True
            continue
        if not header_seen or not TABLE_ROW_RE.match(line):
            continue

        cells = split_markdown_row(line)
        if is_separator_row(cells):
            continue
        if len(cells) < 13:
            continue

        causal_status = cells[9].lower()
        if not any(item in causal_status for item in allowed):
            warnings.append(
                format_issue(
                    path,
                    line_number,
                    f"candidate figure row has non-conservative causal_status {cells[9]!r}",
                )
            )

    return warnings


def print_section(title: str, lines: list[str]) -> None:
    print(f"{title}:")
    if not lines:
        print("- none")
        return
    for line in lines:
        print(f"- {line}")


def main() -> int:
    notes = iter_notes()
    errors: list[str] = []
    warnings: list[str] = []

    for path in notes:
        try:
            text = read_text(path)
        except OSError as exc:
            errors.append(format_issue(path, None, f"could not read note: {exc}"))
            continue

        errors.extend(validate_required_sections(path, text))
        errors.extend(validate_candidate_headers(path, text))
        warnings.extend(validate_risky_phrasing(path, text))
        warnings.extend(validate_candidate_causal_status(path, text))

    print(f"Notes scanned: {len(notes)}")
    for path in notes:
        print(f"- {relative_path(path)}")
    print_section("Errors", errors)
    print_section("Warnings", warnings)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
