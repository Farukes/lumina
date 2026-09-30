import React, { useState, useEffect } from "react";
import { 
  Zap, Command, Activity, Cpu, TrendingUp, Volume2, 
  VolumeX, Play, Shield, Terminal, Search, Plus, Sparkles 
} from "lucide-react";

/**
 * KRONOS OS — Autonomous Agent Neural Control Plane
 * Built strictly adhering to the Lumina Premium Design System (Linear + Teenage Engineering tier).
 * 
 * Key Principles Enforced:
 * 1. Zero AI Slop: No generic purple/indigo gradients; obsidian depth (#09090b) with metallic chamfers.
 * 2. Asymmetric Living Bento: Dominant 60% Visual Anchor + Satellites + Micro-controls.
 * 3. 1px Chamfer Highlight: shadow-[inset_0_1px_0_0_rgba(255,255,255,0.08)] and border-white/[0.08].
 * 4. Micro-Typography: tracking-tight on headings, font-mono text-[10px] tracking-widest on metadata.
 * 5. Tactile Feedback: active:scale-[0.98] with spring physics.
 */

export function KronosDashboard() {
  const [tokensProcessed, setTokensProcessed] = useState(41289140);
  const [activeArchetype, setActiveArchetype] = useState<"linear" | "teenage" | "spatial" | "brutalist">("linear");
  const [turboMode, setTurboMode] = useState(true);
  const [harmonicFreq, setHarmonicFreq] = useState("1.42 GHz");

  // Telemetry stream tick
  useEffect(() => {
    const timer = setInterval(() => {
      setTokensProcessed(prev => prev + Math.floor(Math.random() * 320 + 120));
    }, 1500);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="min-h-screen bg-[#09090b] text-neutral-100 font-sans selection:bg-emerald-500/30 selection:text-white p-4 sm:p-8">
      
      {/* Ambient Radial Bloom */}
      <div className="fixed top-10 left-1/2 -translate-x-1/2 w-[650px] h-[320px] bg-emerald-500/10 blur-[130px] rounded-full pointer-events-none -z-10" />

      {/* Top Floating Glass Header */}
      <header className="max-w-7xl mx-auto mb-8">
        <div className="bg-[#121215]/80 backdrop-blur-xl border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] rounded-2xl p-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-emerald-500 flex items-center justify-center font-mono font-bold text-neutral-950 text-xs shadow-[0_0_20px_rgba(16,185,129,0.3)]">
              KR
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-sm tracking-tight text-white">KRONOS NEURAL</span>
                <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-white/[0.06] text-neutral-400 uppercase tracking-widest">
                  v2.4 Sovereign
                </span>
              </div>
              <p className="text-[11px] text-neutral-500 hidden sm:block">Autonomous Agent Control Plane</p>
            </div>
          </div>

          {/* Archetype Quick Switcher */}
          <div className="flex items-center gap-1 bg-black/40 border border-white/[0.06] p-1 rounded-xl text-xs font-mono">
            {(["linear", "teenage", "spatial", "brutalist"] as const).map(arch => (
              <button
                key={arch}
                onClick={() => setActiveArchetype(arch)}
                className={`px-3 py-1.5 rounded-lg capitalize transition-all active:scale-[0.98] ${
                  activeArchetype === arch 
                    ? "bg-white/15 text-white font-medium shadow-sm" 
                    : "text-neutral-400 hover:text-neutral-200"
                }`}
              >
                {arch}
              </button>
            ))}
          </div>

          {/* Micro Action Buttons */}
          <div className="flex items-center gap-2">
            <button className="flex items-center gap-2 px-3 py-1.5 rounded-xl border border-white/[0.08] bg-white/[0.03] text-xs font-mono text-neutral-400 hover:text-white hover:border-white/20 active:scale-[0.98] transition-all">
              <Command className="w-3.5 h-3.5" />
              <span>Cmd+K</span>
              <kbd className="text-[10px] bg-white/10 px-1 py-0.5 rounded">⌘K</kbd>
            </button>
          </div>
        </div>
      </header>

      {/* Asymmetric Bento Grid Architecture */}
      <main className="max-w-7xl mx-auto grid grid-cols-12 gap-6">

        {/* 1. DOMINANT VISUAL ANCHOR (60% Weight): col-span-12 lg:col-span-8 */}
        <section className="col-span-12 lg:col-span-8 bg-[#121215] border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] rounded-3xl p-6 relative overflow-hidden flex flex-col justify-between">
          <div className="flex items-center justify-between pb-4 border-b border-white/[0.06]">
            <div>
              <span className="font-mono text-[10px] uppercase tracking-widest text-emerald-400">
                Visual Anchor // 60% Weight
              </span>
              <h2 className="text-2xl font-bold tracking-tight text-white mt-1">
                Vector Inference Field Simulation
              </h2>
            </div>
            <div className="flex items-center gap-2 font-mono text-xs">
              <span className="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
              <span className="text-neutral-300">2,840 tokens/s</span>
            </div>
          </div>

          {/* Living Canvas / Graphical Preview Simulator */}
          <div className="relative my-6 rounded-2xl bg-black/60 border border-white/[0.06] aspect-[16/9] flex items-center justify-center overflow-hidden">
            <div className="absolute inset-0 bg-[radial-gradient(#10b981_1px,transparent_1px)] [background-size:20px_20px] opacity-25" />
            <div className="text-center z-10 space-y-2">
              <Activity className="w-10 h-10 text-emerald-400 mx-auto animate-pulse" />
              <p className="font-mono text-xs text-neutral-400 tracking-wider">60FPS TENSOR MESH COMPUTATION ACTIVE</p>
              <div className="font-mono text-xs text-neutral-500">Latency: 9.4ms • FP8 TensorCore • Loss: 0.0014</div>
            </div>
          </div>

          <div className="flex items-center justify-between pt-4 border-t border-white/[0.06] font-mono text-xs">
            <span className="text-neutral-500">Hover over field to perturb vector tensors.</span>
            <button className="bg-white hover:bg-neutral-100 text-neutral-950 font-semibold px-4 py-2 rounded-xl active:scale-[0.98] transition-all shadow-[0_1px_2px_rgba(0,0,0,0.2)]">
              Dispatch Agent Job
            </button>
          </div>
        </section>

        {/* 2. SATELLITE TELEMETRY CARD: col-span-12 sm:col-span-6 lg:col-span-4 */}
        <section className="col-span-12 sm:col-span-6 lg:col-span-4 bg-[#121215] border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] rounded-3xl p-6 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-3 border-b border-white/[0.06]">
              <span className="font-mono text-[10px] uppercase tracking-widest text-neutral-400">Context Satellite 01</span>
              <Cpu className="w-4 h-4 text-neutral-500" />
            </div>

            <div className="mt-4">
              <span className="font-mono text-xs text-neutral-400 uppercase tracking-wider">Cumulative Ingestion</span>
              <h3 className="text-4xl font-extrabold font-mono tracking-tight text-white mt-1">
                {tokensProcessed.toLocaleString()}
              </h3>
              <div className="flex items-center gap-1.5 mt-2 font-mono text-xs text-emerald-400">
                <TrendingUp className="w-3.5 h-3.5" />
                <span>+18.4% vs previous cycle</span>
              </div>
            </div>

            {/* Sparkline Visual */}
            <div className="mt-6 p-3 rounded-xl bg-white/[0.02] border border-white/[0.06]">
              <div className="flex items-center justify-between font-mono text-[10px] text-neutral-500 mb-2">
                <span>INFERENCE PEAK</span>
                <span className="text-emerald-400">3.8K/S</span>
              </div>
              <div className="h-10 w-full bg-gradient-to-t from-emerald-500/10 to-transparent border-b border-emerald-500/40 rounded flex items-end">
                <div className="w-full h-1 bg-emerald-400 rounded-full" />
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-white/[0.06] font-mono text-xs space-y-2">
            <div className="flex justify-between text-neutral-400">
              <span>Cluster State</span>
              <span className="text-emerald-400 font-bold">100% OPERATIONAL</span>
            </div>
          </div>
        </section>

        {/* 3. HARDWARE MICRO-CONTROLS (Teenage Engineering Tier): col-span-12 sm:col-span-6 lg:col-span-4 */}
        <section className="col-span-12 sm:col-span-6 lg:col-span-4 bg-[#121215] border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] rounded-3xl p-6 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-3 border-b border-white/[0.06]">
              <span className="font-mono text-[10px] uppercase tracking-widest text-neutral-400">Tactile Micro-Control</span>
              <span className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">
                HAPTIC READY
              </span>
            </div>

            <h3 className="text-lg font-bold tracking-tight text-white mt-3">Synthesizer Relay Matrix</h3>
            <p className="text-xs text-neutral-400 font-mono mt-1">Mechanical toggles with Web Audio click synthesis.</p>

            {/* Turbo Toggle */}
            <div className="mt-6 flex items-center justify-between p-3.5 rounded-xl bg-white/[0.02] border border-white/[0.06]">
              <div>
                <div className="text-xs font-bold text-white">Turbo Concurrency</div>
                <div className="text-[11px] font-mono text-neutral-500">Uncapped speculative execution</div>
              </div>
              <button
                onClick={() => setTurboMode(!turboMode)}
                className={`w-12 h-6 flex items-center rounded-full p-1 transition-colors duration-200 active:scale-[0.98] ${
                  turboMode ? "bg-emerald-500" : "bg-neutral-800"
                }`}
              >
                <div className={`w-4 h-4 rounded-full bg-neutral-950 shadow-md transform transition-transform duration-200 ${
                  turboMode ? "translate-x-6" : "translate-x-0"
                }`} />
              </button>
            </div>
          </div>

          <div className="pt-4 border-t border-white/[0.06] flex items-center justify-between font-mono text-xs text-neutral-400">
            <span>Harmonic Bias: {harmonicFreq}</span>
            <button className="px-2.5 py-1 rounded-lg border border-white/10 hover:bg-white/5 active:scale-[0.98]">
              Test Click
            </button>
          </div>
        </section>

        {/* 4. SUBAGENT QUEUE TABLE: col-span-12 lg:col-span-8 */}
        <section className="col-span-12 lg:col-span-8 bg-[#121215] border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] rounded-3xl p-6">
          <div className="flex items-center justify-between pb-4 border-b border-white/[0.06]">
            <div>
              <span className="font-mono text-[10px] uppercase tracking-widest text-neutral-400">Subagent Fleet Queue</span>
              <h3 className="text-lg font-bold tracking-tight text-white mt-1">Active Neural Threads</h3>
            </div>
            <button className="px-3 py-1.5 rounded-xl border border-white/10 hover:bg-white/5 font-mono text-xs text-white active:scale-[0.98] transition-all flex items-center gap-1.5">
              <Plus className="w-3.5 h-3.5" /> Spawn Worker
            </button>
          </div>

          <div className="mt-4 divide-y divide-white/[0.04] font-mono text-xs">
            {[
              { id: "agent-01", role: "Research Architect", model: "Gemini 2.5 Pro", status: "EXECUTING", color: "emerald" },
              { id: "agent-02", role: "Style AST Polisher", model: "Claude 3.7 Sonnet", status: "IDLE WAITING", color: "amber" },
              { id: "agent-03", role: "Vector Synthesizer", model: "Claude 3.5 Haiku", status: "STREAMING", color: "sky" }
            ].map((ag) => (
              <div key={ag.id} className="py-3 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <span className={`w-2 h-2 rounded-full bg-${ag.color}-400`} />
                  <div>
                    <span className="text-white font-medium">{ag.id} // {ag.role}</span>
                    <span className="text-[10px] text-neutral-500 ml-2">[{ag.model}]</span>
                  </div>
                </div>
                <span className="px-2 py-0.5 rounded bg-white/[0.04] border border-white/[0.08] text-[10px] text-neutral-300">
                  {ag.status}
                </span>
              </div>
            ))}
          </div>
        </section>

      </main>

    </div>
  );
}