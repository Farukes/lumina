import React from 'react';
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
