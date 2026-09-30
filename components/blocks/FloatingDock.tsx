import React, { useState } from 'react';
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