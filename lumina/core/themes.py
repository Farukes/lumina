"""
Lumina Theme Registry - 5 World-Class Aesthetic Presets
"""
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ThemeDefinition:
    id: str
    name: str
    description: str
    archetype: str
    font_sans: str
    font_mono: str
    css_variables: str
    tailwind_extensions: Dict[str, any]
    traits: List[str]

THEMES: Dict[str, ThemeDefinition] = {
    "linear-dark": ThemeDefinition(
        id="linear-dark",
        name="Obsidian Linear",
        description="Dark luxury aesthetic inspired by Linear & Raycast with metallic chamfers and tactile depth.",
        archetype="Developer Tools & High-End B2B SaaS",
        font_sans="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        font_mono="'JetBrains Mono', 'Fira Code', monospace",
        traits=[
            "1px inner chamfer highlight (inset 0 1px 0 0 rgba(255,255,255,0.08))",
            "Deep obsidian background (#09090b)",
            "Subtle emerald & electric cyan accents",
            "Keyboard shortcut micro-badges (<kbd>⌘K</kbd>)",
            "High data density with crisp contrast"
        ],
        css_variables="""
:root {
  --background: #09090b;
  --foreground: #f4f4f5;
  --card: #121215;
  --card-foreground: #f4f4f5;
  --popover: #121215;
  --popover-foreground: #f4f4f5;
  --primary: #10b981;
  --primary-foreground: #042f2e;
  --secondary: #27272a;
  --secondary-foreground: #fafafa;
  --muted: #18181b;
  --muted-foreground: #a1a1aa;
  --accent: #27272a;
  --accent-foreground: #fafafa;
  --destructive: #ef4444;
  --destructive-foreground: #f8fafc;
  --border: rgba(255, 255, 255, 0.08);
  --input: rgba(255, 255, 255, 0.12);
  --ring: #10b981;
  --radius: 0.5rem;
  --chamfer-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
}
""",
        tailwind_extensions={
            "boxShadow": {
                "chamfer": "inset 0 1px 0 0 rgba(255, 255, 255, 0.08)",
                "glow": "0 0 25px -5px rgba(16, 185, 129, 0.25)",
                "card-subtle": "0 4px 20px -2px rgba(0, 0, 0, 0.5)"
            }
        }
    ),

    "apple-clean": ThemeDefinition(
        id="apple-clean",
        name="Cupertino Glass",
        description="Apple precision with multi-layer backdrop blurs, squircle radii, and generous negative space.",
        archetype="Consumer Tech, Mobile-First SaaS, Lifestyle",
        font_sans="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Plus Jakarta Sans', sans-serif",
        font_mono="'SF Mono', monospace",
        traits=[
            "Ultra-high backdrop blur (backdrop-blur-2xl with saturated glass)",
            "Generous white space & airy breathing room",
            "Multi-tiered soft atmospheric shadows",
            "Squircle curvature (rounded-2xl / rounded-3xl)",
            "Silky spring motion transitions"
        ],
        css_variables="""
:root {
  --background: #fbfbfd;
  --foreground: #1d1d1f;
  --card: rgba(255, 255, 255, 0.85);
  --card-foreground: #1d1d1f;
  --popover: rgba(255, 255, 255, 0.95);
  --popover-foreground: #1d1d1f;
  --primary: #0071e3;
  --primary-foreground: #ffffff;
  --secondary: #f5f5f7;
  --secondary-foreground: #1d1d1f;
  --muted: #f5f5f7;
  --muted-foreground: #86868b;
  --accent: #e8e8ed;
  --accent-foreground: #1d1d1f;
  --destructive: #ff3b30;
  --destructive-foreground: #ffffff;
  --border: rgba(0, 0, 0, 0.06);
  --input: rgba(0, 0, 0, 0.08);
  --ring: #0071e3;
  --radius: 1rem;
  --chamfer-highlight: inset 0 1px 1px 0 rgba(255, 255, 255, 0.8);
}
.dark {
  --background: #000000;
  --foreground: #f5f5f7;
  --card: rgba(28, 28, 30, 0.85);
  --card-foreground: #f5f5f7;
  --popover: rgba(28, 28, 30, 0.95);
  --popover-foreground: #f5f5f7;
  --primary: #2997ff;
  --primary-foreground: #000000;
  --secondary: #1c1c1e;
  --secondary-foreground: #f5f5f7;
  --muted: #1c1c1e;
  --muted-foreground: #86868b;
  --accent: #2c2c2e;
  --accent-foreground: #f5f5f7;
  --border: rgba(255, 255, 255, 0.1);
  --ring: #2997ff;
}
""",
        tailwind_extensions={
            "boxShadow": {
                "apple-card": "0 2px 8px rgba(0, 0, 0, 0.04), 0 12px 24px rgba(0, 0, 0, 0.06)",
                "apple-popover": "0 8px 32px rgba(0, 0, 0, 0.12)"
            }
        }
    ),

    "vercel-mono": ThemeDefinition(
        id="vercel-mono",
        name="Vercel Monolith",
        description="High-contrast brutalist minimalism with razor-thin hairline borders and Geist typography.",
        archetype="Cloud Platforms, Developer Tooling, Infra",
        font_sans="'Geist', -apple-system, BlinkMacSystemFont, sans-serif",
        font_mono="'Geist Mono', monospace",
        traits=[
            "Strict monochrome discipline (Zero gratuitous gradients)",
            "0.5px - 1px razor-sharp grid lines",
            "Geist Sans and Geist Mono pairing",
            "Micro-labeling with uppercase tracking-widest",
            "Ultra high data density and contrast"
        ],
        css_variables="""
:root {
  --background: #000000;
  --foreground: #ededed;
  --card: #0a0a0a;
  --card-foreground: #ededed;
  --popover: #0a0a0a;
  --popover-foreground: #ededed;
  --primary: #ffffff;
  --primary-foreground: #000000;
  --secondary: #171717;
  --secondary-foreground: #ededed;
  --muted: #171717;
  --muted-foreground: #a1a1a1;
  --accent: #262626;
  --accent-foreground: #ededed;
  --destructive: #f43f5e;
  --destructive-foreground: #ffffff;
  --border: #262626;
  --input: #262626;
  --ring: #ffffff;
  --radius: 0.375rem;
  --chamfer-highlight: none;
}
""",
        tailwind_extensions={
            "boxShadow": {
                "vercel-glow": "0 0 0 1px #333333, 0 8px 24px -4px rgba(0,0,0,0.8)"
            }
        }
    ),

    "stripe-saas": ThemeDefinition(
        id="stripe-saas",
        name="Stripe Horizon",
        description="Sophisticated fintech elegance with subtle mesh auroras, deep indigo accents and smooth charts.",
        archetype="Fintech, Payment Platforms, Global SaaS",
        font_sans="'Plus Jakarta Sans', -apple-system, sans-serif",
        font_mono="'JetBrains Mono', monospace",
        traits=[
            "Multilayered soft ambient aura backgrounds",
            "Fintech-grade badge & stat card styling",
            "Deep slate backgrounds with warm violet micro-tinting",
            "Isometric soft shadows with dimensional lift",
            "Smooth sparklines and real-time metric indicators"
        ],
        css_variables="""
:root {
  --background: #0b0f19;
  --foreground: #f1f5f9;
  --card: #111827;
  --card-foreground: #f1f5f9;
  --popover: #111827;
  --popover-foreground: #f1f5f9;
  --primary: #6366f1;
  --primary-foreground: #ffffff;
  --secondary: #1e293b;
  --secondary-foreground: #f1f5f9;
  --muted: #1e293b;
  --muted-foreground: #94a3b8;
  --accent: #334155;
  --accent-foreground: #f1f5f9;
  --destructive: #ef4444;
  --destructive-foreground: #ffffff;
  --border: rgba(99, 102, 241, 0.15);
  --input: rgba(99, 102, 241, 0.2);
  --ring: #6366f1;
  --radius: 0.75rem;
  --chamfer-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}
""",
        tailwind_extensions={
            "boxShadow": {
                "stripe-lift": "0 20px 40px -15px rgba(0, 0, 0, 0.5), 0 0 30px -10px rgba(99, 102, 241, 0.25)"
            }
        }
    ),

    "cyber-tactile": ThemeDefinition(
        id="cyber-tactile",
        name="Cyber Tactile",
        description="Raycast-inspired haptic terminal aesthetic with amber phosphor, dot-matrix grids, and keyboard focus.",
        archetype="CLI Companions, AI Agent Interfaces, Hacker Tools",
        font_sans="'Space Grotesk', -apple-system, sans-serif",
        font_mono="'JetBrains Mono', 'Courier New', monospace",
        traits=[
            "Web Audio micro-click feedback built-in",
            "Dot-matrix and scanline ambient textures",
            "Amber phosphor (#f59e0b) and cyber emerald (#10b981)",
            "Keyboard-first navigation with action keys",
            "Terminal command bar center stage"
        ],
        css_variables="""
:root {
  --background: #0d0e12;
  --foreground: #f3f4f6;
  --card: #15171e;
  --card-foreground: #f3f4f6;
  --popover: #15171e;
  --popover-foreground: #f3f4f6;
  --primary: #f59e0b;
  --primary-foreground: #000000;
  --secondary: #1f222e;
  --secondary-foreground: #f3f4f6;
  --muted: #1f222e;
  --muted-foreground: #9ca3af;
  --accent: #2e3346;
  --accent-foreground: #f3f4f6;
  --destructive: #f87171;
  --destructive-foreground: #000000;
  --border: rgba(245, 158, 11, 0.2);
  --input: rgba(245, 158, 11, 0.25);
  --ring: #f59e0b;
  --radius: 0.25rem;
  --chamfer-highlight: inset 0 1px 0 0 rgba(245, 158, 11, 0.15);
}
""",
        tailwind_extensions={
            "boxShadow": {
                "cyber-glow": "0 0 15px rgba(245, 158, 11, 0.25)",
                "terminal-card": "inset 0 0 0 1px rgba(245, 158, 11, 0.2), 0 8px 30px rgba(0, 0, 0, 0.7)"
            }
        }
    ),

    "teenage-industrial": ThemeDefinition(
        id="teenage-industrial",
        name="Teenage Industrial",
        description="Teenage Engineering hardware luxury with matte aluminum, dot-matrix telemetry, and punchy Safety Orange accents.",
        archetype="Hardware Synths, Creative Audio, Modern DevTools, Industrial Design",
        font_sans="'JetBrains Mono', 'Space Mono', monospace",
        font_mono="'JetBrains Mono', monospace",
        traits=[
            "Matte anodized aluminum (#18181b / #222226) with tactile physical controls",
            "Punchy Safety Orange (#ff4400) and Matte Citron (#e2f952) primary markers",
            "Dot-matrix background patterns and rotary dial micro-components",
            "Hardware-inspired uppercase micro-typography (font-mono text-[10px] tracking-widest)",
            "Zero-latency mechanical spring snap physics (stiffness 500, damping 40)"
        ],
        css_variables="""
:root {
  --background: #121214;
  --foreground: #e4e4e7;
  --card: #1c1c20;
  --card-foreground: #f4f4f5;
  --popover: #222227;
  --popover-foreground: #f4f4f5;
  --primary: #ff4400;
  --primary-foreground: #ffffff;
  --secondary: #27272e;
  --secondary-foreground: #e4e4e7;
  --muted: #1e1e24;
  --muted-foreground: #71717a;
  --accent: #ff4400;
  --accent-foreground: #ffffff;
  --destructive: #ef4444;
  --destructive-foreground: #ffffff;
  --border: rgba(255, 255, 255, 0.1);
  --input: rgba(255, 255, 255, 0.12);
  --ring: #ff4400;
  --radius: 0.125rem;
  --chamfer-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
}
""",
        tailwind_extensions={
            "boxShadow": {
                "industrial-bevel": "inset 0 1px 0 0 rgba(255, 255, 255, 0.15), 0 2px 0 0 rgba(0, 0, 0, 0.6)",
                "knob-inset": "inset 0 2px 4px 0 rgba(0, 0, 0, 0.8), inset 0 -1px 0 0 rgba(255, 255, 255, 0.1)"
            }
        }
    ),

    "stripe-editorial": ThemeDefinition(
        id="stripe-editorial",
        name="Stripe Editorial Luxury",
        description="High-end editorial literature aesthetic inspired by Stripe Press & Cosmos with warm parchment, serif typography, and hairline rules.",
        archetype="Editorial Publications, High-End Knowledge Bases, Luxury Goods, Thought Leadership",
        font_sans="'Newsreader', 'Editorial New', 'Playfair Display', Georgia, serif",
        font_mono="'JetBrains Mono', 'Courier Prime', monospace",
        traits=[
            "Warm unbleached paper background (#fbf9f5 / #f7f5f0)",
            "High-contrast editorial serif display headlines paired with crisp monospace metadata",
            "0.5px ultra-fine hairline dividers (#e4e0d7)",
            "Generous editorial whitespace and wide margin columns",
            "Hypnotic zen spring transitions (stiffness 180, damping 35)"
        ],
        css_variables="""
:root {
  --background: #fbf9f5;
  --foreground: #1c1917;
  --card: #ffffff;
  --card-foreground: #1c1917;
  --popover: #ffffff;
  --popover-foreground: #1c1917;
  --primary: #1c1917;
  --primary-foreground: #fbf9f5;
  --secondary: #f3efe6;
  --secondary-foreground: #1c1917;
  --muted: #f3efe6;
  --muted-foreground: #78716c;
  --accent: #292524;
  --accent-foreground: #fbf9f5;
  --destructive: #b91c1c;
  --destructive-foreground: #ffffff;
  --border: #e7e2d7;
  --input: #e7e2d7;
  --ring: #1c1917;
  --radius: 0.25rem;
  --chamfer-highlight: none;
}
.dark {
  --background: #11100f;
  --foreground: #ede8df;
  --card: #181715;
  --card-foreground: #ede8df;
  --popover: #181715;
  --popover-foreground: #ede8df;
  --primary: #ede8df;
  --primary-foreground: #11100f;
  --secondary: #22201d;
  --secondary-foreground: #ede8df;
  --muted: #22201d;
  --muted-foreground: #8c827a;
  --border: rgba(237, 232, 223, 0.12);
  --ring: #ede8df;
}
""",
        tailwind_extensions={
            "boxShadow": {
                "editorial-card": "0 1px 3px rgba(0, 0, 0, 0.04), 0 8px 24px rgba(0, 0, 0, 0.03)"
            }
        }
    ),

    "spatial-glass": ThemeDefinition(
        id="spatial-glass",
        name="Cupertino Spatial Glass",
        description="visionOS-inspired liquid glass morphism with specular perimeter light, depth blur, and viscous physics.",
        archetype="Spatial Computing, Premium Audio/Video SaaS, Luxury Portfolios",
        font_sans="-apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif",
        font_mono="'SF Mono', monospace",
        traits=[
            "Refractive multi-layer backdrop filter (backdrop-blur-3xl saturate-150)",
            "Specular top rim reflection highlight (border-t border-t-white/40)",
            "Volumetric lighting diffusion with responsive mouse tilt",
            "Deep dark space background (#050508) with luminous glowing floating orbs",
            "Viscous liquid spring physics (stiffness 260, damping 28)"
        ],
        css_variables="""
:root {
  --background: #050508;
  --foreground: #f8fafc;
  --card: rgba(255, 255, 255, 0.04);
  --card-foreground: #f8fafc;
  --popover: rgba(20, 20, 28, 0.7);
  --popover-foreground: #f8fafc;
  --primary: #38bdf8;
  --primary-foreground: #030712;
  --secondary: rgba(255, 255, 255, 0.08);
  --secondary-foreground: #f8fafc;
  --muted: rgba(255, 255, 255, 0.06);
  --muted-foreground: #94a3b8;
  --accent: rgba(56, 189, 248, 0.15);
  --accent-foreground: #38bdf8;
  --destructive: #f43f5e;
  --destructive-foreground: #ffffff;
  --border: rgba(255, 255, 255, 0.12);
  --input: rgba(255, 255, 255, 0.15);
  --ring: #38bdf8;
  --radius: 1.25rem;
  --chamfer-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.35);
}
""",
        tailwind_extensions={
            "boxShadow": {
                "specular-glass": "inset 0 1px 0 0 rgba(255, 255, 255, 0.4), inset 0 0 1px 0 rgba(255, 255, 255, 0.3), 0 20px 50px -10px rgba(0, 0, 0, 0.7)",
                "spatial-glow": "0 0 35px -5px rgba(56, 189, 248, 0.3)"
            }
        }
    ),

    "refined-brutalism": ThemeDefinition(
        id="refined-brutalism",
        name="Refined Neo-Brutalism",
        description="Contemporary high-contrast brutalism with 2px ink borders, zero-blur 3px hard offset shadows, and electric accents.",
        archetype="Creative Studios, Avant-Garde Web3, Indie Hackers, Bold Consumer SaaS",
        font_sans="'Plus Jakarta Sans', -apple-system, sans-serif",
        font_mono="'Space Mono', monospace",
        traits=[
            "Stark 2px solid ink borders (border-2 border-black dark:border-white)",
            "Crisp zero-blur 3px or 4px hard offset drop shadows (shadow-[3px_3px_0_0_#000])",
            "High contrast palette with Electric Lime (#d9f99d) or Neon Acid yellow accents",
            "Bold geometric buttons with instant mechanical depression on active (translate-x-[2px] translate-y-[2px])",
            "Unapologetic, confident visual weight"
        ],
        css_variables="""
:root {
  --background: #fafaf9;
  --foreground: #09090b;
  --card: #ffffff;
  --card-foreground: #09090b;
  --popover: #ffffff;
  --popover-foreground: #09090b;
  --primary: #09090b;
  --primary-foreground: #ffffff;
  --secondary: #e7e5e4;
  --secondary-foreground: #09090b;
  --muted: #f5f5f4;
  --muted-foreground: #57534e;
  --accent: #bef264;
  --accent-foreground: #09090b;
  --destructive: #ef4444;
  --destructive-foreground: #ffffff;
  --border: #09090b;
  --input: #09090b;
  --ring: #09090b;
  --radius: 0.375rem;
  --chamfer-highlight: none;
}
.dark {
  --background: #09090b;
  --foreground: #f4f4f5;
  --card: #18181b;
  --card-foreground: #f4f4f5;
  --popover: #18181b;
  --popover-foreground: #f4f4f5;
  --primary: #f4f4f5;
  --primary-foreground: #09090b;
  --secondary: #27272a;
  --secondary-foreground: #f4f4f5;
  --muted: #27272a;
  --muted-foreground: #a1a1aa;
  --accent: #bef264;
  --accent-foreground: #09090b;
  --border: #ffffff;
  --input: #ffffff;
  --ring: #bef264;
}
""",
        tailwind_extensions={
            "boxShadow": {
                "brutal-hard": "3px 3px 0 0 #000000",
                "brutal-hard-dark": "3px 3px 0 0 #ffffff",
                "brutal-pop": "5px 5px 0 0 #bef264"
            }
        }
    )
}

# Legal Trademark-Clean Original Aliases
THEME_ALIASES: Dict[str, str] = {
    "obsidian-craft": "linear-dark",
    "pure-cupertino": "apple-clean",
    "stark-monolith": "vercel-mono",
    "fintech-horizon": "stripe-saas",
    "amber-terminal": "cyber-tactile",
    "industrial-machina": "teenage-industrial",
    "parchment-editorial": "stripe-editorial",
    "liquid-spatial": "spatial-glass",
}

# Register aliases into THEMES
for alias_id, target_id in THEME_ALIASES.items():
    if target_id in THEMES:
        target_def = THEMES[target_id]
        THEMES[alias_id] = ThemeDefinition(
            id=alias_id,
            name=target_def.name,
            description=target_def.description,
            archetype=target_def.archetype,
            font_sans=target_def.font_sans,
            font_mono=target_def.font_mono,
            css_variables=target_def.css_variables,
            tailwind_extensions=target_def.tailwind_extensions,
            traits=target_def.traits
        )

def get_theme(theme_id: str) -> ThemeDefinition:
    """Safely retrieves theme definition supporting both original and legacy keys."""
    if theme_id in THEMES:
        return THEMES[theme_id]
    resolved = THEME_ALIASES.get(theme_id, "linear-dark")
    return THEMES.get(resolved, THEMES["linear-dark"])

SPRING_PHYSICS = {
    "snappy": {
        "description": "Linear/Raycast tactile snap with instantaneous feedback",
        "stiffness": 400,
        "damping": 30,
        "mass": 0.8
    },
    "mechanical-relay": {
        "description": "Teenage Engineering instant tactile hardware switch",
        "stiffness": 520,
        "damping": 42,
        "mass": 0.7
    },
    "viscous-spatial": {
        "description": "Apple visionOS liquid glass and fluid buoyancy",
        "stiffness": 260,
        "damping": 28,
        "mass": 1.0
    },
    "zen": {
        "description": "Stripe Editorial smooth expansive literary drift",
        "stiffness": 180,
        "damping": 35,
        "mass": 1.2
    }
}
