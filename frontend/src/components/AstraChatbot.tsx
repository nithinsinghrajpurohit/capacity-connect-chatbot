import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { toPng } from 'html-to-image';
import {
  Send,
  Mic,
  MicOff,
  Image as ImageIcon,
  RotateCcw,
  X,
  BookOpen,
  Code2,
  Calculator,
  Compass,
  Layers,
  FileText,
  FileDown,
  CheckCircle2,
  Copy,
  Check,
  ChevronRight,
  User,
  Loader2,
  Volume2,
  VolumeX,
  Paperclip,
  Camera,
  Download,
  Maximize2,
  Sparkles,
  Table as TableIcon,
} from 'lucide-react';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  image?: string;
  pdfUrl?: string;
  docName?: string;
  mode?: string;
  suggestions?: string[];
  cards?: Array<{ front: string; back: string }>;
  timestamp: string;
}

const MODES = [
  { id: 'learn', label: 'Learn', icon: BookOpen, desc: 'Quick definition & example (less content)' },
  { id: 'deep', label: 'Deep Explanation', icon: Sparkles, desc: 'Comprehensive breakdown, table & code' },
  { id: 'image', label: 'Visual & Table', icon: TableIcon, desc: 'Vector Concept Diagrams & Tables' },
  { id: 'notes', label: 'Study Notes & PDF', icon: FileText, desc: 'Complete PDF study & step-by-step notes' },
  { id: 'quiz', label: 'Quiz', icon: CheckCircle2, desc: 'Quick concept check (simple & direct)' },
  { id: 'code', label: 'Code Debug', icon: Code2, desc: 'Identify errors, explain, fix & show output' },
  { id: 'math', label: 'Math Solver', icon: Calculator, desc: 'Step-by-step solving & solution' },
  { id: 'path', label: 'Learning Path', icon: Compass, desc: 'Curriculum roadmap' },
  { id: 'revise', label: 'Flashcards', icon: Layers, desc: 'Active recall' },
];

const renderFormattedInline = (text: string) => {
  const parts: React.ReactNode[] = [];
  let remaining = text;
  let keyIdx = 0;
  const tokenRegex = /(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)/;

  while (remaining) {
    const match = remaining.match(tokenRegex);
    if (!match || match.index === undefined) {
      parts.push(remaining);
      break;
    }

    if (match.index > 0) {
      parts.push(remaining.substring(0, match.index));
    }

    const token = match[0];
    if (token.startsWith('`') && token.endsWith('`')) {
      parts.push(
        <code
          key={keyIdx++}
          className="px-1.5 py-0.5 rounded bg-slate-100 font-mono text-[12px] text-indigo-700 font-medium"
        >
          {token.slice(1, -1)}
        </code>
      );
    } else if (token.startsWith('**') && token.endsWith('**')) {
      parts.push(
        <strong key={keyIdx++} className="font-semibold text-[#0a1b33]">
          {token.slice(2, -2)}
        </strong>
      );
    } else if (token.startsWith('*') && token.endsWith('*')) {
      parts.push(
        <em key={keyIdx++} className="italic text-slate-700">
          {token.slice(1, -1)}
        </em>
      );
    }

    remaining = remaining.substring(match.index + token.length);
  }

  return parts;
};

interface ParsedBlock {
  type: 'paragraph' | 'heading' | 'bullet' | 'code' | 'table' | 'divider' | 'solution' | 'verification' | 'step';
  content?: string;
  lang?: string;
  headers?: string[];
  rows?: string[][];
}

const parseStructuredContent = (rawText: string): ParsedBlock[] => {
  const blocks: ParsedBlock[] = [];
  const lines = rawText.split('\n');
  let i = 0;

  while (i < lines.length) {
    const rawLine = lines[i];
    const trimmed = rawLine.trim();

    // 0. Horizontal Divider
    if (trimmed === '---' || trimmed === '***' || trimmed === '___') {
      blocks.push({ type: 'divider' });
      i++;
      continue;
    }

    // 0.5. Prominent Final Solution
    if (trimmed.startsWith('🎯 Final Solution:') || trimmed.startsWith('🎯 Solution:') || trimmed.startsWith('Final Solution:')) {
      blocks.push({
        type: 'solution',
        content: trimmed.replace(/^🎯\s*/, ''),
      });
      i++;
      continue;
    }

    // 0.6. Verification Proof Check
    if (trimmed.includes('LHS = RHS') || trimmed.includes('Verified Correct!') || trimmed.startsWith('◈ 5. Substitution Proof')) {
      blocks.push({
        type: 'verification',
        content: trimmed,
      });
      i++;
      continue;
    }

    // 0.7. Math / Process Step Card
    if (/^(?:•\s*)?(?:✦\s*)?Step\s+\d+[:.]/i.test(trimmed) || trimmed.startsWith('✦ Step ')) {
      blocks.push({
        type: 'step',
        content: trimmed,
      });
      i++;
      continue;
    }

    // 1. Code Block
    if (trimmed.startsWith('```')) {
      const lang = trimmed.replace(/^```/, '').trim();
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // Skip closing ```
      blocks.push({
        type: 'code',
        lang: lang || 'text',
        content: codeLines.join('\n'),
      });
      continue;
    }

    // 2. Markdown Table Detection
    if (
      trimmed.includes('|') &&
      i + 1 < lines.length &&
      /^\s*\|?\s*[-:]+\s*\|/.test(lines[i + 1])
    ) {
      const parseCells = (rowStr: string) => {
        let clean = rowStr.trim();
        if (clean.startsWith('|')) clean = clean.substring(1);
        if (clean.endsWith('|')) clean = clean.substring(0, clean.length - 1);
        return clean.split('|').map((c) => c.trim());
      };

      const headers = parseCells(rawLine);
      i += 2; // skip header and separator row

      const rows: string[][] = [];
      while (i < lines.length && lines[i].trim().includes('|')) {
        const rowCells = parseCells(lines[i]);
        if (rowCells.length > 0 && rowCells.some((c) => c.length > 0)) {
          rows.push(rowCells);
        }
        i++;
      }

      blocks.push({
        type: 'table',
        headers,
        rows,
      });
      continue;
    }

    // 3. Headings
    if (
      trimmed.startsWith('## ') ||
      trimmed.startsWith('### ') ||
      trimmed.startsWith('✦ ') ||
      trimmed.startsWith('◈ ') ||
      trimmed.startsWith('❖ ') ||
      trimmed.startsWith('🎬 ') ||
      trimmed.startsWith('🧠 ') ||
      trimmed.startsWith('🌿 ') ||
      trimmed.startsWith('⚡ ') ||
      trimmed.startsWith('🧪 ') ||
      trimmed.startsWith('🎯 ') ||
      trimmed.startsWith('💎 ') ||
      trimmed.startsWith('📌 ')
    ) {
      const headingText = trimmed.replace(/^#+\s*/, '');
      blocks.push({
        type: 'heading',
        content: headingText,
      });
      i++;
      continue;
    }

    // 4. Bullet lists
    if (
      trimmed.startsWith('• ') ||
      trimmed.startsWith('❯ ') ||
      trimmed.startsWith('- ') ||
      trimmed.startsWith('* ')
    ) {
      const bulletText = trimmed.replace(/^[•❯\-*]\s*/, '');
      blocks.push({
        type: 'bullet',
        content: bulletText,
      });
      i++;
      continue;
    }

    // 5. Empty spacer
    if (!trimmed) {
      blocks.push({
        type: 'paragraph',
        content: '',
      });
      i++;
      continue;
    }

    // 6. Regular Paragraph
    blocks.push({
      type: 'paragraph',
      content: rawLine,
    });
    i++;
  }

  return blocks;
};

export const AstraChatbot: React.FC<{
  isOpen: boolean;
  onClose: () => void;
}> = ({ isOpen, onClose }) => {
  const [userProfile, setUserProfile] = useState<{
    id: number;
    full_name: string;
    role: string;
    department?: string;
  }>(() => {
    const saved = localStorage.getItem('sastra_learner_profile');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        // If it was the previous hardcoded 'Mourya', migrate to 'Learner'
        if (parsed && parsed.full_name && parsed.full_name.toLowerCase() !== 'mourya') {
          return parsed;
        }
      } catch {}
    }
    // Clear old hardcoded Mourya default from localStorage
    try {
      localStorage.removeItem('sastra_learner_profile');
    } catch {}
    return {
      id: 1,
      full_name: 'Learner',
      role: 'trainee',
      department: 'Digital Skills & Capacity',
    };
  });

  const [messages, setMessages] = useState<Message[]>([
    {
      id: 'init-1',
      role: 'assistant',
      content:
        "Hello! I'm Sastra, your AI Learning Operating System for Capacity Connect.\n\n👉 **To begin chatting, please first select a learning mode from the top toolbar:**\n\n• **Math Solver** 🧮: Step-by-step mathematical solving, formulas & verification proof\n• **Learning Path** 🧭: 5-Phase step-by-step curriculum roadmaps for any topic\n• **Flashcards** 🎴: Interactive click-to-flip active recall revision cards\n• **Visual & Table** 📊: High-definition diagrams & structured clinical dataset tables\n• **Learn** 📖: Concise definitions & practical examples\n• **Deep Explanation** ✨: Comprehensive pedagogical masterclasses\n• **Quiz** 🎯: Interactive concept checks & assessments\n• **Study Notes & PDF** 📄: Step-by-step notes & official printable PDF guides\n• **Code Debug** 💻: Error identification, explanations, fixes & test output\n\nClick any mode button above or a starter chip below to activate your session!",
      suggestions: [
        'Math Solver 🧮',
        'Learning Path 🧭',
        'Flashcards 🎴',
        'Visual & Table 📊',
        'Learn 📖',
      ],
      timestamp: 'Just now',
    },
  ]);
  const [input, setInput] = useState('');
  const [attachedImage, setAttachedImage] = useState<string | null>(null);
  const [attachedDoc, setAttachedDoc] = useState<{ name: string; data: string; type: string } | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingStatus, setLoadingStatus] = useState<string>('Sastra thinking...');
  const [activeMode, setActiveMode] = useState<string | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [downloadingPdfId, setDownloadingPdfId] = useState<string | null>(null);
  const [speakingMsgId, setSpeakingMsgId] = useState<string | null>(null);
  const [sessionId] = useState<string>(() => `sess-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`);
  const [flippedCards, setFlippedCards] = useState<Record<string, boolean>>({});

  const toggleFlipCard = (cardKey: string) => {
    setFlippedCards((prev) => ({ ...prev, [cardKey]: !prev[cardKey] }));
  };

  const handleModeSelect = (modeId: string) => {
    const isDeselect = activeMode === modeId;
    const newMode = isDeselect ? null : modeId;
    setActiveMode(newMode);

    if (newMode) {
      const modeObj = MODES.find((m) => m.id === newMode);
      let modeSuggestions: string[] = [];
      if (newMode === 'math') {
        modeSuggestions = ['Solve 2x + 5 = 15 🧮', 'Solve 2x^2 + 5x - 3 = 0', 'Derivative of x^3 + 4x', 'Pythagorean theorem a=3, b=4'];
      } else if (newMode === 'path') {
        modeSuggestions = ['Python Programming Roadmap 🧭', 'Full-Stack Web Dev Path', 'Machine Learning & AI', 'Cloud & DevOps'];
      } else if (newMode === 'revise') {
        modeSuggestions = ['React Flashcards 🎴', 'Python Flashcards', 'Docker & Kubernetes', 'Data Structures'];
      } else if (newMode === 'image') {
        modeSuggestions = ['give me patient data set 📊', 'Photosynthesis visual & table 🌿', 'Neural Network Architecture 🧠', 'Operating System Kernel 💻'];
      } else if (newMode === 'learn') {
        modeSuggestions = ['What are Python Variables? 🌿', 'What is Virtual DOM?', 'What is Docker Container?', 'What is Gradient Descent?'];
      } else if (newMode === 'deep') {
        modeSuggestions = ['Deep Dive Photosynthesis 🌿', 'Deep Dive Kubernetes', 'Deep Dive Transformers & LLMs', 'Deep Dive Database Indexing'];
      } else if (newMode === 'quiz') {
        modeSuggestions = ['Quiz on Python 🎯', 'Quiz on Web Development', 'Quiz on Cloud Computing', 'Quiz on Data Structures'];
      } else if (newMode === 'notes') {
        modeSuggestions = ['Notes on Machine Learning 📄', 'Notes on React Hooks', 'Notes on Linux Networking', 'Download PDF Guide'];
      } else if (newMode === 'code') {
        modeSuggestions = ['Debug list mutation in loop 💻', 'Fix NoneType error in function', 'Optimize quadratic time O(N²)', 'Explain Python decorators'];
      }

      const activationMsg: Message = {
        id: `act-${Date.now()}`,
        role: 'assistant',
        content: `🎯 **${modeObj?.label || newMode} Mode Activated!**\n\n${modeObj?.desc || ''}\n\nType your question below or pick one of the starter prompts to begin:`,
        suggestions: modeSuggestions,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      setMessages((prev) => [...prev, activationMsg]);
    }
  };

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const docInputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    if (isOpen) {
      scrollToBottom();
    }
  }, [messages, isOpen]);

  // Auto-detect and synchronize with external website login / session data
  useEffect(() => {
    const detectAndSyncHostUser = () => {
      // 1. Check URL parameters (?username=... or ?user=... or ?name=...)
      try {
        const params = new URLSearchParams(window.location.search);
        const qName = params.get('username') || params.get('user') || params.get('name') || params.get('user_name') || params.get('login_user');
        if (qName && qName.trim()) {
          const clean = qName.trim();
          setUserProfile((prev) => ({ ...prev, full_name: clean, id: prev.full_name === clean ? prev.id : 0 }));
          return;
        }
      } catch (e) {}

      // 2. Check window global variables set by host login pages
      const win = window as any;
      const hostUser = win.SASTRA_USER || win.ASTRA_USER || win.CURRENT_USER || win.LOGGED_IN_USER || win.USER_NAME || win.userName || win.username || (win.SastraConfig && win.SastraConfig.user) || (win.AstraConfig && win.AstraConfig.user);
      if (hostUser) {
        if (typeof hostUser === 'string' && hostUser.trim()) {
          const clean = hostUser.trim();
          setUserProfile((prev) => ({ ...prev, full_name: clean, id: prev.full_name === clean ? prev.id : 0 }));
          return;
        } else if (typeof hostUser === 'object') {
          const fn = hostUser.full_name || hostUser.name || hostUser.username || hostUser.email;
          if (fn && typeof fn === 'string') {
            setUserProfile((prev) => ({ ...prev, full_name: fn.trim(), role: hostUser.role || prev.role, department: hostUser.department || prev.department }));
            return;
          }
        }
      }

      // 3. Check localStorage & sessionStorage keys used by external login pages
      const storageKeys = [
        'username', 'user_name', 'name', 'full_name', 'user', 'currentUser', 
        'auth_user', 'authUser', 'loggedUser', 'login_user', 'capacity_user', 
        'userProfile', 'profile', 'userData'
      ];
      for (const k of storageKeys) {
        const val = localStorage.getItem(k) || sessionStorage.getItem(k);
        if (val) {
          try {
            const parsed = JSON.parse(val);
            if (parsed && typeof parsed === 'object') {
              const fn = parsed.full_name || parsed.name || parsed.username;
              if (fn && typeof fn === 'string') {
                setUserProfile((prev) => ({ ...prev, full_name: fn.trim(), role: parsed.role || prev.role }));
                return;
              }
            }
          } catch (e) {
            if (typeof val === 'string' && val.length > 1 && val.length < 50 && !val.includes('{')) {
              setUserProfile((prev) => ({ ...prev, full_name: val.trim() }));
              return;
            }
          }
        }
      }

      // 4. Check active DOM elements on host login page
      const loginInp = document.querySelector('input[name="username"], input[name="user"], input#username, input#user, input[autocomplete="username"], input[data-user-name]') as HTMLInputElement;
      if (loginInp && loginInp.value && loginInp.value.trim().length >= 2) {
        setUserProfile((prev) => ({ ...prev, full_name: loginInp.value.trim() }));
      }
    };

    detectAndSyncHostUser();

    // 5. Cross-window / iframe message listener for host login pages
    const handleMessage = (event: MessageEvent) => {
      if (event.data && (event.data.type === 'SASTRA_SET_USER' || event.data.type === 'ASTRA_SET_USER' || event.data.type === 'LOGIN_SUCCESS' || event.data.type === 'USER_LOGIN')) {
        const p = event.data.user || event.data.username || event.data.user_name || event.data.full_name || event.data.name;
        if (typeof p === 'string' && p.trim()) {
          const clean = p.trim();
          setUserProfile((prev) => ({ ...prev, full_name: clean }));
          try { localStorage.setItem('sastra_learner_profile', JSON.stringify({ id: 0, full_name: clean, role: 'trainee' })); } catch (e) {}
        } else if (typeof p === 'object' && p) {
          const fn = p.full_name || p.name || p.username;
          if (fn) {
            const updated = { id: p.id || 0, full_name: fn.trim(), role: p.role || 'trainee', department: p.department };
            setUserProfile(updated);
            try { localStorage.setItem('sastra_learner_profile', JSON.stringify(updated)); } catch (e) {}
          }
        }
      }
    };

    window.addEventListener('message', handleMessage);

    // 6. Global JS API for host developers
    (window as any).Sastra = (window as any).Astra = {
      setUser: (u: any) => {
        if (typeof u === 'string') {
          const updated = { id: 0, full_name: u.trim(), role: 'trainee' };
          setUserProfile(updated);
          try { localStorage.setItem('sastra_learner_profile', JSON.stringify(updated)); } catch (e) {}
        } else if (typeof u === 'object' && u) {
          const updated = { id: u.id || 0, full_name: (u.full_name || u.name || u.username || 'Learner').trim(), role: u.role || 'trainee', department: u.department };
          setUserProfile(updated);
          try { localStorage.setItem('sastra_learner_profile', JSON.stringify(updated)); } catch (e) {}
        }
      },
      getUser: () => userProfile,
    };

    return () => {
      window.removeEventListener('message', handleMessage);
    };
  }, []);

  const handleSpeakMessage = (text: string, msgId: string) => {
    if (speakingMsgId === msgId) {
      window.speechSynthesis.cancel();
      setSpeakingMsgId(null);
      return;
    }
    window.speechSynthesis.cancel();
    const cleanSpeechText = text
      .replace(/```[\s\S]*?```/g, 'Code block omitted from audio.')
      .replace(/[#*`_~✦◈❯❖🌿☀️💧🍃🧪🍎💨⚡🎤🔊🧠🎯💎📌🎬⏱️]/g, '')
      .replace(/\n+/g, '. ');
    const utterance = new SpeechSynthesisUtterance(cleanSpeechText);

    // Pick optimal natural voice
    const voices = window.speechSynthesis.getVoices();
    const preferredVoice = voices.find(
      (v) =>
        (v.lang.startsWith('en') &&
          (v.name.includes('Natural') ||
            v.name.includes('Google') ||
            v.name.includes('Neural') ||
            v.name.includes('Samantha') ||
            v.name.includes('India'))) ||
        v.lang === 'en-US' ||
        v.lang === 'en-IN' ||
        v.lang === 'en-GB'
    );
    if (preferredVoice) {
      utterance.voice = preferredVoice;
    }

    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    utterance.onend = () => setSpeakingMsgId(null);
    utterance.onerror = () => setSpeakingMsgId(null);
    setSpeakingMsgId(msgId);
    window.speechSynthesis.speak(utterance);
  };

  // Dynamic API Base URL: checks Vite environment variable first, then window global, then empty (relative)
  const rawApiBase =
    (import.meta as any).env?.VITE_API_BASE_URL ||
    (import.meta as any).env?.VITE_API_URL ||
    (typeof window !== 'undefined' && (window as any).SASTRA_API_URL) ||
    '';
  const API_BASE = rawApiBase ? rawApiBase.replace(/\/+$/, '') : '';

  const fetchWithFallback = async (endpoint: string, options: RequestInit) => {
    const cleanEp = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;

    // 1. If API_BASE is explicitly set (e.g., Render backend on Vercel)
    if (API_BASE) {
      try {
        const res = await fetch(`${API_BASE}${cleanEp}`, options);
        if (res.ok) return res;
      } catch (e) {
        console.warn(`Fetch to ${API_BASE}${cleanEp} failed:`, e);
      }
    }

    // 2. Relative endpoint (works with Vite proxy or Vercel rewrites)
    try {
      const res = await fetch(cleanEp, options);
      if (res.ok) return res;
    } catch (e) {
      console.warn('Relative fetch failed, attempting localhost fallback...', e);
    }

    // 3. Fallback to local 127.0.0.1:5000 if developing locally
    const fallbackUrl = `http://127.0.0.1:5000${cleanEp}`;
    return await fetch(fallbackUrl, options);
  };

  const handleDownloadPdf = async (text: string, title = 'Sastra Study Guide', msgId?: string) => {
    if (msgId) setDownloadingPdfId(msgId);
    try {
      const res = await fetchWithFallback('/api/pdf/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text,
          title: title.slice(0, 45),
          topic: 'Capacity Building Curriculum',
          author: 'Sastra AI',
        }),
      });
      if (res.ok) {
        const data = await res.json();
        if (data.url) {
          const hostBase = API_BASE || (typeof window !== 'undefined' && window.location.hostname.includes('localhost') ? 'http://127.0.0.1:5000' : window.location.origin);
          const fullUrl = data.url.startsWith('http')
            ? data.url
            : `${hostBase}${data.url.startsWith('/') ? data.url : `/${data.url}`}`;
          // Open PDF directly in a new browser tab for immediate viewing & reading
          window.open(fullUrl, '_blank', 'noopener,noreferrer');
        }
      }
    } catch (err) {
      console.error('PDF generation error:', err);
    } finally {
      if (msgId) setDownloadingPdfId(null);
    }
  };

  const handleSend = async (customText?: string) => {
    const textToSend = customText || input.trim();
    if ((!textToSend && !attachedImage && !attachedDoc) || loading) return;

    // Strict Mode-First Enforcement: User must select a learning mode first
    if (!activeMode) {
      if (!customText) setInput('');
      const userMsg: Message = {
        id: `usr-${Date.now()}`,
        role: 'user',
        content: textToSend || (attachedDoc ? `📄 ${attachedDoc.name}` : '📷 Visual'),
        image: attachedImage || undefined,
        docName: attachedDoc?.name,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      const modeNoticeMsg: Message = {
        id: `sys-${Date.now()}`,
        role: 'assistant',
        content:
          '⚠️ **Please select a learning mode first!**\n\nTo chat with Sastra AI, please select one of the specialized learning modes from the top toolbar first:\n\n• **Math Solver** 🧮: Step-by-step mathematical problem solving & verification\n• **Learning Path** 🧭: 5-Phase learning roadmap for any topic\n• **Flashcards** 🎴: Active recall revision cards\n• **Visual & Table** 📊: Concept diagrams & structured dataset tables\n• **Learn** 📖: Bite-sized definitions & quick examples\n• **Deep Explanation** ✨: Comprehensive masterclasses\n• **Quiz** 🎯: Interactive concept checks\n• **Study Notes & PDF** 📄: Exhaustive study guides\n• **Code Debug** 💻: Error identification & bug fixing\n\n👉 *Click any mode button above or a suggestion chip below to activate it and chat!*',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        suggestions: ['Math Solver 🧮', 'Learning Path 🧭', 'Flashcards 🎴', 'Visual & Table 📊', 'Learn 📖'],
      };
      setMessages((prev) => [...prev, userMsg, modeNoticeMsg]);
      return;
    }

    const userMsg: Message = {
      id: `usr-${Date.now()}`,
      role: 'user',
      content:
        textToSend ||
        (attachedDoc
          ? `📄 Analyzing attached document: ${attachedDoc.name}`
          : '📷 Analyzing attached visual...'),
      image: attachedImage || undefined,
      docName: attachedDoc?.name,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    const sentImage = attachedImage;
    const sentDoc = attachedDoc;
    if (!customText) setInput('');
    setAttachedImage(null);
    setAttachedDoc(null);
    setLoading(true);
    setLoadingStatus(
      sentDoc
        ? `Sastra studying complete PDF (${sentDoc.name}) & explaining all topics step-by-step...`
        : sentImage
        ? 'Performing multimodal vision reasoning...'
        : activeMode === 'notes'
        ? 'Synthesizing complete step-by-step study notes & PDF guide...'
        : 'Sastra thinking...'
    );

    // Auto-detect user name introduction (e.g. "hi i am mourya", "my name is mourya", "call me Mourya")
    let currentName = userProfile.full_name;
    const nameMatch = textToSend.match(/(?:i am|i\'m|my name is|this is|call me)\s+([a-zA-Z]+)/i);
    if (nameMatch && nameMatch[1]) {
      const extracted = nameMatch[1].charAt(0).toUpperCase() + nameMatch[1].slice(1).toLowerCase();
      if (extracted.toLowerCase() !== 'sastra' && extracted.toLowerCase() !== 'astra') {
        currentName = extracted;
        const updated = { ...userProfile, full_name: currentName };
        setUserProfile(updated);
        localStorage.setItem('sastra_learner_profile', JSON.stringify(updated));
      }
    }

    try {
      // 1. Check if Image / Diagram Generation Request
      const isImageGenRequest =
        activeMode === 'image' ||
        (activeMode !== 'deep' && activeMode !== 'learn' && activeMode !== 'quiz' &&
          /(?:@?(?:create|generate|show|draw|make|render)\s+(?:an?\s+)?(?:image|diagram|visual|illustration|roadmap|photo|graphic|picture|wallpaper)|@?(?:image|diagram|illustrate|visualize)\b|\b(?:generate|create|draw)\s+(?:an?\s+)?(?:image|diagram|visual|photo|picture)\b|\b(?:make it photorealistic|cyberpunk neon|3d pixar|studio ghibli)\b)/i.test(
            textToSend
          )) ||
        textToSend.trim().startsWith('@image') || textToSend.trim().startsWith('@create image');

      setLoadingStatus(
        isImageGenRequest
          ? 'Synthesizing educational study visual...'
          : sentImage
          ? 'Performing multimodal vision reasoning...'
          : 'Sastra formulating answer...'
      );

      // Send to /api/chat with mode: 'image' when image requested
      const res = await fetchWithFallback('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: textToSend,
          image: sentImage || undefined,
          file: sentDoc?.data || undefined,
          filename: sentDoc?.name || undefined,
          mode: isImageGenRequest ? 'image' : (activeMode || undefined),
          user_id: userProfile.id,
          user_name: currentName,
          session_id: sessionId,
        }),
      });

      if (!res.ok) throw new Error(`Server returned HTTP ${res.status}`);
      const data = await res.json();

      let botImage = data.image;
      let botSuggestions = data.suggestions;
      if (data.mode === 'deep' || activeMode === 'deep') {
        botSuggestions = ['Download PDF Notes 📄'];
      }

      const botMsg: Message = {
        id: `bot-${Date.now()}`,
        role: 'assistant',
        content: data.reply || '✦ I am ready to help you learn.',
        image: botImage,
        mode: data.mode,
        suggestions: botSuggestions || (activeMode === 'deep' ? ['Download PDF Notes 📄'] : [
          '📄 Download PDF Study Guide',
          'Explain with rich symbols 🌿',
          'Draw an AI diagram 🎨',
          'Quiz me on this 🎯',
        ]),
        cards: data.cards,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => [...prev, botMsg]);
    } catch (err: any) {
      setTimeout(() => {
        const targetHost = API_BASE || '127.0.0.1:5000';
        const fallbackMsg: Message = {
          id: `bot-${Date.now()}`,
          role: 'assistant',
          content: `⚠️ Sastra backend connection notice:\nCould not reach the Python backend at ${targetHost}.\n\nIf you are running on Vercel, please ensure that your Render backend is deployed and VITE_API_BASE_URL is configured in your Vercel Project Settings.\n\n(Details: ${err?.message || 'Network unreachable'})`,
          suggestions: ['Retry question 🔄', 'Explain Photosynthesis 🌿', 'Quiz me 🎯'],
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        };
        setMessages((prev) => [...prev, fallbackMsg]);
      }, 500);
    } finally {
      setLoading(false);
    }
  };

  const handleVoiceInput = () => {
    const SpeechRecognition =
      (window as unknown as { SpeechRecognition?: any; webkitSpeechRecognition?: any })
        .SpeechRecognition ||
      (window as unknown as { webkitSpeechRecognition?: any }).webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert('Speech recognition is not supported in this browser.');
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;

    if (!isRecording) {
      setIsRecording(true);
      recognition.start();
      recognition.onresult = (event: any) => {
        const transcript = event.results[0][0].transcript;
        setInput((prev) => (prev ? `${prev} ${transcript}` : transcript));
        setIsRecording(false);
      };
      recognition.onerror = () => setIsRecording(false);
      recognition.onend = () => setIsRecording(false);
    } else {
      setIsRecording(false);
      recognition.stop();
    }
  };

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const dataUrl = event.target?.result as string;
      setAttachedImage(dataUrl);
    };
    reader.readAsDataURL(file);
  };

  // Localhost-only detection: only enabled during local testing/debugging, hidden in production
  const isLocalhost =
    typeof window !== 'undefined' &&
    (window.location.hostname === 'localhost' ||
      window.location.hostname === '127.0.0.1' ||
      window.location.hostname === '[::1]' ||
      window.location.hostname.endsWith('.local'));

  const chatThreadRef = useRef<HTMLDivElement>(null);
  const [isCapturingScreenshot, setIsCapturingScreenshot] = useState(false);
  const [screenshotNotice, setScreenshotNotice] = useState<string | null>(null);

  // Complete screenshot capture of the entire conversation thread done with Sastra AI
  const captureFullChatScreenshot = async () => {
    const el = chatThreadRef.current;
    if (!el) {
      alert('Chat thread container not found.');
      return;
    }

    setIsCapturingScreenshot(true);
    try {
      // Save original container styles & scroll position
      const originalHeight = el.style.height;
      const originalMaxHeight = el.style.maxHeight;
      const originalOverflow = el.style.overflow;
      const prevScrollTop = el.scrollTop;

      // Ensure any lazy loaded images in chat thread are marked eager before capture
      const lazyImages = el.querySelectorAll('img[loading="lazy"]');
      lazyImages.forEach((img) => ((img as HTMLImageElement).loading = 'eager'));

      // Temporarily expand to entire scrollHeight so ALL conversation messages are fully rendered
      const fullHeight = Math.max(el.scrollHeight, el.offsetHeight, 600);
      const fullWidth = Math.max(el.scrollWidth, el.offsetWidth, 700);

      el.style.height = `${fullHeight}px`;
      el.style.maxHeight = 'none';
      el.style.overflow = 'visible';

      // Capture full thread with html-to-image
      // fontEmbedCSS: '' and skipFonts: true prevent any cross-origin Google Fonts CSS SecurityError
      let dataUrl = '';
      try {
        dataUrl = await toPng(el, {
          backgroundColor: '#fafbfc',
          width: fullWidth,
          height: fullHeight,
          pixelRatio: 2, // High resolution for crisp readability of all text, code, and symbols
          skipFonts: true,
          fontEmbedCSS: '',
          onImageErrorHandler: () => '',
        });
      } catch (innerErr) {
        console.warn('First toPng pass failed, retrying with simple options...', innerErr);
        dataUrl = await toPng(el, {
          backgroundColor: '#fafbfc',
          skipFonts: true,
          fontEmbedCSS: '',
          onImageErrorHandler: () => '',
        });
      }

      // Restore original dimensions immediately
      el.style.height = originalHeight;
      el.style.maxHeight = originalMaxHeight;
      el.style.overflow = originalOverflow;
      el.scrollTop = prevScrollTop;

      if (!dataUrl) {
        throw new Error('Screenshot generation produced empty image data.');
      }

      const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
      const filename = `sastra-chat-complete-${timestamp}.png`;

      // Always download the complete chat image to user's computer
      const a = document.createElement('a');
      a.href = dataUrl;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

      // Attempt to copy image to clipboard as well for direct Ctrl+V pasting into chat
      try {
        const res = await fetch(dataUrl);
        const blob = await res.blob();
        if (navigator.clipboard && (window as any).ClipboardItem) {
          await navigator.clipboard.write([
            new (window as any).ClipboardItem({ 'image/png': blob })
          ]);
        }
      } catch (clipErr) {
        // Clipboard writing is optional
      }

      setScreenshotNotice(`📸 Full chat saved to Downloads as "${filename}" and copied to clipboard! You can now share it with your AI pair programmer.`);
      setTimeout(() => setScreenshotNotice(null), 10000);
    } catch (err: any) {
      console.error('Failed to capture complete chat screenshot:', err);
      alert('Could not capture full chat screenshot: ' + (err?.message || 'Unknown error'));
    } finally {
      setIsCapturingScreenshot(false);
    }
  };

  const handleDocumentUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const dataUrl = event.target?.result as string;
      setAttachedDoc({
        name: file.name,
        data: dataUrl,
        type: file.type || 'application/pdf'
      });
    };
    reader.readAsDataURL(file);
  };

  const copyToClipboard = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 1500);
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-900/40 backdrop-blur-md">
          {/* Main Modal Panel */}
          <motion.div
            initial={{ opacity: 0, scale: 0.94, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.94, y: 20 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
            className="relative w-full max-w-4xl h-[92vh] max-h-[860px] bg-white rounded-[36px] shadow-[0_30px_100px_rgba(0,0,0,0.18)] border border-slate-200/80 flex flex-col overflow-hidden font-sans"
          >
            {/* Top Sleek Header */}
            <header className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-white/80 backdrop-blur-xl">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-slate-900 flex items-center justify-center text-white text-base shadow-sm">
                  ✦
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h2 className="font-display font-semibold text-[17px] text-[#0a1b33]">
                      Sastra AI
                    </h2>
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-semibold tracking-wide bg-gradient-to-r from-blue-500/10 to-indigo-500/10 text-blue-600 border border-blue-200/60">
                      RAG • PDF EXPORT • VISION • DOCS & CODE
                    </span>
                  </div>
                  <p className="text-[12px] text-slate-400">
                    Capacity Connect — Personal AI Learning Operating System
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-2">
                {/* Active Host Logged-in User Badge with Click-to-Edit */}
                <button
                  type="button"
                  onClick={() => {
                    const currentVal = userProfile.full_name === 'Learner' ? '' : userProfile.full_name;
                    const entered = window.prompt('Enter your name / learner ID:', currentVal);
                    if (entered && entered.trim()) {
                      const updated = { ...userProfile, full_name: entered.trim() };
                      setUserProfile(updated);
                      try {
                        localStorage.setItem('sastra_learner_profile', JSON.stringify(updated));
                      } catch {}
                    }
                  }}
                  className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100/90 hover:bg-blue-50 border border-slate-200/80 hover:border-blue-300 text-[12px] font-medium text-[#0a1b33] cursor-pointer transition-all shadow-2xs group"
                  title="Click to change your learner name"
                >
                  <div className="w-5 h-5 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center text-[10px] font-bold shadow-2xs group-hover:scale-105 transition-transform">
                    {userProfile.full_name ? userProfile.full_name.charAt(0).toUpperCase() : 'L'}
                  </div>
                  <span className="font-semibold text-slate-800 group-hover:text-blue-700">
                    {userProfile.full_name || 'Learner'}
                  </span>
                  <span className="text-[10px] text-slate-400 group-hover:text-blue-500 underline decoration-dotted">
                    edit
                  </span>
                  <span className="flex h-1.5 w-1.5 relative ml-0.5" title="Live Synced">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
                  </span>
                </button>

                {/* Localhost-Only Full Chat Screenshot Tool in Header */}
                {isLocalhost && (
                  <button
                    type="button"
                    onClick={() => captureFullChatScreenshot()}
                    disabled={isCapturingScreenshot}
                    className="flex items-center gap-1.5 bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 px-3 py-1 rounded-full text-amber-800 text-xs font-semibold shadow-2xs cursor-pointer transition-colors"
                    title="📸 Download complete chat conversation as PNG image to share with your AI pair programmer"
                  >
                    {isCapturingScreenshot ? (
                      <Loader2 className="w-3.5 h-3.5 animate-spin text-amber-600" />
                    ) : (
                      <Camera className="w-3.5 h-3.5 text-amber-600" />
                    )}
                    <span className="text-[11px] font-semibold">📸 Download Chat Image</span>
                  </button>
                )}

                <button
                  onClick={() => {
                    const saluteName = userProfile.full_name && userProfile.full_name !== 'Learner' ? ` ${userProfile.full_name}` : '';
                    setMessages([
                      {
                        id: `init-${Date.now()}`,
                        role: 'assistant',
                        content:
                          `Hello${saluteName}! Fresh learning session started. What shall we master, export to PDF, or generate today?`,
                        suggestions: [
                          'Explain Photosynthesis 🌿',
                          'Download PDF study guide 📄',
                          'Draw an AI diagram 🎨',
                          'Quiz me on ML 🎯',
                        ],
                        timestamp: 'Just now',
                      },
                    ]);
                  }}
                  title="Reset Session"
                  className="p-2 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors cursor-pointer"
                >
                  <RotateCcw className="w-4 h-4" />
                </button>
                <button
                  onClick={onClose}
                  className="p-2 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </header>

            {/* Mode-First Requirement Banner */}
            {!activeMode && (
              <div className="px-6 py-2 bg-gradient-to-r from-amber-500/15 via-orange-500/10 to-blue-500/10 border-b border-amber-200/80 flex items-center justify-between gap-2 text-xs font-semibold text-amber-900 animate-pulse">
                <span className="flex items-center gap-1.5">
                  <span className="text-amber-700 font-bold">👉 Step 1:</span> Please select a learning mode below first to chat with Sastra AI
                </span>
                <span className="text-[10px] bg-amber-100 text-amber-800 px-2.5 py-0.5 rounded-full border border-amber-300 font-bold">
                  Mode Required
                </span>
              </div>
            )}

            {/* Mode Selector Pill Bar */}
            <div className="px-6 py-2.5 bg-slate-50/70 border-b border-slate-100 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider mr-1 shrink-0">
                Mode:
              </span>
              {MODES.map((m) => {
                const Icon = m.icon;
                const isSelected = activeMode === m.id;
                return (
                  <button
                    key={m.id}
                    onClick={() => handleModeSelect(m.id)}
                    className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[12px] font-medium transition-all shrink-0 cursor-pointer ${
                      isSelected
                        ? 'bg-[#0a152d] text-white shadow-sm ring-1 ring-white/20'
                        : 'bg-white text-slate-600 hover:text-[#0a1b33] border border-slate-200/60 hover:border-slate-300'
                    }`}
                  >
                    <Icon
                      className={`w-3.5 h-3.5 ${isSelected ? 'text-cyan-300' : 'text-slate-400'}`}
                    />
                    <span>{m.label}</span>
                  </button>
                );
              })}
            </div>

            {/* Messages Thread (Scrollable container captured by html2canvas) */}
            <div
              ref={chatThreadRef}
              className="flex-1 overflow-y-auto px-6 py-6 space-y-6 bg-[#fafbfc]"
            >
              {messages.map((msg) => (
                <motion.div
                  key={msg.id}
                  initial={{ opacity: 0, y: 12 }}
                  animate={{ opacity: 1, y: 0 }}
                  className={`flex gap-3 max-w-[85%] ${
                    msg.role === 'user' ? 'ml-auto flex-row-reverse' : 'mr-auto'
                  }`}
                >
                  {/* Avatar */}
                  <div
                    className={`w-8 h-8 rounded-full shrink-0 flex items-center justify-center text-xs font-semibold select-none shadow-xs ${
                      msg.role === 'user'
                        ? 'bg-gradient-to-tr from-blue-600 to-indigo-600 text-white'
                        : 'bg-[#0a152d] text-white border border-slate-200'
                    }`}
                  >
                    {msg.role === 'user' ? (
                      userProfile.full_name ? (
                        userProfile.full_name.charAt(0).toUpperCase()
                      ) : (
                        <User className="w-4 h-4" />
                      )
                    ) : (
                      '✦'
                    )}
                  </div>

                  {/* Message Bubble & Content */}
                  <div className="flex flex-col gap-2">
                    <div
                      className={`relative px-5 py-4 rounded-[24px] text-[14px] leading-relaxed shadow-xs group ${
                        msg.role === 'user'
                          ? 'bg-[#f0f4ff] text-[#0a1b33] border border-blue-200/90 rounded-tr-sm'
                          : 'bg-white text-[#0a1b33] border border-slate-200/70 rounded-tl-sm'
                      }`}
                    >
                      {/* Name Subtitle on top of bubble */}
                      <div className="flex items-center justify-between gap-2 mb-1.5 pb-1 border-b border-slate-100">
                        <span className="text-[11px] font-semibold flex items-center gap-1.5">
                          {msg.role === 'user' ? (
                            <>
                              <span className="text-blue-600 font-bold">👤 {userProfile.full_name}</span>
                              <span className="text-[10px] text-slate-400 font-normal capitalize">
                                ({userProfile.role})
                              </span>
                            </>
                          ) : (
                            <>
                              <span className="text-indigo-600 font-bold">✦ Sastra AI</span>
                              <span className="text-[10px] text-blue-500 font-medium">Assistant</span>
                            </>
                          )}
                        </span>
                        <span className="text-[10px] text-slate-400 font-normal">{msg.timestamp}</span>
                      </div>

                      {/* Attached Image Preview */}
                      {msg.image && (
                        <div className="mb-3 overflow-hidden rounded-2xl border border-slate-700/60 bg-[#070d1e] shadow-xl p-1.5 transition-all">
                          {/* Top Action & Badge Bar */}
                          <div className="flex items-center justify-between px-3 py-1.5 mb-1.5 bg-slate-900/90 rounded-xl border border-slate-800 text-[11px]">
                            <span className="flex items-center gap-1.5 font-semibold text-cyan-400">
                              <Sparkles className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                              {msg.image.startsWith('data:image/svg')
                                ? '📐 Educational Blueprint & Study Diagram'
                                : '📚 Educational Study Visual (1024×1024)'}
                            </span>
                            <div className="flex items-center gap-1.5">
                              <button
                                onClick={() => {
                                  const a = document.createElement('a');
                                  a.href = msg.image!;
                                  a.download = `sastra-study-visual-${Date.now()}.${msg.image!.startsWith('data:image/svg') ? 'svg' : 'jpg'}`;
                                  a.target = '_blank';
                                  document.body.appendChild(a);
                                  a.click();
                                  document.body.removeChild(a);
                                }}
                                className="px-2.5 py-1 rounded-lg bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 hover:text-white flex items-center gap-1 text-[11px] font-medium transition-colors"
                                title="Download High-Resolution Visual"
                              >
                                <Download className="w-3 h-3" /> Download
                              </button>
                              <button
                                onClick={() => window.open(msg.image, '_blank')}
                                className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
                                title="Open Fullscreen in New Tab"
                              >
                                <Maximize2 className="w-3 h-3" />
                              </button>
                            </div>
                          </div>

                          {/* Rendered Image Canvas */}
                          <div className="relative rounded-xl overflow-hidden bg-[#070d1e] flex items-center justify-center min-h-[160px]">
                            <img
                              src={msg.image}
                              alt="Educational Study Visual"
                              className="w-full h-auto max-h-[480px] object-contain rounded-xl block"
                              loading="eager"
                            />
                          </div>
                        </div>
                      )}

                      {/* Text content with rich formatting & zero raw markdown asterisks */}
                      <div className="font-sans space-y-1 pr-14 text-[14px]">
                        {parseStructuredContent(msg.content).map((block, bIdx) => {
                          if (block.type === 'table' && block.headers && block.rows) {
                            return (
                              <div
                                key={bIdx}
                                className="my-3.5 overflow-x-auto rounded-2xl border border-slate-200/90 bg-white shadow-xs"
                              >
                                <table className="w-full text-left text-[13px] border-collapse min-w-[340px]">
                                  <thead>
                                    <tr className="bg-gradient-to-r from-slate-100 to-indigo-50/40 text-slate-800 border-b border-slate-200">
                                      {block.headers.map((h, hIdx) => (
                                        <th
                                          key={hIdx}
                                          className="px-4 py-3 font-semibold text-slate-900 border-r border-slate-200/60 last:border-r-0"
                                        >
                                          {renderFormattedInline(h)}
                                        </th>
                                      ))}
                                    </tr>
                                  </thead>
                                  <tbody className="divide-y divide-slate-100">
                                    {block.rows.map((row, rIdx) => (
                                      <tr
                                        key={rIdx}
                                        className={
                                          rIdx % 2 === 1
                                            ? 'bg-slate-50/50 hover:bg-blue-50/40 transition-colors'
                                            : 'bg-white hover:bg-blue-50/40 transition-colors'
                                        }
                                      >
                                        {row.map((cell, cIdx) => (
                                          <td
                                            key={cIdx}
                                            className="px-4 py-2.5 text-slate-700 leading-relaxed border-r border-slate-100 last:border-r-0"
                                          >
                                            {renderFormattedInline(cell)}
                                          </td>
                                        ))}
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            );
                          }

                          if (block.type === 'code') {
                            return (
                              <div
                                key={bIdx}
                                className="my-3 overflow-hidden rounded-xl border border-slate-800 bg-[#0d1424] shadow-md"
                              >
                                <div className="flex items-center justify-between px-3.5 py-1.5 bg-[#080d19] border-b border-slate-800 text-[11px] text-slate-400 font-mono">
                                  <span>{block.lang || 'code'}</span>
                                  <button
                                    onClick={() => copyToClipboard(block.content || '', `code-${bIdx}`)}
                                    className="flex items-center gap-1 text-slate-400 hover:text-white transition-colors cursor-pointer"
                                  >
                                    <Copy className="w-3 h-3" /> Copy
                                  </button>
                                </div>
                                <pre className="p-3.5 overflow-x-auto text-[13px] font-mono text-emerald-300 leading-relaxed">
                                  <code>{block.content}</code>
                                </pre>
                              </div>
                            );
                          }

                          if (block.type === 'heading') {
                            return (
                              <h3
                                key={bIdx}
                                className="font-display font-semibold text-[15px] text-[#0a1b33] mt-3.5 mb-1 flex items-center gap-1.5"
                              >
                                {renderFormattedInline(block.content || '')}
                              </h3>
                            );
                          }

                          if (block.type === 'bullet') {
                            return (
                              <div key={bIdx} className="flex items-start gap-2 my-1 pl-0.5">
                                <span className="text-blue-500 font-bold text-xs mt-0.5 shrink-0">
                                  ❯
                                </span>
                                <div className="text-[#0a1b33] leading-relaxed">
                                  {renderFormattedInline(block.content || '')}
                                </div>
                              </div>
                            );
                          }

                          if (block.type === 'divider') {
                            return <hr key={bIdx} className="my-3.5 border-slate-200/80" />;
                          }

                          if (block.type === 'solution') {
                            return (
                              <div
                                key={bIdx}
                                className="my-3.5 p-4 rounded-xl bg-gradient-to-r from-emerald-500/15 via-teal-500/10 to-blue-500/10 border-2 border-emerald-500/50 shadow-sm"
                              >
                                <div className="flex items-center gap-2 text-emerald-900 font-bold text-[14px]">
                                  <span className="text-lg">🎯</span>
                                  <span>{renderFormattedInline(block.content || '')}</span>
                                </div>
                              </div>
                            );
                          }

                          if (block.type === 'verification') {
                            return (
                              <div
                                key={bIdx}
                                className="my-2.5 p-3 rounded-xl bg-emerald-50/90 border border-emerald-300/80 flex items-center gap-2.5 text-xs font-semibold text-emerald-800 shadow-xs"
                              >
                                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                                <span>{renderFormattedInline(block.content || '')}</span>
                              </div>
                            );
                          }

                          if (block.type === 'step') {
                            return (
                              <div
                                key={bIdx}
                                className="my-2 p-3 rounded-xl bg-blue-50/60 border border-blue-200/70 hover:border-blue-300 transition-colors shadow-xs"
                              >
                                <div className="text-xs font-semibold text-blue-950 leading-relaxed">
                                  {renderFormattedInline(block.content || '')}
                                </div>
                              </div>
                            );
                          }

                          if (!block.content) {
                            return <div key={bIdx} className="h-1" />;
                          }

                          return (
                            <p key={bIdx} className="my-1 leading-relaxed text-[#0a1b33]">
                              {renderFormattedInline(block.content)}
                            </p>
                          );
                        })}
                      </div>

                      {/* Interactive Active-Recall Flashcards */}
                      {msg.cards && msg.cards.length > 0 && (
                        <div className="mt-4 pt-3 border-t border-slate-100 space-y-3">
                          <div className="flex items-center justify-between">
                            <p className="text-xs font-semibold text-slate-700 flex items-center gap-1.5 uppercase tracking-wider">
                              <Layers className="w-3.5 h-3.5 text-indigo-600" />
                              Interactive Active-Recall Flashcards ({msg.cards.length} Cards):
                            </p>
                            <button
                              type="button"
                              onClick={() => {
                                const allFlipped = msg.cards!.every((_, cIdx) => flippedCards[`${msg.id}-${cIdx}`]);
                                setFlippedCards((prev) => {
                                  const next = { ...prev };
                                  msg.cards!.forEach((_, cIdx) => {
                                    next[`${msg.id}-${cIdx}`] = !allFlipped;
                                  });
                                  return next;
                                });
                              }}
                              className="text-[11px] font-medium text-indigo-600 hover:text-indigo-800 bg-indigo-50 hover:bg-indigo-100 px-2.5 py-1 rounded-full transition-colors cursor-pointer"
                            >
                              {msg.cards.every((_, cIdx) => flippedCards[`${msg.id}-${cIdx}`]) ? 'Hide All Answers 🙈' : 'Reveal All Answers 💡'}
                            </button>
                          </div>
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            {msg.cards.map((c, cIdx) => {
                              const cardKey = `${msg.id}-${cIdx}`;
                              const isFlipped = !!flippedCards[cardKey];
                              return (
                                <div
                                  key={cIdx}
                                  onClick={() => toggleFlipCard(cardKey)}
                                  className={`p-3.5 rounded-xl border transition-all cursor-pointer select-none min-h-[110px] flex flex-col justify-between shadow-xs ${
                                    isFlipped
                                      ? 'bg-gradient-to-br from-emerald-500/10 via-teal-500/5 to-white border-emerald-300 ring-1 ring-emerald-400/30'
                                      : 'bg-white hover:bg-indigo-50/40 border-slate-200/90 hover:border-indigo-300 hover:shadow-sm'
                                  }`}
                                >
                                  <div>
                                    <div className="flex items-center justify-between mb-2">
                                      <span
                                        className={`text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider ${
                                          isFlipped
                                            ? 'bg-emerald-100 text-emerald-800'
                                            : 'bg-indigo-100 text-indigo-800'
                                        }`}
                                      >
                                        {isFlipped ? '💡 Answer (Back)' : `🎴 Card ${cIdx + 1} (Front)`}
                                      </span>
                                      <span className="text-[11px] text-slate-400 font-medium">
                                        {isFlipped ? '🔄 Click to flip' : '👆 Click to reveal'}
                                      </span>
                                    </div>
                                    <p
                                      className={`text-xs leading-relaxed ${
                                        isFlipped
                                          ? 'text-emerald-950 font-medium'
                                          : 'text-slate-900 font-semibold'
                                      }`}
                                    >
                                      {isFlipped ? c.back : c.front}
                                    </p>
                                  </div>
                                  <div className="mt-2.5 pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
                                    <span
                                      className={`font-medium ${
                                        isFlipped ? 'text-emerald-700' : 'text-indigo-600'
                                      }`}
                                    >
                                      {isFlipped ? '✓ Recalled' : '❓ Test Recall'}
                                    </span>
                                    <span className="text-slate-400 hover:text-slate-600">
                                      {isFlipped ? 'Turn over ↩' : 'Show answer ➔'}
                                    </span>
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      )}

                      {/* Top Action Buttons (Voice Speak, PDF Export & Copy) */}
                      <div className="absolute top-3 right-3 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                        {msg.role === 'assistant' && (
                          <>
                            <button
                              onClick={() => handleSpeakMessage(msg.content, msg.id)}
                              className={`p-1.5 rounded-md transition-colors cursor-pointer ${
                                speakingMsgId === msg.id
                                  ? 'text-rose-500 bg-rose-50 animate-pulse'
                                  : 'text-slate-400 hover:text-indigo-600 hover:bg-indigo-50'
                              }`}
                              title={
                                speakingMsgId === msg.id
                                  ? 'Stop Voice Output'
                                  : 'Listen to Sastra Voice Output'
                              }
                            >
                              {speakingMsgId === msg.id ? (
                                <VolumeX className="w-3.5 h-3.5" />
                              ) : (
                                <Volume2 className="w-3.5 h-3.5" />
                              )}
                            </button>
                            <button
                              onClick={() =>
                                handleDownloadPdf(msg.content, 'Sastra Study Guide', msg.id)
                              }
                              disabled={downloadingPdfId === msg.id}
                              className="p-1.5 rounded-md text-slate-400 hover:text-blue-600 hover:bg-blue-50 transition-colors cursor-pointer"
                              title="Download as Official PDF Study Guide"
                            >
                              {downloadingPdfId === msg.id ? (
                                <Loader2 className="w-3.5 h-3.5 animate-spin text-blue-500" />
                              ) : (
                                <FileDown className="w-3.5 h-3.5" />
                              )}
                            </button>
                          </>
                        )}
                        <button
                          onClick={() => copyToClipboard(msg.content, msg.id)}
                          className="p-1.5 rounded-md text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors cursor-pointer"
                          title="Copy text"
                        >
                          {copiedId === msg.id ? (
                            <Check className="w-3.5 h-3.5 text-emerald-500" />
                          ) : (
                            <Copy className="w-3.5 h-3.5" />
                          )}
                        </button>
                      </div>
                    </div>

                    {/* Suggestions Chips */}
                    {(() => {
                      const isDeepMsg = msg.mode === 'deep' || (activeMode === 'deep' && msg.role === 'assistant');
                      const activeSuggestions = isDeepMsg
                        ? ['Download PDF Notes 📄']
                        : msg.suggestions;

                      if (!activeSuggestions || activeSuggestions.length === 0) return null;

                      return (
                        <div className="flex flex-wrap gap-1.5 pt-1">
                          {activeSuggestions.map((sug, sIdx) => {
                            const isPdfChip =
                              sug.toLowerCase().includes('pdf') || sug.includes('📄');
                            return (
                              <button
                                key={sIdx}
                                onClick={() => {
                                  if (isPdfChip && msg.content) {
                                    handleDownloadPdf(msg.content, 'Sastra Study Guide', msg.id);
                                  } else {
                                    const matchMode = MODES.find((m) =>
                                      sug.toLowerCase().includes(m.label.toLowerCase()) ||
                                      (m.id === 'revise' && sug.toLowerCase().includes('flashcard')) ||
                                      (m.id === 'math' && sug.toLowerCase().includes('math')) ||
                                      (m.id === 'path' && sug.toLowerCase().includes('path')) ||
                                      (m.id === 'image' && (sug.toLowerCase().includes('visual') || sug.toLowerCase().includes('diagram')))
                                    );
                                    if (matchMode && !activeMode) {
                                      handleModeSelect(matchMode.id);
                                      return;
                                    }
                                    handleSend(sug);
                                  }
                                }}
                                className={`text-[11px] font-medium px-3 py-1 rounded-full shadow-2xs transition-all flex items-center gap-1 cursor-pointer border ${
                                  isPdfChip
                                    ? 'bg-blue-50/70 hover:bg-blue-100 text-blue-700 border-blue-200 font-semibold'
                                    : 'bg-white hover:bg-slate-50 text-slate-600 hover:text-[#0a1b33] border-slate-200/80 hover:border-slate-300'
                                }`}
                              >
                                <span>{sug}</span>
                                {isPdfChip ? (
                                  <FileDown className="w-3 h-3 text-blue-500" />
                                ) : (
                                  <ChevronRight className="w-3 h-3 text-slate-400" />
                                )}
                              </button>
                            );
                          })}
                        </div>
                      );
                    })()}
                  </div>
                </motion.div>
              ))}

              {/* Typing Indicator / Video Polling */}
              {loading && (
                <motion.div
                  initial={{ opacity: 0, y: 8 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="flex items-center gap-2 text-slate-400 text-xs px-2"
                >
                  <div className="w-7 h-7 rounded-full bg-[#0a152d] text-white flex items-center justify-center text-xs">
                    ✦
                  </div>
                  <div className="bg-white border border-slate-200/80 px-4 py-2.5 rounded-full flex items-center gap-2 shadow-xs">
                    <Loader2 className="w-3.5 h-3.5 text-blue-500 animate-spin" />
                    <span className="text-[11px] font-medium text-slate-600">{loadingStatus}</span>
                  </div>
                </motion.div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Bottom Input Bar */}
            <div className="p-4 bg-white border-t border-slate-100 flex flex-col gap-2">
              {/* Document Preview if attached */}
              {attachedDoc && (
                <div className="relative inline-flex items-center gap-2 bg-emerald-50 px-3 py-1.5 rounded-2xl border border-emerald-200 max-w-sm shadow-2xs">
                  <FileText className="w-4 h-4 text-emerald-600 shrink-0" />
                  <div className="flex flex-col min-w-0 pr-1">
                    <span className="text-xs text-emerald-900 truncate font-semibold">
                      📄 {attachedDoc.name}
                    </span>
                    <span className="text-[10px] text-emerald-700 truncate font-medium">
                      Study Complete PDF & Step-by-Step Breakdown
                    </span>
                  </div>
                  <button
                    onClick={() => setAttachedDoc(null)}
                    className="p-1 rounded-full hover:bg-emerald-200 text-emerald-500 hover:text-emerald-800 ml-auto cursor-pointer"
                    title="Remove document"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              )}

              {/* Screenshot Download Toast Notification */}
              {screenshotNotice && (
                <div className="flex items-center justify-between gap-2 bg-emerald-50 border border-emerald-200 text-emerald-800 px-3.5 py-2 rounded-xl text-xs font-medium shadow-xs animate-in fade-in">
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                    <span>{screenshotNotice}</span>
                  </div>
                  <button
                    type="button"
                    onClick={() => setScreenshotNotice(null)}
                    className="p-1 text-emerald-600 hover:text-emerald-900 rounded-full hover:bg-emerald-100 cursor-pointer transition-colors"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              )}

              {/* Image / Screenshot Preview if attached */}
              {attachedImage && (
                <div className="relative inline-flex items-center gap-2 bg-indigo-50/90 px-3 py-1.5 rounded-2xl border border-indigo-200/80 max-w-sm shadow-xs">
                  <img
                    src={attachedImage}
                    alt="Screenshot"
                    className="w-7 h-7 object-cover rounded-md border border-indigo-200 shadow-2xs shrink-0"
                  />
                  <div className="flex flex-col min-w-0 pr-1">
                    <span className="text-xs text-indigo-900 font-semibold truncate flex items-center gap-1">
                      📸 Screenshot Attached
                    </span>
                    <span className="text-[10px] text-indigo-600 truncate">
                      Ready for Sastra Vision Analysis
                    </span>
                  </div>
                  <button
                    type="button"
                    onClick={() => setAttachedImage(null)}
                    className="p-1 rounded-full hover:bg-indigo-200 text-indigo-400 hover:text-indigo-800 ml-auto cursor-pointer transition-colors"
                    title="Remove screenshot"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              )}

              <div className="relative flex items-center bg-slate-50/80 rounded-full border border-slate-200/80 shadow-xs px-3 py-2 focus-within:border-slate-400 focus-within:bg-white transition-all">
                {/* Document Upload for PDF & Word Analysis */}
                <input
                  type="file"
                  ref={docInputRef}
                  onChange={handleDocumentUpload}
                  accept=".pdf,.docx,.doc,.txt,.md,.json,.csv"
                  className="hidden"
                />
                <button
                  type="button"
                  onClick={() => docInputRef.current?.click()}
                  className="p-2 text-slate-400 hover:text-emerald-600 rounded-full hover:bg-emerald-50 transition-colors cursor-pointer"
                  title="Upload PDF, Word (.docx), or Notes for Deep AI Analysis"
                >
                  <Paperclip className="w-4 h-4" />
                </button>

                {/* Image Upload for Multimodal Vision Reasoning */}
                <input
                  type="file"
                  ref={fileInputRef}
                  onChange={handleImageUpload}
                  accept="image/png,image/jpeg,image/jpg,image/webp"
                  className="hidden"
                />
                <button
                  type="button"
                  onClick={() => fileInputRef.current?.click()}
                  className="p-2 text-slate-400 hover:text-slate-600 rounded-full hover:bg-slate-200/50 transition-colors cursor-pointer"
                  title="Upload Image / Diagram for Vision Reasoning"
                >
                  <ImageIcon className="w-4 h-4" />
                </button>

                {/* Localhost-Only Complete Chat Screenshot Button in Input Bar */}
                {isLocalhost && (
                  <button
                    type="button"
                    onClick={() => captureFullChatScreenshot()}
                    disabled={isCapturingScreenshot}
                    className="p-2 text-amber-700 hover:text-amber-900 bg-amber-50 hover:bg-amber-100 rounded-full transition-all cursor-pointer border border-amber-200/80 shadow-xs flex items-center gap-1 shrink-0"
                    title="📸 Download complete conversation image as PNG to share with AI assistant"
                  >
                    {isCapturingScreenshot ? (
                      <Loader2 className="w-4 h-4 text-amber-600 animate-spin" />
                    ) : (
                      <Camera className="w-4 h-4 text-amber-600" />
                    )}
                    <span className="text-[10px] font-bold text-amber-800 uppercase tracking-wider pr-1 hidden sm:inline">
                      Chat Snap
                    </span>
                  </button>
                )}

                {/* Voice Input Button */}
                <button
                  type="button"
                  onClick={handleVoiceInput}
                  className={`p-2 rounded-full transition-colors cursor-pointer ${
                    isRecording
                      ? 'bg-rose-500 text-white animate-pulse'
                      : 'text-slate-400 hover:text-slate-600 hover:bg-slate-200/50'
                  }`}
                  title="Voice input"
                >
                  {isRecording ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
                </button>

                {/* Text Input */}
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter') {
                      e.preventDefault();
                      handleSend();
                    }
                  }}
                  placeholder={
                    attachedDoc
                      ? `Study complete PDF & explain every topic step-by-step: ${attachedDoc.name}...`
                      : attachedImage
                      ? 'Ask a question or explain this image / diagram...'
                      : !activeMode
                      ? '⚠️ Step 1: Please select a learning mode above first to chat with Sastra AI...'
                      : activeMode === 'math'
                      ? 'Enter any math question or equation for step-by-step solution (e.g. "Solve 2x + 5 = 15")...'
                      : activeMode === 'path'
                      ? 'Enter any topic for a 5-phase step-by-step learning path (e.g. "React", "Kubernetes", "Python")...'
                      : activeMode === 'revise'
                      ? 'Enter any topic for active recall flashcards (e.g. "React", "Python", "Docker")...'
                      : activeMode === 'image'
                      ? 'Prompt a vector diagram or table (e.g. "give me patient data set", "Photosynthesis diagram")...'
                      : activeMode === 'learn'
                      ? 'Enter a topic for quick definition & example (e.g. "Photosynthesis", "Variables")...'
                      : activeMode === 'deep'
                      ? 'Enter a topic for deep explanation with tables & simulation (e.g. "Photosynthesis", "Docker")...'
                      : activeMode === 'quiz'
                      ? 'Enter a topic for a quick quiz (e.g. "Cloud Computing", "Python")...'
                      : activeMode === 'notes'
                      ? 'Upload PDF or enter topic for complete step-by-step study notes & PDF export...'
                      : activeMode === 'code'
                      ? 'Paste code or describe an error to identify bugs, explain, fix & show output...'
                      : `Ask Sastra (${activeMode} mode)...`
                  }
                  className="flex-1 bg-transparent border-none outline-none text-[14px] text-slate-800 px-3 placeholder:text-slate-400"
                />

                {/* Send Button */}
                <button
                  type="button"
                  onClick={() => handleSend()}
                  disabled={(!input.trim() && !attachedImage && !attachedDoc) || loading}
                  className={`p-2.5 rounded-full flex items-center justify-center transition-all cursor-pointer ${
                    (input.trim() || attachedImage || attachedDoc) && !loading
                      ? 'bg-[#0a152d] text-white hover:scale-105 shadow-sm'
                      : 'bg-slate-200 text-slate-400 cursor-not-allowed'
                  }`}
                >
                  <Send className="w-4 h-4" />
                </button>
              </div>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};

export default AstraChatbot;
