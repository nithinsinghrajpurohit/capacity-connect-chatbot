import React, { useState } from 'react';
import HeroSection from './components/HeroSection';
import MarqueeScroller from './components/MarqueeScroller';
import RulesSection from './components/RulesSection';
import RulesModal from './components/RulesModal';
import AstraChatbot from './components/AstraChatbot';
import { motion } from 'motion/react';

export const App: React.FC = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [isRulesOpen, setIsRulesOpen] = useState(false);

  return (
    <main className="min-h-screen w-full bg-[#f9fafb] py-8 md:py-12 px-4 sm:px-6 lg:px-8 flex flex-col items-center justify-start relative">
      {/* Hero Section Container */}
      <HeroSection
        onOpenChat={() => setIsChatOpen(true)}
        onOpenRules={() => setIsRulesOpen(true)}
      />

      {/* Seamless Marquee Logo Scroller */}
      <div className="w-full max-w-[1400px]">
        <MarqueeScroller />
      </div>

      {/* Dedicated Rules of Use Section at Landing Page */}
      <RulesSection
        onOpenRules={() => setIsRulesOpen(true)}
        onOpenChat={() => setIsChatOpen(true)}
      />

      {/* Floating Action Button for Astra Chatbot */}
      <motion.button
        whileHover={{ scale: 1.08 }}
        whileTap={{ scale: 0.94 }}
        onClick={() => setIsChatOpen(true)}
        className="fixed bottom-6 right-6 z-40 w-14 h-14 rounded-full bg-[#0a152d] text-white shadow-[0_12px_36px_rgba(10,21,45,0.25)] border border-slate-700/50 flex items-center justify-center cursor-pointer group"
      >
        <div className="relative">
          <span className="text-xl font-bold font-display select-none">✦</span>
          <span className="absolute -top-1 -right-1 flex h-2.5 w-2.5">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-cyan-500"></span>
          </span>
        </div>
      </motion.button>

      {/* Sastra AI Operating Rules Modal */}
      <RulesModal
        isOpen={isRulesOpen}
        onClose={() => setIsRulesOpen(false)}
        onOpenChat={() => {
          setIsRulesOpen(false);
          setIsChatOpen(true);
        }}
      />

      {/* Astra AI Chatbot Modal */}
      <AstraChatbot isOpen={isChatOpen} onClose={() => setIsChatOpen(false)} />
    </main>
  );
};

export default App;
