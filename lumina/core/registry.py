"""
Lumina AAA Component Registry - Handcrafted World-Class Blocks
"""
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ComponentItem:
    id: str
    name: str
    category: str
    description: str
    dependencies: List[str]
    filename: str
    code: str

COMPONENTS: Dict[str, ComponentItem] = {
    "bento-grid": ComponentItem(
        id="bento-grid",
        name="Asymmetric Bento Grid",
        category="Layout & Showcase",
        description="Linear-style asymmetric Bento Grid featuring live metrics, sparklines, chamfers, and interactive toggles.",
        dependencies=["lucide-react", "framer-motion", "clsx", "tailwind-merge"],
        filename="components/blocks/BentoGrid.tsx",
        code="""import React, { useState } from 'react';
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
"""
    ),

    "command-bar": ComponentItem(
        id="command-bar",
        name="Tactile Command Palette (Cmd+K)",
        category="Navigation & Overlay",
        description="Raycast-inspired fast keyboard command bar with search, group filters, and audio feedback.",
        dependencies=["lucide-react", "framer-motion"],
        filename="components/blocks/CommandBar.tsx",
        code="""import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sparkles, Terminal, FileCode, Sliders, ArrowRight, CornerDownLeft } from 'lucide-react';

export function CommandBar() {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setIsOpen((prev) => !prev);
      }
      if (e.key === 'Escape') {
        setIsOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const commands = [
    { id: '1', title: 'Switch Theme to Obsidian Linear', category: 'Themes', icon: Sparkles, shortcut: '⌘1' },
    { id: '2', title: 'Audit Current Workspace for AI Slop', category: 'Lumina Engine', icon: Terminal, shortcut: '⌘A' },
    { id: '3', title: 'Inject Dynamic Bento Grid Block', category: 'Components', icon: FileCode, shortcut: '⌘B' },
    { id: '4', title: 'Configure OKLCH Color Space & Chamfers', category: 'Preferences', icon: Sliders, shortcut: '⌘,' },
  ];

  const filtered = commands.filter(c => c.title.toLowerCase().includes(query.toLowerCase()));

  return (
    <>
      {/* Trigger Button */}
      <button 
        onClick={() => setIsOpen(true)}
        className="inline-flex items-center gap-3 px-4 py-2 rounded-xl bg-neutral-900 border border-white/[0.08] text-neutral-400 hover:text-white hover:border-white/20 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] transition-all active:scale-[0.98]"
      >
        <Search className="w-4 h-4 text-neutral-400" />
        <span className="text-sm">Search commands & components...</span>
        <kbd className="ml-4 px-2 py-0.5 text-[11px] font-mono rounded bg-white/[0.06] border border-white/[0.1] text-neutral-300">
          ⌘K
        </kbd>
      </button>

      {/* Modal Dialog */}
      <AnimatePresence>
        {isOpen && (
          <div className="fixed inset-0 z-50 flex items-start justify-center pt-24 px-4 bg-black/70 backdrop-blur-md">
            <motion.div 
              initial={{ opacity: 0, scale: 0.95, y: -10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: -10 }}
              transition={{ type: "spring", stiffness: 450, damping: 30 }}
              className="w-full max-w-xl rounded-2xl bg-neutral-950 border border-white/[0.12] shadow-2xl overflow-hidden"
            >
              {/* Search Header */}
              <div className="flex items-center px-4 py-3.5 border-b border-white/[0.08] gap-3">
                <Search className="w-5 h-5 text-neutral-500" />
                <input 
                  type="text"
                  autoFocus
                  placeholder="Type a command or search..."
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  className="w-full bg-transparent text-white text-sm focus:outline-none placeholder-neutral-500"
                />
                <button 
                  onClick={() => setIsOpen(false)}
                  className="text-xs font-mono text-neutral-500 hover:text-white px-1.5 py-0.5 rounded border border-white/[0.08]"
                >
                  ESC
                </button>
              </div>

              {/* Command List */}
              <div className="p-2 max-h-80 overflow-y-auto space-y-1">
                {filtered.map((item) => {
                  const Icon = item.icon;
                  return (
                    <button
                      key={item.id}
                      onClick={() => {
                        alert(`Executed: ${item.title}`);
                        setIsOpen(false);
                      }}
                      className="w-full flex items-center justify-between px-3 py-2.5 rounded-xl hover:bg-white/[0.06] text-neutral-300 hover:text-white group transition-colors text-left"
                    >
                      <div className="flex items-center gap-3">
                        <div className="p-1.5 rounded-lg bg-white/[0.04] border border-white/[0.06] text-neutral-400 group-hover:text-emerald-400">
                          <Icon className="w-4 h-4" />
                        </div>
                        <div>
                          <div className="text-sm font-medium">{item.title}</div>
                          <div className="text-[11px] text-neutral-500">{item.category}</div>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <kbd className="px-1.5 py-0.5 text-[10px] font-mono text-neutral-500 group-hover:text-neutral-300 bg-white/[0.03] border border-white/[0.06] rounded">
                          {item.shortcut}
                        </kbd>
                        <CornerDownLeft className="w-3.5 h-3.5 text-neutral-500 opacity-0 group-hover:opacity-100 transition-opacity" />
                      </div>
                    </button>
                  );
                })}
              </div>

              {/* Footer */}
              <div className="px-4 py-2.5 bg-neutral-900/50 border-t border-white/[0.06] flex items-center justify-between text-[11px] text-neutral-500 font-mono">
                <span>Navigation: ↑ ↓</span>
                <span>Select: ↵</span>
                <span>Close: Esc</span>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </>
  );
}
"""
    ),

    "floating-dock": ComponentItem(
        id="floating-dock",
        name="Dynamic Island Floating Dock",
        category="Navigation",
        description="iOS Dynamic Island / macOS style floating navigation with spring-morphing active indicators.",
        dependencies=["lucide-react", "framer-motion"],
        filename="components/blocks/FloatingDock.tsx",
        code="""import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Home, Layers, Sparkles, Terminal, Settings } from 'lucide-react';

export function FloatingDock() {
  const [activeTab, setActiveTab] = useState('home');

  const navItems = [
    { id: 'home', label: 'Overview', icon: Home },
    { id: 'layers', label: 'Components', icon: Layers },
    { id: 'sparkles', label: 'Themes', icon: Sparkles },
    { id: 'terminal', label: 'Audit', icon: Terminal },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  return (
    <div className="fixed bottom-6 inset-x-0 flex justify-center z-40 pointer-events-none">
      <motion.nav 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ type: "spring", stiffness: 400, damping: 30 }}
        className="pointer-events-auto flex items-center gap-1 p-2 rounded-2xl bg-neutral-950/80 backdrop-blur-xl border border-white/[0.1] shadow-[0_8px_32px_rgba(0,0,0,0.5),inset_0_1px_0_0_rgba(255,255,255,0.08)]"
      >
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;

          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className="relative px-3.5 py-2 rounded-xl text-xs font-medium transition-colors duration-200 active:scale-95"
            >
              {isActive && (
                <motion.div 
                  layoutId="activeDockPill"
                  transition={{ type: "spring", stiffness: 500, damping: 35 }}
                  className="absolute inset-0 bg-white/[0.1] border border-white/[0.15] rounded-xl shadow-[inset_0_1px_0_0_rgba(255,255,255,0.1)]"
                />
              )}
              <div className={`relative z-10 flex items-center gap-2 ${isActive ? 'text-white' : 'text-neutral-400 hover:text-neutral-200'}`}>
                <Icon className="w-4 h-4" />
                <span>{item.label}</span>
              </div>
            </button>
          );
        })}
      </motion.nav>
    </div>
  );
}
"""
    ),

    "glow-hero": ComponentItem(
        id="glow-hero",
        name="Ambient Glow Hero",
        category="Hero Section",
        description="Showcase hero section with diffused radial mesh glow, chamfered window, and zero AI-slop.",
        dependencies=["lucide-react", "framer-motion"],
        filename="components/blocks/GlowHero.tsx",
        code="""import React from 'react';
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
"""
    ),

    "magnetic-button": ComponentItem(
        id="magnetic-button",
        name="Tactile Magnetic Button",
        category="Buttons & Inputs",
        description="Button with spring active-scale, animated rotating border beam, and tactile mouse follow.",
        dependencies=["framer-motion"],
        filename="components/blocks/MagneticButton.tsx",
        code="""import React from 'react';
import { motion } from 'framer-motion';

export function MagneticButton({ children = "Get Started", onClick }: { children?: React.ReactNode, onClick?: () => void }) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.97 }}
      transition={{ type: "spring", stiffness: 450, damping: 25 }}
      onClick={onClick}
      className="relative group p-[1px] rounded-xl overflow-hidden focus:outline-none"
    >
      {/* Animated Border Beam */}
      <span className="absolute inset-[-1000%] animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#000000_0%,#10b981_50%,#000000_100%)] opacity-80 group-hover:opacity-100 transition-opacity" />

      {/* Inner Button Body */}
      <span className="relative z-10 block px-6 py-3 rounded-[11px] bg-neutral-950 font-medium text-sm text-neutral-100 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.15)] group-hover:text-white transition-colors">
        {children}
      </span>
    </motion.button>
  );
}
"""
    ),

    "stat-cards": ComponentItem(
        id="stat-cards",
        name="High-Density Stat Cards",
        category="Data Display",
        description="Metric cards featuring sparklines, live delta indicators, and metallic chamfers.",
        dependencies=["lucide-react"],
        filename="components/blocks/StatCards.tsx",
        code="""import React from 'react';
import { TrendingUp, Users, DollarSign, Cpu } from 'lucide-react';

export function StatCards() {
  const stats = [
    { title: 'Total Volume', value: '$84,230', delta: '+12.4%', icon: DollarSign, positive: true },
    { title: 'Active Agents', value: '1,429', delta: '+28.1%', icon: Cpu, positive: true },
    { title: 'Subscribed Devs', value: '4,892', delta: '+8.3%', icon: Users, positive: true },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-5xl mx-auto p-4">
      {stats.map((stat, idx) => {
        const Icon = stat.icon;
        return (
          <div 
            key={idx}
            className="rounded-2xl bg-neutral-950/80 border border-white/[0.08] p-5 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] relative overflow-hidden group hover:border-white/[0.15] transition-all"
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono text-neutral-400 tracking-wider uppercase">{stat.title}</span>
              <div className="p-2 rounded-lg bg-white/[0.04] border border-white/[0.06] text-neutral-400 group-hover:text-white">
                <Icon className="w-4 h-4" />
              </div>
            </div>
            
            <div className="mt-4 flex items-baseline justify-between">
              <div className="text-3xl font-bold tracking-tight text-white">{stat.value}</div>
              <div className="text-xs font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full flex items-center gap-1">
                <TrendingUp className="w-3 h-3" />
                {stat.delta}
              </div>
            </div>

            {/* Sparkline Decorative Bar */}
            <div className="mt-4 h-1 w-full bg-neutral-900 rounded-full overflow-hidden">
              <div className="h-full bg-emerald-500 rounded-full w-2/3" />
            </div>
          </div>
        );
      })}
    </div>
  );
}
"""
    ),

    "skeleton-shimmer": ComponentItem(
        id="skeleton-shimmer",
        name="Ray Shimmer Skeleton",
        category="Feedback & Loading",
        description="Luxury loading state with smooth diagonal light ray shimmer rather than cheap pulsing gray.",
        dependencies=[],
        filename="components/blocks/SkeletonShimmer.tsx",
        code="""import React from 'react';

export function SkeletonShimmer({ className = "h-6 w-full rounded-lg" }: { className?: string }) {
  return (
    <div 
      className={`relative overflow-hidden bg-neutral-900 border border-white/[0.04] ${className}`}
    >
      <div className="absolute inset-0 -translate-x-full animate-[shimmer_1.8s_infinite] bg-gradient-to-r from-transparent via-white/[0.06] to-transparent" />
    </div>
  );
}
"""
    ),

    "empty-state": ComponentItem(
        id="empty-state",
        name="Tactile Empty State",
        category="Feedback & Loading",
        description="Engaging empty state with dashed chamfer border, interactive trigger, and keyboard shortcut hint.",
        dependencies=["lucide-react"],
        filename="components/blocks/EmptyState.tsx",
        code="""import React from 'react';
import { Plus, FolderDashed } from 'lucide-react';

export function EmptyState({ onAction }: { onAction?: () => void }) {
  return (
    <div className="w-full max-w-lg mx-auto p-8 rounded-2xl border border-dashed border-white/[0.12] bg-neutral-950/40 text-center flex flex-col items-center justify-center">
      <div className="w-12 h-12 rounded-2xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-center text-neutral-400 mb-4 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]">
        <FolderDashed className="w-6 h-6" />
      </div>
      <h3 className="text-white text-base font-semibold tracking-tight">No active deployments found</h3>
      <p className="text-neutral-400 text-xs mt-1 max-w-xs">
        Connect your repository or dispatch a new container instance to initialize telemetry.
      </p>
      <button 
        onClick={onAction}
        className="mt-6 px-4 py-2 rounded-xl bg-white hover:bg-neutral-100 text-neutral-950 font-medium text-xs shadow-sm active:scale-[0.98] transition-all inline-flex items-center gap-2"
      >
        <Plus className="w-3.5 h-3.5" />
        <span>Deploy Pipeline</span>
        <kbd className="ml-1 text-[10px] font-mono px-1.5 py-0.5 rounded bg-black/10">⌘N</kbd>
      </button>
    </div>
  );
}
"""
    )
}
