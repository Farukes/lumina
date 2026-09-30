"""
LUMINA CLI - Master CLI Entry Point for Antigravity & Claude Code Builders
"""
import os
import sys
import webbrowser
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add project root to sys.path for direct execution
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn

from lumina.banner import print_banner
from lumina.core.themes import THEMES
from lumina.core.rules_generator import inject_rules
from lumina.core.registry import COMPONENTS
from lumina.core.auditor import DesignAuditor
from lumina.core.prompt_engine import generate_prompt, PROMPT_TEMPLATES

console = Console()

@click.group()
@click.version_option("1.0.0", prog_name="lumina")
def main():
    """Lumina CLI - Premium Frontend Engine for AGY & Claude Code."""
    pass

# ---------------------------------------------------------------------------
# COMMAND: INIT
# ---------------------------------------------------------------------------
@main.command()
@click.option("--theme", "-t", default=None, help="Theme ID (linear-dark, apple-clean, vercel-mono, stripe-saas, cyber-tactile)")
@click.option("--force", "-f", is_flag=True, help="Force overwrite existing configurations")
def init(theme, force):
    """Initialize Lumina in the current workspace with AGY/Claude rules & theme tokens."""
    print_banner("Project Scaffolding & AI Rule Injection")

    selected_theme_id = theme
    if not selected_theme_id:
        try:
            import questionary
            theme_choices = [
                f"{t.id} - {t.name} ({t.archetype})" for t in THEMES.values()
            ]
            choice = questionary.select(
                "Select your project's visual aesthetic DNA:",
                choices=theme_choices,
                default=theme_choices[0]
            ).ask()
            if not choice:
                console.print("[yellow]Initialization cancelled.[/yellow]")
                return
            selected_theme_id = choice.split(" - ")[0]
        except Exception:
            selected_theme_id = "linear-dark"

    theme_def = THEMES.get(selected_theme_id, THEMES["linear-dark"])

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        # Task 1: Ingest Rules
        t1 = progress.add_task("Injecting AGY & Claude Code design constitutions...", total=1)
        res = inject_rules(".")
        progress.update(t1, advance=1)

        # Task 2: Inject Theme CSS
        t2 = progress.add_task(f"Applying theme tokens ({theme_def.name})...", total=1)
        css_dir = Path("styles") if Path("styles").exists() else Path("src") / "app" if (Path("src") / "app").exists() else Path(".")
        css_file = css_dir / "globals.css"
        if not css_file.exists():
            css_file = Path("globals.css")
        
        with open(css_file, "a" if css_file.exists() else "w", encoding="utf-8") as f:
            f.write(f"\n/* --- LUMINA DESIGN TOKENS ({theme_def.name}) --- */\n")
            f.write(theme_def.css_variables)
            f.write("\n")
        progress.update(t2, advance=1)

    console.print(Panel(
        f"[bold green]✔ Lumina successfully initialized in this project![/bold green]\n\n"
        f"[bold cyan]Selected Theme:[/bold cyan] {theme_def.name} ({theme_def.archetype})\n"
        f"[bold cyan]Active Rules:[/bold cyan]\n"
        + "\n".join([f"  • {f}" for f in res["created_files"]]) +
        f"\n  • {css_file}\n\n"
        f"[bold yellow]Next Steps:[/bold yellow]\n"
        f"  1. Run [bold white]lumina add bento-grid[/bold white] to inject world-class components.\n"
        f"  2. Run [bold white]lumina audit[/bold white] to check existing code for AI-slop.\n"
        f"  3. Ask AGY or Claude Code to build UI; it now automatically follows the Lumina Constitution!",
        title="[bold blue]Setup Complete[/bold blue]",
        border_style="green"
    ))

# ---------------------------------------------------------------------------
# COMMAND: THEME
# ---------------------------------------------------------------------------
@main.command()
@click.argument("name", required=False)
def theme(name):
    """View or switch between the 5 world-class aesthetic presets."""
    if not name:
        print_banner("Theme Explorer")
        table = Table(title="💎 Lumina World-Class Theme Presets", border_style="bright_blue")
        table.add_column("ID", style="bold cyan")
        table.add_column("Name", style="bold white")
        table.add_column("Archetype", style="magenta")
        table.add_column("Signature Traits", style="dim")

        for t in THEMES.values():
            table.add_row(
                t.id,
                t.name,
                t.archetype,
                "\n".join([f"• {trait}" for trait in t.traits[:3]])
            )
        console.print(table)
        console.print("\n[dim]To apply a theme, run:[/dim] [bold green]lumina theme <id>[/bold green]\n")
        return

    theme_def = THEMES.get(name)
    if not theme_def:
        console.print(f"[bold red]Error:[/bold red] Theme '{name}' not found. Available: {', '.join(THEMES.keys())}")
        return

    css_file = Path("globals.css")
    if not css_file.exists() and (Path("src") / "app" / "globals.css").exists():
        css_file = Path("src") / "app" / "globals.css"

    with open(css_file, "a" if css_file.exists() else "w", encoding="utf-8") as f:
        f.write(f"\n/* --- LUMINA DESIGN TOKENS ({theme_def.name}) --- */\n")
        f.write(theme_def.css_variables)
        f.write("\n")

    console.print(f"[bold green]✔ Applied theme '{theme_def.name}' to {css_file}![/bold green]")

# ---------------------------------------------------------------------------
# COMMAND: ADD
# ---------------------------------------------------------------------------
@main.command()
@click.argument("component", required=False)
def add(component):
    """Add a handcrafted AAA-tier component to your project."""
    if not component:
        print_banner("Component Registry")
        table = Table(title="📦 Available Lumina AAA Components", border_style="bright_blue")
        table.add_column("ID", style="bold cyan")
        table.add_column("Component", style="bold white")
        table.add_column("Category", style="magenta")
        table.add_column("Dependencies", style="yellow")
        table.add_column("Description", style="dim")

        for c in COMPONENTS.values():
            table.add_row(
                c.id,
                c.name,
                c.category,
                ", ".join(c.dependencies) if c.dependencies else "None",
                c.description
            )
        console.print(table)
        console.print("\n[dim]To inject a component, run:[/dim] [bold green]lumina add <component-id>[/bold green]\n")
        return

    comp_item = COMPONENTS.get(component)
    if not comp_item:
        console.print(f"[bold red]Error:[/bold red] Component '{component}' not found. Run [bold cyan]lumina add[/bold cyan] to see available blocks.")
        return

    dest_path = Path(comp_item.filename)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(comp_item.code)

    console.print(Panel(
        f"[bold green]✔ Successfully created [bold white]{comp_item.filename}[/bold white]![/bold green]\n\n"
        f"[bold cyan]Category:[/bold cyan] {comp_item.category}\n"
        f"[bold cyan]Dependencies required:[/bold cyan] {', '.join(comp_item.dependencies) if comp_item.dependencies else 'None'}\n\n"
        f"[dim]Install dependencies if needed:[/dim]\n"
        f"[bold white]npm install {' '.join(comp_item.dependencies)}[/bold white]",
        title=f"[bold blue]{comp_item.name}[/bold blue]",
        border_style="green"
    ))

# ---------------------------------------------------------------------------
# COMMAND: AUDIT
# ---------------------------------------------------------------------------
@main.command()
@click.option("--path", "-p", default=".", help="Directory to scan")
def audit(path):
    """Scan workspace for AI-slop anti-patterns & generate an AI refactoring prompt."""
    print_banner("AI-Slop Codebase Auditor")

    auditor = DesignAuditor(path)
    with console.status("[bold cyan]Scanning JSX, TSX, HTML and CSS files for AI slop...", spinner="dots"):
        result = auditor.audit()

    score = result["score"]
    score_color = "green" if score >= 85 else "yellow" if score >= 70 else "red"

    console.print(Panel(
        f"[bold {score_color}]Design Quality Score: {score} / 100[/bold {score_color}] — [bold white]{result['grade']}[/bold white]\n"
        f"Files Scanned: [cyan]{result['files_scanned']}[/cyan] | Issues Detected: [magenta]{result['total_issues']}[/magenta]",
        border_style=score_color,
        title="[bold]Audit Summary[/bold]"
    ))

    if result["issues"]:
        table = Table(title="Detected AI-Slop Tells", border_style="red")
        table.add_column("Severity", style="bold")
        table.add_column("Location", style="cyan")
        table.add_column("Issue", style="white")
        table.add_column("Recommendation", style="green")

        for iss in result["issues"][:15]:
            sev_style = "bold red" if iss.severity == "HIGH" else "yellow" if iss.severity == "MEDIUM" else "blue"
            table.add_row(
                Text(iss.severity, style=sev_style),
                f"{iss.file_path}:{iss.line_number}",
                iss.message,
                iss.recommendation
            )
        console.print(table)

        # Generate fix prompt
        prompt_content = auditor.generate_fix_prompt(result)
        out_dir = Path(".lumina")
        out_dir.mkdir(exist_ok=True)
        prompt_path = out_dir / "ai-fix-prompt.md"
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt_content)

        console.print(f"\n[bold green]✔ Auto-Fix Prompt generated at:[/bold green] [bold cyan]{prompt_path}[/bold cyan]")
        console.print("[dim]Feed this prompt to AGY or Claude Code to eliminate all detected slop in one pass![/dim]\n")
    else:
        console.print("[bold green]🎉 Zero AI slop detected! Your code adheres to world-class design standards.[/bold green]\n")

# ---------------------------------------------------------------------------
# COMMAND: PROMPT
# ---------------------------------------------------------------------------
@main.command()
@click.argument("feature", required=False)
def prompt(feature):
    """Generate a zero-slop architectural prompt for AGY or Claude Code."""
    if not feature:
        print_banner("Zero-Slop Prompt Generator")
        console.print("[bold cyan]Available Presets:[/bold cyan] " + ", ".join(PROMPT_TEMPLATES.keys()))
        console.print("\n[dim]Usage:[/dim] [bold green]lumina prompt dashboard[/bold green] or [bold green]lumina prompt \"custom feature\"[/bold green]\n")
        return

    generated = generate_prompt(feature)
    console.print(Panel(
        generated,
        title=f"[bold green]Lumina AI Prompt Directive: {feature.upper()}[/bold green]",
        border_style="cyan"
    ))
    console.print("[dim]Copy and send this prompt to AGY or Claude Code for flawless execution.[/dim]\n")

# ---------------------------------------------------------------------------
# COMMAND: RULES
# ---------------------------------------------------------------------------
@main.command()
def rules():
    """Inject or refresh AGY and Claude Code rule constitutions."""
    print_banner("Rule Constitution Ingestion")
    res = inject_rules(".")
    console.print(f"[bold green]✔ Injected rules into {len(res['created_files'])} locations:[/bold green]")
    for f in res["created_files"]:
        console.print(f"  • [cyan]{f}[/cyan]")

# ---------------------------------------------------------------------------
# COMMAND: SHOWCASE
# ---------------------------------------------------------------------------
@main.command()
def showcase():
    """Launch the interactive live HTML5 showcase in your browser."""
    print_banner("Launching Interactive Showcase")
    showcase_path = Path(__file__).parent.parent / "showcase" / "index.html"
    if showcase_path.exists():
        console.print(f"[bold green]Opening showcase in browser...[/bold green] ([dim]{showcase_path}[/dim])")
        webbrowser.open(showcase_path.as_uri())
    else:
        console.print("[red]Showcase file not found.[/red]")

# ---------------------------------------------------------------------------
# COMMAND: GHOST (The In-Browser AI HUD & Reverse-Agent Teleport)
# ---------------------------------------------------------------------------
@main.command()
@click.option("--no-browser", is_flag=True, help="Do not automatically open browser demo")
def ghost(no_browser):
    """Launch the Lumina Ghost in-browser AI HUD bridge (port 3939)."""
    print_banner("Lumina Ghost // In-Browser AI HUD Bridge")
    bridge_script = Path(__file__).parent.parent / "ghost" / "bridge.py"
    from ghost.bridge import run_bridge
    run_bridge(open_browser=not no_browser)

if __name__ == "__main__":
    main()

