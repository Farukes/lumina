"""
Lumina Style Polisher - Automated AI-Slop Code Refactoring Engine
Like Prettier/ESLint, but for Design Quality & Apple/Linear Aesthetics.
"""
import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class PolishDiff:
    file_path: str
    line_number: int
    rule_name: str
    original: str
    replacement: str

class StylePolisher:
    IGNORE_DIRS = {
        "node_modules", ".git", ".next", "dist", "build", ".turbo", ".cache", "coverage", ".lumina"
    }
    VALID_EXTS = {".tsx", ".jsx", ".html", ".vue", ".svelte", ".css"}

    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()

    def polish(self, dry_run: bool = False) -> Dict:
        """Scans and automatically refactors AI-slop in target files."""
        total_files = 0
        modified_files = 0
        all_diffs: List[PolishDiff] = []

        for root, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if d not in self.IGNORE_DIRS]

            for file in files:
                ext = Path(file).suffix.lower()
                if ext in self.VALID_EXTS:
                    total_files += 1
                    file_path = Path(root) / file
                    diffs = self._polish_file(file_path, dry_run=dry_run)
                    if diffs:
                        modified_files += 1
                        all_diffs.extend(diffs)

        return {
            "total_files": total_files,
            "modified_files": modified_files,
            "total_fixes": len(all_diffs),
            "diffs": all_diffs,
            "dry_run": dry_run
        }

    def _polish_file(self, file_path: Path, dry_run: bool = False) -> List[PolishDiff]:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            return []

        original_content = content
        diffs: List[PolishDiff] = []
        rel_path = str(file_path.relative_to(self.root_dir))

        lines = content.splitlines()
        new_lines = []

        for idx, line in enumerate(lines, start=1):
            modified_line = line

            # 1. Transform generic purple/indigo gradients on buttons
            if re.search(r'bg-gradient-to-r\s+from-(?:purple|indigo)-(?:500|600)\s+to-(?:pink|indigo|purple)-(?:500|600)', modified_line):
                replaced = re.sub(
                    r'bg-gradient-to-r\s+from-(?:purple|indigo)-(?:500|600)\s+to-(?:pink|indigo|purple)-(?:500|600)[^\s"]*',
                    'bg-white hover:bg-neutral-100 text-neutral-950 font-semibold shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_20px_rgba(255,255,255,0.15)] active:scale-[0.98] transition-all',
                    modified_line
                )
                diffs.append(PolishDiff(rel_path, idx, "Eliminate Purple Gradient", line.strip(), replaced.strip()))
                modified_line = replaced

            # 2. Add 1px Chamfer Highlight to flat dark cards
            if re.search(r'(?:bg-zinc-900|bg-neutral-900|bg-neutral-950)\s+border\s+border-(?:zinc|neutral)-(?:800|700)', modified_line) and "shadow-[inset" not in modified_line:
                replaced = re.sub(
                    r'(bg-(?:zinc|neutral)-(?:900|950)\s+border\s+border-(?:zinc|neutral)-(?:800|700))',
                    r'\1 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] border-white/[0.08]',
                    modified_line
                )
                diffs.append(PolishDiff(rel_path, idx, "Add 1px Chamfer Highlight", line.strip(), replaced.strip()))
                modified_line = replaced

            # 3. Add tracking-tight to display headings
            if re.search(r'<h[1-3][^>]*class(?:Name)?="[^"]*text-(?:3|4|5|6|7)xl(?![^"]*tracking-tight)[^"]*"', modified_line):
                replaced = re.sub(
                    r'(class(?:Name)?="[^"]*text-(?:3|4|5|6|7)xl)',
                    r'\1 tracking-tight',
                    modified_line
                )
                diffs.append(PolishDiff(rel_path, idx, "Add tracking-tight to Heading", line.strip(), replaced.strip()))
                modified_line = replaced

            # 4. Add tactile active:scale-[0.98] to buttons
            if "<button" in modified_line and "active:scale-" not in modified_line and "class" in modified_line:
                replaced = re.sub(
                    r'(class(?:Name)?="[^"]*)(")',
                    r'\1 active:scale-[0.98] transition-transform duration-100\2',
                    modified_line
                )
                diffs.append(PolishDiff(rel_path, idx, "Add Tactile Spring Scale to Button", line.strip(), replaced.strip()))
                modified_line = replaced

            new_lines.append(modified_line)

        new_content = "\n".join(new_lines)

        if not dry_run and new_content != original_content:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
            except Exception as e:
                print(f"Error saving {file_path}: {e}")

        return diffs
