#!/usr/bin/env python3
"""
Skill-to-Tools Unified Command-Line Interface (CLI)
Exposes the Master Ecosystem across any terminal or agent prompt:
  - Video-to-Skill (Lum1104/video-to-skill)
  - Skill Seekers (yusufkaraaslan/Skill_Seekers)
  - Book-to-Skill (virgiliojr94/book-to-skill)
  - MCP Python SDK (modelcontextprotocol/python-sdk)
  - Agent Skills (agentskills/agentskills)
"""

import sys
import os
import argparse
from pathlib import Path

# Ensure core and parent directory are on python path
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

try:
    from core.engine import SkillToToolsEngine
except ImportError:
    from engine import SkillToToolsEngine

BANNER = """
========================================================================
   ____  __     _ ____         __         ______            __    
  / __/ / /__  (_) / /  ____  / /____    /_  __/___  ___   / /____
 _\\ \\  /  '_/ / / / /--/___/ / __/ _ \\    / / / __ \\/ _ \\ / //___/
/___/ /_/\\_\\ /_/_/_/         \\__/\\___/   /_/  \\___/\\___//_/     
========================================================================
 The Autonomous AI Skill & Tool Engineering Ecosystem
  [1] Video-to-Skill  [2] Skill Seekers  [3] Book-to-Skill
  [4] MCP Python SDK  [5] Agent Skills Standard
========================================================================
"""

def print_banner():
    print(BANNER)

def cmd_check(args, engine):
    print_banner()
    print(">>> Auditing Skill-to-Tools 5-Engine Architecture:\n")
    report = engine.check_environment()
    print(f"Python Runtime: {report['python']} ({report['executable']})\n")
    
    for mod_name, mod_info in report["modules"].items():
        status = "[READY]" if mod_info["available"] else "[MISSING]"
        print(f"  {status:9} {mod_name}")
        print(f"            Path: {mod_info['path']}")
        print(f"            Role: {mod_info['description']}\n")
    print(f"All modules registered and centralized in {engine.modules_dir}")

def cmd_book(args, engine):
    print(f">>> [Module 3: Book-to-Skill] Ingesting book/document: {args.path}")
    res = engine.convert_book(args.path, mode=args.mode)
    if res["success"]:
        print("\n[SUCCESS] Extraction completed:")
        print(res.get("stdout", ""))
    else:
        print(f"\n[ERROR] Failed to extract from book: {res.get('error') or res.get('stderr')}")
        if res.get("stdout"):
            print(res["stdout"])

def cmd_web(args, engine):
    print(f">>> [Module 2: Skill Seekers] Ingesting website/docs/repo: {args.url}")
    res = engine.convert_web_or_repo(args.url, name=args.name, output_dir=args.output)
    if res["success"]:
        print("\n[SUCCESS] Skill generated from web/repo source:")
        print(res.get("stdout", ""))
    else:
        print(f"\n[ERROR] Skill extraction failed: {res.get('error') or res.get('stderr')}")
        if res.get("stdout"):
            print(res["stdout"])

def cmd_detect(args, engine):
    print(f">>> [Module 2: Skill Seekers] Detecting source structure: {args.url}")
    res = engine.detect_source(args.url)
    if res["success"]:
        print(res.get("stdout", ""))
    else:
        print(f"[ERROR] Detection failed: {res.get('error') or res.get('stderr')}")

def cmd_video(args, engine):
    print(f">>> [Module 1: Video-to-Skill] Ingesting video/course: {args.source}")
    res = engine.convert_video(args.source, output_dir=args.output)
    if res["success"]:
        print("\n[SUCCESS] Video skill generated:")
        print(res.get("stdout", ""))
    else:
        print(f"\n[ERROR] Video skill generation failed: {res.get('error') or res.get('stderr')}")
        if res.get("stdout"):
            print(res["stdout"])

def cmd_validate(args, engine):
    print(f">>> [Module 5: Agent Skills] Validating skill: {args.skill_dir}")
    res = engine.validate_skill(args.skill_dir)
    if res["success"]:
        print("\n[PASSED] Skill adheres to the open Agent Skills standard specification!")
        if res.get("stdout"):
            print(res["stdout"])
    else:
        print(f"\n[FAILED] Validation errors detected:\n{res.get('stdout') or res.get('stderr') or res.get('error')}")

def cmd_mcp(args, engine):
    print(f">>> [Module 4: MCP Python SDK] Building Executable MCP Server for: {args.skill_dir}")
    res = engine.build_mcp_server(args.skill_dir, output_dir=args.output, server_name=args.name)
    if res["success"]:
        print("\n[SUCCESS] MCP Server generated successfully!")
        print(f"  Server Entrypoint: {res['server_path']}")
        print(f"  Runner Script:     {res['runner_path']}")
        print(f"  Server Name:       {res['server_name']}")
    else:
        print(f"\n[ERROR] Failed to build MCP server: {res.get('error')}")

def cmd_pipeline(args, engine):
    print_banner()
    print(f">>> Autonomous End-to-End Skill-to-Tools Pipeline")
    print(f"    Source Target: {args.source}\n")
    
    source_lower = args.source.lower()
    skill_output = None

    if source_lower.endswith((".pdf", ".epub", ".docx", ".mobi", ".azw", ".rtf", ".txt")):
        print("--> Step 1: Detected Book/PDF document. Running Book-to-Skill extraction...")
        b_res = engine.convert_book(args.source)
        if not b_res["success"]:
            print(f"Pipeline failed at Book extraction: {b_res.get('error')}")
            return
        print(b_res.get("stdout", ""))
        skill_output = Path(args.source).stem

    elif "youtube.com" in source_lower or "youtu.be" in source_lower or source_lower.endswith((".mp4", ".mov", ".m4a", ".mp3")):
        print("--> Step 1: Detected Video source. Running Video-to-Skill extraction...")
        v_res = engine.convert_video(args.source)
        if not v_res["success"]:
            print(f"Pipeline failed at Video extraction: {v_res.get('error')}")
            return
        print(v_res.get("stdout", ""))

    elif source_lower.startswith(("http://", "https://")):
        print("--> Step 1: Detected Web / Documentation source. Running Skill Seekers extraction...")
        w_res = engine.convert_web_or_repo(args.source)
        if not w_res["success"]:
            print(f"Pipeline failed at Web extraction: {w_res.get('error')}")
            return
        print(w_res.get("stdout", ""))

    print("\n--> Step 2: Skill Extraction & Standardization Complete!")
    if args.build_mcp and skill_output and Path(skill_output).is_dir():
        print("--> Step 3: Generating Executable MCP Server Tool Wrapper...")
        m_res = engine.build_mcp_server(skill_output)
        if m_res["success"]:
            print(f"[PIPELINE COMPLETE] MCP Server created at: {m_res['server_path']}")

def main():
    parser = argparse.ArgumentParser(
        prog="skill-to-tools",
        description="Skill-to-Tools Unified AI Skill & Tool Engineering Ecosystem"
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    # check
    p_check = subparsers.add_parser("check", help="Audit all 5 core modules and python runtime")
    p_check.set_defaults(func=cmd_check)

    # book
    p_book = subparsers.add_parser("book", help="Extract skill from Book/PDF/EPUB (Book-to-Skill)")
    p_book.add_argument("path", help="Path to book or document file")
    p_book.add_argument("--mode", choices=["text", "technical"], default="text", help="Extraction mode")
    p_book.set_defaults(func=cmd_book)

    # pdf alias
    p_pdf = subparsers.add_parser("pdf", help="Alias for book command (Book-to-Skill)")
    p_pdf.add_argument("path", help="Path to PDF document")
    p_pdf.add_argument("--mode", choices=["text", "technical"], default="text", help="Extraction mode")
    p_pdf.set_defaults(func=cmd_book)

    # web
    p_web = subparsers.add_parser("web", help="Extract skill from Website or Repo (Skill Seekers)")
    p_web.add_argument("url", help="URL of website or GitHub repository")
    p_web.add_argument("--name", help="Custom skill name")
    p_web.add_argument("--output", help="Output directory")
    p_web.set_defaults(func=cmd_web)

    # scrape alias
    p_scrape = subparsers.add_parser("scrape", help="Alias for web command")
    p_scrape.add_argument("url", help="URL of website or GitHub repository")
    p_scrape.add_argument("--name", help="Custom skill name")
    p_scrape.add_argument("--output", help="Output directory")
    p_scrape.set_defaults(func=cmd_web)

    # repo alias
    p_repo = subparsers.add_parser("repo", help="Extract skill from GitHub repository")
    p_repo.add_argument("url", help="URL of GitHub repository")
    p_repo.add_argument("--name", help="Custom skill name")
    p_repo.add_argument("--output", help="Output directory")
    p_repo.set_defaults(func=cmd_web)

    # detect
    p_detect = subparsers.add_parser("detect", help="Detect website/source type and estimated pages")
    p_detect.add_argument("url", help="URL of website or repository to inspect")
    p_detect.set_defaults(func=cmd_detect)

    # video
    p_video = subparsers.add_parser("video", help="Extract skill from Video or Course (Video-to-Skill)")
    p_video.add_argument("source", help="Video file or YouTube/course URL")
    p_video.add_argument("--output", help="Output directory")
    p_video.set_defaults(func=cmd_video)

    # validate
    p_val = subparsers.add_parser("validate", help="Validate skill against open Agent Skills standard")
    p_val.add_argument("skill_dir", help="Path to skill directory containing SKILL.md")
    p_val.set_defaults(func=cmd_validate)

    # mcp
    p_mcp = subparsers.add_parser("mcp", help="Generate executable MCP server from skill (MCP SDK)")
    p_mcp.add_argument("skill_dir", help="Path to skill directory")
    p_mcp.add_argument("--name", help="Custom server name")
    p_mcp.add_argument("--output", help="Custom output directory")
    p_mcp.set_defaults(func=cmd_mcp)

    # pipeline
    p_pipe = subparsers.add_parser("pipeline", help="Autonomous End-to-End Pipeline (Source -> Skill -> MCP Tool)")
    p_pipe.add_argument("source", help="Document, URL, or Video source")
    p_pipe.add_argument("--build-mcp", action="store_true", help="Automatically generate executable MCP server")
    p_pipe.set_defaults(func=cmd_pipeline)

    args = parser.parse_args()
    engine = SkillToToolsEngine()

    if not args.subcommand:
        print_banner()
        parser.print_help()
        sys.exit(0)

    args.func(args, engine)

if __name__ == "__main__":
    main()
