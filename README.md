# Skill to Tools: Unified Engine for Book to Skill, Video to Skill, PDF to Skill & Video to Tool

> **The Unified 5-in-1 Autonomous AI Skill & Tool Engineering Ecosystem**  
> Turn written books, PDF documents, video courses, and web repositories into standardized Agent Skills and executable Model Context Protocol (MCP) tools.

[![Architecture](https://img.shields.io/badge/Architecture-5--in--1%20Unified-blueviolet.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-Agent%20Skills%20Open%20Spec-blue.svg)](#)
[![Protocol](https://img.shields.io/badge/MCP-Python%20SDK%20v2.3-green.svg)](#)
[![Supported Formats](https://img.shields.io/badge/Formats-PDF%20|%20EPUB%20|%20MP4%20|%20YouTube%20|%20Docs-orange.svg)](#)
[![Status](https://img.shields.io/badge/Status-100%25%20Operational-brightgreen.svg)](#)

---

> **Key Takeaway:** **Skill to Tools** is an open-source pipeline that extracts structured knowledge from technical books, PDF documents, video courses, and documentation websites, converts them into open-standard Agent Skills (`SKILL.md`), and wraps them into production-ready FastMCP executable tools in a single command.

---

## 📑 Table of Contents

- [Overview & Architecture](#-overview--architecture)
- [Book to Skill & PDF to Skill Conversion](#-book-to-skill--pdf-to-skill-conversion)
- [Video to Skill & Video to Tool Pipeline](#-video-to-skill--video-to-tool-pipeline)
- [Skill to Tools: Generating Executable MCP Tools](#-skill-to-tools-generating-executable-mcp-tools)
- [Web & Repository Ingestion](#-web--repository-ingestion-skill-seekers)
- [Comparison Matrix](#-feature--capability-matrix)
- [Command-Line Interface (CLI) Reference](#-command-line-interface-cli-reference)
- [Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)
- [GitHub Repository Optimization](#-recommended-github-topics--tags)

---

## 🌟 Overview & Architecture

Modern AI agents require clear procedural workflows and callable tools rather than massive unorganized context dumps. **Skill to Tools** bridges this gap by unifying five industry-standard frameworks into one automated pipeline:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        SKILL-TO-TOOLS PIPELINE                         │
├─────────────────┬──────────────────────────────────────────────────────┤
│ 1. Ingest       │ Books, PDFs, Videos, YouTube Playlists, Web Docs     │
│ 2. Extract      │ Book-to-Skill, Video-to-Skill, Skill Seekers         │
│ 3. Standardize  │ Agent Skills Standard (Clean metadata, modular docs) │
│ 4. Validate     │ Strict Schema Validation (skills-ref engine)         │
│ 5. Toolify      │ FastMCP Python SDK (Executable AI Tools & Servers)   │
└─────────────────┴──────────────────────────────────────────────────────┘
```

### The 5 Integrated Sub-Engines

| Engine | Upstream Framework | Core Function |
| :--- | :--- | :--- |
| **01-video-to-skill** | [Lum1104/video-to-skill](https://github.com/Lum1104/video-to-skill) | Converts video courses and playlists into structured skills. |
| **02-skill-seekers** | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Scrapes documentation websites, GitHub repos, and web articles. |
| **03-book-to-skill** | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Extracts mental models, principles, and chapters from books and PDFs. |
| **04-mcp-python-sdk** | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Builds executable FastMCP servers and callable agent functions. |
| **05-agent-skills** | [agentskills/agentskills](https://github.com/agentskills/agentskills) | Provides open standard specification, schema parsing, and validation. |

---

## 📚 Book to Skill & PDF to Skill Conversion

Extracting raw text from a document is not enough. The **Book to Skill** and **PDF to Skill** engine extracts the author's crystallized expertise—identifying named frameworks, decision heuristics, step-by-step techniques, and anti-patterns.

### Supported Document Formats
- **PDF** (`.pdf`): Supports text-heavy books via `pypdf`/`pdfminer` and technical layouts with mathematical formulas and tables.
- **E-Books** (`.epub`, `.mobi`, `.azw`, `.azw3`): Structural parsing preserving chapter boundaries.
- **Documents** (`.docx`, `.html`, `.rtf`, `.txt`, `.md`): Clean AST-based extraction.

### CLI Commands for Book & PDF to Skill

```bash
# Convert a technical book into an Agent Skill
stt book "C:\docs\Designing-Data-Intensive-Applications.pdf"

# Run with deep technical formula and table mode
stt book "C:\docs\quantum-computing.pdf" --mode technical

# Direct PDF to Skill shortcut
stt pdf "C:\docs\handbook.pdf"
```

The output generates a self-contained skill folder containing `SKILL.md`, modular chapter files in `chapters/`, and glossary definitions in `references/`.

---

## 🎥 Video to Skill & Video to Tool Pipeline

Turning multimedia content into AI utility involves two progressive stages:

1. **Video to Skill**: Ingests video lectures, YouTube courses, or local MP4/MOV files, extracts verified transcripts with timestamps, identifies key instructional segments, and generates a structured skill.
2. **Video to Tool**: Takes the extracted procedural knowledge and wraps it directly into executable Python tool functions using the Model Context Protocol (MCP).

### Video to Skill & Video to Tool Commands

```bash
# Convert an entire YouTube course playlist into an Agent Skill
stt video "https://www.youtube.com/playlist?list=PLxxx"

# Convert a local video recording into a skill
stt video "C:\recordings\lecture.mp4"

# Video to Tool: Convert video and generate executable FastMCP tool server
stt pipeline "https://www.youtube.com/watch?v=example" --build-mcp
```

---

## ⚙️ Skill to Tools: Generating Executable MCP Tools

Transforming a passive skill folder into an active, callable tool allows AI agents (Anthropic Claude, Google Gemini, OpenAI ChatGPT, Cursor) to run queries against the material deterministically.

```bash
# Generate a FastMCP server wrapper from any skill folder
stt mcp ./my-custom-skill --name "MyDomainTools"
```

This generates `mcp_server/server.py` exposing:
- `get_skill_instructions()`: Returns core directives and frameworks.
- `list_chapters_and_references()`: Lists modular sub-documents.
- `read_reference_chapter(relative_path)`: Streams specific chapters on-demand.

---

## 🌐 Web & Repository Ingestion (Skill Seekers)

Automate knowledge extraction from public documentation sites and software repositories:

```bash
# Detect site structure and estimated pages before scraping
stt detect https://docs.python.org/3/

# Scrape documentation site into an Agent Skill
stt web https://docs.djangoproject.com/ --name django

# Scrape a GitHub repository
stt repo https://github.com/psf/requests --name requests
```

---

## 📊 Feature & Capability Matrix

| Feature | Book to Skill | Video to Skill | PDF to Skill | Video to Tool | Web to Skill |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Primary Input** | EPUB, MOBI, PDF | YouTube, MP4 | PDF Documents | Video + Transcripts | HTML Docs, GitHub |
| **Output Format** | Open Agent Skill | Open Agent Skill | Open Agent Skill | Executable FastMCP | Open Agent Skill |
| **Chapter Splitting** | Automated | Timestamp-Based | Page / TOC Bound | Function Mapped | Hierarchy Crawled |
| **Executable Tool?** | Via `stt mcp` | Via `stt mcp` | Via `stt mcp` | Native Pipeline | Via `stt mcp` |
| **Validation** | `skills-ref` 100% | `skills-ref` 100% | `skills-ref` 100% | FastMCP Contract | `skills-ref` 100% |

---

## 💻 Command-Line Interface (CLI) Reference

| Command | Action |
| :--- | :--- |
| `stt check` | Verifies runtime health and readiness of all 5 engines. |
| `stt book <path>` | Extracts frameworks and chapters from books. |
| `stt pdf <path>` | Extracts structured skill from PDF files. |
| `stt video <source>` | Converts video courses or playlists into skills. |
| `stt detect <url>` | Analyzes a documentation site's structure before scraping. |
| `stt web <url>` | Scrapes documentation websites into a skill. |
| `stt repo <github_url>` | Extracts codebase architecture from GitHub. |
| `stt validate <skill_dir>` | Validates any skill against the official Agent Skills standard. |
| `stt mcp <skill_dir>` | Generates a runnable FastMCP server wrapping the skill. |
| `stt pipeline <source> --build-mcp` | Runs full automated pipeline: Source ➔ Skill ➔ Executable MCP Tool. |

---

## ❓ Frequently Asked Questions (FAQ)

### What is the difference between Book to Skill and PDF to Skill?
**Book to Skill** focuses on extracting conceptual frameworks, mental models, and decision heuristics from long-form literature. **PDF to Skill** handles both technical books and dense reference manuals, parsing structured tables, code snippets, and mathematical notations into modular chapter files.

### What is the Video to Tool workflow?
**Video to Tool** takes video or audio course instruction beyond passive notes. It extracts the step-by-step procedural demonstrations from the video transcript and automatically builds an executable Model Context Protocol (MCP) server so agents can run the methods directly.

### Are generated skills compatible with all AI agents?
Yes. Every skill generated conforms to the [Agent Skills](https://agentskills.io) open standard (`SKILL.md`), making them compatible across Google Antigravity, Claude Code, GitHub Copilot CLI, OpenAI Codex, Cursor, and OpenCode.

---

## 🏷️ Recommended GitHub Topics & Tags

When publishing to GitHub, set these repository topics to optimize search discovery:

```
skill-to-tools, book-to-skill, video-to-skill, pdf-to-skill, video-to-tool, agent-skills, mcp-server, fastmcp, model-context-protocol, ai-tools, llm-tools, knowledge-extraction
```
