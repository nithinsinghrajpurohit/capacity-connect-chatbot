import React from 'react';
import { motion } from 'motion/react';
import { ChevronRight, Sparkles } from 'lucide-react';

interface HeroSectionProps {
  onOpenChat: () => void;
}

export const HeroSection: React.FC<HeroSectionProps> = ({ onOpenChat }) => {
  return (
    <div className="relative w-full max-w-[1400px] mx-auto rounded-[48px] bg-white border border-slate-200/50 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.03)] overflow-hidden h-[600px] flex flex-col">
      {/* Underlying Video Background Layer */}
      <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden select-none">
        <video
          autoPlay
          loop
          muted
          playsInline
          className="w-full h-full object-cover scale-105 transition-transform duration-1000"
          src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260505_101331_74f9b798-3f00-4e86-8a01-377aa16ffeaa.mp4"
        />
      </div>

      {/* Hero Text Content Wrapper */}
      <div className="relative z-20 flex-1 px-8 md:px-16 pt-12 md:pt-16 flex flex-col items-start">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          className="max-w-2xl flex flex-col items-start"
        >
          {/* Headline */}
          <h1 className="font-display text-[42px] md:text-[56px] font-medium tracking-tight text-[#0a1b33] leading-[1.08] mb-4">
            Foundation of the
            <br />
            new digital epoch
          </h1>

          {/* Subheadline */}
          <p className="font-sans text-[14px] md:text-[15px] text-[#64748b] leading-relaxed max-w-lg mb-8">
            Designing products, powering ecosystems and laying the foundation of a
            decentralized web for enterprises, builders and communities alike.
          </p>

          {/* Contact Button -> Launches Sastra Assistant */}
          <motion.button
            whileHover={{ scale: 1.04 }}
            whileTap={{ scale: 0.98 }}
            transition={{ type: 'spring', stiffness: 400, damping: 25 }}
            onClick={onOpenChat}
            className="bg-[#0a152d] text-white px-7 py-3 rounded-full text-[14px] font-medium shadow-sm hover:shadow-md transition-shadow cursor-pointer flex items-center gap-2"
          >
            <span>Ask Sastra Assistant</span>
            <Sparkles className="w-4 h-4 text-cyan-400" />
          </motion.button>
        </motion.div>
      </div>

      {/* Floating Bottom Navbar Wrapper */}
      <div className="absolute bottom-10 left-1/2 -translate-x-1/2 z-30">
        <motion.nav
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
          className="flex items-center bg-white/90 backdrop-blur-2xl px-1.5 py-1.5 rounded-full shadow-[0_12px_40px_rgba(0,0,0,0.08)] border border-slate-200/40 gap-1 sm:gap-2"
        >
          {/* Circular Star Logo Placeholder -> Launches Sastra */}
          <button
            onClick={onOpenChat}
            className="w-9 h-9 bg-white border border-slate-100 shadow-sm rounded-full flex items-center justify-center text-sm font-semibold text-[#0a1b33] select-none shrink-0 hover:bg-slate-50 transition-colors cursor-pointer"
            title="Open Sastra AI"
          >
            ✦
          </button>

          {/* Standard Text Buttons */}
          <div className="flex items-center gap-1 sm:gap-2 px-1">
            <button
              onClick={onOpenChat}
              className="text-[12px] font-semibold text-slate-500 hover:text-[#0a1b33] px-3 py-1.5 rounded-full transition-colors cursor-pointer"
            >
              Learn
            </button>
            <button
              onClick={onOpenChat}
              className="text-[12px] font-semibold text-slate-500 hover:text-[#0a1b33] px-3 py-1.5 rounded-full transition-colors cursor-pointer"
            >
              Quiz
            </button>
          </div>

          {/* Get in Touch Button */}
          <button
            onClick={onOpenChat}
            className="bg-white px-5 py-2 rounded-full text-[12px] font-semibold text-[#0a1b33] border border-slate-200/60 shadow-sm hover:border-slate-300 transition-all flex items-center gap-1 cursor-pointer whitespace-nowrap"
          >
            <span>Chat with Sastra</span>
            <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
          </button>
        </motion.nav>
      </div>
    </div>
  );
};

export default HeroSection;
