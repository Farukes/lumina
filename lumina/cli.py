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
from lumina.core.polisher import StylePolisher
from lumina.core.prompt_engine import generate_prompt, PROMPT_TEMPLATES

console = Console()

@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option("2.0.0", prog_name="lumina")
def main(ctx):
    """Lumina CLI - The World-Class Frontend Engine for AGY & Claude Code."""
    if ctx.invoked_subcommand is None:
        print_banner("Ultra-Simplified CLI // Master Control")
        console.print(Panel(
            "[bold white]⚡ LUMINA CORE COMMANDS (Sadece 4 Temel Komut):[/bold white]\n\n"
            "  [bold green]lumina on[/bold green]     [dim]➔[/dim]  [cyan]Başlat:[/cyan] Projeye lüks tasarım kurallarını ve tema tokenlarını enjekte eder\n"
            "  [bold green]lumina fix[/bold green]    [dim]➔[/dim]  [cyan]Düzelt:[/cyan] Kodundaki tüm AI-slop (mor gradyan, eksik pah vb.) hatalarını otomatik refactor eder\n"
            "  [bold green]lumina check[/bold green]  [dim]➔[/dim]  [cyan]Kontrol Et:[/cyan] Kod tabanını tarar, 0-100 arası tasarım kalitesi puanı verir\n"
            "  [bold green]lumina off[/bold green]    [dim]➔[/dim]  [cyan]Kaldır:[/cyan] Projeden iz bırakmadan Lumina'yı tamamen temizler\n\n"
            "[bold white]🛠️ Hızlı Yardımcılar:[/bold white]\n"
            "  [bold yellow]lumina theme[/bold yellow]  [dim]➔[/dim]  9 lüks arketip arasında geçiş yap\n"
            "  [bold yellow]lumina view[/bold yellow]   [dim]➔[/dim]  Canlı interaktif vitrini tarayıcıda aç\n"
            "  [bold yellow]lumina add[/bold yellow]    [dim]➔[/dim]  Hazır AAA bileşen ekle (bento-grid, command-bar)\n",
            title="[bold green]Lumina CLI Quick Guide[/bold green]",
            border_style="green"
        ))
        try:
            import questionary
            action = questionary.select(
                "Ne yapmak istersiniz?",
                choices=[
                    "✨ Kodları Düzelt & Parlat (lumina fix)",
                    "🔍 Tasarım Puanını Ölç (lumina check)",
                    "🚀 Projeyi Başlat / Aç (lumina on)",
                    "🎨 Temayı Değiştir (lumina theme)",
                    "👁️ Canlı Vitrini Aç (lumina view)",
                    "🧹 Projeden Kaldır (lumina remove)",
                    "🗑️ Bütün Bilgisayardan Sil (lumina uninstall)",
                    "Çıkış"
                ]
            ).ask()
            if action and "fix" in action:
                ctx.invoke(fix_cmd)
            elif action and "check" in action:
                ctx.invoke(check_cmd)
            elif action and "on" in action:
                ctx.invoke(on_cmd)
            elif action and "theme" in action:
                ctx.invoke(theme)
            elif action and "view" in action:
                ctx.invoke(view_cmd)
            elif action and "remove" in action:
                ctx.invoke(remove_cmd)
            elif action and "uninstall" in action:
                ctx.invoke(uninstall_cmd)
        except Exception:
            pass

# ---------------------------------------------------------------------------
# COMMAND: ON (Enable Lumina in Workspace)
# ---------------------------------------------------------------------------
@main.command(name="on")
@click.option("--theme", "-t", default=None, help="Theme ID (e.g. obsidian-craft, industrial-machina, liquid-spatial)")
@click.option("--ai", default="auto", type=click.Choice(["auto", "agy", "claude", "both"]), help="Target AI assistant: auto (detected), agy, claude, or both")
@click.option("--force", "-f", is_flag=True, help="Force overwrite existing configurations")
def on_cmd(theme, ai, force):
    """Enable Lumina in the current workspace with AGY/Claude rules & theme tokens."""
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
        t1 = progress.add_task("Injecting AI design constitutions...", total=1)
        res = inject_rules(".", ai_target=ai)
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

    rules_summary = [f"  • {f}" for f in res["created_files"]]
    if res.get("skipped_files"):
        rules_summary.append("  [dim]• Sistemde bulunmayan AI araçları için gereksiz dosya üretilmedi:[/dim]")
        for skip_note in res["skipped_files"]:
            rules_summary.append(f"    [dim]- {skip_note}[/dim]")

    console.print(Panel(
        f"[bold green]✔ Lumina successfully initialized in this project![/bold green]\n\n"
        f"[bold cyan]Selected Theme:[/bold cyan] {theme_def.name} ({theme_def.archetype})\n"
        f"[bold cyan]Active Rules:[/bold cyan]\n"
        + "\n".join(rules_summary) +
        f"\n  • {css_file}\n\n"
        f"[bold yellow]Next Steps:[/bold yellow]\n"
        f"  1. Run [bold white]lumina add bento-grid[/bold white] to inject world-class components.\n"
        f"  2. Run [bold white]lumina fix[/bold white] to polish existing code for AI-slop.\n"
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
# COMMAND: CHECK (Scan & Calculate Design Quality Score)
# ---------------------------------------------------------------------------
@main.command(name="check")
@click.option("--path", "-p", default=".", help="Directory to scan")
def check_cmd(path):
    """Scan workspace for AI-slop anti-patterns & calculate 0-100 design quality score."""
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
# COMMAND: VIEW (Launch Live Showcase in Browser)
# ---------------------------------------------------------------------------
@main.command(name="view")
def view_cmd():
    """Launch the interactive live HTML5 showcase in your browser."""
    print_banner("Launching Interactive Showcase")
    showcase_path = Path(__file__).parent.parent / "showcase" / "index.html"
    if showcase_path.exists():
        console.print(f"[bold green]Opening showcase in browser...[/bold green] ([dim]{showcase_path}[/dim])")
        webbrowser.open(showcase_path.as_uri())
    else:
        console.print("[red]Showcase file not found.[/red]")

# ---------------------------------------------------------------------------
# COMMAND: FIX (Automated Codebase Refactoring & Slop Removal)
# ---------------------------------------------------------------------------
@main.command(name="fix")
@click.option("--path", "-p", default=".", help="Directory to polish")
@click.option("--dry-run", is_flag=True, help="Preview changes without saving to disk")
def fix_cmd(path, dry_run):
    """Scan and automatically refactor AI-slop into Apple/Linear design standards."""
    print_banner("Lumina Code Polisher // Automated Refactor")

    polisher = StylePolisher(path)
    with console.status("[bold cyan]Polishing codebase (chamfers, gradients, spring physics)...", spinner="dots"):
        res = polisher.polish(dry_run=dry_run)

    if res["total_fixes"] == 0:
        console.print("[bold green]🎉 Zero design defects found! Your code is already world-class.[/bold green]\n")
        return

    table = Table(title="Lumina Polished Elements", border_style="green")
    table.add_column("Location", style="cyan")
    table.add_column("Refactoring Rule", style="bold white")
    table.add_column("Original Snippet", style="red")
    table.add_column("Polished Replacement", style="green")

    for diff in res["diffs"][:20]:
        table.add_row(
            f"{diff.file_path}:{diff.line_number}",
            diff.rule_name,
            diff.original[:45] + "...",
            diff.replacement[:45] + "..."
        )

    console.print(table)
    action_text = "Previewed (Dry-Run)" if dry_run else "Refactored & Saved directly to disk"
    console.print(Panel(
        f"[bold green]✔ Successfully {action_text}![/bold green]\n\n"
        f"Files Scanned: [cyan]{res['total_files']}[/cyan] | Files Modified: [magenta]{res['modified_files']}[/magenta] | Fixes Applied: [green]{res['total_fixes']}[/green]",
        border_style="green",
        title="[bold]Polish Summary[/bold]"
    ))

# ---------------------------------------------------------------------------
# COMMAND: MCP (Model Context Protocol Server for AGY & Claude Code)
# ---------------------------------------------------------------------------
@main.command()
def mcp():
    """Launch the Lumina Model Context Protocol (MCP) server over stdio."""
    from mcp.server import main as run_mcp
    run_mcp()

# ---------------------------------------------------------------------------
# COMMAND: REMOVE / OFF (Trace-Free Complete Uninstallation)
# ---------------------------------------------------------------------------
@main.command(name="remove")
@click.option("--force", "-f", is_flag=True, default=True, help="Skip confirmation prompt")
def remove_cmd(force):
    """Remove all Lumina rules, tokens, and configs without leaving any trace."""
    import shutil
    print_banner("Trace-Free Uninstaller & Eject Engine")

    removed_items = []

    # 1. Remove .lumina/ directory
    lumina_dir = Path(".lumina")
    if lumina_dir.exists():
        shutil.rmtree(lumina_dir, ignore_errors=True)
        removed_items.append(".lumina/ (temporary reports directory)")

    # 2. Remove .agents/rules/frontend-premium.md
    agy_rule = Path(".agents/rules/frontend-premium.md")
    if agy_rule.exists():
        agy_rule.unlink()
        removed_items.append(".agents/rules/frontend-premium.md (AGY rule)")
        # remove parent dirs if empty
        try:
            agy_rule.parent.rmdir()
            agy_rule.parent.parent.rmdir()
        except OSError:
            pass

    # 3. Remove .claude/skills/frontend-design/
    claude_skill = Path(".claude/skills/frontend-design")
    if claude_skill.exists():
        shutil.rmtree(claude_skill, ignore_errors=True)
        removed_items.append(".claude/skills/frontend-design/ (Claude skill)")
        try:
            claude_skill.parent.rmdir()
            claude_skill.parent.parent.rmdir()
        except OSError:
            pass

    # 4. Remove or clean CLAUDE.md & GEMINI.md
    for rule_file in [Path("CLAUDE.md"), Path("GEMINI.md")]:
        if rule_file.exists():
            try:
                content = rule_file.read_text(encoding="utf-8")
                if "Lumina" in content or "THE LUMINA FRONTEND CONSTITUTION" in content:
                    rule_file.unlink()
                    removed_items.append(f"{rule_file.name} (design guidelines)")
            except Exception:
                pass

    # 5. Clean Lumina tokens from globals.css
    css_candidates = [Path("globals.css"), Path("styles/globals.css"), Path("src/app/globals.css")]
    for css_file in css_candidates:
        if css_file.exists():
            try:
                content = css_file.read_text(encoding="utf-8")
                import re
                cleaned = re.sub(r'/\* --- LUMINA DESIGN TOKENS.*?/\* --- END LUMINA --- \*/', '', content, flags=re.DOTALL)
                if cleaned == content:
                    # Alternative match without end marker
                    cleaned = re.sub(r'/\* --- LUMINA DESIGN TOKENS[^\n]*\n:root\s*\{[^}]*\}', '', content, flags=re.DOTALL)
                if cleaned != content:
                    css_file.write_text(cleaned.strip() + "\n", encoding="utf-8")
                    removed_items.append(f"{css_file} (stripped Lumina CSS tokens)")
            except Exception:
                pass

    # 6. Safely clean MCP configuration (never touches any other MCP server)
    try:
        from lumina.core.installer import _clean_mcp_configs
        mcp_cleaned = _clean_mcp_configs()
        removed_items.extend(mcp_cleaned)
    except Exception:
        pass

    if removed_items:
        table = Table(title="Cleaned Artifacts (Zero Traces Remaining)", border_style="green")
        table.add_column("Artifact Removed / Cleaned", style="bold green")
        for item in removed_items:
            table.add_row(item)
        console.print(table)
        console.print(Panel(
            "[bold green]✔ Lumina has been completely removed from this project without leaving any trace![/bold green]\n"
            "[dim]No registry entries, no daemons, no background processes, no orphaned files.[/dim]",
            border_style="green",
            title="[bold]Eject Successful[/bold]"
        ))
    else:
        console.print("[yellow]No Lumina artifacts or configurations found in this directory.[/yellow]")

@main.command(name="off", hidden=True)
@click.option("--force", "-f", is_flag=True, default=True, help="Skip confirmation prompt")
def off_cmd(force):
    """Alias for remove."""
    return remove_cmd(force)


# ---------------------------------------------------------------------------
# COMMAND: INSTALL (Download and Install Globally from GitHub)
# ---------------------------------------------------------------------------
@main.command(name="install")
@click.option("--repo", "-r", default="Farukes/lumina", help="GitHub repository (user/repo)")
@click.option("--branch", "-b", default="main", help="Git branch")
def install_cmd(repo, branch):
    """Download and install Lumina globally to your computer from GitHub."""
    from lumina.core.installer import install_lumina
    install_lumina(repo=repo, branch=branch)

# ---------------------------------------------------------------------------
# COMMAND: UNINSTALL (Completely Remove Lumina from Entire Computer)
# ---------------------------------------------------------------------------
@main.command(name="uninstall")
def uninstall_cmd():
    """Completely remove Lumina from your entire system without leaving any trace."""
    from lumina.core.installer import uninstall_lumina
    uninstall_lumina()

if __name__ == "__main__":
    main()

