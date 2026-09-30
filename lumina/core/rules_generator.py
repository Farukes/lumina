"""
Lumina Rules Generator - Injects Elite Design Directives for AGY & Claude Code
"""
import os
from pathlib import Path

AGY_FRONTEND_RULE = """---
description: Elite Frontend Design Directive & Anti-AI-Slop Constitution for Antigravity & Claude Code
globs: ["**/*.tsx", "**/*.jsx", "**/*.html", "**/*.css", "**/*.vue", "**/*.svelte"]
always_on: true
---

# 💎 THE LUMINA FRONTEND CONSTITUTION: WORLD-CLASS DESIGN STANDARDS

You are acting as an Elite Principal Design Engineer at a world-class studio (tier: Linear, Apple, Stripe, Raycast, Vercel).
The user is relying on you to produce bespoke, tactile, and uncompromisingly high-end user interfaces.
You have ZERO tolerance for generic "AI-slop", boilerplate templates, or amateur design patterns.

---

## 🚫 ARTICLE I: STRICT NEGATIVE CONSTRAINTS (ANTI-AI-SLOP DIRECTIVES)

You are strictly FORBIDDEN from using the following common "AI tells":

1. **NO GENERIC PURPLE/INDIGO GRADIENTS:**
   - ❌ NEVER write: `bg-gradient-to-r from-purple-500 to-indigo-600` on hero titles, CTAs, or background cards.
   - ✅ DO USE: Monochromatic depth, subtle mesh diffusion, or dark obsidian tones with a single razor-sharp accent (e.g., emerald, electric amber, cyan, or crisp white).

2. **NO 3-IDENTICAL-CARD SYMMETRY:**
   - ❌ NEVER generate 3 equal-width cards side by side (`grid grid-cols-1 md:grid-cols-3`) with generic icons and 2 lines of lorem ipsum.
   - ✅ DO USE: **Asymmetrical Bento Grids** with varied spans (`col-span-2`, `row-span-2`), featuring live interactive widgets, mini sparklines, toggles, or code windows.

3. **NO FLAT, UNCHAMFERED DARK CARDS:**
   - ❌ NEVER use flat `bg-zinc-900 border border-zinc-800` without depth.
   - ✅ ALWAYS apply the **1px Chamfer Highlight**:
     `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`
     This simulates Apple/Linear metallic edge reflection.

4. **NO RAW, UNTRACKED FONTS:**
   - ❌ NEVER use plain `font-sans` without tracking hierarchy.
   - ✅ Headings: `font-semibold tracking-tight`.
   - ✅ Micro-labels, badges, metadata: `font-mono text-[11px] tracking-wider uppercase opacity-70`.

5. **NO DEAD, UNREACTIVE BUTTONS:**
   - ❌ NEVER use static buttons with only `hover:bg-blue-600`.
   - ✅ ALWAYS add spring active feedback: `active:scale-[0.98] transition-transform duration-100 ease-out`.

6. **NO EMPTY OR DEAD STATES:**
   - ❌ NEVER leave tables or lists with a boring "No items found" text.
   - ✅ Provide tactile empty states with illustrated drop zones, keyboard shortcut hints, or direct creation triggers.

---

## 🏆 ARTICLE II: THE LUXURY DESIGN BLUEPRINT

Whenever generating or refining frontend components:

1. **Information Architecture & Density:**
   - Give content room to breathe without wasting screen space.
   - Group related controls into unified floating bars or segmented controls.
   - Use subtle divider lines: `border-white/[0.06]` or `divide-white/[0.04]`.

2. **Micro-Interactions & Motion:**
   - When using Framer Motion, use spring curves rather than linear easings:
     `transition={{ type: "spring", stiffness: 350, damping: 25 }}`
   - Use `layoutId` for smooth tab switches and active pill indicators.

3. **Keyboard Accessibility & Shortcuts:**
   - Always display micro-badges for keyboard shortcuts: `<kbd className="px-1.5 py-0.5 text-[10px] font-mono bg-white/10 border border-white/10 rounded">⌘K</kbd>`.
   - Provide Cmd+K Command Palette patterns for primary operations.

4. **Color Tokens & Semantic Consistency:**
   - Always utilize CSS variable tokens (`var(--background)`, `var(--card)`, `var(--border)`, `var(--primary)`) rather than hardcoded hex codes.
   - Support dark mode natively with rich zinc/neutral undertones.
"""

CLAUDE_MD_CONTENT = """# Project Guidelines for Claude Code & AI Assistants

## Design System: Lumina Premium Standard
This project follows the **Lumina Premium Design System** (Linear, Apple, Vercel tier).
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

3. **Component Structure:**
   - Place reusable UI primitives in `components/ui/`.
   - Place composite blocks (Bento, Hero, Navigation) in `components/blocks/`.
"""

def inject_rules(target_dir: str = ".") -> dict:
    """Injects AGY and Claude Code rule files into the target project directory."""
    base = Path(target_dir).resolve()
    created_files = []

    # 1. AGY Rule: .agents/rules/frontend-premium.md
    agents_rules_dir = base / ".agents" / "rules"
    agents_rules_dir.mkdir(parents=True, exist_ok=True)
    agy_rule_path = agents_rules_dir / "frontend-premium.md"
    with open(agy_rule_path, "w", encoding="utf-8") as f:
        f.write(AGY_FRONTEND_RULE)
    created_files.append(str(agy_rule_path.relative_to(base)))

    # 2. Project GEMINI.md (Root rule for Antigravity)
    gemini_path = base / "GEMINI.md"
    gemini_content = f"# Antigravity Project Context\n\nSee detailed frontend guidelines in `.agents/rules/frontend-premium.md`.\n\n"
    if not gemini_path.exists():
        with open(gemini_path, "w", encoding="utf-8") as f:
            f.write(gemini_content + CLAUDE_MD_CONTENT)
        created_files.append("GEMINI.md")

    # 3. Claude Code: CLAUDE.md
    claude_path = base / "CLAUDE.md"
    if not claude_path.exists():
        with open(claude_path, "w", encoding="utf-8") as f:
            f.write(CLAUDE_MD_CONTENT)
        created_files.append("CLAUDE.md")

    # 4. Claude Code Skill: .claude/skills/frontend-design/SKILL.md
    claude_skills_dir = base / ".claude" / "skills" / "frontend-design"
    claude_skills_dir.mkdir(parents=True, exist_ok=True)
    claude_skill_path = claude_skills_dir / "SKILL.md"
    with open(claude_skill_path, "w", encoding="utf-8") as f:
        f.write(AGY_FRONTEND_RULE)
    created_files.append(str(claude_skill_path.relative_to(base)))

    return {
        "status": "success",
        "created_files": created_files
    }
