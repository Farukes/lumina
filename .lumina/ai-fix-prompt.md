# 🛠️ LUMINA AI-SLOP REFACTORING DIRECTIVE

> **Instructions for AGY / Claude Code:**
> The Lumina Design Auditor scanned the project and detected **4 design defects / AI-slop anti-patterns**.
> Current Design Score: **72/100** (B (Polished with Minor Slop)).
> Please refactor the target files step-by-step to meet Linear and Apple luxury frontend standards.

## 📋 Detected Issues & Exact Remediation Steps:

### 📄 `KronosDashboard.tsx`
- **Line 76** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button className="flex items-center gap-2 px-3 py-1.5 rounded-xl border border-white/[0.08] bg-whit`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 117** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button className="bg-white hover:bg-neutral-100 text-neutral-950 font-semibold px-4 py-2 rounded-xl`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 196** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button className="px-2.5 py-1 rounded-lg border border-white/10 hover:bg-white/5 active:scale-[0.98`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 209** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button className="px-3 py-1.5 rounded-xl border border-white/10 hover:bg-white/5 font-mono text-xs `
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.

## 🎨 Core Design Principles to Enforce During Refactor:
1. **Apply 1px Chamfer Highlights:** Use `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]` on cards.
2. **Eliminate Purple/Pink Gradients:** Shift to monochromatic obsidian depth with emerald, amber, or cyan accents.
3. **Add Tactile Motion:** Give all buttons `active:scale-[0.98]` and spring physics.
4. **Refine Typography:** Add `tracking-tight` on headings and `font-mono text-xs uppercase tracking-wider` on metadata.
5. Verify responsive layouts and dark mode contrast.

Begin refactoring now.