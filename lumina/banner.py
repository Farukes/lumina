import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console(highlight=False)

LOGO = r"""
 ██▓     █    ██  ███▄ ▄███▓ ██▓ ███▄    █  ▄▄▄      
▓██▒     ██  ▓██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒████▄    
▒██░    ▓██  ▒██░▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██  ▀█▄  
▒██░    ▓▓█  ░██░▒██    ▓██ ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
░██████▒▒▒█████▓ ▒██▒   ░██▒░██░▒██░   ▓██░ ▓█   ▓██▒
░ ▒░▓  ░ ▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
░ ░ ▒  ░ ░▒░ ░ ░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░ ░    ░░░ ░ ░ ░      ░    ▒ ░   ░   ░ ░   ░   ▒   
    ░  ░   ░            ░    ░           ░       ░  ░
"""

def print_banner(subtitle: str = "Premium AI Frontend Engine for AGY & Claude Code"):
    logo_text = Text(LOGO, style="bold cyan")
    title_text = Text("⚡ LUMINA CLI // WORLD-CLASS FRONTEND TOOLKIT", style="bold white on dark_blue")
    sub_text = Text(f"\n{subtitle}\nLinear · Apple · Vercel · Stripe · Raycast Standards\n", style="dim italic")
    
    combined = Text()
    combined.append(logo_text)
    combined.append("\n")
    combined.append(title_text)
    combined.append(sub_text)
    
    panel = Panel(
        Align.center(combined),
        border_style="bright_blue",
        padding=(0, 2),
        subtitle="[bold green]v1.0.0[/bold green] · [dim]Designed for AGY & Claude Code[/dim]",
        subtitle_align="right"
    )
    console.print(panel)
