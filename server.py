from pathlib import Path
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("flyrank-workspace")

ROOT = Path(os.environ.get("FLRANK_WORKSPACE", Path(__file__).resolve().parents[1])).resolve()


def safe_path(relative_path: str) -> Path:
    target = (ROOT / relative_path).resolve()
    if target != ROOT and ROOT not in target.parents:
        raise ValueError("Path is outside the approved workspace")
    if target.is_dir():
        raise ValueError("Expected a file, not a directory")
    return target


@mcp.tool()
def list_project_files() -> str:
    """List files in the approved FlyRank Week 7 workspace."""
    files = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file()]
    return "\n".join(sorted(files)) or "No files found."


@mcp.tool()
def read_project_file(path: str) -> str:
    """Read one UTF-8 text file from the approved workspace."""
    target = safe_path(path)
    if not target.exists():
        raise FileNotFoundError(path)
    return target.read_text(encoding="utf-8")


@mcp.tool()
def search_project(query: str) -> str:
    """Search UTF-8 text files in the approved workspace for a phrase."""
    results = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if query.lower() in text.lower():
            lines = [f"{i}: {line.strip()}" for i, line in enumerate(text.splitlines(), 1) if query.lower() in line.lower()]
            results.append(f"FILE: {path.relative_to(ROOT).as_posix()}\n" + "\n".join(lines[:20]))
    return "\n\n".join(results) or f"No matches for: {query}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
