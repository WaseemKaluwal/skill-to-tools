#!/usr/bin/env python3
"""
Template for generating FastMCP servers from Agent Skills
Powered by Anthropic Model Context Protocol Python SDK
"""

import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP

SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_ROOT / "SKILL.md"

# Instantiate FastMCP server
mcp = FastMCP("Skill Knowledge Server")

@mcp.tool()
def get_skill_instructions() -> str:
    """Retrieve full core instructions, frameworks, and philosophy from SKILL.md."""
    if SKILL_MD.exists():
        return SKILL_MD.read_text(encoding="utf-8")
    return "Error: SKILL.md not found in skill root."

@mcp.tool()
def list_chapters_and_references() -> list:
    """List all available reference documents, chapters, and frameworks in this skill."""
    results = []
    for sub in ["references", "chapters", "docs"]:
        target = SKILL_ROOT / sub
        if target.is_dir():
            for f in target.glob("*.md"):
                results.append(f"{sub}/{f.name}")
    return results

@mcp.tool()
def read_reference_chapter(relative_path: str) -> str:
    """Read full text of a specific reference document or chapter from the skill."""
    target_file = SKILL_ROOT / relative_path
    if target_file.exists() and target_file.is_file():
        return target_file.read_text(encoding="utf-8")
    return f"Reference file not found: {relative_path}"

if __name__ == "__main__":
    mcp.run()
