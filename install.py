#!/usr/bin/env python3
"""
Lumina One-Line Global Installer
Usage:
  python install.py
Or from web:
  python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Farukes/lumina/main/install.py').read())"
"""

import os
import sys

# Ensure UTF-8 stdout on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import subprocess
import shutil
import urllib.request
import zipfile
import io
from pathlib import Path

REPO = "Farukes/lumina"
BRANCH = "main"
LUMINA_HOME = Path.home() / ".lumina"
LUMINA_BIN = LUMINA_HOME / "bin"

def main():
    print("\n⚡ LUMINA GLOBAL INSTALLER // WORLD-CLASS FRONTEND TOOLKIT")
    print("=" * 60)

    # 1. Ensure dependencies (click, rich)
    print("\n[1/3] Checking Python dependencies (click, rich)...")
    try:
        import click
        import rich
    except ImportError:
        print("Installing required dependencies (click, rich, questionary)...")
        subprocess.run([sys.executable, "-m", "pip", "install", "click", "rich", "questionary"], check=True)

    # 2. Setup directories
    print("[2/3] Setting up ~/.lumina environment...")
    LUMINA_HOME.mkdir(parents=True, exist_ok=True)
    LUMINA_BIN.mkdir(parents=True, exist_ok=True)

    dest_engine = LUMINA_HOME / "engine"

    # Check if run locally or remotely
    local_script = Path(__file__).resolve().parent / "lumina" / "cli.py"
    if local_script.exists():
        print("  -> Syncing engine from local repository...")
        root = local_script.parent.parent
        shutil.copytree(root / "lumina", dest_engine / "lumina", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        shutil.copytree(root / "mcp", dest_engine / "mcp", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        if (root / "components").exists():
            shutil.copytree(root / "components", dest_engine / "components", dirs_exist_ok=True)
        if (root / "showcase").exists():
            shutil.copytree(root / "showcase", dest_engine / "showcase", dirs_exist_ok=True)
    else:
        print(f"  -> Downloading latest release from https://github.com/{REPO}...")
        zip_url = f"https://github.com/{REPO}/archive/refs/heads/{BRANCH}.zip"
        req = urllib.request.Request(zip_url, headers={"User-Agent": "Lumina-Installer"})
        with urllib.request.urlopen(req) as resp:
            zip_data = resp.read()
        with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
            zf.extractall(LUMINA_HOME)
        extracted = LUMINA_HOME / f"lumina-{BRANCH}"
        if extracted.exists():
            if dest_engine.exists():
                shutil.rmtree(dest_engine, ignore_errors=True)
            extracted.rename(dest_engine)

    cli_path = dest_engine / "lumina" / "cli.py"

    # 3. Create wrappers & PATH
    print("[3/3] Registering global 'lumina' command in PATH...")
    if sys.platform == "win32":
        cmd_wrapper = LUMINA_BIN / "lumina.cmd"
        cmd_wrapper.write_text(f'@echo off\npython "{cli_path}" %*\n', encoding="utf-8")

        ps1_wrapper = LUMINA_BIN / "lumina.ps1"
        ps1_wrapper.write_text(f'& python "{cli_path}" @args\n', encoding="utf-8")

        # Windows User PATH
        try:
            ps_cmd = (
                f'$curr = [Environment]::GetEnvironmentVariable("PATH", "User"); '
                f'if ($curr -notlike "*{LUMINA_BIN}*") {{ '
                f'[Environment]::SetEnvironmentVariable("PATH", "$curr;{LUMINA_BIN}", "User") }}'
            )
            subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True, capture_output=True)
        except Exception:
            pass
    else:
        sh_wrapper = LUMINA_BIN / "lumina"
        sh_wrapper.write_text(f'#!/usr/bin/env bash\npython3 "{cli_path}" "$@"\n', encoding="utf-8")
        sh_wrapper.chmod(0o755)
        for rc in [Path.home() / ".bashrc", Path.home() / ".zshrc"]:
            if rc.exists() and str(LUMINA_BIN) not in rc.read_text(encoding="utf-8"):
                with open(rc, "a", encoding="utf-8") as f:
                    f.write(f'\nexport PATH="$PATH:{LUMINA_BIN}"\n')

    # 4. Register MCP Server
    print("\n[4/4] Registering Lumina MCP Server in Antigravity & AI Assistants...")
    try:
        import json
        gemini_dir = Path.home() / ".gemini"
        if gemini_dir.exists():
            gemini_config = gemini_dir / "config" / "mcp_config.json"
            gemini_config.parent.mkdir(parents=True, exist_ok=True)
            data = {}
            if gemini_config.exists():
                try:
                    data = json.loads(gemini_config.read_text(encoding="utf-8"))
                except Exception:
                    data = {}
            mcp_servers = data.get("mcpServers", {})
            mcp_servers["lumina"] = {
                "command": "lumina",
                "args": ["mcp"]
            }
            data["mcpServers"] = mcp_servers
            gemini_config.write_text(json.dumps(data, indent=2), encoding="utf-8")
            print("  ✔ Configured Lumina MCP in Antigravity (~/.gemini/config/mcp_config.json)")
    except Exception:
        pass

    print("\n" + "=" * 60)
    print("✔ LUMINA SUCCESSFULLY INSTALLED GLOBALLY!")
    print("=" * 60)
    print(f"Engine Path: {LUMINA_HOME}")
    print(f"Binary Path: {LUMINA_BIN}\n")
    print("Now you can open ANY terminal and simply type:")
    print("  lumina          -> Launch interactive menu")
    print("  lumina on       -> Enable luxury design in current project")
    print("  lumina fix      -> Polish & fix AI-slop in codebase")
    print("  lumina check    -> Score codebase design (0-100)")
    print("  lumina remove   -> Clean project")
    print("  lumina uninstall-> Remove completely from entire computer without a trace\n")

if __name__ == "__main__":
    main()
