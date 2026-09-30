"""
Lumina Design Auditor - Scans Codebase for AI Slop & Generates Refactor Directives
"""
import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class AuditIssue:
    file_path: str
    line_number: int
    rule_id: str
    severity: str  # HIGH, MEDIUM, LOW
    message: str
    recommendation: str
    snippet: str

class DesignAuditor:
    RULES = [
        {
            "id": "generic-purple-gradient",
            "severity": "HIGH",
            "penalty": 12,
            "pattern": re.compile(r'from-(?:purple|indigo)-(?:500|600)\s+to-(?:pink|indigo|purple)-(?:500|600)', re.IGNORECASE),
            "message": "Generic AI purple/indigo gradient detected.",
            "recommendation": "Replace with monochromatic depth, subtle mesh radial diffusion, or a single razor-sharp accent (emerald, amber, or cyan)."
        },
        {
            "id": "missing-chamfer-highlight",
            "severity": "MEDIUM",
            "penalty": 8,
            "pattern": re.compile(r'(?:bg-zinc-900|bg-neutral-900|bg-neutral-950)\s+border\s+border-(?:zinc|neutral)-(?:800|700)(?!.*shadow-\[inset)', re.IGNORECASE),
            "message": "Flat dark card without 1px chamfer highlight.",
            "recommendation": "Add metallic edge reflection: shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] and border-white/[0.08]."
        },
        {
            "id": "untracked-heading-font",
            "severity": "MEDIUM",
            "penalty": 6,
            "pattern": re.compile(r'<h[1-3][^>]*class(?:Name)?="[^"]*text-(?:3|4|5|6)xl(?![^"]*tracking-tight)[^"]*"', re.IGNORECASE),
            "message": "Large heading without tracking adjustment.",
            "recommendation": "Add `tracking-tight` or `tracking-tighter` to tighten modern display typography."
        },
        {
            "id": "unreactive-button",
            "severity": "MEDIUM",
            "penalty": 7,
            "pattern": re.compile(r'<button[^>]*class(?:Name)?="[^"]*(?<!active:scale-)px-[^"]*"', re.IGNORECASE),
            "message": "Button lacks spring tactile active scale.",
            "recommendation": "Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback."
        },
        {
            "id": "boring-empty-state",
            "severity": "MEDIUM",
            "penalty": 8,
            "pattern": re.compile(r'(?:No items found|No data available|Nothing here yet)(?!.*(?:<button|<kbd))', re.IGNORECASE),
            "message": "Dead/passive empty state without interactive recovery or shortcut.",
            "recommendation": "Add interactive action button with keyboard shortcut hint (e.g. <kbd>⌘N</kbd>) and dashed border."
        },
        {
            "id": "hardcoded-generic-hex",
            "severity": "LOW",
            "penalty": 4,
            "pattern": re.compile(r'#(?:6366f1|7c3aed|8b5cf6|3b82f6|ec4899)', re.IGNORECASE),
            "message": "Hardcoded generic SaaS hex code detected.",
            "recommendation": "Use semantic CSS variable tokens (var(--primary), var(--accent)) or OKLCH palette."
        },
        {
            "id": "symmetric-card-grid",
            "severity": "LOW",
            "penalty": 5,
            "pattern": re.compile(r'grid\s+grid-cols-1\s+(?:md:grid-cols-3|lg:grid-cols-3)\s+gap-(?:4|6|8)(?!.*col-span-2)', re.IGNORECASE),
            "message": "Predictable 3-column symmetric card layout detected.",
            "recommendation": "Consider an Asymmetric Bento Grid layout with variable column spans and live interactive widgets."
        },
        {
            "id": "uninspired-pulse-loader",
            "severity": "LOW",
            "penalty": 4,
            "pattern": re.compile(r'animate-pulse\s+bg-(?:gray|zinc|neutral)-(?:200|700|800)', re.IGNORECASE),
            "message": "Standard gray pulse loader reads as low-fidelity template.",
            "recommendation": "Upgrade to diagonal ray shimmer skeleton: `bg-gradient-to-r from-transparent via-white/[0.06] to-transparent`."
        }
    ]

    IGNORE_DIRS = {
        "node_modules", ".git", ".next", "dist", "build", ".turbo", ".cache", "coverage", ".lumina"
    }

    VALID_EXTS = {".tsx", ".jsx", ".html", ".vue", ".svelte", ".css"}

    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()

    def audit(self) -> Dict:
        issues: List[AuditIssue] = []
        files_scanned = 0

        for root, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if d not in self.IGNORE_DIRS]
            
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in self.VALID_EXTS:
                    files_scanned += 1
                    file_path = Path(root) / file
                    self._scan_file(file_path, issues)

        total_penalty = sum(
            next((r["penalty"] for r in self.RULES if r["id"] == iss.rule_id), 5)
            for iss in issues
        )
        
        score = max(10, 100 - total_penalty) if files_scanned > 0 else 100
        
        if score >= 95:
            grade = "S (World-Class / Linear Tier)"
        elif score >= 85:
            grade = "A (Premium Craft)"
        elif score >= 70:
            grade = "B (Polished with Minor Slop)"
        elif score >= 50:
            grade = "C (Common AI Boilerplate)"
        else:
            grade = "F (High Density AI-Slop)"

        return {
            "score": score,
            "grade": grade,
            "files_scanned": files_scanned,
            "issues": issues,
            "total_issues": len(issues)
        }

    def _scan_file(self, file_path: Path, issues: List[AuditIssue]):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            return

        rel_path = str(file_path.relative_to(self.root_dir))

        for line_idx, line in enumerate(lines, start=1):
            for rule in self.RULES:
                if rule["pattern"].search(line):
                    issues.append(AuditIssue(
                        file_path=rel_path,
                        line_number=line_idx,
                        rule_id=rule["id"],
                        severity=rule["severity"],
                        message=rule["message"],
                        recommendation=rule["recommendation"],
                        snippet=line.strip()[:100]
                    ))

    def generate_fix_prompt(self, audit_result: Dict) -> str:
        """Generates an actionable Markdown prompt to feed directly to AGY or Claude Code."""
        issues = audit_result["issues"]
        if not issues:
            return "# Lumina Audit: Clean Bill of Health!\n\nNo AI slop detected. Your frontend aligns with Linear and Apple tier standards."

        lines = [
            "# 🛠️ LUMINA AI-SLOP REFACTORING DIRECTIVE",
            "",
            "> **Instructions for AGY / Claude Code:**",
            f"> The Lumina Design Auditor scanned the project and detected **{len(issues)} design defects / AI-slop anti-patterns**.",
            f"> Current Design Score: **{audit_result['score']}/100** ({audit_result['grade']}).",
            "> Please refactor the target files step-by-step to meet Linear and Apple luxury frontend standards.",
            "",
            "## 📋 Detected Issues & Exact Remediation Steps:",
            ""
        ]

        grouped = {}
        for iss in issues:
            grouped.setdefault(iss.file_path, []).append(iss)

        for file_path, file_issues in grouped.items():
            lines.append(f"### 📄 `{file_path}`")
            for iss in file_issues:
                lines.append(f"- **Line {iss.line_number}** [{iss.severity}]: {iss.message}")
                lines.append(f"  - *Problem Snippet:* `{iss.snippet}`")
                lines.append(f"  - *Fix:* {iss.recommendation}")
            lines.append("")

        lines.extend([
            "## 🎨 Core Design Principles to Enforce During Refactor:",
            "1. **Apply 1px Chamfer Highlights:** Use `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]` on cards.",
            "2. **Eliminate Purple/Pink Gradients:** Shift to monochromatic obsidian depth with emerald, amber, or cyan accents.",
            "3. **Add Tactile Motion:** Give all buttons `active:scale-[0.98]` and spring physics.",
            "4. **Refine Typography:** Add `tracking-tight` on headings and `font-mono text-xs uppercase tracking-wider` on metadata.",
            "5. Verify responsive layouts and dark mode contrast.",
            "",
            "Begin refactoring now."
        ])

        return "\n".join(lines)
