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
    )
}
