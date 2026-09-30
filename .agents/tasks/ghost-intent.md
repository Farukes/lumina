# 🛸 LUMINA GHOST: VISUAL INTENT DIRECTIVE
Timestamp: 2026-09-30T18:09:01.6812453+03:00
Page URL: http://localhost:3000

## 🎯 Target Component
- **Component / Name:** `HeroCTA`
- **Tag:** `BUTTON`
- **Classes:** `px-8 py-3.5 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600`
- **Text Snippet:** "Generic Purple AI Button"

## ⚡ User Action & Directive
- **Action Type:** `linear-polish`
- **Instructions:** Apply 1px metallic chamfer, obsidian depth and spring active scale

## 🎨 Recommended Fixes:
1. If Linear Polish: Add 1px chamfer (`border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`), dark obsidian background, and spring active scale (`active:scale-[0.98]`).
2. If Apple Glass: Add `backdrop-blur-2xl bg-white/[0.06] border border-white/[0.12] rounded-2xl`.
3. If Purge Slop: Remove generic purple/indigo gradients and enforce tight font tracking.
4. Refactor the corresponding source file and let Vite HMR update the browser.
