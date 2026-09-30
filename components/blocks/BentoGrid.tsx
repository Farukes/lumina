import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Activity, ShieldCheck, Zap, Sparkles, ArrowUpRight, Terminal } from 'lucide-react';

export function BentoGrid() {
  const [activeToggle, setActiveToggle] = useState(true);
  const [metricCount, setMetricCount] = useState(1420);

  return (
    <div className="w-full max-w-6xl mx-auto p-6 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 auto-rows-[220px]">
      
      {/* 1. Hero Showcase Card (Spans 2 cols, 2 rows) */}
      <motion.div 
        whileHover={{ y: -3 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="md:col-span-2 md:row-span-2 relative overflow-hidden rounded-2xl bg-neutral-950/80 border border-white/[0.08] p-8 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] flex flex-col justify-between group"
      >
        <div className="absolute top-0 right-0 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-emerald-500/15 transition-all duration-700" />
        
        <div className="flex items-center justify-between">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-mono tracking-wide">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
            LIVE TELEMETRY
          </div>
          <span className="text-xs font-mono text-neutral-500">SYS_V2.4</span>
        </div>

        <div>
          <div className="text-5xl font-bold tracking-tight text-white font-sans flex items-baseline gap-3">
            {metricCount.toLocaleString()}
            <span className="text-emerald-400 text-sm font-mono flex items-center font-normal">
              <ArrowUpRight className="w-4 h-4" /> +18.4%
            </span>
          </div>
          <p className="text-neutral-400 text-sm mt-2 max-w-sm">
            Autonomous agent workflow executions with zero latency degradation.
          </p>
        </div>

        <div className="pt-4 border-t border-white/[0.06] flex items-center justify-between">
          <div className="flex gap-2">
            {['EU-Central', 'US-East', 'AP-East'].map((region, i) => (
              <span key={i} className="px-2 py-1 rounded bg-white/[0.04] text-[11px] font-mono text-neutral-300 border border-white/[0.04]">
                {region}
              </span>
            ))}
          </div>
          <button 
            onClick={() => setMetricCount(c => c + 15)}
            className="px-3 py-1.5 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-neutral-950 font-medium text-xs active:scale-[0.98] transition-all"
          >
            Increment Stream
          </button>
        </div>
      </motion.div>

      {/* 2. Interactive Toggle Card */}
      <motion.div 
        whileHover={{ y: -3 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="rounded-2xl bg-neutral-950/80 border border-white/[0.08] p-6 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] flex flex-col justify-between"
      >
        <div className="flex items-center justify-between">
          <div className="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-neutral-300">
            <Zap className="w-4 h-4 text-amber-400" />
          </div>
          <button 
            onClick={() => setActiveToggle(!activeToggle)}
            className={`w-11 h-6 flex items-center rounded-full p-1 transition-colors duration-200 ease-in-out ${
              activeToggle ? 'bg-amber-500' : 'bg-neutral-800'
            }`}
          >
            <div className={`bg-neutral-950 w-4 h-4 rounded-full shadow-md transform transition-transform duration-200 ease-in-out ${
              activeToggle ? 'translate-x-5' : 'translate-x-0'
            }`} />
          </button>
        </div>
        <div>
          <h4 className="text-white text-sm font-semibold tracking-tight">Turbo Acceleration</h4>
          <p className="text-neutral-400 text-xs mt-1">Direct kernel bypass for sub-millisecond IO.</p>
        </div>
      </motion.div>

      {/* 3. Security Shield Card */}
      <motion.div 
        whileHover={{ y: -3 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="rounded-2xl bg-neutral-950/80 border border-white/[0.08] p-6 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] flex flex-col justify-between"
      >
        <div className="p-2 w-fit rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-400">
          <ShieldCheck className="w-4 h-4" />
        </div>
        <div>
          <div className="text-cyan-400 text-xs font-mono uppercase tracking-wider">Zero Trust Guard</div>
          <h4 className="text-white text-sm font-semibold tracking-tight mt-1">Enclave Isolation</h4>
          <p className="text-neutral-400 text-xs mt-1">Hardware encrypted memory pools.</p>
        </div>
      </motion.div>

      {/* 4. Terminal Command Card (Spans 2 cols) */}
      <motion.div 
        whileHover={{ y: -3 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="md:col-span-2 rounded-2xl bg-neutral-950/80 border border-white/[0.08] p-6 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] flex flex-col justify-between"
      >
        <div className="flex items-center gap-2 text-neutral-400 text-xs font-mono">
          <Terminal className="w-3.5 h-3.5 text-neutral-500" />
          <span>SESSION_DAEMON</span>
        </div>
        <div className="font-mono text-xs text-neutral-300 bg-black/60 rounded-xl p-3 border border-white/[0.04]">
          <span className="text-emerald-400">$</span> lumina pipeline --target=production --strict
          <div className="text-neutral-500 text-[11px] mt-1">✔ 0 lint errors, 142 tokens verified, chamfers active</div>
        </div>
        <div className="flex items-center justify-between text-xs text-neutral-400">
          <span>Latency: 4.2ms</span>
          <span className="text-white font-mono text-[11px]">STATUS: OK</span>
        </div>
      </motion.div>

    </div>
  );
}