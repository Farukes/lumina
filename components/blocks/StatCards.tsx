import React from 'react';
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