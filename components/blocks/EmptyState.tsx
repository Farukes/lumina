import React from 'react';
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