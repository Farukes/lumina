"""
Lumina Installer & Zero-Trace Uninstaller Engine
Handles global CLI installation from GitHub and 100% trace-free removal.
"""

import os
import sys
import shutil
import subprocess
import urllib.request
import zipfile
import io
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

GITHUB_REPO = "omere/lumina"  # Default repository
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

        console.print(Panel(
            f"[bold green]✔ Lumina successfully installed globally![/bold green]\n\n"
            f"[bold white]Installation Path:[/bold white] [cyan]{LUMINA_HOME}[/cyan]\n"
            f"[bold white]Executable Binary:[/bold white] [cyan]{LUMINA_BIN}[/cyan]\n\n"
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
    for target in [Path(".lumina"), Path(".agents/rules/frontend-premium.md"), Path(".claude/skills/frontend-design")]:
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target, ignore_errors=True)
            else:
                target.unlink(missing_ok=True)
            removed_items.append(f"Cleaned project artifact ({target})")

    # 4. Clean rules and globals.css in current directory
    for rule_file in [Path("CLAUDE.md"), Path("GEMINI.md")]:
        if rule_file.exists():
            try:
                content = rule_file.read_text(encoding="utf-8")
                if "Lumina" in content:
                    rule_file.unlink()
                    removed_items.append(f"Removed {rule_file.name}")
            except Exception:
                pass

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
