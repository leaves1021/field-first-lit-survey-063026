#!/usr/bin/env python3
"""Read-only leakage checker for commit-eligible project text files."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

SINGLE_FILES = [
    "AGENTS.md",
    "README.md",
    ".env.example",
    ".gitignore",
    "requirements.txt",
]

GLOB_PATTERNS = [
    "scripts/**/*.py",
    "scripts/**/*.md",
    "templates/**/*.md",
    "synthesis/**/*.md",
    "notes/**/*.md",
    "tables/**/*.csv",
    "logs/**/*.md",
    "data/processed/**/*.csv",
]

SKIP_PREFIXES = (
    "papers/raw_pdf/",
    "papers/extracted_text/",
    "papers/supplementary/",
    "data/raw/",
)

WINDOWS_PATH_RE = re.compile(r"(?<![A-Za-z0-9_])(?:[A-Za-z]:\\[^\s`'\"<>|]+)")
FILE_URL_RE = re.compile(r"file:///[A-Za-z]:/[^\s`'\"<>]+", re.IGNORECASE)
ZOTERO_STORAGE_RE = re.compile(r"zotero[\\/]+storage", re.IGNORECASE)
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?<![A-Za-z0-9_])"
    r"(?:[A-Za-z0-9_]*API_KEY|SEMANTIC_SCHOLAR_API_KEY|NCBI_API_KEY|SECRET|TOKEN)"
    r"\s*=\s*"
    r"([^\s#]+)"
)
PEM_MARKER_RE = re.compile(r"BEGIN (?:RSA )?PRIVATE KEY")
PAGE_MARKER_RE = re.compile(r"^## Page \d+\s*$")


def relative_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_under_skipped_prefix(path: Path) -> bool:
    rel = relative_posix(path)
    return any(rel.startswith(prefix) for prefix in SKIP_PREFIXES)


def iter_text_files() -> list[Path]:
    paths: set[Path] = set()

    for name in SINGLE_FILES:
        path = ROOT / name
        if path.exists() and path.is_file():
            paths.add(path)

    references_bib = ROOT / "references.bib"
    if references_bib.exists() and references_bib.is_file():
        paths.add(references_bib)

    for pattern in GLOB_PATTERNS:
        for path in ROOT.glob(pattern):
            if path.is_file() and not is_under_skipped_prefix(path):
                paths.add(path)

    return sorted(paths, key=relative_posix)


def truncate_snippet(text: str, limit: int = 120) -> str:
    clean = " ".join(text.strip().split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3] + "..."


def is_allowed_empty_env_example(path: Path, line: str, match: re.Match[str]) -> bool:
    if relative_posix(path) != ".env.example":
        return False
    assigned_value = match.group(1).strip()
    return assigned_value == ""


def add_error(
    errors: list[str],
    path: Path,
    line_number: int,
    reason: str,
    line: str,
) -> None:
    errors.append(
        f"{relative_posix(path)}:{line_number}: {reason}: "
        f"{truncate_snippet(line)!r}"
    )


def scan_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        warnings.append(f"{relative_posix(path)}: could not read file: {exc}")
        return errors, warnings

    page_marker_hits: list[tuple[int, str]] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        if WINDOWS_PATH_RE.search(line):
            add_error(errors, path, line_number, "Windows absolute path", line)

        if FILE_URL_RE.search(line):
            add_error(errors, path, line_number, "file URL absolute path", line)

        if ZOTERO_STORAGE_RE.search(line):
            add_error(errors, path, line_number, "Zotero storage path", line)

        for match in SECRET_ASSIGNMENT_RE.finditer(line):
            if is_allowed_empty_env_example(path, line, match):
                continue
            add_error(errors, path, line_number, "possible API key or token assignment", line)

        if PEM_MARKER_RE.search(line):
            add_error(errors, path, line_number, "PEM private key marker", line)

        if PAGE_MARKER_RE.match(line):
            page_marker_hits.append((line_number, line))

    if len(page_marker_hits) >= 3:
        first_line_number, first_line = page_marker_hits[0]
        add_error(
            errors,
            path,
            first_line_number,
            "possible copied extracted PDF text with repeated page markers",
            first_line,
        )

    return errors, warnings


def print_section(title: str, lines: list[str]) -> None:
    print(f"{title}:")
    if not lines:
        print("- none")
        return
    for line in lines:
        print(f"- {line}")


def main() -> int:
    files = iter_text_files()
    errors: list[str] = []
    warnings: list[str] = []

    for path in files:
        file_errors, file_warnings = scan_file(path)
        errors.extend(file_errors)
        warnings.extend(file_warnings)

    print(f"Files scanned: {len(files)}")
    if files:
        for path in files:
            print(f"- {relative_posix(path)}")

    print_section("Warnings", warnings)
    print_section("Errors", errors)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
