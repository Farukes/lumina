"""
Lumina Visual & Interaction Primitives
Atomic, lightweight mathematical building blocks and micro-interactions.
These primitives preserve AI creativity by acting as un-opinionated visual effects
that can be injected into any custom component.
"""

from typing import Dict, Any

PRIMITIVES: Dict[str, Dict[str, Any]] = {
    "border-beam": {
        "name": "Border Beam (Conic Laser Highlight)",
        "description": "An animated perimeter laser that travels along the card border using pure CSS mask-composite and conic gradients.",
        "category": "Visual Effect",
        "dependencies": ["lucide-react"],
        "snippet": """
// Border Beam Primitive (Pure CSS & Tailwind)
export function BorderBeam({
  size = 200,
  duration = 12,
  anchor = 90,
  borderWidth = 1.5,
  colorFrom = "#ffaa40",
  colorTo = "#9c40ff",
  delay = 0,
  className = "",
}: {
  size?: number;
  duration?: number;
  anchor?: number;
  borderWidth?: number;
  colorFrom?: string;
  colorTo?: string;
  delay?: number;
  className?: string;
}) {
  return (
    <div
      style={
        {
          "--size": `${size}px`,
          "--duration": `${duration}s`,
          "--anchor": `${anchor}%`,
          "--border-width": `${borderWidth}px`,
          "--color-from": colorFrom,
          "--color-to": colorTo,
          "--delay": `-${delay}s`,
        } as React.CSSProperties
      }
      className={`pointer-events-none absolute inset-0 rounded-[inherit] [border:calc(var(--border-width)*1px)_solid_transparent] ![mask-clip:padding-box,border-box] ![mask-composite:intersect] [mask:linear-gradient(transparent,transparent),linear-gradient(white,white)] after:absolute after:aspect-square after:w-[calc(var(--size)*1px)] after:animate-border-beam after:[animation-delay:var(--delay)] after:[background:linear-gradient(to_left,var(--color-from),var(--color-to),transparent)] after:[offset-anchor:calc(var(--anchor)*1%)_50%] after:[offset-path:rect(0_auto_auto_0_round_calc(var(--size)*1px))] ${className}`}
    />
  );
}
"""
    },

    "spotlight-cone": {
        "name": "Spotlight Cone (Cursor Follow Light)",
        "description": "A dynamic radial gradient spotlight that follows mouse movement with silky damping to illuminate card textures.",
        "category": "Lighting Effect",
        "dependencies": ["framer-motion"],
        "snippet": """
// Spotlight Cone Primitive
import React, { useRef, useState, useCallback } from "react";

export function SpotlightCard({
  children,
  className = "",
  spotlightColor = "rgba(255, 255, 255, 0.08)",
}: {
  children: React.ReactNode;
  className?: string;
  spotlightColor?: string;
}) {
  const divRef = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [opacity, setOpacity] = useState(0);

  const handleMouseMove = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
    if (!divRef.current) return;
    const rect = divRef.current.getBoundingClientRect();
    setPosition({ x: e.clientX - rect.left, y: e.clientY - rect.top });
  }, []);

  return (
    <div
      ref={divRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)}
      onMouseLeave={() => setOpacity(0)}
      className={`relative overflow-hidden rounded-2xl border border-white/[0.08] bg-zinc-950 p-6 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)] ${className}`}
    >
      <div
        className="pointer-events-none absolute -inset-px transition-opacity duration-300"
        style={{
          opacity,
          background: `radial-gradient(600px circle at ${position.x}px ${position.y}px, ${spotlightColor}, transparent 40%)`,
        }}
      />
      <div className="relative z-10">{children}</div>
    </div>
  );
}
"""
    },

    "3d-tilt": {
        "name": "3D Perspective Tilt",
        "description": "Mathematical 3D tilt with spring damping that rotates elements based on cursor distance from center.",
        "category": "Physical Interaction",
        "dependencies": ["framer-motion"],
        "snippet": """
// 3D Perspective Spring Tilt
import React, { useRef } from "react";
import { motion, useMotionValue, useSpring, useTransform } from "framer-motion";

export function TiltCard({
  children,
  className = "",
  maxTilt = 12,
}: {
  children: React.ReactNode;
  className?: string;
  maxTilt?: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  const mouseXSpring = useSpring(x, { stiffness: 300, damping: 30 });
  const mouseYSpring = useSpring(y, { stiffness: 300, damping: 30 });

  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], [maxTilt, -maxTilt]);
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], [-maxTilt, maxTilt]);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    x.set(mouseX / width - 0.5);
    y.set(mouseY / height - 0.5);
  };

  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      style={{
        rotateY,
        rotateX,
        transformStyle: "preserve-3d",
      }}
      className={`relative transform-gpu transition-shadow duration-300 ${className}`}
    >
      <div style={{ transform: "translateZ(30px)" }}>
        {children}
      </div>
    </motion.div>
  );
}
"""
    },

    "text-scramble": {
        "name": "Text Scramble (Terminal Monospace Cipher)",
        "description": "Matrix/Cyber cipher text animation that scrambles characters before settling into the final word on hover or state change.",
        "category": "Micro-Typography",
        "dependencies": [],
        "snippet": """
// Text Scramble Cipher Primitive
import React, { useState, useEffect, useRef } from "react";

const CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";

export function TextScramble({
  text,
  speed = 30,
  triggerOnHover = true,
  className = "",
}: {
  text: string;
  speed?: number;
  triggerOnHover?: boolean;
  className?: string;
}) {
  const [display, setDisplay] = useState(text);
  const animating = useRef(false);

  const scramble = () => {
    if (animating.current) return;
    animating.current = true;
    let iteration = 0;
    const interval = setInterval(() => {
      setDisplay(
        text
          .split("")
          .map((char, index) => {
            if (char === " ") return " ";
            if (index < iteration) return text[index];
            return CHARS[Math.floor(Math.random() * CHARS.length)];
          })
          .join("")
      );

      if (iteration >= text.length) {
        clearInterval(interval);
        animating.current = false;
      }
      iteration += 1 / 3;
    }, speed);
  };

  useEffect(() => {
    scramble();
  }, [text]);

  return (
    <span
      onMouseEnter={triggerOnHover ? scramble : undefined}
      className={`font-mono inline-block cursor-default ${className}`}
    >
      {display}
    </span>
  );
}
"""
    },

    "web-audio-haptic": {
        "name": "Web Audio Haptics (Zero-Dependency Synthetic Clicker)",
        "description": "Ultra-lightweight Web Audio synthesizer generating subtle mechanical switch clicks, pops, and ticks without requiring MP3 assets.",
        "category": "Sensory Feedback",
        "dependencies": [],
        "snippet": """
// Web Audio Synthetic Haptic Clicker (Zero-Dependency)
class SoundFx {
  private ctx: AudioContext | null = null;

  private getContext(): AudioContext {
    if (!this.ctx && typeof window !== "undefined") {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume();
    }
    return this.ctx!;
  }

  // Linear / Raycast crisp switch snap
  public click(freq = 1200) {
    try {
      const ctx = this.getContext();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(100, ctx.currentTime + 0.04);

      gain.gain.setValueAtTime(0.08, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.04);
    } catch {
      // Audio context blocked or unsupported
    }
  }

  // Soft mechanical keyboard thock
  public thock() {
    this.click(450);
  }

  // Modern pop confirmation
  public pop() {
    try {
      const ctx = this.getContext();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "triangle";
      osc.frequency.setValueAtTime(280, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(840, ctx.currentTime + 0.08);

      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.08);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.08);
    } catch {}
  }
}

export const hapticSound = new SoundFx();
"""
    }
}
