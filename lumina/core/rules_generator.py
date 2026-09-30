"""
Lumina Rules Generator - Injects Elite Design Directives for AGY & Claude Code
Equips LLMs with the Lumina Generative Design Constitution and Luxury Archetypes.
"""
import os
import shutil
from pathlib import Path

AGY_FRONTEND_RULE = """---
description: Elite Frontend Design Directive & Anti-AI-Slop Constitution for Antigravity & Claude Code
globs: ["**/*.tsx", "**/*.jsx", "**/*.html", "**/*.css", "**/*.vue", "**/*.svelte"]
always_on: true
---

# 💎 THE LUMINA FRONTEND CONSTITUTION: WORLD-CLASS DESIGN STANDARDS

You are acting as an Elite Principal Design Systems Engineer at a world-class studio (Linear, Apple, Stripe Press, Teenage Engineering, Raycast, Vercel).
The user is relying on you to produce bespoke, tactile, and uncompromisingly high-end user interfaces.
You have ZERO tolerance for generic "AI-slop", boilerplate templates, or amateur design patterns.

---

## 🚫 ARTICLE I: STRICT NEGATIVE CONSTRAINTS (ANTI-AI-SLOP DIRECTIVES)

You are strictly FORBIDDEN from using the following common "AI tells":

1. **NO GENERIC PURPLE/INDIGO GRADIENTS:**
   - ❌ NEVER write: `bg-gradient-to-r from-purple-500 to-indigo-600` on hero titles, CTAs, or background cards.
   - ✅ DO USE: Monochromatic depth, subtle mesh diffusion, or dark obsidian tones with a single razor-sharp accent (emerald, electric amber, cyan, safety orange, or crisp white).

2. **NO 3-IDENTICAL-CARD COOKIE-CUTTER SLOP:**
   - ❌ NEVER generate 3 equal-width cards side by side (`grid grid-cols-1 md:grid-cols-3`) with generic icons and 2 lines of lorem ipsum.
   - ✅ DO USE: **Asymmetrical Living Bento Grids** with varied spans:
     - 1 Dominant Visual Anchor (60% weight, living canvas, real-time telemetry or interactive preview).
     - 2-3 Context Satellites (micro sparklines, status pills, monospace telemetry).
     - 1 Tactile Micro-Control (segmented switch, haptic button, keyboard badge).

3. **NO FLAT, UNCHAMFERED CARDS:**
   - ❌ NEVER use flat `bg-zinc-900 border border-zinc-800` without depth.
   - ✅ ALWAYS apply the **1px Chamfer Highlight**:
     `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`
     This simulates Apple/Linear metallic edge reflection.

4. **NO RAW, UNTRACKED FONTS:**
   - ❌ NEVER use plain `font-sans` without tracking hierarchy.
   - ✅ Headings: `font-semibold tracking-tight` (or `tracking-tighter` on massive display sizes).
   - ✅ Micro-labels, badges, metadata: `font-mono text-[11px] tracking-wider uppercase opacity-75`.

5. **NO DEAD, UNREACTIVE BUTTONS:**
   - ❌ NEVER use static buttons with only `hover:bg-blue-600`.
   - ✅ ALWAYS add spring active feedback: `active:scale-[0.98] transition-transform duration-100 ease-out`.

6. **NO EMPTY OR DEAD STATES:**
   - ❌ NEVER leave tables or lists with a boring "No items found" text.
   - ✅ Provide tactile empty states with illustrated drop zones, keyboard shortcut hints (<kbd>⌘N</kbd>), or direct creation triggers.

---

## 🎨 ARTICLE II: THE 9 LUXURY AESTHETIC ARCHETYPES

When styling a project, select the archetype best matching the domain:

1. **Obsidian Linear (`linear-dark`):** Deep obsidian (`#09090b`), 1px inner chamfers, emerald accents, keyboard shortcuts (<kbd>⌘K</kbd>).
2. **Cupertino Glass (`apple-clean`):** Multi-tier backdrop blurs (`backdrop-blur-2xl`), squircle radii (`rounded-2xl`), airy negative space.
3. **Vercel Monolith (`vercel-mono`):** Razor-thin 1px hairline borders, strict monochrome discipline, Geist Sans/Mono pairing.
4. **Stripe Horizon (`stripe-saas`):** Fintech elegance, warm indigo mesh auroras, dimensional soft isometric shadows.
5. **Cyber Tactile (`cyber-tactile`):** Raycast-inspired amber phosphor (`#f59e0b`), dot-matrix grids, command-first navigation.
6. **Teenage Industrial (`teenage-industrial`):** Matte aluminum (`#18181b`), dot-matrix telemetry, Safety Orange (`#ff4400`) accents, zero-latency mechanical snap.
7. **Stripe Editorial (`stripe-editorial`):** Warm unbleached paper (`#fbf9f5`), editorial serif headlines (`Newsreader`), 0.5px hairline rules.
8. **Cupertino Spatial Glass (`spatial-glass`):** visionOS liquid refraction, specular top rim reflection (`border-t-white/40`), viscous spring physics.
9. **Refined Neo-Brutalism (`refined-brutalism`):** 2px stark ink borders, 3px zero-blur hard offset shadows (`shadow-[3px_3px_0_0_#000]`), electric lime/acid accents.

---

## 🛠️ ARTICLE III: LEVERAGING THE LUMINA MCP SERVER

If the Lumina MCP server is connected, use its intelligent tools to preserve originality:
- Call `synthesize_design_tokens` to receive parametric OKLCH tokens and spring physics tailored to the requested density and materiality.
- Call `get_composition_grammar` to understand spatial hierarchy, wireframes, and layout balance before writing custom code.
- Call `get_visual_primitive` to retrieve pure math & CSS primitives (`border-beam`, `spotlight-cone`, `3d-tilt`, `text-scramble`, `web-audio-haptic`).
- Call `critique_ui_design` to audit your draft code against Design Director standards.
"""

CLAUDE_MD_CONTENT = """# Project Guidelines for Claude Code & AI Assistants

## Design System: Lumina Premium Standard
This project follows the **Lumina Premium Design System** (Linear, Apple, Stripe, Teenage Engineering tier).
When writing UI components (React, Next.js, HTML, CSS):

1. **Avoid AI Slop:**
   - No generic purple-indigo gradients.
   - No 3 identical feature cards. Use asymmetrical Bento Grids.
   - No flat unchamfered cards. Use `border-white/[0.08]` and `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`.
   - No un-tracked typography. Use `tracking-tight` on headings and `font-mono text-xs uppercase tracking-wider` on badges.
   - No static buttons. Add `active:scale-[0.98]`.

2. **Tech Stack & Conventions:**
   - Styling: Tailwind CSS with CSS Variables (`globals.css`).
   - Icons: Lucide React (`lucide-react`).
   - Motion: Framer Motion (`framer-motion`) with spring physics.
   - Primitives: Radix UI / headless primitives.

3. **Archetypes Available in Lumina:**
   - `linear-dark`, `apple-clean`, `vercel-mono`, `stripe-saas`, `cyber-tactile`,
     `teenage-industrial`, `stripe-editorial`, `spatial-glass`, `refined-brutalism`.

4. **Component Structure:**
   - Place reusable UI primitives in `components/ui/`.
   - Place composite blocks (Bento, Hero, Navigation) in `components/blocks/`.
"""

def detect_installed_ai(target_dir: Path) -> dict:
    """Detects whether Antigravity (AGY) and/or Claude Code are present on the system/workspace."""
    has_claude_cli = bool(shutil.which("claude") or (Path.home() / ".claude").exists())
    has_agy_cli = bool(shutil.which("agy") or (Path.home() / ".gemini").exists())

    # 1. If one is installed on the machine and the other is not, respect the machine environment
    if has_agy_cli and not has_claude_cli:
        return {"agy": True, "claude": False}
    if has_claude_cli and not has_agy_cli:
        return {"agy": False, "claude": True}

    # 2. Check project directory clues if CLI tools aren't exclusively found
    has_claude_proj = bool((target_dir / ".claude").exists() or (target_dir / "CLAUDE.md").exists())
    has_agy_proj = bool((target_dir / ".agents").exists() or (target_dir / "GEMINI.md").exists())

    if has_agy_proj and not has_claude_proj:
        return {"agy": True, "claude": False}
    if has_claude_proj and not has_agy_proj:
        return {"agy": False, "claude": True}

    return {"agy": has_agy_cli or has_agy_proj, "claude": has_claude_cli or has_claude_proj}

def inject_rules(target_dir: str = ".", ai_target: str = "auto") -> dict:
    """Injects AGY and/or Claude Code rule files depending on detected or specified AI tool."""
    base = Path(target_dir).resolve()
    created_files = []
    skipped_files = []

    ai_info = detect_installed_ai(base)
    
    install_agy = False
    install_claude = False

    if ai_target == "agy":
        install_agy = True
    elif ai_target == "claude":
        install_claude = True
    elif ai_target in ("both", "all"):
        install_agy = True
        install_claude = True
    else:  # auto
        if ai_info["agy"] and not ai_info["claude"]:
            install_agy = True
        elif ai_info["claude"] and not ai_info["agy"]:
            install_claude = True
        else:
            # If both or neither detected, install for both to ensure compatibility
            install_agy = True
            install_claude = True

    # 1. AGY Rules
    if install_agy:
        agents_rules_dir = base / ".agents" / "rules"
        agents_rules_dir.mkdir(parents=True, exist_ok=True)
        agy_rule_path = agents_rules_dir / "frontend-premium.md"
        with open(agy_rule_path, "w", encoding="utf-8") as f:
            f.write(AGY_FRONTEND_RULE)
        created_files.append(str(agy_rule_path.relative_to(base)))

        gemini_path = base / "GEMINI.md"
        gemini_content = f"# Antigravity Project Context\n\nSee detailed frontend guidelines in `.agents/rules/frontend-premium.md`.\n\n"
        with open(gemini_path, "w", encoding="utf-8") as f:
            f.write(gemini_content + CLAUDE_MD_CONTENT)
        created_files.append("GEMINI.md")
    else:
        skipped_files.append("Claude Code detected only -> Antigravity rules skipped")

    # 2. Claude Code Rules (only if Claude is installed or requested)
    if install_claude:
        claude_path = base / "CLAUDE.md"
        with open(claude_path, "w", encoding="utf-8") as f:
            f.write(CLAUDE_MD_CONTENT)
        created_files.append("CLAUDE.md")

        claude_skills_dir = base / ".claude" / "skills" / "frontend-design"
        claude_skills_dir.mkdir(parents=True, exist_ok=True)
        claude_skill_path = claude_skills_dir / "SKILL.md"
        with open(claude_skill_path, "w", encoding="utf-8") as f:
            f.write(AGY_FRONTEND_RULE)
        created_files.append(str(claude_skill_path.relative_to(base)))
    else:
        skipped_files.append("Antigravity detected only -> Claude Code files (CLAUDE.md, .claude/) skipped")

    return {
        "status": "success",
        "created_files": created_files,
        "skipped_files": skipped_files,
        "installed_agy": install_agy,
        "installed_claude": install_claude
    }

