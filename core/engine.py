#!/usr/bin/env python3
"""
Skill-to-Tools Unified Core Engine
Orchestrates 5-in-1 AI Skill & Tool Engineering Ecosystem:
  1. Video-to-Skill    (Video / Audio / Course knowledge extraction)
  2. Skill Seekers     (Web docs, GitHub repos, PDFs, wikis)
  3. Book-to-Skill     (Deep framework & mental model extraction from books/PDFs)
  4. MCP Python SDK    (Executable AI tools and Model Context Protocol servers)
  5. Agent Skills      (Open standard specification, parsing, and validation)
"""

import os
import sys
import subprocess
import json
import shutil
from pathlib import Path

# Auto-inject static_ffmpeg and user Python scripts to ensure ffmpeg, ffprobe, and CLI tools are discoverable
try:
    import static_ffmpeg
    static_ffmpeg.add_paths()
except Exception:
    pass

user_scripts = Path(os.environ.get("APPDATA", "")) / "Python" / f"Python{sys.version_info.major}{sys.version_info.minor}" / "Scripts"
if user_scripts.is_dir() and str(user_scripts) not in os.environ.get("PATH", ""):
    os.environ["PATH"] = str(user_scripts) + os.pathsep + os.environ.get("PATH", "")

BASE_DIR = Path(__file__).resolve().parent.parent
MODULES_DIR = BASE_DIR / "modules"
MODULE_VIDEO = MODULES_DIR / "01-video-to-skill"
MODULE_SEEKERS = MODULES_DIR / "02-skill-seekers"
MODULE_BOOK = MODULES_DIR / "03-book-to-skill"
MODULE_MCP = MODULES_DIR / "04-mcp-python-sdk"
MODULE_AGENT_SKILLS = MODULES_DIR / "05-agent-skills"

class SkillToToolsEngine:
    def __init__(self):
        self.base_dir = BASE_DIR
        self.modules_dir = MODULES_DIR

    def check_environment(self):
        """Audit all 5 core modules and dependencies."""
        ffmpeg_bin = shutil.which("ffmpeg")
        report = {
            "modules": {},
            "python": sys.version.split()[0],
            "executable": sys.executable,
            "ffmpeg": ffmpeg_bin or "Missing (static_ffmpeg fallback active)",
        }

        # Check 01-video-to-skill
        v_script = MODULE_VIDEO / "scripts" / "video_to_skill.py"
        report["modules"]["01-video-to-skill"] = {
            "path": str(MODULE_VIDEO),
            "available": v_script.exists(),
            "description": "Convert videos and courses into evidence-grounded AI skills"
        }

        # Check 02-skill-seekers
        s_src = MODULE_SEEKERS / "src"
        report["modules"]["02-skill-seekers"] = {
            "path": str(MODULE_SEEKERS),
            "available": s_src.exists(),
            "description": "Extract knowledge from websites, GitHub, wikis and PDFs"
        }

        # Check 03-book-to-skill
        b_cli = MODULE_BOOK / "book_to_skill" / "cli.py"
        report["modules"]["03-book-to-skill"] = {
            "path": str(MODULE_BOOK),
            "available": b_cli.exists(),
            "description": "Extract mental models, frameworks and chapters from books/PDFs"
        }

        # Check 04-mcp-python-sdk
        m_src = MODULE_MCP / "src" / "mcp"
        report["modules"]["04-mcp-python-sdk"] = {
            "path": str(MODULE_MCP),
            "available": m_src.exists(),
            "description": "Build executable AI tools and MCP servers (Anthropic standard)"
        }

        # Check 05-agent-skills
        a_src = MODULE_AGENT_SKILLS / "skills-ref" / "src" / "skills_ref"
        report["modules"]["05-agent-skills"] = {
            "path": str(MODULE_AGENT_SKILLS),
            "available": a_src.exists(),
            "description": "Standardize, validate, and manage AI Skills"
        }

        return report

    def convert_book(self, source_path, output_dir=None, mode="text"):
        """Extract skill from Book/PDF using 03-book-to-skill."""
        source = Path(source_path).resolve()
        if not source.exists():
            return {"success": False, "error": f"Source file does not exist: {source}"}

        cli_script = MODULE_BOOK / "scripts" / "extract.py"
        cmd = [sys.executable, str(cli_script), str(source)]
        if mode == "technical":
            cmd.extend(["--mode", "technical"])

        env = os.environ.copy()
        env["PYTHONPATH"] = str(MODULE_BOOK) + os.pathsep + env.get("PYTHONPATH", "")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, env=env)
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "source": str(source)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def detect_source(self, target_url):
        """Detect source structure and frameworks using 02-skill-seekers."""
        cmd = [sys.executable, "-m", "skill_seekers.cli.main", "detect", target_url]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(MODULE_SEEKERS / "src") + os.pathsep + env.get("PYTHONPATH", "")
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, env=env)
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "target": target_url
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def convert_web_or_repo(self, target_url, output_dir=None, name=None):
        """Extract knowledge from documentation site or GitHub repo using 02-skill-seekers."""
        script_path = MODULE_SEEKERS / "src" / "skill_seekers" / "cli" / "main.py"
        if not script_path.exists():
            # Try module command
            cmd = [sys.executable, "-m", "skill_seekers.cli.main", "create", target_url]
        else:
            cmd = [sys.executable, str(script_path), "create", target_url]

        if name:
            cmd.extend(["--name", name])
        if output_dir:
            cmd.extend(["--output-dir", str(output_dir)])

        env = os.environ.copy()
        env["PYTHONPATH"] = str(MODULE_SEEKERS / "src") + os.pathsep + env.get("PYTHONPATH", "")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, env=env)
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "target": target_url
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def convert_video(self, video_input, output_dir=None, host="codex", language=None, output_language=None):
        """Convert video or playlist to skill using 01-video-to-skill."""
        import tempfile
        workspace_dir = Path(output_dir) if output_dir else Path(tempfile.gettempdir()) / "video_to_skill_workspace"
        workspace_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            sys.executable,
            "-m", "video_to_skill.cli",
            "run",
            str(video_input),
            "--workspace", str(workspace_dir),
            "--host", str(host),
        ]
        if output_dir:
            cmd.extend(["--output", str(output_dir)])
        if language:
            cmd.extend(["--language", str(language)])
        if output_language:
            cmd.extend(["--output-language", str(output_language)])

        env = os.environ.copy()
        env["PYTHONPATH"] = str(MODULE_VIDEO / "src") + os.pathsep + env.get("PYTHONPATH", "")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, env=env)
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "video": str(video_input),
                "workspace": str(workspace_dir),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def validate_skill(self, skill_dir):
        """Validate an Agent Skill folder against open Agent Skills standard."""
        skill_path = Path(skill_dir).resolve()
        cmd = [sys.executable, "-m", "skills_ref.cli", "validate", str(skill_path)]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(MODULE_AGENT_SKILLS / "skills-ref" / "src") + os.pathsep + env.get("PYTHONPATH", "")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, env=env)
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "skill_path": str(skill_path)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def build_mcp_server(self, skill_dir, output_dir=None, server_name=None):
        """
        Generate an executable FastMCP server wrapper from any Agent Skill folder.
        Leverages 04-mcp-python-sdk to expose skill chapters and tools as MCP functions.
        """
        skill_path = Path(skill_dir).resolve()
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            return {"success": False, "error": f"No SKILL.md found in {skill_path}"}

        # Parse skill name
        title = server_name or skill_path.name
        safe_name = title.lower().replace("-", "_").replace(" ", "_")
        
        target_dir = Path(output_dir).resolve() if output_dir else skill_path / "mcp_server"
        target_dir.mkdir(parents=True, exist_ok=True)
        server_file = target_dir / "server.py"

        server_code = f'''#!/usr/bin/env python3
"""
MCP Server generated automatically by Skill-to-Tools Ecosystem
Wrapping Agent Skill: {title}
Powered by Model Context Protocol Python SDK (04-mcp-python-sdk)
"""

import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_ROOT / "SKILL.md"

mcp = FastMCP("{title} Knowledge Server")

@mcp.tool()
def get_skill_overview() -> str:
    """Retrieve full core instructions, frameworks, and philosophy for {title}."""
    if SKILL_MD.exists():
        return SKILL_MD.read_text(encoding="utf-8")
    return "SKILL.md not found."

@mcp.tool()
def list_skill_references() -> list:
    """List all reference documents and chapters available in this skill."""
    refs = []
    for sub in ["references", "chapters", "docs"]:
        target = SKILL_ROOT / sub
        if target.is_dir():
            for f in target.glob("*.md"):
                refs.append(f"{{sub}}/{{f.name}}")
    return refs

@mcp.tool()
def read_skill_reference(relative_path: str) -> str:
    """Read a specific chapter or reference document from the skill."""
    safe_path = SKILL_ROOT / relative_path
    if safe_path.exists() and safe_path.is_file():
        return safe_path.read_text(encoding="utf-8")
    return f"File not found: {{relative_path}}"

if __name__ == "__main__":
    mcp.run()
'''
        server_file.write_text(server_code, encoding="utf-8")

        # Create runner script
        runner_cmd = target_dir / "run_server.cmd"
        runner_cmd.write_text(f"@echo off\npython \"%~dp0server.py\"\n", encoding="utf-8")

        return {
            "success": True,
            "server_path": str(server_file),
            "runner_path": str(runner_cmd),
            "server_name": safe_name
        }
