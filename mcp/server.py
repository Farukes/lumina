#!/usr/bin/env python3
"""
Lumina MCP Server - Model Context Protocol Server for AGY & Claude Code
Provides AI agents with native design intelligence, verified blueprints, and auto-polish tools.
"""
import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lumina.core.themes import THEMES
from lumina.core.registry import COMPONENTS
from lumina.core.polisher import StylePolisher
from lumina.core.auditor import DesignAuditor

TOOLS = [
    {
        "name": "get_design_tokens",
        "description": "Returns luxury design system tokens, OKLCH color palettes, chamfer shadows, and spring physics curves for a specified theme.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "theme": {
                    "type": "string",
                    "description": "Theme ID: 'linear-dark', 'apple-clean', 'vercel-mono', 'stripe-saas', or 'cyber-tactile'",
                    "enum": ["linear-dark", "apple-clean", "vercel-mono", "stripe-saas", "cyber-tactile"]
                }
            },
            "required": ["theme"]
        }
    },
    {
        "name": "get_component_blueprint",
        "description": "Returns verified, production-grade React/TypeScript code for AAA-tier components (Bento Grid, Command Bar, Floating Dock, etc.) to prevent AI hallucination.",
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
        "name": "audit_code_design",
        "description": "Audits a given JSX/TSX/HTML code snippet for AI-slop anti-patterns (generic purple gradients, unchamfered cards, untracked typography) and returns a score and remediation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Source code to audit for design anti-patterns"
                }
            },
            "required": ["code"]
        }
    }
]

def handle_call_tool(name: str, args: dict) -> dict:
    if name == "get_design_tokens":
        theme_id = args.get("theme", "linear-dark")
        theme_def = THEMES.get(theme_id, THEMES["linear-dark"])
        return {
            "theme_name": theme_def.name,
            "archetype": theme_def.archetype,
            "traits": theme_def.traits,
            "css_variables": theme_def.css_variables.strip(),
            "tailwind_extensions": theme_def.tailwind_extensions,
            "fonts": {
                "sans": theme_def.font_sans,
                "mono": theme_def.font_mono
            }
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

    elif name == "audit_code_design":
        code = args.get("code", "")
        # Run temporary file check
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
        return {
            "score": score,
            "issues_count": len(issues),
            "issues": issues,
            "verdict": "World-Class" if score >= 90 else "Needs Polish" if score >= 70 else "High Density AI-Slop"
        }

    return {"error": f"Unknown tool: {name}"}

def main():
    """Simple JSON-RPC 2.0 stdio server for Model Context Protocol."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

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
                            "version": "1.0.0"
                        }
                    }
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
                                "text": json.dumps(tool_res, indent=2)
                            }
                        ]
                    }
                }
            else:
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                }

            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_res = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32603,
                    "message": str(e)
                }
            }
            sys.stdout.write(json.dumps(err_res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
