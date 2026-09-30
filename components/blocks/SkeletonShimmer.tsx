import React from 'react';

export function SkeletonShimmer({ className = "h-6 w-full rounded-lg" }: { className?: string }) {
  return (
    <div 
      className={`relative overflow-hidden bg-neutral-900 border border-white/[0.04] ${className}`}
    >
      <div className="absolute inset-0 -translate-x-full animate-[shimmer_1.8s_infinite] bg-gradient-to-r from-transparent via-white/[0.06] to-transparent" />
    </div>
  );
}
