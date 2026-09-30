"""
Lumina Prompt Engine - Generates Zero-Slop Architectural Prompts for AGY & Claude Code
"""
from typing import Dict

PROMPT_TEMPLATES: Dict[str, Dict[str, str]] = {
    "dashboard": {
        "title": "Executive Telemetry & SaaS Dashboard",
        "description": "Linear-tier metrics dashboard with live telemetry, sparklines, chamfers, and command palette.",
        "prompt": """Act as an Elite Principal Design Engineer at a tier-1 studio (Linear / Apple).
Build a high-density, luxury SaaS analytics dashboard using React, Tailwind CSS, Lucide icons, and Framer Motion.

Aesthetic & Architectural Requirements:
1. Palette & Depth: Obsidian dark mode (bg #09090b). Use 1px metallic chamfers on every card:
   `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`
2. Layout: Asymmetric Bento Grid.
   - Hero telemetry card (spans 2 cols, 2 rows) with live counter and animated pulse dot.
   - Mini sparkline card with SVG trendline.
   - Hardware status / region latency widget.
   - Interactive toggle card with spring switch.
3. Typography:
   - Headings: `font-semibold tracking-tight text-white`
   - Data numbers: Large font-sans tabular numbers.
   - Metadata / Status: `font-mono text-xs uppercase tracking-wider text-neutral-400`
4. Tactile Polish:
   - Buttons: `active:scale-[0.98] transition-transform`
   - Keyboard shortcuts: Include `<kbd>⌘K</kbd>` for quick search.
5. Strict Negative Constraints:
   - ZERO purple/indigo gradients.
   - ZERO 3-identical-card symmetry.
   - NO low-contrast gray text.
   - NO dead states without recovery actions.
"""
    },

    "landing-page": {
        "title": "High-Conversion Ambient Glow Landing Page",
        "description": "Showcase landing page with diffused radial glow, dynamic island navbar, bento features, and social proof.",
        "prompt": """Act as an Elite Design Lead creating a world-class landing page for a cutting-edge developer tool.
Tech Stack: React, Tailwind CSS, Lucide icons, Framer Motion.

Aesthetic & Architectural Requirements:
1. Hero Section:
   - Ambient diffused mesh glow in background (`blur-[140px]`).
   - Pill badge at top: `inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/[0.04] border border-white/[0.08] text-xs font-mono`.
   - Punchy headline with subtle gradient text mask (`bg-gradient-to-b from-white via-white to-neutral-400 bg-clip-text text-transparent`).
   - Magnetic primary CTA button with rotating border beam.
   - Secondary button with 1px chamfer inset shadow.
2. Feature Section:
   - Bento grid with asymmetric cards showcasing actual product capability (not generic icon + 2 lines of text).
3. Floating Navigation:
   - Dynamic Island style floating navbar centered at top with backdrop blur (`backdrop-blur-xl bg-black/60`).
4. Strict Negative Constraints:
   - NO generic stock illustrations.
   - NO centered 3-card feature section.
   - NO unadjusted fonts. All headings must have `tracking-tight`.
"""
    },

    "settings": {
        "title": "Tactile Preferences & API Settings Panel",
        "description": "Deep-slate settings screen with tab transitions, API key reveals, danger zones, and haptic feedback.",
        "prompt": """Act as a Senior UI/UX Engineer at Apple/Linear.
Build a comprehensive Settings & Preferences panel with high tactile responsiveness.

Aesthetic & Architectural Requirements:
1. Navigation: Vertical tab bar on the left with sliding pill layout transition (`layoutId="activeSettingsTab"`).
2. Sections:
   - Profile & Organization: Avatar upload zone with dashed chamfer border and hover glow.
   - API Keys & Telemetry: Secret key field with one-click copy, masked bullets, and `<kbd>` shortcuts.
   - Webhooks: Interactive URL input with status badge.
   - Danger Zone: Destructive panel with subtle red border tint (`border-red-500/20 bg-red-500/[0.02]`).
3. Interactivity:
   - Smooth toggle switches with Framer Motion spring physics.
   - Save button with animated loading spinner/check mark state transition.
4. Strict Negative Constraints:
   - NO generic Bootstrap-style forms.
   - NO unstyled input borders. Inputs must have `bg-white/[0.03] border-white/[0.08] focus:border-white/20`.
"""
    },

    "pricing": {
        "title": "Fintech Tier Comparison & Feature Matrix",
        "description": "Stripe/Linear style pricing cards with billing interval toggle, popular badge glow, and feature breakdown.",
        "prompt": """Act as an Elite Design Engineer. Build a high-converting, premium Pricing page.

Aesthetic & Architectural Requirements:
1. Billing Switcher: Monthly / Annual segmented control with spring sliding pill and "Save 20%" micro-badge.
2. Tier Cards (Free, Pro, Enterprise):
   - Pro card highlighted with subtle ambient border glow and `border-emerald-500/40`.
   - Price display with large tabular numerals and `/month` micro-label.
   - Feature checkmarks with custom emerald icons and micro-tooltips.
   - Primary CTA on Pro tier with magnetic spring feedback (`active:scale-[0.98]`).
3. Strict Negative Constraints:
   - NO generic bright gradient backgrounds.
   - NO oversized cheesy icons.
   - NO crowded tables without padding hierarchy.
"""
    }
}

def generate_prompt(feature_name: str, custom_context: str = "") -> str:
    """Generates an elite prompt based on feature type and optional custom context."""
    feature_key = feature_name.lower().strip()
    
    if feature_key in PROMPT_TEMPLATES:
        base_prompt = PROMPT_TEMPLATES[feature_key]["prompt"]
    else:
        base_prompt = f"""Act as an Elite Principal Design Engineer at a tier-1 studio (Linear / Apple).
Build a world-class, bespoke implementation of: **{feature_name}**.

Aesthetic & Architectural Requirements:
1. Styling & Palette: Use Obsidian dark mode or Cupertino clean with semantic CSS variables and OKLCH color space.
2. Depth: Apply 1px Chamfer Highlights on all cards:
   `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`
3. Motion: Spring physics for interactive elements (Framer Motion: `stiffness: 400, damping: 25`).
4. Typography: Heading with `tracking-tight`, badges with `font-mono text-xs uppercase tracking-wider`.
5. Tactile Polish: Buttons must feature `active:scale-[0.98]`.
6. Negative Constraints: ZERO purple gradients, ZERO 3-card symmetry, ZERO untracked fonts.
"""

    if custom_context:
        base_prompt += f"\nSpecific Project Context:\n{custom_context}\n"

    return base_prompt
