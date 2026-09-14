import React from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  X,
  ShieldCheck,
  Calculator,
  Compass,
  Layers,
  BookOpen,
  FileText,
  CheckCircle2,
  Sparkles,
  ArrowRight,
} from 'lucide-react';

interface RulesModalProps {
  isOpen: boolean;
  onClose: () => void;
  onOpenChat: () => void;
}

const RULES = [
  {
    id: 1,
    badge: 'Mandatory Prerequisite',
    badgeColor: 'bg-amber-50 text-amber-700 border-amber-200',
    icon: Compass,
    iconBg: 'bg-amber-500/10 text-amber-600',
    title: '1. Mode-First Interaction Principle',
    desc: 'You must select an active learning mode from the top toolbar (e.g. Math Solver, Learning Path, Flashcards, Deep Explanation, Quiz) before chatting. This primes Sastra’s pedagogical reasoning pipeline with the exact curriculum rules for your task.',
    ruleItem: 'Always pick your mode first before submitting inquiries.',
  },
  {
    id: 2,
    badge: 'Step-by-Step Logic',
    badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    icon: Calculator,
    iconBg: 'bg-emerald-500/10 text-emerald-600',
    title: '2. Mathematical Derivations & Verified Proofs',
    desc: 'In Math Solver mode, every solution includes numbered derivations (✦ Step 1, Step 2...), governing formulas, prominent final answers, and a substitution check (LHS = RHS ✓). Review the entire derivation to master the underlying logic.',
    ruleItem: 'Study the full derivation and verification proof rather than copying raw answers.',
  },
  {
    id: 3,
    badge: 'Progressive Learning',
    badgeColor: 'bg-blue-50 text-blue-700 border-blue-200',
    icon: Layers,
    iconBg: 'bg-blue-500/10 text-blue-600',
    title: '3. 5-Phase Sequential Curriculum Progression',
    desc: 'Learning Paths provide a 5-column roadmap table and 5 progressive phases (Foundations ➔ Architecture ➔ Systems ➔ Resilience ➔ Capstone). Complete hands-on milestone projects and kickoff drills sequentially.',
    ruleItem: 'Complete early phases and practice drills before jumping to advanced capstones.',
  },
  {
    id: 4,
    badge: 'Active Recall',
    badgeColor: 'bg-purple-50 text-purple-700 border-purple-200',
    icon: BookOpen,
    iconBg: 'bg-purple-500/10 text-purple-600',
    title: '4. Active Recall & Self-Testing Integrity',
    desc: 'When using Flashcards (interactive click-to-flip) or Quiz mode, attempt to recall or select the answer aloud before viewing reverse explanations. Honest self-testing solidifies long-term memory retention.',
    ruleItem: 'Attempt memory retrieval before clicking to reveal flashcard answers.',
  },
  {
    id: 5,
    badge: 'Privacy & Compliance',
    badgeColor: 'bg-rose-50 text-rose-700 border-rose-200',
    icon: ShieldCheck,
    iconBg: 'bg-rose-500/10 text-rose-600',
    title: '5. Patient Data Privacy & Synthetic EHR Standards',
    desc: 'Never input confidential credentials or real Protected Health Information (PHI). Visual and table dataset queries generate normalized, synthetic EHR records adhering strictly to HIPAA Safe Harbor de-identification.',
    ruleItem: 'Strictly prohibit real personal or clinical health data uploads.',
  },
  {
    id: 6,
    badge: 'Academic Mastery',
    badgeColor: 'bg-cyan-50 text-cyan-700 border-cyan-200',
    icon: FileText,
    iconBg: 'bg-cyan-500/10 text-cyan-600',
    title: '6. Academic Integrity & Study Guide Exports',
    desc: 'Sastra AI is an instructional mentor designed to develop critical problem-solving skills. Export printable PDF notes and study guides for offline retention and revision.',
    ruleItem: 'Utilize printable PDF notes for structured offline mastery and revision.',
  },
];

export const RulesModal: React.FC<RulesModalProps> = ({ isOpen, onClose, onOpenChat }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 md:p-6 select-text">
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-slate-900/60 backdrop-blur-md transition-opacity"
          />

          {/* Modal Container */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 16 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 16 }}
            transition={{ type: 'spring', damping: 28, stiffness: 350 }}
            className="relative w-full max-w-4xl max-h-[90vh] bg-white rounded-[32px] border border-slate-200 shadow-2xl overflow-hidden flex flex-col z-10"
          >
            {/* Header */}
            <div className="px-6 sm:px-8 pt-6 pb-5 border-b border-slate-100 flex items-start justify-between bg-gradient-to-r from-slate-50/80 via-white to-blue-50/30">
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-2xl bg-[#0a152d] text-white flex items-center justify-center text-xl shrink-0 shadow-md border border-slate-700/50">
                  📜
                </div>
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <h2 className="font-display text-xl sm:text-2xl font-bold text-[#0a1b33]">
                      Sastra AI — Operating Rules &amp; Guidelines
                    </h2>
                    <span className="hidden sm:inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-cyan-50 text-cyan-700 border border-cyan-200">
                      Official Standards
                    </span>
                  </div>
                  <p className="text-slate-500 text-xs sm:text-sm leading-relaxed">
                    Please review the core operating rules and prerequisites for interacting with the Sastra AI Learning Operating System.
                  </p>
                </div>
              </div>

              <button
                onClick={onClose}
                className="p-2 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors cursor-pointer shrink-0 ml-2"
                title="Close rules"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Scrollable Rules List */}
            <div className="flex-1 overflow-y-auto px-6 sm:px-8 py-6 space-y-4 bg-slate-50/40">
              {/* Important Banner */}
              <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-300/60 flex items-start gap-3">
                <span className="text-xl">⚠️</span>
                <div className="text-xs sm:text-sm text-amber-900 leading-relaxed">
                  <strong className="font-semibold text-amber-950">Important Notice:</strong> First select your preferred mode on the chatbot toolbar (Math Solver, Learning Path, Flashcards, Deep Explanation, etc.) before chatting. Unselected sessions are paused until a mode is picked.
                </div>
              </div>

              {/* 6 Core Rules Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {RULES.map((rule) => {
                  const Icon = rule.icon;
                  return (
                    <div
                      key={rule.id}
                      className="p-5 rounded-2xl bg-white border border-slate-200/80 shadow-xs hover:shadow-md hover:border-slate-300 transition-all flex flex-col justify-between"
                    >
                      <div>
                        <div className="flex items-center justify-between mb-3">
                          <span
                            className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full border ${rule.badgeColor}`}
                          >
                            {rule.badge}
                          </span>
                          <div className={`p-2 rounded-xl ${rule.iconBg}`}>
                            <Icon className="w-4 h-4" />
                          </div>
                        </div>
                        <h3 className="font-display text-[15px] font-bold text-[#0a1b33] mb-1.5">
                          {rule.title}
                        </h3>
                        <p className="text-slate-600 text-xs leading-relaxed mb-3">
                          {rule.desc}
                        </p>
                      </div>

                      <div className="pt-2 border-t border-slate-100 flex items-center gap-1.5 text-[11px] font-medium text-slate-500">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                        <span className="truncate">{rule.ruleItem}</span>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Modal Footer */}
            <div className="px-6 sm:px-8 py-4 bg-white border-t border-slate-200/80 flex flex-col sm:flex-row items-center justify-between gap-3">
              <div className="flex items-center gap-2 text-xs text-slate-500">
                <Sparkles className="w-4 h-4 text-cyan-500" />
                <span>Adherence to these rules ensures maximum pedagogical growth.</span>
              </div>

              <div className="flex items-center gap-2.5 w-full sm:w-auto justify-end">
                <button
                  onClick={onClose}
                  className="px-5 py-2.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors cursor-pointer"
                >
                  Close
                </button>
                <button
                  onClick={() => {
                    onClose();
                    onOpenChat();
                  }}
                  className="px-6 py-2.5 rounded-full text-xs font-semibold bg-[#0a152d] hover:bg-[#122347] text-white shadow-sm hover:shadow-md transition-all flex items-center gap-2 cursor-pointer"
                >
                  <span>Accept &amp; Start Learning</span>
                  <ArrowRight className="w-3.5 h-3.5 text-cyan-400" />
                </button>
              </div>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};

export default RulesModal;
