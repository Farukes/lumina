# 🛠️ LUMINA AI-SLOP REFACTORING DIRECTIVE

> **Instructions for AGY / Claude Code:**
> The Lumina Design Auditor scanned the project and detected **17 design defects / AI-slop anti-patterns**.
> Current Design Score: **10/100** (F (High Density AI-Slop)).
> Please refactor the target files step-by-step to meet Linear and Apple luxury frontend standards.

## 📋 Detected Issues & Exact Remediation Steps:

### 📄 `showcase\index.html`
- **Line 53** [LOW]: Hardcoded generic SaaS hex code detected.
  - *Problem Snippet:* `--primary: #6366f1;`
  - *Fix:* Use semantic CSS variable tokens (var(--primary), var(--accent)) or OKLCH palette.
- **Line 112** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('linear')" class="theme-btn px-3 py-1.5 rounded-lg transition-all bg-white`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 113** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('apple')" class="theme-btn px-3 py-1.5 rounded-lg transition-all text-neut`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 114** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('vercel')" class="theme-btn px-3 py-1.5 rounded-lg transition-all text-neu`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 115** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('stripe')" class="theme-btn px-3 py-1.5 rounded-lg transition-all text-neu`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 116** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('cyber')" class="theme-btn px-3 py-1.5 rounded-lg transition-all text-neut`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 124** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="openCmd()" class="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 164** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="runAuditDemo()" class="chamfer-card px-5 py-3 rounded-xl text-sm font-medium text-n`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 217** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="incrementStream()" class="px-3 py-1.5 rounded-lg bg-emerald-500 hover:bg-emerald-40`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 284** [HIGH]: Generic AI purple/indigo gradient detected.
  - *Problem Snippet:* `<div class="text-neutral-400 mt-1">src/components/Hero.tsx:42 -> from-purple-500 to-indigo-600</div>`
  - *Fix:* Replace with monochromatic depth, subtle mesh radial diffusion, or a single razor-sharp accent (emerald, amber, or cyan).
- **Line 297** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="closeAuditModal()" class="px-4 py-2 rounded-xl bg-white hover:bg-neutral-200 text-n`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 310** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="closeCmd()" class="text-xs font-mono text-neutral-500 hover:text-white px-1.5 py-0.`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 334** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('linear'); playClick();" class="dock-btn px-3 py-2 rounded-xl text-xs font`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 338** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('apple'); playClick();" class="dock-btn px-3 py-2 rounded-xl text-xs font-`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 342** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('vercel'); playClick();" class="dock-btn px-3 py-2 rounded-xl text-xs font`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 346** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="setTheme('cyber'); playClick();" class="dock-btn px-3 py-2 rounded-xl text-xs font-`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.
- **Line 350** [MEDIUM]: Button lacks spring tactile active scale.
  - *Problem Snippet:* `<button onclick="runAuditDemo(); playClick();" class="dock-btn px-3 py-2 rounded-xl text-xs font-med`
  - *Fix:* Add `active:scale-[0.98]` and `transition-transform duration-100` for tactile press feedback.

## 🎨 Core Design Principles to Enforce During Refactor:
1. **Apply 1px Chamfer Highlights:** Use `border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]` on cards.
2. **Eliminate Purple/Pink Gradients:** Shift to monochromatic obsidian depth with emerald, amber, or cyan accents.
3. **Add Tactile Motion:** Give all buttons `active:scale-[0.98]` and spring physics.
4. **Refine Typography:** Add `tracking-tight` on headings and `font-mono text-xs uppercase tracking-wider` on metadata.
5. Verify responsive layouts and dark mode contrast.

Begin refactoring now.