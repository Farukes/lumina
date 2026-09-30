"""
Lumina Composition Grammar
Structural Visual Rules & Layout Archetypes that empower AI creativity
without dictating monolithic, cookie-cutter JSX code.
"""

from typing import Dict, Any, List

GRAMMAR_PATTERNS: Dict[str, Dict[str, Any]] = {
    "bento-grid": {
        "pattern_name": "Asymmetrical Living Bento",
        "philosophy": (
            "Never build 3 or 4 identical static boxes. A world-class Bento Grid operates as an asymmetrical "
            "narrative canvas with one Dominant Visual Anchor, 2-3 Context Satellites, and 1 Tactile Micro-Control."
        ),
        "visual_hierarchy": {
            "dominant_anchor": {
                "span": "col-span-12 lg:col-span-8",
                "purpose": "The primary hero card (60% visual weight). Must contain a living interactive element: dynamic telemetry chart, interactive canvas, 3D simulation, or live code runner.",
                "traits": ["High contrast", "Living state or animated loop", "Spotlight cone or border-beam highlight"]
            },
            "context_satellites": {
                "span": "col-span-12 sm:col-span-6 lg:col-span-4",
                "purpose": "Provide peripheral telemetry, status pills, or dynamic micro-data.",
                "traits": ["Monospace data counters", "Micro sparklines", "Chamfer 1px highlight"]
            },
            "tactile_micro_control": {
                "span": "col-span-12 sm:col-span-6 lg:col-span-4",
                "purpose": "An interactive utility widget (haptic toggle slider, segmented pill bar, or command trigger).",
                "traits": ["Keyboard badge (<kbd>⌘K</kbd>)", "active:scale-[0.98] interaction", "Instant state change"]
            }
        },
        "ascii_wireframe": """
+-------------------------------------------------------------+
| [DOMINANT VISUAL ANCHOR: 60% Visual Weight]                 |
| (Real-time chart, live code runner, or living canvas)       |
| Span: col-span-12 lg:col-span-8                             |
+------------------------------+------------------------------+
| [SATELLITE 1: Telemetry]     | [SATELLITE 2: Micro-Controls]|
| Metric + Sparkline           | Segmented switch / Haptic    |
| Span: col-span-6 lg:col-4    | Span: col-span-6 lg:col-4    |
+------------------------------+------------------------------+
""",
        "creative_prompts_for_ai": [
            "Tailor the Dominant Anchor to the user's specific domain (e.g. if Crypto: live mempool stream; if AI: live token inference stream; if DevTools: AST tree visualizer).",
            "Vary the card aspect ratios and padding (p-6 vs p-8) to create dynamic tension.",
            "Use motion.div with container stagger (staggerChildren: 0.08) for entrance physics."
        ]
    },

    "hero-section": {
        "pattern_name": "Kinetic Atmospheric Hero",
        "philosophy": (
            "Avoid flat text and generic purple gradients. A luxury hero combines a luminous atmospheric aura, "
            "tightly-tracked display typography, a living product preview, and tactile dual CTAs."
        ),
        "visual_hierarchy": {
            "luminous_backdrop": {
                "purpose": "Atmospheric depth using layered SVG mesh gradients or radial blur orbs (blur-[120px]) with dark obsidian background.",
            },
            "announcement_badge": {
                "purpose": "Monospace pill badge with animated border-beam or pulsating status dot.",
                "classes": "inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.03] px-3 py-1 font-mono text-xs uppercase tracking-wider"
            },
            "display_headline": {
                "purpose": "High-contrast, negative-tracked headline with optional gradient text clip on key emphasis words.",
                "classes": "text-5xl sm:text-7xl font-bold tracking-tight text-white leading-[1.08]"
            },
            "dual_tactile_cta": {
                "purpose": "Primary solid button with 1px chamfer and active scale; Secondary transparent button with keyboard shortcut hint.",
                "classes": "Primary: bg-white text-black active:scale-[0.98] | Secondary: border border-white/10 active:scale-[0.98]"
            },
            "living_product_stage": {
                "purpose": "Floating isometric mockup or live interactive dashboard preview with 3D tilt and ambient glow shadow.",
                "classes": "rounded-2xl border border-white/[0.08] shadow-[0_20px_60px_-15px_rgba(0,0,0,0.8)]"
            }
        },
        "ascii_wireframe": """
                     [Announcement Pill: v2.4 Live •]
           THE DISPLAY HEADLINE WITH TIGHT TRACKING
                 Refined subtitle with muted editorial weight.
                  [Primary Action]  [<kbd>⌘K</kbd> Quick Tour]

    +--------------------------------------------------------------+
    |                                                              |
    |          [LIVING PRODUCT STAGE: 3D Perspective Tilt]         |
    |            Interactive UI Canvas with Specular Border        |
    |                                                              |
    +--------------------------------------------------------------+
""",
        "creative_prompts_for_ai": [
            "Incorporate mouse-following spotlight or ambient radial bloom behind the product preview.",
            "Craft the subtitle with font-normal text-lg sm:text-xl text-neutral-400 max-w-2xl mx-auto.",
            "Add subtle haptic sound trigger on primary CTA click."
        ]
    },

    "command-palette": {
        "pattern_name": "Raycast-Grade Command Palette",
        "philosophy": (
            "The heart of high-efficiency developer interfaces. Instant 0ms modal appearance, keyboard shortcut "
            "discipline, grouped action sections, and live search filtration."
        ),
        "visual_hierarchy": {
            "backdrop_shield": "fixed inset-0 bg-black/60 backdrop-blur-md z-50",
            "modal_container": "max-w-2xl w-full mx-auto rounded-xl border border-white/10 bg-zinc-950/90 shadow-2xl overflow-hidden",
            "search_input": "h-14 w-full bg-transparent px-4 font-mono text-sm text-white placeholder-zinc-500 focus:outline-none",
            "item_row": "flex items-center justify-between px-4 py-2.5 rounded-lg text-sm transition-colors data-[selected=true]:bg-white/10",
            "shortcut_indicator": "flex items-center gap-1 font-mono text-xs text-zinc-500 <kbd>⌥⏎</kbd>"
        },
        "ascii_wireframe": """
+---------------------------------------------------------------+
| 🔍 Search commands, files, or actions...             [ESC]   |
+---------------------------------------------------------------+
| RECENT                                                        |
|   ⚡ Quick Deploy Production                           ⌘⏎     |
|   🔄 Sync Environment Variables                       ⌥S     |
| SUGGESTIONS                                                   |
|   🎨 Switch Theme Archetype                           ⌘T     |
|   📊 Open Telemetry Inspector                         ⌘I     |
+---------------------------------------------------------------+
| Navigation: ↑↓    Select: ↵    Action: ⇥                     |
+---------------------------------------------------------------+
""",
        "creative_prompts_for_ai": [
            "Group items by semantic domain (Navigation, Actions, Settings, Developer).",
            "Use Lucide icons matching each action with subtle 1px stroke weight.",
            "Trigger haptic click on item selection."
        ]
    },

    "dashboard-telemetry": {
        "pattern_name": "Mission-Control Telemetry HUD",
        "philosophy": (
            "High-density data architecture inspired by Bloomberg Terminals, SpaceX Dragon telemetry, and Vercel analytics. "
            "Prioritizes legibility, monospace alignment, and live pulse status."
        ),
        "visual_hierarchy": {
            "telemetry_header": "Global status banner with live pulse ping dot and latency counter (e.g. 12ms • Operational).",
            "stat_strip": "Horizontal grid of 4 key performance indicators with delta percentage badges (+14.2% vs last hour).",
            "primary_stream": "Real-time stream/event log with monospace timestamp, status pill, and auto-scroll freeze toggle.",
            "density_level": "Compact 4px padding grid, jetbrains mono metrics, razor-thin hairline borders."
        },
        "ascii_wireframe": """
[ ● LIVE CLUSTER: us-east-1 ]   [ 12ms Latency ]   [ 99.99% Uptime ]
+-------------------+-------------------+-------------------+-------------------+
| ACTIVE REQUESTS   | THROUGHPUT        | ERROR RATE        | P99 LATENCY       |
| 142,890 /s        | 1.24 GB/s         | 0.001%            | 18.4 ms           |
| +12.4% vs avg     | [=== Sparkline =] | -0.04% stable     | optimal           |
+-------------------+-------------------+-------------------+-------------------+
| EVENT LOG STREAM (Real-time telemetry)                     [Auto-scroll: ON]  |
| 18:24:01.104  INFO   cluster/node-04  Inference batch completed in 14ms       |
| 18:24:01.120  DEBUG  gateway/proxy    TLS handshake 1.3 negotiated            |
+-------------------------------------------------------------------------------+
""",
        "creative_prompts_for_ai": [
            "Use JetBrains Mono or Geist Mono for all numerical data.",
            "Apply green/amber/rose indicator dots with animate-ping for real-time states.",
            "Keep card borders at border-white/[0.08] to avoid heavy visual clutter."
        ]
    }
}
