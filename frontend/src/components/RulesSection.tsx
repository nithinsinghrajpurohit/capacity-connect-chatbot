import React from 'react';
import { motion } from 'motion/react';
import {
  Compass,
  Calculator,
  Layers,
  BookOpen,
  ShieldCheck,
  FileText,
  ChevronRight,
  Sparkles,
} from 'lucide-react';

interface RulesSectionProps {
  onOpenRules: () => void;
  onOpenChat: () => void;
}

const HIGHLIGHT_RULES = [
  {
    icon: Compass,
    iconBg: 'bg-amber-500/10 text-amber-600 border-amber-200/60',
    title: '1. Mode-First Selection (Mandatory)',
    desc: 'Always select your learning mode (Math Solver, Learning Path, Flashcards, etc.) from the top toolbar before sending a message.',
    tag: 'Prerequisite',
  },
  {
    icon: Calculator,
    iconBg: 'bg-emerald-500/10 text-emerald-600 border-emerald-200/60',
    title: '2. Step-by-Step Derivation & Proofs',
    desc: 'Math and Code solutions provide numbered steps and substitution checks (LHS = RHS ✓) to teach reasoning mechanics.',
    tag: 'Step-by-Step',
  },
  {
    icon: Layers,
    iconBg: 'bg-blue-500/10 text-blue-600 border-blue-200/60',
    title: '3. 5-Phase Curriculum Progression',
    desc: 'Master topics through structured 5-phase roadmaps, milestone projects, and immediate kickoff drills sequentially.',
    tag: 'Curriculum',
  },
  {
    icon: BookOpen,
    iconBg: 'bg-purple-500/10 text-purple-600 border-purple-200/60',
    title: '4. Active Recall & Card Flipping',
    desc: 'In Flashcard mode, mentally retrieve answers before clicking to flip cards to solidify long-term retention.',
    tag: 'Active Recall',
  },
  {
    icon: ShieldCheck,
    iconBg: 'bg-rose-500/10 text-rose-600 border-rose-200/60',
    title: '5. Synthetic Clinical Data Only',
    desc: 'Never upload real patient information. Clinical and healthcare queries generate HIPAA-compliant synthetic EHR data.',
    tag: 'Privacy',
  },
  {
    icon: FileText,
    iconBg: 'bg-cyan-500/10 text-cyan-600 border-cyan-200/60',
    title: '6. Official Study Guide Exports',
    desc: 'Export high-yield printable PDF notes for comprehensive offline revision and independent mastery.',
    tag: 'Mastery',
  },
];

export const RulesSection: React.FC<RulesSectionProps> = ({ onOpenRules, onOpenChat }) => {
  return (
    <section className="w-full max-w-[1400px] mx-auto mt-12 mb-16 px-4 sm:px-6">
      <div className="rounded-[40px] bg-white border border-slate-200/70 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.04)] p-8 sm:p-12 md:p-16 relative overflow-hidden">
        {/* Subtle Background Glow */}
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-gradient-to-br from-blue-100/40 via-cyan-50/30 to-transparent rounded-full blur-3xl -z-10 pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-gradient-to-tr from-amber-100/30 via-slate-50/40 to-transparent rounded-full blur-2xl -z-10 pointer-events-none" />

        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10 pb-8 border-b border-slate-100">
          <div className="max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 border border-slate-200/80 text-[12px] font-semibold text-[#0a1b33] mb-4">
              <span>📜</span>
              <span>Platform Operating Standards</span>
            </div>
            <h2 className="font-display text-3xl sm:text-4xl font-bold tracking-tight text-[#0a1b33] leading-tight">
              Rules of Using Sastra AI Assistant
            </h2>
            <p className="mt-3 text-slate-500 text-sm sm:text-base leading-relaxed">
              To ensure optimal pedagogical learning, verified mathematical correctness, and strict data privacy, all learners are expected to follow these core operating guidelines.
            </p>
          </div>

          <div className="flex items-center gap-3 shrink-0">
            <button
              onClick={onOpenRules}
              className="bg-white hover:bg-slate-50 text-[#0a152d] border border-slate-200 px-5 py-3 rounded-full text-xs sm:text-sm font-semibold shadow-2xs hover:shadow-sm transition-all flex items-center gap-2 cursor-pointer"
            >
              <span>View Full Rules Handbook</span>
              <ChevronRight className="w-4 h-4 text-slate-400" />
            </button>

            <button
              onClick={onOpenChat}
              className="bg-[#0a152d] hover:bg-[#122347] text-white px-5 py-3 rounded-full text-xs sm:text-sm font-semibold shadow-sm hover:shadow-md transition-all flex items-center gap-2 cursor-pointer"
            >
              <span>Start Learning</span>
              <Sparkles className="w-4 h-4 text-cyan-400" />
            </button>
          </div>
        </div>

        {/* 6 Grid Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {HIGHLIGHT_RULES.map((rule, idx) => {
            const Icon = rule.icon;
            return (
              <motion.div
                key={idx}
                whileHover={{ y: -4 }}
                transition={{ duration: 0.2 }}
                onClick={onOpenRules}
                className="p-6 rounded-[24px] bg-slate-50/50 hover:bg-white border border-slate-200/70 hover:border-slate-300 shadow-2xs hover:shadow-md transition-all flex flex-col justify-between cursor-pointer group"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className={`w-10 h-10 rounded-xl border flex items-center justify-center ${rule.iconBg}`}>
                      <Icon className="w-5 h-5" />
                    </div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 bg-white px-2.5 py-1 rounded-full border border-slate-200/60">
                      {rule.tag}
                    </span>
                  </div>

                  <h3 className="font-display text-[15px] font-bold text-[#0a1b33] mb-2 group-hover:text-blue-600 transition-colors">
                    {rule.title}
                  </h3>

                  <p className="text-slate-500 text-xs sm:text-[13px] leading-relaxed">
                    {rule.desc}
                  </p>
                </div>

                <div className="mt-5 pt-3 border-t border-slate-200/50 flex items-center justify-between text-xs font-semibold text-blue-600">
                  <span>Click to view details</span>
                  <ChevronRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* Bottom Banner Notice */}
        <div className="mt-10 p-4 rounded-2xl bg-blue-50/60 border border-blue-200/60 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
          <div className="flex items-center gap-3">
            <span className="text-xl">💡</span>
            <p className="text-xs sm:text-sm text-blue-900 font-medium">
              Ready to chat? Remember to select your mode (e.g. Math Solver or Learning Path) on the top toolbar to begin.
            </p>
          </div>
          <button
            onClick={onOpenRules}
            className="text-xs font-bold text-blue-700 hover:text-blue-800 underline underline-offset-2 shrink-0 cursor-pointer"
          >
            Review all 6 rules ➔
          </button>
        </div>
      </div>
    </section>
  );
};

export default RulesSection;
