#!/usr/bin/env python3
"""
Lumina MCP Server - Model Context Protocol Server for AGY & Claude Code
Generative AI Design Intelligence Engine:
- Parametric Token Synthesizer (9 Luxury Archetypes + Physics)
- Composition Grammar Engine (Preserves AI Creativity, Eliminates Cookie-Cutter Slop)
- Visual & Haptic Primitives (Border Beam, Spotlight, 3D Tilt, Text Scramble, Audio)
- Production Blueprints (Reference Architecture)
- Design Director Critique & Slop Auditor
"""
import sys
import json
from pathlib import Path

# Ensure UTF-8 stdio on Windows
if sys.platform == "win32":
    try:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lumina.core.themes import THEMES, SPRING_PHYSICS, get_theme
from lumina.core.primitives import PRIMITIVES
from lumina.core.grammar import GRAMMAR_PATTERNS
from lumina.core.registry import COMPONENTS
from lumina.core.auditor import DesignAuditor

TOOLS = [
    {
        "name": "synthesize_design_tokens",
        "description": "Synthesizes parametric luxury design tokens (OKLCH palettes, specular chamfers, spring physics, and fonts) tailored to the specified archetype, density, and materiality.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "archetype": {
                    "type": "string",
                    "description": "Theme archetype: 'linear-dark', 'apple-clean', 'vercel-mono', 'stripe-saas', 'cyber-tactile', 'teenage-industrial', 'stripe-editorial', 'spatial-glass', 'refined-brutalism'",
                    "enum": [
                        "linear-dark", "apple-clean", "vercel-mono", "stripe-saas", "cyber-tactile",
                        "teenage-industrial", "stripe-editorial", "spatial-glass", "refined-brutalism"
                    ]
                },
                "density": {
                    "type": "string",
                    "description": "Interface data density: 'compact' (4px telemetric), 'balanced' (8px standard), 'editorial' (16px expansive)",
                    "enum": ["compact", "balanced", "editorial"]
                },
                "materiality": {
                    "type": "string",
                    "description": "Surface materiality: 'metallic-chamfer' (1px inner specular highlight), 'glass' (visionOS liquid refraction), 'raw-slab' (hard offset shadow), 'anodized-matte' (diffuse metal)",
                    "enum": ["metallic-chamfer", "glass", "raw-slab", "anodized-matte"]
                },
                "motion_physics": {
                    "type": "string",
                    "description": "Spring physics profile: 'snappy' (Linear/Raycast 400/30), 'mechanical-relay' (Teenage Eng 520/42), 'viscous-spatial' (visionOS 260/28), 'zen' (Stripe 180/35)",
                    "enum": ["snappy", "mechanical-relay", "viscous-spatial", "zen"]
                }
            },
            "required": ["archetype"]
        }
    },
    {
        "name": "get_composition_grammar",
        "description": "Returns structural visual design laws, layout hierarchy formulas, and ASCII wireframes for a UI pattern. Teaches the AI how to compose original, balanced interfaces without imposing cookie-cutter JSX code.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string",
                    "description": "UI layout pattern: 'bento-grid', 'hero-section', 'command-palette', 'dashboard-telemetry'",
                    "enum": ["bento-grid", "hero-section", "command-palette", "dashboard-telemetry"]
                },
                "domain_context": {
                    "type": "string",
                    "description": "Specific project domain or purpose (e.g. 'AI Coding Agent', 'High-Frequency Crypto Trading', 'Audiophile Synthesizer', 'B2B Analytics')"
                }
            },
            "required": ["pattern"]
        }
    },
    {
        "name": "get_visual_primitive",
        "description": "Returns atomic mathematical formulas, interaction logic, and micro-interaction building blocks (Border Beam, Spotlight Follow, 3D Perspective Tilt, Text Scramble Cipher, Web Audio Haptics) that can be injected into any custom UI.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "primitive_id": {
                    "type": "string",
                    "description": "Primitive ID: 'border-beam', 'spotlight-cone', '3d-tilt', 'text-scramble', 'web-audio-haptic'",
                    "enum": ["border-beam", "spotlight-cone", "3d-tilt", "text-scramble", "web-audio-haptic"]
                }
            },
            "required": ["primitive_id"]
        }
    },
    {
        "name": "get_component_blueprint",
        "description": "Returns verified, production-grade reference component blueprints (Bento Grid, Command Bar, Floating Dock, etc.) for rapid scaffolding.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "component_id": {
                    "type": "string",
                    "description": "Component ID: 'bento-grid', 'command-bar', 'floating-dock', 'glow-hero', 'magnetic-button', 'stat-cards', 'skeleton-shimmer', 'empty-state'",
                    "enum": ["bento-grid", "command-bar", "floating-dock", "glow-hero", "magnetic-button", "stat-cards", "skeleton-shimmer", "empty-state"]
                }
            },
            "required": ["component_id"]
        }
    },
    {
        "name": "critique_ui_design",
        "description": "Acts as a Senior Design Director auditing a JSX/TSX/HTML code snippet for visual hierarchy, contrast, typography tracking, tactile feedback, and AI-slop anti-patterns with actionable remediation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Source code snippet to critique"
                }
            },
            "required": ["code"]
        }
    }
]

def handle_call_tool(name: str, args: dict) -> dict:
    if name == "synthesize_design_tokens":
        arch_id = args.get("archetype", "linear-dark")
        density = args.get("density", "balanced")
        materiality = args.get("materiality", "metallic-chamfer")
        motion_id = args.get("motion_physics", "snappy")

        theme_def = get_theme(arch_id)
        spring = SPRING_PHYSICS.get(motion_id, SPRING_PHYSICS["snappy"])

        # Density adaptations
        density_rules = {
            "compact": {"padding_scale": "p-3 to p-4", "gap_scale": "gap-2 to gap-3", "target_audience": "Developer HUD, High-density Finance"},
            "balanced": {"padding_scale": "p-6", "gap_scale": "gap-4 to gap-6", "target_audience": "Modern B2B SaaS, Admin Dashboards"},
            "editorial": {"padding_scale": "p-8 to p-12", "gap_scale": "gap-8 to gap-12", "target_audience": "Luxury Consumer, Publishing, Marketing"}
        }

        # Materiality highlights
        materiality_map = {
            "metallic-chamfer": "border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.08)]",
            "glass": "backdrop-blur-2xl bg-white/[0.04] border-t-white/30 border-white/10 shadow-2xl",
            "raw-slab": "border-2 border-black dark:border-white shadow-[3px_3px_0_0_#000]",
            "anodized-matte": "bg-[#18181b] border-white/10 shadow-none ring-1 ring-white/5"
        }

        return {
            "archetype": theme_def.name,
            "target_use": theme_def.archetype,
            "traits": theme_def.traits,
            "typography": {
                "font_sans": theme_def.font_sans,
                "font_mono": theme_def.font_mono
            },
            "density_configuration": density_rules.get(density, density_rules["balanced"]),
            "materiality_class": materiality_map.get(materiality, materiality_map["metallic-chamfer"]),
            "spring_physics": spring,
            "css_variables": theme_def.css_variables.strip(),
            "tailwind_extensions": theme_def.tailwind_extensions
        }

    elif name == "get_composition_grammar":
        pattern_id = args.get("pattern", "bento-grid")
        domain = args.get("domain_context", "General SaaS / Developer Tool")
        grammar = GRAMMAR_PATTERNS.get(pattern_id)
        if not grammar:
            return {"error": f"Pattern '{pattern_id}' not found."}

        return {
            "pattern": grammar["pattern_name"],
            "core_philosophy": grammar["philosophy"],
            "domain_context": domain,
            "visual_hierarchy": grammar["visual_hierarchy"],
            "ascii_wireframe": grammar["ascii_wireframe"],
            "creative_direction_for_ai": grammar["creative_prompts_for_ai"]
        }

    elif name == "get_visual_primitive":
        prim_id = args.get("primitive_id", "border-beam")
        prim = PRIMITIVES.get(prim_id)
        if not prim:
            return {"error": f"Primitive '{prim_id}' not found."}

        return {
            "name": prim["name"],
            "category": prim["category"],
            "description": prim["description"],
            "dependencies": prim["dependencies"],
            "code_snippet": prim["snippet"].strip()
        }

    elif name == "get_component_blueprint":
        comp_id = args.get("component_id", "bento-grid")
        comp = COMPONENTS.get(comp_id)
        if not comp:
            return {"error": f"Component '{comp_id}' not found."}
        return {
            "name": comp.name,
            "category": comp.category,
            "dependencies": comp.dependencies,
            "suggested_filename": comp.filename,
            "code": comp.code
        }

    elif name == "critique_ui_design":
        code = args.get("code", "")
        auditor = DesignAuditor()
        issues = []
        for line_idx, line in enumerate(code.splitlines(), start=1):
            for rule in auditor.RULES:
                if rule["pattern"].search(line):
                    issues.append({
                        "line": line_idx,
                        "rule": rule["id"],
                        "severity": rule["severity"],
                        "message": rule["message"],
                        "recommendation": rule["recommendation"]
                    })
        score = max(10, 100 - len(issues) * 10)
        
        # Design Director Evaluation
        director_notes = []
        if "active:scale-" not in code and "<button" in code:
            director_notes.append("Buttons feel static and unreactive. Inject `active:scale-[0.98]` and `duration-100` for tactile spring response.")
        if "tracking-tight" not in code and ("text-4xl" in code or "text-5xl" in code or "text-6xl" in code):
            director_notes.append("Display typography lacks modern tracking discipline. Apply `tracking-tight` to tighten headline letter-spacing.")
        if "from-purple" in code or "from-indigo" in code:
            director_notes.append("Generic AI gradient detected. Substitute with obsidian depth, specular chamfers, or singular accent colorways.")

        return {
            "design_score": score,
            "director_grade": "World-Class (S-Tier)" if score >= 90 else "Competent but Generic (B-Tier)" if score >= 70 else "AI-Slop Detected (F-Tier)",
            "total_defects": len(issues),
            "defects": issues,
            "director_refactoring_notes": director_notes
        }

    return {"error": f"Unknown tool: {name}"}

def main():
    """Production-grade JSON-RPC 2.0 stdio server compliant with Model Context Protocol."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        # In JSON-RPC 2.0 / MCP: Notifications have NO 'id' and MUST NOT receive any response!
        is_notification = (req_id is None) or (method and method.startswith("notifications/"))

        if method == "initialize":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "lumina-design-mcp",
                        "version": "2.0.0"
                    }
                }
            }
        elif method in ("notifications/initialized", "initialized"):
            # Client notification that initialization is complete -> NEVER reply
            continue
        elif method == "ping":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {}
            }
        elif method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": TOOLS
                }
            }
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            tool_res = handle_call_tool(tool_name, tool_args)
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(tool_res, indent=2, ensure_ascii=False)
                        }
                    ]
                }
            }
        elif method == "resources/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "resources": []
                }
            }
        elif method == "prompts/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "prompts": []
                }
            }
        else:
            if is_notification:
                # Silently ignore any unhandled notifications
                continue
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }

        try:
            sys.stdout.write(json.dumps(res, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception:
            pass

if __name__ == "__main__":
    main()
