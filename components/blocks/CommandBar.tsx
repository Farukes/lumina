import React, { useState, useEffect } from 'react';
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
