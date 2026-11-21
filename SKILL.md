---
name: Skill-to-Tools
description: "Skill-to-Tools Master Ecosystem: Book to Skill, Video to Skill, PDF to Skill, and Video to Tool. Transforms books, PDFs, videos, and web repositories into standardized Agent Skills and executable FastMCP server tools."
metadata:
  opencode/slash: "true"
  argument-hint: "check | video <source> | web <url> | repo <url> | book <path> | pdf <path> | mcp <skill_dir> | validate <skill_dir> | pipeline <source>"
  version: "1.0.0"
---

# /skill-to-tools - Unified AI Skill & Tool Engineering Ecosystem

The **Skill-to-Tools Master Ecosystem** unifies five industry-leading skill generation, knowledge extraction, and tool-building frameworks into a single centralized engine located at `C:\Skill-to-Tools`.

---

## 🏛️ Centralized Architecture (`C:\Skill-to-Tools`)

```
C:\Skill-to-Tools\
├── bin\                     # Global CLI executables (stt, skill-to-tools)
├── core\                    # Unified Python CLI & Orchestration Engine
│   ├── cli.py               # Main CLI dispatcher
│   └── engine.py            # 5-module coordination logic
├── modules\                 # Integrated Upstream Engines
│   ├── 01-video-to-skill\   # Convert videos, playlists, audio & courses to skills
│   ├── 02-skill-seekers\    # Extract knowledge from 18+ sources (web, GitHub, docs)
│   ├── 03-book-to-skill\    # Ingest books & PDFs into deep structured frameworks
│   ├── 04-mcp-python-sdk\   # Anthropic MCP Python SDK for executable AI tools
│   └── 05-agent-skills\     # Open Agent Skills standard specification & validator
├── templates\               # Reusable FastMCP and Agent Skill templates
└── references\              # Skill specifications, schemas & cheat sheets
```

---

## 🚀 Quick Reference / Commands

| Command | Action |
| :--- | :--- |
| `/skill-to-tools check` or `stt check` | Audits all 5 core modules and python runtime availability. |
| `/skill-to-tools video <url_or_file>` | Extracts evidence-grounded AI skill from video, playlist, or course. |
| `/skill-to-tools web <url>` | Scrapes documentation or websites into structured Agent Skills (Skill Seekers). |
| `/skill-to-tools repo <github_url>` | Extracts codebase architecture and APIs into an Agent Skill. |
| `/skill-to-tools book <path>` or `stt pdf <path>` | Extracts mental models, frameworks & chapters from Books and PDFs. |
| `/skill-to-tools validate <skill_dir>` | Validates an Agent Skill folder against the official Open Agent Skills standard. |
| `/skill-to-tools mcp <skill_dir>` | Generates an executable Python FastMCP server wrapper from any skill folder. |
| `/skill-to-tools pipeline <source>` | Autonomous end-to-end pipeline: **[Source] ➔ [Agent Skill] ➔ [Executable MCP Tool]**. |
