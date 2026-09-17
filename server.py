from __future__ import annotations

from pathlib import Path
from typing import List

from mcp.server.fastmcp import FastMCP


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".py", ".html", ".css", ".js", ".yaml", ".yml"}

mcp = FastMCP("flyrank-week6-files")


def safe_path(relative_path: str) -> Path:
    """Resolve a project-relative path and block traversal outside the project."""
    candidate = (PROJECT_ROOT / relative_path).resolve()
    if candidate != PROJECT_ROOT and PROJECT_ROOT not in candidate.parents:
        raise ValueError("Path is outside the Week 6 project directory")
    return candidate


def text_files() -> List[Path]:
    return [
        path
        for path in PROJECT_ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS
    ]


@mcp.tool()
def list_files(subdirectory: str = "") -> str:
    """List project files below an optional project-relative directory."""
    base = safe_path(subdirectory)
    if not base.exists() or not base.is_dir():
        return f"Directory not found: {subdirectory or '.'}"

    files = sorted(
        str(path.relative_to(PROJECT_ROOT))
        for path in base.rglob("*")
        if path.is_file()
    )
    return "\n".join(files) if files else "No files found."


@mcp.tool()
def read_file(relative_path: str, max_chars: int = 12000) -> str:
    """Read a UTF-8 text file from the Week 6 project."""
    path = safe_path(relative_path)
    if not path.is_file():
        return f"File not found: {relative_path}"
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return "Only approved text file types can be read."

    content = path.read_text(encoding="utf-8")
    if len(content) > max_chars:
        content = content[:max_chars] + "\n...[truncated]"
    return content


@mcp.tool()
def search_files(query: str, subdirectory: str = "") -> str:
    """Search approved text files for a case-insensitive phrase."""
    if not query.strip():
        return "Search query cannot be empty."

    base = safe_path(subdirectory)
    if not base.exists() or not base.is_dir():
        return f"Directory not found: {subdirectory or '.'}"

    matches = []
    needle = query.lower()
    for path in sorted(base.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, start=1):
            if needle in line.lower():
                matches.append(f"{path.relative_to(PROJECT_ROOT)}:{number}: {line.strip()}")

    return "\n".join(matches) if matches else "No matches found."


@mcp.resource("workflow://fl-04")
def fl04_workflow() -> str:
    """Expose the FL-04 workflow as read-only context."""
    return """FL-04 Source-Grounded Technical Study Notes workflow:
1. Gather source-supported facts.
2. Synthesize evidence into a logical structure.
3. Draft beginner-friendly study notes.
4. Review support, gaps, clarity, and formatting.
5. Human checks important claims before use.
"""


@mcp.prompt()
def review_workflow_file(file_path: str) -> str:
    """Create a reusable prompt for reviewing a workflow evidence file."""
    return (
        "Review the workflow evidence file at "
        f"{file_path}. Check whether the document clearly identifies the workflow "
        "stage, handoff, evidence, failure point, and required human review. "
        "Do not invent missing evidence."
    )


if __name__ == "__main__":
    mcp.run()
