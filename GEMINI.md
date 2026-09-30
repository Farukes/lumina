# Antigravity Project Context

See detailed frontend guidelines in `.agents/rules/frontend-premium.md`.

# Project Guidelines for Claude Code & AI Assistants

## Design System: Lumina Premium Standard
This project follows the **Lumina Premium Design System** (Linear, Apple, Vercel tier).
When writing UI components (React, Next.js, HTML, CSS):

1. **Avoid AI Slop:**
   - No generic purple-indigo gradients.
   - No 3 identical feature cards. Use asymmetrical Bento Grids.
   - No flat unchamfered cards. Use `border-white/[0.08]` and `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`.
   - No un-tracked typography. Use `tracking-tight` on headings and `font-mono text-xs uppercase tracking-wider` on badges.
   - No static buttons. Add `active:scale-[0.98]`.

2. **Tech Stack & Conventions:**
   - Styling: Tailwind CSS with CSS Variables (`globals.css`).
   - Icons: Lucide React (`lucide-react`).
   - Motion: Framer Motion (`framer-motion`) with spring physics.
   - Primitives: Radix UI / headless primitives.

3. **Component Structure:**
   - Place reusable UI primitives in `components/ui/`.
   - Place composite blocks (Bento, Hero, Navigation) in `components/blocks/`.
