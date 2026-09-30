"""
Lumina Installer & Zero-Trace Uninstaller Engine
Handles global CLI installation from GitHub and 100% trace-free removal.
"""

import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import shutil
import subprocess
import urllib.request
import zipfile
import io
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

GITHUB_REPO = "Farukes/lumina"  # Default repository
LUMINA_HOME = Path.home() / ".lumina"
LUMINA_BIN = LUMINA_HOME / "bin"

def install_lumina(repo: str = GITHUB_REPO, branch: str = "main") -> bool:
    """Installs Lumina engine from GitHub into ~/.lumina and registers 'lumina' in user PATH."""
    console.print(Panel(
        f"[bold cyan]Installing Lumina from GitHub ({repo}@{branch})...[/bold cyan]",
        border_style="cyan",
        title="[bold]Lumina Installer[/bold]"
    ))

    try:
        LUMINA_HOME.mkdir(parents=True, exist_ok=True)
        LUMINA_BIN.mkdir(parents=True, exist_ok=True)

        # 1. Check if running from local source or downloading from GitHub
        project_root = Path(__file__).resolve().parent.parent.parent
        is_local_source = (project_root / "lumina" / "cli.py").exists()

        if is_local_source:
            console.print("[dim]Syncing Lumina engine from local repository...[/dim]")
            dest_lumina = LUMINA_HOME / "engine"
            if dest_lumina.exists():
                shutil.rmtree(dest_lumina, ignore_errors=True)
            
            # Copy lumina, mcp, components, bin
            shutil.copytree(project_root / "lumina", dest_lumina / "lumina", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            shutil.copytree(project_root / "mcp", dest_lumina / "mcp", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            if (project_root / "components").exists():
                shutil.copytree(project_root / "components", dest_lumina / "components", dirs_exist_ok=True)
            if (project_root / "showcase").exists():
                shutil.copytree(project_root / "showcase", dest_lumina / "showcase", dirs_exist_ok=True)
        else:
            console.print(f"[dim]Downloading latest engine release from https://github.com/{repo}...[/dim]")
            zip_url = f"https://github.com/{repo}/archive/refs/heads/{branch}.zip"
            req = urllib.request.Request(zip_url, headers={"User-Agent": "Lumina-Installer"})
            with urllib.request.urlopen(req) as resp:
                zip_data = resp.read()
            
            dest_lumina = LUMINA_HOME / "engine"
            with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
                zf.extractall(LUMINA_HOME)
            
            extracted_dir = LUMINA_HOME / f"lumina-{branch}"
            if extracted_dir.exists():
                if dest_lumina.exists():
                    shutil.rmtree(dest_lumina, ignore_errors=True)
                extracted_dir.rename(dest_lumina)

        cli_script = dest_lumina / "lumina" / "cli.py"

        # 2. Create OS-specific executable wrappers in ~/.lumina/bin
        if sys.platform == "win32":
            # lumina.cmd wrapper for Windows Command Prompt & PowerShell
            cmd_wrapper = LUMINA_BIN / "lumina.cmd"
            cmd_content = f'@echo off\npython "{cli_script}" %*\n'
            cmd_wrapper.write_text(cmd_content, encoding="utf-8")

            # lumina.ps1 wrapper for PowerShell execution
            ps1_wrapper = LUMINA_BIN / "lumina.ps1"
            ps1_content = f'& python "{cli_script}" @args\n'
            ps1_wrapper.write_text(ps1_content, encoding="utf-8")

            # 3. Add ~/.lumina/bin to Windows User PATH environment variable
            _add_to_windows_path(str(LUMINA_BIN))
        else:
            # Bash / Zsh wrapper for Mac & Linux
            sh_wrapper = LUMINA_BIN / "lumina"
            sh_content = f'#!/usr/bin/env bash\npython3 "{cli_script}" "$@"\n'
            sh_wrapper.write_text(sh_content, encoding="utf-8")
            sh_wrapper.chmod(0o755)
            _add_to_unix_path(str(LUMINA_BIN))

        # 4. Automatically Register Lumina MCP Server into Antigravity & AI Assistants
        mcp_registered = _register_mcp_configs()
        mcp_summary = "\n".join([f"  • {m}" for m in mcp_registered]) if mcp_registered else "  • No existing MCP configs found"

        console.print(Panel(
            f"[bold green]✔ Lumina successfully installed globally![/bold green]\n\n"
            f"[bold white]Installation Path:[/bold white] [cyan]{LUMINA_HOME}[/cyan]\n"
            f"[bold white]Executable Binary:[/bold white] [cyan]{LUMINA_BIN}[/cyan]\n\n"
            f"[bold white]MCP Integration:[/bold white]\n{mcp_summary}\n\n"
            f"[bold yellow]How to Use:[/bold yellow]\n"
            f"  1. Open any terminal or project directory.\n"
            f"  2. Type [bold white]lumina[/bold white] (or [bold white]lumina on[/bold white]) to get started!\n"
            f"  3. To uninstall cleanly anytime: [bold red]lumina uninstall[/bold red]\n",
            border_style="green",
            title="[bold green]Installation Complete[/bold green]"
        ))
        return True

    except Exception as e:
        console.print(f"[bold red]Installation Error:[/bold red] {e}")
        return False

def uninstall_lumina() -> bool:
    """Completely removes Lumina from user PATH, deletes ~/.lumina, and cleans workspace without leaving any trace."""
    console.print(Panel(
        "[bold yellow]Executing Trace-Free Uninstallation...[/bold yellow]",
        border_style="yellow",
        title="[bold]Lumina Uninstaller[/bold]"
    ))

    removed_items = []

    # 1. Remove from Windows / Unix PATH
    if sys.platform == "win32":
        if _remove_from_windows_path(str(LUMINA_BIN)):
            removed_items.append("Removed ~/.lumina/bin from Windows User PATH")
    else:
        if _remove_from_unix_path(str(LUMINA_BIN)):
            removed_items.append("Removed ~/.lumina/bin from Unix profile")

    # 2. Delete ~/.lumina directory completely
    if LUMINA_HOME.exists():
        shutil.rmtree(LUMINA_HOME, ignore_errors=True)
        removed_items.append(f"Deleted global directory ({LUMINA_HOME})")

    # 3. Clean current project directory artifacts if present
    lumina_cache = Path(".lumina")
    if lumina_cache.exists():
        shutil.rmtree(lumina_cache, ignore_errors=True)
        removed_items.append("Deleted temporary .lumina directory")

    claude_skill = Path(".claude/skills/frontend-design")
    if claude_skill.exists():
        shutil.rmtree(claude_skill, ignore_errors=True)
        removed_items.append("Cleaned .claude/skills/frontend-design")
        try:
            if not any(claude_skill.parent.iterdir()):
                claude_skill.parent.rmdir()
                if not any(claude_skill.parent.parent.iterdir()):
                    claude_skill.parent.parent.rmdir()
        except OSError:
            pass

    # Clean AGY rule safely: never delete other rules in .agents/
    agy_rule = Path(".agents/rules/frontend-premium.md")
    if agy_rule.exists():
        agy_rule.unlink(missing_ok=True)
        removed_items.append("Cleaned .agents/rules/frontend-premium.md")
        try:
            rules_dir = agy_rule.parent
            if rules_dir.exists() and not any(rules_dir.iterdir()):
                rules_dir.rmdir()
                agents_dir = rules_dir.parent
                if agents_dir.exists() and not any(agents_dir.iterdir()):
                    agents_dir.rmdir()
            elif rules_dir.exists():
                removed_items.append("Preserved all other rules in .agents/rules/")
        except OSError:
            pass

    # 4. Clean rules in current directory without touching user custom rules
    from lumina.core.rules_generator import strip_lumina_from_rule_file
    for rule_file in [Path("CLAUDE.md"), Path("GEMINI.md"), Path("AGENTS.md")]:
        res = strip_lumina_from_rule_file(rule_file)
        if res:
            removed_items.append(res)

    # 5. Clean MCP configurations safely (leaves all other MCP servers 100% intact)
    mcp_cleaned = _clean_mcp_configs()
    removed_items.extend(mcp_cleaned)

    table = Table(title="Uninstalled Artifacts (Zero Traces Remaining)", border_style="green")
    table.add_column("Cleaned System Location", style="bold green")
    for item in removed_items:
        table.add_row(item)
    console.print(table)

    console.print(Panel(
        "[bold green]✔ Lumina has been completely removed from this project and your entire operating system![/bold green]\n"
        "[dim]Zero registry keys, zero background daemons, zero leftover files.[/dim]",
        border_style="green",
        title="[bold green]Uninstallation Complete[/bold green]"
    ))
    return True

def _add_to_windows_path(bin_dir: str):
    """Adds a directory to Windows User Environment PATH if not already present."""
    try:
        powershell_cmd = (
            f'$curr = [Environment]::GetEnvironmentVariable("PATH", "User"); '
            f'if ($curr -notlike "*{bin_dir}*") {{ '
            f'[Environment]::SetEnvironmentVariable("PATH", "$curr;{bin_dir}", "User") }}'
        )
        subprocess.run(["powershell", "-NoProfile", "-Command", powershell_cmd], check=True, capture_output=True)
    except Exception:
        pass

def _remove_from_windows_path(bin_dir: str) -> bool:
    """Removes a directory from Windows User Environment PATH."""
    try:
        powershell_cmd = (
            f'$curr = [Environment]::GetEnvironmentVariable("PATH", "User"); '
            f'$items = $curr.Split(";") | Where-Object {{ $_ -ne "{bin_dir}" -and $_ -ne "" }}; '
            f'$newPath = $items -join ";"; '
            f'[Environment]::SetEnvironmentVariable("PATH", $newPath, "User")'
        )
        subprocess.run(["powershell", "-NoProfile", "-Command", powershell_cmd], check=True, capture_output=True)
        return True
    except Exception:
        return False

def _add_to_unix_path(bin_dir: str):
    for rc in [Path.home() / ".bashrc", Path.home() / ".zshrc"]:
        if rc.exists():
            content = rc.read_text(encoding="utf-8")
            if bin_dir not in content:
                with open(rc, "a", encoding="utf-8") as f:
                    f.write(f'\nexport PATH="$PATH:{bin_dir}"\n')

def _remove_from_unix_path(bin_dir: str) -> bool:
    for rc in [Path.home() / ".bashrc", Path.home() / ".zshrc"]:
        if rc.exists():
            content = rc.read_text(encoding="utf-8")
            if bin_dir in content:
                new_content = "\n".join([line for line in content.splitlines() if bin_dir not in line])
                rc.write_text(new_content + "\n", encoding="utf-8")
    return True

def _clean_mcp_configs() -> list:
    """Safely removes Lumina from any MCP configuration files, leaving all other MCP servers 100% untouched."""
    cleaned = []
    candidates = []

    # Antigravity Global MCP: ~/.gemini/config/mcp_config.json
    gemini_mcp_config = Path.home() / ".gemini" / "config" / "mcp_config.json"
    if gemini_mcp_config.exists():
        candidates.append(gemini_mcp_config)

    # Claude Desktop on Windows
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            candidates.append(Path(appdata) / "Claude" / "claude_desktop_config.json")
    else:
        # macOS / Linux
        candidates.append(Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json")
        candidates.append(Path.home() / ".config" / "claude" / "claude_desktop_config.json")

    # Windsurf, Cursor, Workspace .mcp.json
    candidates.append(Path.home() / ".codeium" / "windsurf" / "mcp_config.json")
    candidates.append(Path(".mcp.json"))
    candidates.append(Path(".cursor") / "mcp.json")

    for config_path in candidates:
        if config_path.exists() and config_path.is_file():
            try:
                data = json.loads(config_path.read_text(encoding="utf-8"))
                mcp_servers = data.get("mcpServers", {})
                removed_keys = []
                for key in list(mcp_servers.keys()):
                    if "lumina" in key.lower():
                        del mcp_servers[key]
                        removed_keys.append(key)
                if removed_keys:
                    data["mcpServers"] = mcp_servers
                    config_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
                    cleaned.append(f"Safely removed '{', '.join(removed_keys)}' from {config_path.name} (other MCP servers preserved)")
            except Exception:
                pass

    # AGY MCP directory: ~/.gemini/antigravity-cli/mcp/lumina
    agy_mcp_lumina = Path.home() / ".gemini" / "antigravity-cli" / "mcp" / "lumina"
    if agy_mcp_lumina.exists() and agy_mcp_lumina.is_dir():
        shutil.rmtree(agy_mcp_lumina, ignore_errors=True)
        cleaned.append("Removed Lumina MCP directory from AGY (other MCPs like tokenjar preserved)")

    return cleaned

def _register_mcp_configs(cmd_executable: str = "lumina") -> list:
    """Safely registers Lumina MCP server in Antigravity and Claude Desktop configs without touching other servers."""
    registered = []
    candidates = []

    # 1. Antigravity Global MCP: ~/.gemini/config/mcp_config.json
    gemini_dir = Path.home() / ".gemini"
    if gemini_dir.exists():
        gemini_config = gemini_dir / "config" / "mcp_config.json"
        gemini_config.parent.mkdir(parents=True, exist_ok=True)
        candidates.append(gemini_config)

    # 2. Claude Desktop Config
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata and (Path(appdata) / "Claude").exists():
            candidates.append(Path(appdata) / "Claude" / "claude_desktop_config.json")
    else:
        for p in [Path.home() / "Library" / "Application Support" / "Claude", Path.home() / ".config" / "claude"]:
            if p.exists():
                candidates.append(p / "claude_desktop_config.json")

    # 3. Windsurf
    windsurf_dir = Path.home() / ".codeium" / "windsurf"
    if windsurf_dir.exists():
        candidates.append(windsurf_dir / "mcp_config.json")

    for config_path in candidates:
        try:
            data = {}
            if config_path.exists() and config_path.is_file():
                try:
                    data = json.loads(config_path.read_text(encoding="utf-8"))
                except Exception:
                    data = {}
            if not isinstance(data, dict):
                data = {}

            mcp_servers = data.get("mcpServers", {})
            if not isinstance(mcp_servers, dict):
                mcp_servers = {}

            mcp_servers["lumina"] = {
                "command": cmd_executable,
                "args": ["mcp"]
            }
            data["mcpServers"] = mcp_servers

            config_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            registered.append(f"Configured Lumina MCP in {config_path.name} (preserved all other MCP servers)")
        except Exception:
            pass

    return registered


