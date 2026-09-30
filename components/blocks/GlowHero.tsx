import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles, ArrowRight, CheckCircle2 } from 'lucide-react';

export function GlowHero() {
  return (
    <section className="relative overflow-hidden py-24 px-6 max-w-6xl mx-auto flex flex-col items-center text-center">
      {/* Ambient Radial Glow */}
      <div className="absolute top-1/4 -translate-y-1/2 w-[600px] h-[350px] bg-gradient-to-tr from-emerald-500/20 via-cyan-500/15 to-transparent blur-[120px] rounded-full pointer-events-none -z-10" />

      {/* Pill Badge */}
      <motion.div 
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] text-xs font-mono text-neutral-300 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] mb-8"
      >
        <Sparkles className="w-3.5 h-3.5 text-emerald-400" />
        <span>BUILT FOR AGY & CLAUDE CODE</span>
        <span className="w-1 h-1 rounded-full bg-neutral-600" />
        <span className="text-emerald-400">ZERO SLOP</span>
      </motion.div>

      {/* Hero Headline */}
      <motion.h1 
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-5xl sm:text-7xl font-bold tracking-tight text-white max-w-4xl leading-[1.08]"
      >
        Craft frontends that feel like <span className="text-transparent bg-clip-text bg-gradient-to-b from-white via-white to-neutral-500">pure craftsmanship</span>.
      </motion.h1>

      <motion.p 
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="mt-6 text-lg text-neutral-400 max-w-2xl font-normal leading-relaxed"
      >
        Empower AI agents to build Linear and Apple tier user interfaces. Chamfered edges, spring physics, OKLCH palettes, and strict design constraints.
      </motion.p>

      {/* Action Buttons */}
      <motion.div 
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="mt-10 flex flex-wrap items-center justify-center gap-4"
      >
        <button className="px-6 py-3 rounded-xl bg-white hover:bg-neutral-100 text-neutral-950 font-semibold text-sm shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_20px_rgba(255,255,255,0.2)] active:scale-[0.98] transition-all flex items-center gap-2">
          <span>Explore Component Registry</span>
          <ArrowRight className="w-4 h-4" />
        </button>

        <button className="px-6 py-3 rounded-xl bg-neutral-900/80 hover:bg-neutral-900 border border-white/[0.08] text-neutral-200 font-medium text-sm shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] active:scale-[0.98] transition-all">
          Run lumina audit
        </button>
      </motion.div>

      {/* Feature Badges */}
      <div className="mt-16 flex flex-wrap justify-center gap-8 text-xs text-neutral-500 font-mono">
        <span className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-400" /> OKLCH Color Space</span>
        <span className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-400" /> 1px Chamfer Highlights</span>
        <span className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-400" /> Spring Micro-Physics</span>
      </div>
    </section>
  );
}
