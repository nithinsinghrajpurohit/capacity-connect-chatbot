"""Astra FULL brain — GOD MODE layer on top of astra_engine knowledge base.
Adds: deep explanations, Socratic tutoring, code/debug mode, math mode,
learning paths, flashcards, note synthesis, visual diagrams,
misconception repair, mastery checks, page-aware context, suggestions.
Now with pluggable LLM support (Gemini/OpenAI/Ollama with rule-based fallback).
"""
import json
import random
import re
from database import get_db
import astra_engine as base
# LLM integration — graceful fallback if not configured
try:
    from llm_adapter import get_adapter, RuleBasedAdapter
    from astra_system_prompt import build_system_prompt
    _llm = get_adapter()
    _llm_available = not isinstance(_llm, RuleBasedAdapter)
except ImportError:
    _llm = None
    _llm_available = False
MODES = ["learn", "deep", "socratic", "quiz", "revise", "notes", "path", "code", "math", "project", "research", "image"]
IMAGE_TRIGGERS = ["create image", "generate image", "draw image", "diagram of", "visual of", "illustration", "visual roadmap", "show image", "@image", "@create image", "draw a", "create a visual", "render image"]
QUIZ_TRIGGERS = ["quiz me", "quiz", "take a quiz", "test my knowledge", "test me", "practice questions", "mcq", "knowledge check", "assessment", "question on", "ask a question"]
DEEP_TRIGGERS = ["deep explanation", "explain completely", "teach me", "explain in detail",
                 "comprehensive", "thorough", "go deeper", "explain fully", "master this"]
SOCRATIC_TRIGGERS = ["quiz me step by step", "ask me guiding", "socratic", "don't tell me the answer",
                     "let me figure", "guide me", "hint"]
CODE_TRIGGERS = ["debug", "error", "traceback", "fix my code", "what's wrong with", "code review"]
PATH_TRIGGERS = [
    "learning path", "road map", "roadmap", "curriculum", "syllabus", "study plan",
    "how to learn", "path to learn", "where to start", "steps to master", "how should i learn",
    "master ", "become a ", "prepare for interview"
]
PDF_TRIGGERS = ["pdf", "study guide", "cheat sheet", "handout", "printable", "download notes"]
FLASH_TRIGGERS = ["flashcard", "flash card", "flashcards", "quick revision", "revise", "spaced repetition", "recall", "review cards"]
MATH_TRIGGERS = ["solve equation", "calculate", "derivative", "integral", "matrix", "linear algebra", "calculus", "probability", "statistics", "math problem"]
PROJECT_TRIGGERS = ["build a project", "project idea", "capstone", "portfolio project", "mini project"]
RESEARCH_TRIGGERS = ["research", "compare", "pros and cons", "literature", "survey of", "state of the art"]

def detect_mode(message, explicit_mode=None):
    if explicit_mode in MODES:
        return explicit_mode
    m = message.lower()
    if any(t in m for t in IMAGE_TRIGGERS) or m.startswith("@create image") or m.startswith("@image"):
        return "image"
    if any(t in m for t in QUIZ_TRIGGERS):
        return "quiz"
    if any(t in m for t in PDF_TRIGGERS):
        return "notes"
    if any(t in m for t in FLASH_TRIGGERS):
        return "revise"
    if any(t in m for t in PATH_TRIGGERS):
        return "path"
    if any(t in m for t in SOCRATIC_TRIGGERS):
        return "socratic"
    if any(t in m for t in CODE_TRIGGERS):
        return "code"
    if any(t in m for t in MATH_TRIGGERS):
        return "math"
    if any(t in m for t in PROJECT_TRIGGERS):
        return "project"
    if any(t in m for t in RESEARCH_TRIGGERS):
        return "research"
    if any(t in m for t in DEEP_TRIGGERS):
        return "deep"
    return "learn"

def is_quiz_question_message(msg_text):
    """Detects whether a message contains a multiple-choice quiz question."""
    if not msg_text:
        return False
    lower = msg_text.lower()
    has_options = bool(
        ("option a" in lower and "option b" in lower) or
        ("❯ a)" in lower and "❯ b)" in lower) or
        ("a)" in lower and "b)" in lower and "c)" in lower) or
        ("✦ option a" in lower) or
        (re.search(r'\bOption\s+[A-D]\b', msg_text, re.I))
    )
    has_question_cues = bool(
        re.search(r'\b(quiz|question|which option|what is the output|what will be printed|choose the correct|which of the following|your answer|drop your answer)\b', lower)
    )
    return has_options or (has_question_cues and ("option" in lower or "choice" in lower))

def extract_clean_concept_title(query):
    """Extracts a clean, canonical concept title from conversational user queries, stripping fillers and typos."""
    if not query:
        return None
    # Strip emojis
    text = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff]", "", query).strip()
    # Strip conversational wrappers and question templates iteratively
    wrapper_pattern = r"^(?:i can you|can you|could you|would you|please|kindly|tell me about|tell me|explain to me|explain|what is|what are|how does|how do i|teach me|guide to|deep dive into|deep explanation of|learn about|learn|about|show me)\s+"
    prev = ""
    while prev != text:
        prev = text
        text = re.sub(wrapper_pattern, "", text, flags=re.I).strip()
        text = re.sub(r"^(?:the|a|an)\s+", "", text, flags=re.I).strip()
        text = re.sub(r"^(?:complete|comprehensive|full)\s+", "", text, flags=re.I).strip()
    text = text.strip("'\" :;,.?!")

    # If the remaining text is trivial, a small talk greeting, or a conversational command, return None
    non_topics = (
        "lets start learning", "let's start learning", "start learning", "start with first topic", "first topic",
        "hi", "hello", "hey", "next", "continue", "yes", "no", "ok", "okay", "help", "start", "lets start", "let's start",
        "move on", "next topic", "start from scratch", "start from beginning"
    )
    if not text or len(text) < 2 or text.lower() in non_topics:
        return None
    return text.title()

def extract_quiz_choice(message, last_quiz_msg=None):
    """Extracts a user's MCQ option choice (A, B, C, or D) without mistaking it for a programming topic."""
    if not message:
        return None
    m = message.strip()
    
    # If the user explicitly asks about programming language or concepts, do not treat as bare option
    if any(w in m.lower() for w in ("programming", "language", "compiler", "tutorial", "syntax", "pointer", "malloc", "struct", "header", "gcc")):
        return None
    
    # 1. Bare single letter: "c", "C", "a", "A", "b", "B", "d", "D" (with optional punctuation)
    if re.fullmatch(r"[a-dA-D][\.\!\?]?\s*", m):
        return m[0].upper()
    
    # 2. "option c", "Option C", "choice c", "ans c", "answer is c", "it is c", "i pick c", "c)"
    match = re.search(r"(?:^|\b)(?:option|choice|answer|ans|pick|choose|select|it'?s)?\s*[:\-\)]?\s*([a-dA-D])(?:\b|$|\))", m, re.IGNORECASE)
    if match and len(m.split()) <= 6:
        return match.group(1).upper()
        
    # 3. Numeric choices: "1", "2", "3", "4" or "option 1"
    num_match = re.search(r"(?:^|\b)(?:option|choice)?\s*([1-4])(?:\b|$)", m, re.IGNORECASE)
    if num_match and len(m.split()) <= 4:
        return ["A", "B", "C", "D"][int(num_match.group(1)) - 1]
        
    # 4. Check if user typed the literal option value from the last quiz message (e.g. "60")
    if last_quiz_msg:
        opts = re.findall(r'Option\s+([A-D])\s*:\s*([^\n\r]+)', last_quiz_msg, re.IGNORECASE)
        for letter, val in opts:
            val_clean = val.strip().strip('`*[] ').lower()
            if m.lower() == val_clean or m.lower() in val_clean:
                if len(m) >= 2 or m.isdigit():
                    return letter.upper()

    return None
def extract_last_topic_from_history(history):
    """Extracts the most recent educational topic discussed from conversation history."""
    if not history:
        return None
    for turn in reversed(history):
        if turn.get("role") == "user":
            txt = turn.get("message", "").strip()
            # Strip emojis
            clean = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff]", "", txt).strip()
            # Strip directive prefixes
            clean = re.sub(r"^@?(?:tell me about|explain|what is|how does|learn|deep explanation of|study notes for|quiz me on|teach me|guide to|deep dive into)\s+", "", clean, flags=re.I).strip()
            # Clean quotes
            clean = clean.strip('\'" :;,.?!')
            clean_lower = clean.lower()
            # Ignore generic action buttons or greetings
            generic_phrases = (
                "hi", "hello", "hey", "hii", "heyy", "namaste", "good morning", "good afternoon", "good evening",
                "deep explanation", "deep", "explain deeper", "go deeper", "in detail",
                "quiz me on this", "quiz me", "quiz", "take quiz", "test me", "take mastery quiz",
                "download pdf study guide", "download pdf", "generate pdf", "study notes", "notes", "download roadmap pdf",
                "draw ai diagram", "ai diagram", "generate diagram", "diagram", "show diagram",
                "show learning path", "learning path", "roadmap", "curriculum",
                "explain simpler", "simpler", "explain it simply", "explain simply", "easy format",
                "flashcards", "flash cards", "revise", "give me a hint", "reveal the answer", "hint",
                "option a", "option b", "option c", "option d", "choice a", "choice b", "choice c", "choice d",
                "a", "b", "c", "d", "1", "2", "3", "4"
            )
            if clean_lower not in generic_phrases and len(clean) >= 2:
                return clean
    return None

def get_history(user_id, session_id, limit=8):
    if not user_id and not session_id:
        return []
    conn = get_db()
    try:
        if session_id:
            rows = conn.execute(
                "SELECT role,message FROM chat_history WHERE session_id=? "
                "ORDER BY rowid DESC LIMIT ?", (session_id, limit)).fetchall()
        else:
            rows = conn.execute(
                "SELECT role,message FROM chat_history WHERE user_id=? "
                "ORDER BY rowid DESC LIMIT ?", (user_id or 0, limit)).fetchall()
    except Exception:
        rows = []
    conn.close()
    return list(reversed([dict(r) for r in rows]))
def page_context_text(ctx):
    if not ctx:
        return ""
    parts = []
    if ctx.get("page"):
        parts.append(f"Current page: {ctx['page']}")
    if ctx.get("course_title"):
        parts.append(f"Current course: {ctx['course_title']}")
    if ctx.get("lesson_title"):
        parts.append(f"Current lesson: {ctx['lesson_title']}")
    return (" [Context: " + " | ".join(parts) + "]") if parts else ""
def ascii_diagram(topic_key, subtopic_key):
    diagrams = {
        ("python", "functions"): (
            "```text\n  call greet('Sneha')\n        |\n        v\n  +-------------+     +---------------+\n  | parameters  | --> | function body | --> return value\n  +-------------+     +---------------+\n```"),
        ("python", "loops"): (
            "```text\n  start --> condition? --yes--> body --> update --> condition?\n                  |\n                  no\n                  |\n                  v\n                 done\n```"),
        ("artificial_intelligence", "basics"): (
            "```text\n"
            "                 ARTIFICIAL INTELLIGENCE (Parent Science)\n"
            "              ┌───────────────────────────────────────────┐\n"
            "              │  Symbolic AI • Logic • Search • Robotics  │\n"
            "              │      ┌─────────────────────────────┐      │\n"
            "              │      │      MACHINE LEARNING       │      │\n"
            "              │      │  (Supervised / Unsupervised)│      │\n"
            "              │      │      ┌───────────────┐      │      │\n"
            "              │      │      │ DEEP LEARNING │      │      │\n"
            "              │      │      │  ┌─────────┐  │      │      │\n"
            "              │      │      │  │ GenAI / │  │      │      │\n"
            "              │      │      │  │  LLMs   │  │      │      │\n"
            "              │      │      │  └─────────┘  │      │      │\n"
            "              │      │      └───────────────┘      │      │\n"
            "              │      └─────────────────────────────┘      │\n"
            "              └───────────────────────────────────────────┘\n"
            "```"
        ),
        ("machine_learning", "basics"): (
            "```text\n  Data -> Preprocess -> Features -> Train Model -> Evaluate -> Deploy\n                ^                                              |\n                +------------------ new data ------------------+\n```"),
        ("web_development", "react_state"): (
            "```text\n  state change --> re-render --> updated UI\n       ^                            |\n       +------ user event -----------+\n```"),
    }
    return diagrams.get((topic_key, subtopic_key),
        "```text\n  Concept --> Example --> Practice --> Mastery\n```")
def deep_explain(topic_key, subtopic_key, skill_level="intermediate", frustrated=False, history=None):
    topic_data = base.TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None
    sub = topic_data["topics"].get(subtopic_key) or list(topic_data["topics"].values())[0]
    rel = [t for k, t in topic_data["topics"].items() if t["title"] != sub["title"]][:2]
    out = []
    out.append(f"✦ {sub['title']} — Deep Masterclass & Architectural Mechanics\n")
    out.append(f"◈ 1. First Principles & Formal Definition\n{sub['what']}\nAt a fundamental level, this establishes an explicit contract between memory addresses, symbolic identifiers, and runtime execution semantics.\n")
    out.append(f"◈ 2. Architectural Motivation (Why It Exists)\n{sub['title']} exists because scalable software requires modular decomposition and encapsulation. Without this pattern, systems suffer from state pollution, hard-to-trace side effects, and brittle codebases.\n")
    out.append("◈ 3. Low-Level Mechanics & Memory Model\n• Stack & Heap Allocation: Symbolic bindings are resolved in the call frame stack or allocated on the dynamic heap with reference counters.\n• Scope & Lifetime: Enforces deterministic lifetime rules, preventing out-of-scope variable pollution.\n• Bytecode Execution: Evaluated into optimized opcodes with high-speed symbol lookup.\n")
    out.append("◈ 4. Step-by-Step Execution Lifecycle\n" + "\n".join(f"• Phase {i+1}: {p}" for i, p in enumerate(sub["key_points"])) + "\n")
    out.append(f"◈ 5. Multi-Paradigm Code Implementation\n{sub['example']}\n")
    out.append(f"◈ 6. Architectural Flow & Visual Blueprint\n{ascii_diagram(topic_key, subtopic_key)}\n")
    out.append("◈ 7. Real-World Production & Enterprise Use-Cases\nCritical in high-throughput microservices, real-time data pipelines, and production backend APIs where memory efficiency and predictability are non-negotiable.\n")
    out.append("◈ 8. Edge Cases, Subtle Pitfalls & Failure Modes\n" + "\n".join(f"• Pitfall {i+1}: {x}" for i, x in enumerate(sub.get("common_mistakes", ["Uninitialized references", "Off-by-one boundary conditions", "Unintended global mutations"]))) + "\n")
    out.append("◈ 9. Performance & Complexity Analysis\n• Time Complexity: O(1) direct reference lookup in optimal hash-backed frames.\n• Space Overhead: Constant auxiliary space per stack frame / pointer reference.\n")
    if rel:
        out.append("◈ 10. Related Architectural Concepts\n" + "\n".join(f"• {r['title']}: Builds directly upon these foundational guarantees." for r in rel) + "\n")
    out.append(f"◈ 11. Hands-On Mastery Exercise & Verification\nChallenge: {sub['practice']}\n\n💡 Reply with your solution or architectural reasoning, and I will verify your conceptual mastery!")
    return "\n".join(out)
def dynamic_deep_explain(topic_title):
    clean_title = topic_title.strip().rstrip("?").replace("what is", "").replace("explain", "").strip().title() or "Core Architecture"
    return (
        f"✦ {clean_title} — Deep Masterclass & Architectural Mechanics\n\n"
        f"◈ 1. First Principles & Formal Definition\n{clean_title} is formally defined as an abstraction layer engineered to decouple implementation details from high-level state operations.\n\n"
        f"◈ 2. Architectural Motivation (Why It Exists)\nWithout {clean_title}, software components lack formal encapsulation. This pattern guarantees predictable control flow, modular testing, and decoupled interfaces across distributed tiers.\n\n"
        f"◈ 3. Low-Level Mechanics & Memory Model\n• Memory Footprint: Allocated within dedicated process address space with bounded memory overhead.\n• State Isolation: Prevents unauthorized cross-module mutations and race conditions.\n• Runtime Dispatch: Evaluated with direct pointer indirection or optimized bytecode caches.\n\n"
        f"◈ 4. Step-by-Step Execution Lifecycle\n• Phase 1: Initialization & Parameter Contract Validation.\n• Phase 2: Runtime Evaluation & State Mutation.\n• Phase 3: Cleanup, Garbage Collection / Deallocation, and Return Dispatch.\n\n"
        f"◈ 5. Visual Execution Blueprint\n```text\n  Caller Input ──▶ [ Validation & Frame Setup ] ──▶ [ Core Execution Engine ] ──▶ Verified Output\n```\n\n"
        f"◈ 6. Enterprise & Production Use-Cases\nApplied across cloud architectures, backend microservices, and client-side reactive frameworks to ensure resilience under concurrency.\n\n"
        f"◈ 7. Edge Cases & Subtle Pitfalls\n• Boundary condition overflow / null pointer exceptions.\n• Unhandled asynchronous timeouts and latency spikes.\n• Resource leakage when deallocation hooks are omitted.\n\n"
        f"◈ 8. Performance & Complexity Analysis\n• Algorithmic Efficiency: Targeted for O(1) or O(log N) optimal execution.\n• Space Complexity: O(N) linear in worst-case state caching.\n\n"
        f"◈ 9. Hands-On Mastery Exercise & Verification\nAnalyze how {clean_title} handles an unexpected null or empty input. Reply with your strategy, and I will verify your architectural reasoning!"
    )
def socratic_turn(topic_key, subtopic_key, history):
    topic_data = base.TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None
    sub = topic_data["topics"].get(subtopic_key) or list(topic_data["topics"].values())[0]
    user_turns = [h for h in (history or []) if h.get("role") == "user"]
    step = min(len(user_turns), 3)
    if step <= 1:
        return (f"✦ Socratic Discovery — {sub['title']}\n\n"
                f"Let's figure out {sub['title']} together — I won't just give the answer.\n\n"
                f"◈ Guiding Question 1: In your own words, what do you think happens when this executes?\n{sub['example']}\n\n"
                "Take a guess — even a rough one! Then I will give you a clue for the next step.")
    if step == 2:
        return (f"✦ Socratic Discovery — Step 2\n\n"
                f"Good — you are one step closer to mastering {sub['title']}.\n\n"
                f"◈ Clue: {sub['intuition']}\n\n"
                f"◈ Guiding Question 2: What would change if the input values or data types were completely different? "
                "Reply with your reasoning and I will narrow it down further.")
    return (f"✦ Socratic Discovery — Synthesis\n\n"
            f"Almost there! Here is the core operational principle behind {sub['title']}:\n{sub['what']}\n\n"
            f"🎯 Now verify your mastery: {sub['practice']}\n\nState your answer and I will confirm or repair any subtle misconception!")
def dynamic_socratic(topic_title, history):
    clean_title = topic_title.strip().rstrip("?").replace("guide me through", "").replace("teach me", "").strip().title() or "Concept"
    user_turns = [h for h in (history or []) if h.get("role") == "user"]
    step = min(len(user_turns), 3)
    if step <= 1:
        return (
            f"✦ Socratic Discovery — {clean_title}\n\n"
            f"Let's reason through {clean_title} together from first principles — I won't just hand you the answer.\n\n"
            f"◈ Guiding Question 1:\n"
            f"Imagine you need to store and manipulate state that changes over time during a program's execution. "
            f"What fundamental problems arise if data cannot be isolated or named reliably?\n\n"
            f"Take a guess — even a rough one! Reply with your thoughts and I will give you the next clue."
        )
    if step == 2:
        return (
            f"✦ Socratic Discovery — Step 2\n\n"
            f"You're making great progress towards understanding {clean_title}.\n\n"
            f"◈ Clue:\n"
            f"Think of how an index card or whiteboard works versus carving words permanently into stone.\n\n"
            f"◈ Guiding Question 2:\n"
            f"If multiple parts of your program need to read this same state, how should we reference it so that everyone agrees on the current value?\n\n"
            f"Reply with your reasoning!"
        )
    return (
        f"✦ Socratic Discovery — Synthesis\n\n"
        f"Excellent thinking! Here is how it connects to {clean_title}:\n"
        f"By establishing clear symbolic references with well-defined scope and lifetime, your program safely mutates state without unpredictable side effects.\n\n"
        f"🎯 Verification Challenge: How would you apply this in a real project? Try answering in one sentence!"
    )
def code_mode(message):
    m = message
    has_code = "```" in m or re.search(r"\bdef |import |for |while |class |function|const |let |var ", m)

    if re.search(r"traceback|error|exception|not working|bug|wrong output", m, re.I):
        out = ["✦ Code Debugging & Root-Cause Diagnosis\n"]
        out.append("◈ 1. Probable Root Cause:\nMost runtime errors at this stage stem from uninitialized variables, incorrect indentation, off-by-one boundary shifts, or attempting operations on NoneType.\n")
        out.append("◈ 2. Systematic Troubleshooting Protocol:\n• Examine the exact line number reported at the bottom of the traceback.\n• Insert debug prints right before the failure to inspect actual runtime values.\n• Validate data types against function parameter expectations.\n")
        out.append("◈ 3. Debug Template:\n```text\nError Message: ...\nCode Snippet: ...\nExpected Behavior: ...\nActual Behavior: ...\n```\n")
        out.append("📌 Quick Fix: Paste your snippet and error traceback above and I will produce the corrected code immediately.")
        return "\n".join(out)
    tk, sk = base.find_best_topic(m)
    if tk == "artificial_intelligence":
        return (
            "✦ Artificial Intelligence — Debugging & Spot-the-Bug Challenge\n\n"
            "◈ Buggy Code Snippet (Agent Decision Pipeline):\n"
            "```python\n"
            "# AI Autonomous Agent Action Selection\n"
            "def select_ai_action(user_intent, confidence_score):\n"
            "    if confidence_score < 0.7:\n"
            "        return 'Ask clarification'\n"
            "    elif user_intent == 'emergency':\n"
            "        return 'Escalate immediately'\n"
            "    # Missing fallback return when condition not met!\n\n"
            "action = select_ai_action('query', 0.85)\n"
            "print('Agent Dispatch:', action.upper())  # Crashes with AttributeError!\n"
            "```\n\n"
            "🐞 Spot the Bug:\n"
            "• Why it crashes: For user_intent='query' and confidence=0.85, none of the conditional branches match. The function returns None, causing `action.upper()` to fail.\n"
            "• The error: `AttributeError: 'NoneType' object has no attribute 'upper'`\n\n"
            "✓ Corrected Code (Defensive AI Architecture):\n"
            "```python\n"
            "def select_ai_action(user_intent, confidence_score):\n"
            "    if confidence_score < 0.7:\n"
            "        return 'Ask clarification'\n"
            "    if user_intent == 'emergency':\n"
            "        return 'Escalate immediately'\n"
            "    return f'Execute autonomous response for: {user_intent}'\n\n"
            "action = select_ai_action('query', 0.85)\n"
            "print('Agent Dispatch:', action.upper())  # Works reliably!\n"
            "```\n\n"
            "📌 Debugging Takeaway: Autonomous AI systems require complete branch coverage with deterministic default fallbacks to prevent unhandled runtime states."
        )
    if tk == "python" and sk == "functions":
        return (
            "✦ Python Functions — Debugging & Spot-the-Bug Challenge\n\n"
            "◈ Buggy Code Snippet:\n"
            "```python\n"
            "def calculate_discount(price, discount_rate=0.1):\n"
            "    discounted = price * (1 - discount_rate)\n"
            "    # Missing return statement!\n\n"
            "final_price = calculate_discount(100)\n"
            "print('Total:', final_price + 5)  # Crashes!\n"
            "```\n\n"
            "🐞 Spot the Bug:\n"
            "• Why it crashes: The function forgets to `return discounted`. In Python, omitting `return` means the function implicitly returns `None`.\n"
            "• The error: `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`\n\n"
            "✓ Corrected Code:\n"
            "```python\n"
            "def calculate_discount(price, discount_rate=0.1):\n"
            "    return price * (1 - discount_rate)\n\n"
            "final_price = calculate_discount(100)\n"
            "print('Total:', final_price + 5)  # Output: Total: 95.0\n"
            "```\n\n"
            "📌 Debugging Takeaway: Always verify that your function explicitly returns the calculated variable, especially when chaining or performing arithmetic on results."
        )
    if tk == "python" and sk == "variables":
        return (
            "✦ Python Variables — Debugging & Spot-the-Bug Challenge\n\n"
            "◈ Buggy Code Snippet:\n"
            "```python\n"
            "total_score = 50\n\n"
            "def add_bonus():\n"
            "    total_score = total_score + 10  # UnboundLocalError!\n\n"
            "add_bonus()\n"
            "```\n\n"
            "🐞 Spot the Bug:\n"
            "• Why it crashes: Python detects the assignment `total_score = ...` inside the function and marks it as a local variable. But it tries to read `total_score` on the right-hand side before it has been assigned locally!\n"
            "• The error: `UnboundLocalError: cannot access local variable 'total_score' where it is not associated with a value`\n\n"
            "✓ Corrected Code (Clean Architecture):\n"
            "```python\n"
            "# Best practice: Pass variables as parameters and return new values\n"
            "total_score = 50\n\n"
            "def add_bonus(score, bonus=10):\n"
            "    return score + bonus\n\n"
            "total_score = add_bonus(total_score)\n"
            "print('Updated Score:', total_score)  # Output: 60\n"
            "```\n\n"
            "📌 Debugging Takeaway: Avoid mutating global variables inside functions. Pass variables as arguments and return updated state."
        )
    if tk == "python" and sk == "loops":
        return (
            "✦ Python Loops — Debugging & Spot-the-Bug Challenge\n\n"
            "◈ Buggy Code Snippet:\n"
            "```python\n"
            "# Bug: Modifying a list while iterating over it\n"
            "numbers = [1, 2, 3, 4, 5, 6]\n"
            "for num in numbers:\n"
            "    if num % 2 == 0:\n"
            "        numbers.remove(num)  # Skips elements!\n\n"
            "print('Remaining:', numbers)  # Output is [1, 3, 5, 6] - 6 was missed!\n"
            "```\n\n"
            "🐞 Spot the Bug:\n"
            "• Why it fails: When you remove an item from a list during iteration, remaining elements shift left. The loop index advances, skipping the element directly following the removed item!\n\n"
            "✓ Corrected Code (Idiomatic List Comprehension):\n"
            "```python\n"
            "numbers = [1, 2, 3, 4, 5, 6]\n"
            "odd_numbers = [num for num in numbers if num % 2 != 0]\n"
            "print('Remaining:', odd_numbers)  # Output: [1, 3, 5]\n"
            "```\n\n"
            "📌 Debugging Takeaway: Never mutate the length of a collection while looping over it. Use a list comprehension or filter to produce a new list."
        )
    if tk:
        topic_data = base.TOPIC_KNOWLEDGE[tk]
        sub = topic_data["topics"].get(sk) or list(topic_data["topics"].values())[0]
        return (f"✦ {sub['title']} — Code Execution Analysis\n\n"
                f"◈ Definition:\n{sub['what']}\n\n"
                f"❖ Reference Implementation:\n{sub['example']}\n\n"
                f"🎯 Trace It: Run it mentally with sample inputs, and verify against: {sub['practice']}")
    return ("✦ Code Debugging & Analysis Mode\n\n"
            "Paste your code snippet (in triple backticks) plus the error message, and I will break it down step by step:\n"
            "1. 🐞 Exact issue & line number\n"
            "2. 🔍 Root cause analysis\n"
            "3. ✓ Corrected, optimized code\n"
            "4. 📌 Prevention & production best practices.")
def math_mode(message):
    m = message.lower()
    tk, sk = base.find_best_topic(message)

    if tk == "artificial_intelligence":
        return (
            "✦ Mathematical Foundations of Artificial Intelligence\n\n"
            "◈ 1. Core Mathematical Pillars of AI:\n"
            "• Linear Algebra: High-dimensional vector spaces and tensor mappings: X ∈ ℝ^(n Ã d)\n"
            "• Multivariable Calculus: Gradient descent and loss minimization: Î¸ ← Î¸ - Î± ∇L(Î¸)\n"
            "• Probability & Statistics: Bayes' Theorem P(A|B) = P(B|A)P(A)/P(B), maximum likelihood, and entropy\n\n"
            "◈ 2. The Universal AI Objective Function:\n"
            "```text\n"
            "min_Î¸  (1/N) ∑ Loss(f_Î¸(x_i), y_i) + Î» Â· R(Î¸)\n"
            "```\n"
            "• f_Î¸(x): The model parameterized by weights Î¸\n"
            "• Loss(...): Measures divergence between prediction and ground-truth label\n"
            "• Î» Â· R(Î¸): Regularization penalizing excess model complexity\n\n"
            "◈ 3. Scaled Dot-Product Attention (Modern LLMs & Transformers):\n"
            "```text\n"
            "Attention(Q, K, V) = softmax( (Q Â· Káµ) / √d_k ) Â· V\n"
            "```\n\n"
            "💡 Practice: Ask for any AI derivation (e.g. 'explain gradient descent step' or 'calculate Bayes probability')!"
        )
    if tk == "python" and sk == "functions":
        return (
            "✦ Mathematical Formulation of Functions\n\n"
            "◈ 1. Formal Definition:\n"
            "In mathematics, a function f is a binary relation between two sets X (Domain) and Y (Codomain) such that each element x ∈ X is mapped to exactly one unique element y ∈ Y:\n"
            "```text\n"
            "f: X ──▶ Y\n"
            "y = f(x)\n"
            "```\n\n"
            "◈ 2. Computational Mapping:\n"
            "• Input Arguments: Elements from Domain X.\n"
            "• Function Definition: The deterministic mapping rule f.\n"
            "• Return Value: The computed image f(x) ∈ Y.\n\n"
            "◈ 3. Step-by-Step Example (Polynomial Function):\n"
            "Let f(x) = 2xÂ² + 3x - 5. Evaluate for x = 4:\n"
            "• Step 1: Substitution ──▶ f(4) = 2(4)Â² + 3(4) - 5\n"
            "• Step 2: Exponentiation ──▶ f(4) = 2(16) + 12 - 5\n"
            "• Step 3: Multiplication ──▶ f(4) = 32 + 12 - 5\n"
            "• Step 4: Final Addition ──▶ f(4) = 39\n\n"
            "💡 Practice: Calculate f(2) for f(x) = xÂ³ - 4x."
        )
    if tk == "python" and sk == "variables":
        return (
            "✦ Mathematical Foundations of Variables\n\n"
            "◈ 1. Mathematical vs Programming Variables:\n"
            "• In Algebra: A variable (e.g. x) represents an unknown value in an equation (e.g. 2x + 4 = 10 ──▶ x = 3). It represents a fixed truth value.\n"
            "• In Programming: A variable is a named storage address holding a mutable state (e.g. x = x + 1 is mathematically impossible, but algorithmically updates the stored register value).\n\n"
            "◈ 2. Worked Equation Example:\n"
            "Solve for variable x: 3x - 7 = 14\n"
            "• Step 1: Add 7 to both sides ──▶ 3x = 21\n"
            "• Step 2: Divide both sides by 3 ──▶ x = 7\n"
            "• Verification: 3(7) - 7 = 21 - 7 = 14 ✓\n\n"
            "💡 Practice: Tell me an equation (e.g. 'solve 5x + 10 = 35') and I will solve it step-by-step!"
        )
    if (tk == "machine_learning" and sk == "regression") or "regression" in m or "y =" in m or "y=" in m:
        nums = re.findall(r"-?\d+\.?\d*", message)
        slope, xval, icept = 2.0, 5.0, 3.0
        if len(nums) >= 3:
            try:
                slope, xval, icept = float(nums[0]), float(nums[1]), float(nums[2])
            except Exception:
                pass
        calc = slope * xval + icept
        return (
            "✦ Linear Regression Mathematical Solver\n\n"
            "◈ 1. Governing Equation:\n"
            "```text\n"
            "y = m Â· x + b\n"
            "```\n"
            f"• m (Slope / Weight): {slope}\n"
            f"• x (Input Feature): {xval}\n"
            f"• b (Intercept / Bias): {icept}\n\n"
            f"◈ 2. Step-by-Step Substitution:\n"
            f"• Step 1: Multiply slope by feature ──▶ {slope} Ã {xval} = {slope * xval}\n"
            f"• Step 2: Add bias intercept ──▶ {slope * xval} + {icept} = {calc}\n\n"
            f"◈ 3. Predicted Output: y = {calc}\n\n"
            "💡 Send any equation with numbers (e.g. 'y = 4 * 12 + 7') to calculate instantly!"
        )
    nums = re.findall(r"-?\d+\.?\d*", message)
    if len(nums) >= 2:
        try:
            n1, n2 = float(nums[0]), float(nums[1])
            return (
                f"✦ Mathematical Step-by-Step Solver\n\n"
                f"◈ Given Values: a = {n1}, b = {n2}\n"
                f"• Sum (a + b) = {n1 + n2}\n"
                f"• Difference (a - b) = {n1 - n2}\n"
                f"• Product (a Ã b) = {n1 * n2}\n"
                f"• Quotient (a / b) = {n1 / n2 if n2 != 0 else 'Undefined (ZeroDivision)'}\n\n"
                f"💡 State your formula (e.g. 'solve 2x + 6 = 18') for full step-by-step derivations!"
            )
        except Exception:
            pass
    return (
        "✦ Mathematical Solver Mode\n\n"
        "◈ How to use:\n"
        "1. Tell me an algebraic equation (e.g. 'Solve 4x + 12 = 36')\n"
        "2. Provide Linear Regression parameters (e.g. 'y = 2.5 * 10 + 4')\n"
        "3. Ask for mathematical derivations (e.g. 'Derivative of x^3' or 'Probability formulas')\n\n"
        "I will break down every single algebraic step with zero skipped operations!"
    )
def project_mode(message, context):
    m = message.lower()
    skills = []
    if context:
        skills = [e["title"] for e in context.get("enrollments", [])]
    base_idea = skills[0] if skills else "Python"
    if "idea" in m or "suggest" in m or "beginner" in m:
        return (f"✦ Project Mode — Ideas Tailored to You (Based on: {base_idea})\n\n"
                "◈ 1. Starter Project (1 week): Build an interactive CLI quiz application with input handling, scoring, and file I/O.\n"
                "◈ 2. Intermediate Project (2 weeks): Course Analytics Dashboard with tabular progress tracking and charting.\n"
                "◈ 3. Capstone Project (3–4 weeks): Full-Stack Learning Portal module with authentication, dynamic courses, and verification badges.\n\n"
                "Pick one to generate complete architecture, milestones, and testing checklists!")
    return ("✦ Project Architecture Mode\n\n"
            "Tell me: (1) Objective, (2) Tech stack, (3) Timeline, (4) Current progress.\n\n"
            "I will return: Architecture blueprint ──▶ File structure ──▶ Milestones ──▶ Testing checklist ──▶ Demo script.")
def research_mode(message):
    return (f"✦ Research & Comparative Analysis Mode\n\n"
            f"Query: {message[:140]}\n\n"
            "◈ Methodological Breakdown:\n"
            "• Technical Foundations: Established industry best practices and reference implementations.\n"
            "• Trade-Off Matrix: Comparative evaluation across performance, maintainability, and scalability.\n"
            "• Recommendation: Tailored architectural choices for your specific constraints.\n\n"
            "Rephrase as 'compare X vs Y for goal Z' for deep side-by-side matrices.")
LEARNING_PATHS = {
    "python": [
        "Python Foundations (Variables, Data Types, Control Flow & Loops)",
        "Modular Engineering (Functions, Modules, Scope, Clean Code)",
        "Object-Oriented Architecture (Classes, Inheritance, Encapsulation)",
        "Data Engineering Fundamentals (NumPy, Pandas, Vectorized Ops)",
        "Production Capstone: Building and Testing an End-to-End App"
    ],
    "artificial_intelligence": [
        "AI Foundations: Symbolic Logic, Graph Search (BFS/DFS, A*), Knowledge Representation",
        "Machine Learning Core: Supervised & Unsupervised Algorithms, Loss Optimization",
        "Deep Learning & Neural Networks: Multi-Layer Perceptrons, CNNs, Transformers",
        "Generative AI & LLMs: Attention Mechanisms, Prompt Engineering, RAG Systems",
        "Production Capstone: Autonomous Multi-Modal AI Agent with Tool Use"
    ],
    "machine_learning": [
        "Foundations: Linear Algebra, Probability & Python Refresher",
        "Supervised Learning: Linear Regression, Logistic Classification",
        "Unsupervised Learning: K-Means Clustering, PCA Dimensionality",
        "Deep Learning: Multi-Layer Perceptrons, Backpropagation, PyTorch",
        "Capstone: Real-World Scikit-Learn / PyTorch Model Deployment"
    ],
    "web_development": [
        "Web Foundations: Semantic HTML5, Modern CSS Layouts (Flexbox & Grid)",
        "JavaScript Deep Dive: ES6+, DOM Manipulation, Async/Await",
        "React Architecture: Components, Hooks (useState, useEffect), State Flow",
        "API Integration & Backend: Node.js / Express REST API Development",
        "Capstone: Full-Stack Reactive Learning Dashboard Application"
    ],
    "cloud_computing": [
        "Systems & Networking: Linux Shell, TCP/IP, DNS, Security Groups",
        "Core Cloud Architecture: AWS Compute (EC2), Object Storage (S3), IAM",
        "Containerization: Docker Container Workflows & Docker Compose",
        "Orchestration & Deployments: Kubernetes, CI/CD, Serverless Lambda",
        "Capstone: Multi-Tier Resilient Cloud Infrastructure Deployment"
    ],
    "cybersecurity": [
        "Network Defense: Firewalls, VPNs, TLS Encryption, Packet Analysis",
        "Web Security: OWASP Top 10 Vulnerabilities (SQLi, XSS, CSRF)",
        "Cryptography: Symmetric/Asymmetric Ciphers, Hashing, Key Management",
        "Threat Detection & Incident Response: SIEM, Log Forensics, Zero Trust",
        "Capstone: Defensive Audit & Penetration Testing Report"
    ]
}
def learning_path(message, context=None):
    tk, _ = base.find_best_topic(message)
    key = tk if tk in LEARNING_PATHS else "python"
    steps = LEARNING_PATHS[key]
    phases = ["FOUNDATION", "CORE MECHANICS", "APPLIED PATTERNS", "ADVANCED ARCHITECTURE", "PRODUCTION CAPSTONE"]

    out = [f"✦ Comprehensive Learning Roadmap — {key.replace('_', ' ').title()}\n"]
    for i, s in enumerate(steps):
        phase_label = phases[min(i, len(phases)-1)]
        out.append(f"◈ Step {i+1} [{phase_label}]:\n  ❯ {s}")

    out.append("\n💡 How to Progress: Master each milestone ──▶ Validate with 'Quiz' ──▶ Generate 'Study Notes' for review!")
    return "\n".join(out)
def flashcards(topic_key, subtopic_key, n=4):
    topic_data = base.TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None, []
    sub = topic_data["topics"].get(subtopic_key) or list(topic_data["topics"].values())[0]

    cards = [
        {"front": f"What is {sub['title']}?", "back": sub["what"]},
        {"front": f"How is {sub['title']} implemented in code?", "back": sub["example"][:220]},
        {"front": f"What is the core intuition behind {sub['title']}?", "back": sub["intuition"][:220]},
        {"front": f"What is a common pitfall in {sub['title']}?", "back": sub.get("common_mistakes", ["Syntax error"])[0]}
    ]
    cards = cards[:n]
    lines = [
        f"✦ Interactive Flashcards — {sub['title']}\n",
        "Active recall cards ready! Review the question, recall aloud, then flip to verify:\n"
    ]
    for i, c in enumerate(cards, 1):
        lines.append(f"🎴 Card {i}: {c['front']}\n> 💡 Answer: ||{c['back']}||\n")
    lines.append("💡 Click any flashcard above to review, or select 'Quiz' to test your recall!")
    return "\n".join(lines), cards
def dynamic_flashcards(topic_title):
    clean_title = topic_title.strip().rstrip("?").replace("flashcards for", "").replace("flashcard on", "").strip().title() or "Key Concept"
    return "\n".join(lines), cards

def synthesize_notes(topic_key, subtopic_key, depth="detailed"):
    topic_data = base.TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None
    subs = list(topic_data["topics"].values())
    if subtopic_key and subtopic_key in topic_data["topics"]:
        subs = [topic_data["topics"][subtopic_key]]
    out = [f"# Study Notes — {topic_key.replace('_', ' ').title()}\n"]
    for sub in subs:
        out.append(f"## {sub['title']}")
        out.append(f"✦ Definition:\n{sub['what']}\n")
        if depth == "detailed":
            out.append(f"◈ Intuition:\n{sub['intuition']}\n")
        out.append(f"❖ Code Example:\n{sub['example']}\n")
        out.append("📌 Key Takeaways:\n" + "\n".join(f"• {p}" for p in sub['key_points']) + "\n")
        if depth == "detailed":
            if sub.get('common_mistakes'):
                out.append("⚠️ Mistakes to Avoid:\n" + "\n".join(f"• {m}" for m in sub['common_mistakes']) + "\n")
            out.append(f"🎯 Practice Challenge:\n{sub['practice']}\n")
    out.append("💡 Click the 'Download PDF' button above to export these complete notes as an official PDF study guide.")
    return "\n".join(out)

def dynamic_study_notes(topic_title):
    clean_title = topic_title.strip().rstrip("?").replace("make notes on", "").replace("notes on", "").strip().title() or "Study Notes"
    return (
        f"# Study Notes — {clean_title}\n\n"
        f"✦ Executive Summary\nComprehensive reference guide covering foundations, architecture, and practical application of {clean_title}.\n\n"
        f"◈ Core Principles & Formal Definition\n• Primary Function: Provides structured capability for high-reliability software execution.\n• Theoretical Basis: Grounded in separation of concerns and deterministic state transitions.\n\n"
        f"❖ Structural Components & Syntax Patterns\n• Declarative Specification: Clear, unambiguous declarations and interface contracts.\n• Operational Semantics: Step-by-step evaluation with defensive validation.\n\n"
        f"📌 Key Rules & Best Practices\n• Maintain high cohesion and minimal coupling.\n• Document parameter assumptions and return contracts.\n• Write automated unit tests covering nominal and edge paths.\n\n"
        f"⚠️ Common Mistakes to Avoid\n• Premature optimization before profiling bottlenecks.\n• Ignoring error conditions or swallowing exceptions silently.\n\n"
        f"🎯 Active-Recall Review Questions\n1. What is the single most important purpose of {clean_title}?\n2. What is a primary risk when {clean_title} is improperly configured?\n\n"
        f"💡 Click the 'Download PDF' button above to export these complete notes as an official PDF study guide."
    )


def dynamic_easy_learn(topic_title):
    clean_title = topic_title.strip().rstrip("?").replace("what is", "").replace("explain", "").strip().title() or "Concept"
    return (
        f"✦ {clean_title} — Quick Learning Guide\n\n"
        f"◈ Definition:\n{clean_title} is a fundamental concept used to store, organize, and execute data or logic reliably in software.\n\n"
        f"❯ Everyday Intuition:\nThink of {clean_title} like a clearly labeled container in your workspace: you define it once, and reuse it whenever needed without repeating boilerplate code.\n\n"
        f"❖ Code Example:\n```python\n# Basic practical example of {clean_title}\nvalue = 42\nprint(f'{clean_title} in action: {value}')\n```\n\n"
        f"💡 Key Takeaway: Master this basic definition and syntax first. For internal memory architecture and low-level mechanics, switch to 'Deep Explanations'!"
    )


def teach_topic_concise(topic_key, subtopic_key):
    """Concise definition + practical example for Learning Mode."""
    topic_data = base.TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None
    subtopic = topic_data["topics"].get(subtopic_key) or list(topic_data["topics"].values())[0]
    out = [
        f"✦ {subtopic['title']} — Quick Learning Guide\n",
        f"◈ Definition:\n{subtopic['what']}\n",
        f"❯ Everyday Intuition:\n{subtopic['intuition']}\n",
        f"❖ Code Example:\n{subtopic['example']}\n",
        "💡 Key Takeaway: Master this basic definition and syntax first. For internal memory architecture and low-level mechanics, switch to 'Deep Explanations'!"
    ]
    return "\n".join(out)


TOPIC_MCQ_QUESTIONS = {
    ("python", "variables"): {
        "q": "In Python, which of the following is an INVALID variable identifier?",
        "opts": ["_total_count", "totalCount2", "2nd_total", "total_count"],
        "ans": "C",
        "exp": "Variable names in Python cannot start with a digit. They must begin with a letter or an underscore (_)."
    },
    ("python", "functions"): {
        "q": "What does a Python function return by default if no 'return' statement is explicitly reached?",
        "opts": ["0", "False", "None", "An empty string ''"],
        "ans": "C",
        "exp": "In Python, all functions implicitly return the special value None if they terminate without an explicit return expression."
    },
    ("python", "loops"): {
        "q": "What is the output of `list(range(2, 8, 2))` in Python?",
        "opts": ["[2, 3, 4, 5, 6, 7]", "[2, 4, 6]", "[2, 4, 6, 8]", "[4, 6, 8]"],
        "ans": "B",
        "exp": "range(start, stop, step) starts at 2, increments by 2, and stops strictly before 8, resulting in [2, 4, 6]."
    },
    ("python", "data_types"): {
        "q": "Which of the following built-in Python data types is MUTABLE?",
        "opts": ["Tuple", "String", "List", "Integer"],
        "ans": "C",
        "exp": "Lists in Python are mutable collections, meaning their elements can be added, updated, or deleted in place."
    },
    ("python", "oop"): {
        "q": "In a Python class method definition, what does the first parameter 'self' refer to?",
        "opts": ["The parent class", "The specific instance of the class", "The global namespace", "The __init__ constructor"],
        "ans": "B",
        "exp": "'self' represents the specific instance of the class through which the method is called."
    },
    ("artificial_intelligence", "basics"): {
        "q": "Which of the following correctly describes the relationship between AI, Machine Learning (ML), and Deep Learning (DL)?",
        "opts": [
            "AI and ML are synonyms, while DL is an unrelated field",
            "ML is the parent field containing AI, and AI contains DL",
            "AI is the broad parent science, ML is a subset of AI, and DL is a subset of ML",
            "Deep Learning contains Machine Learning, which in turn contains AI"
        ],
        "ans": "C",
        "exp": "Artificial Intelligence is the broad parent discipline; Machine Learning is a subset focused on learning from data; Deep Learning is a specialized subset of ML using multi-layered neural networks."
    },
    ("machine_learning", "regression"): {
        "q": "In Simple Linear Regression (y = mx + b), what does 'm' represent?",
        "opts": ["The y-intercept", "The slope / regression coefficient", "The mean squared error", "The standard deviation"],
        "ans": "B",
        "exp": "The slope 'm' defines the rate of change in the target variable y for every unit increase in the input feature x."
    },
    ("machine_learning", "classification"): {
        "q": "When detecting rare diseases or fraud where missing a true positive is catastrophic, which metric should be prioritized?",
        "opts": ["Accuracy", "Recall (Sensitivity)", "Specificity", "Mean Absolute Error"],
        "ans": "B",
        "exp": "Recall measures the proportion of actual positives that were correctly identified, minimizing dangerous False Negatives."
    },
    ("machine_learning", "basics"): {
        "q": "Which type of machine learning involves training an agent using states, actions, and rewards?",
        "opts": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Semi-Supervised Learning"],
        "ans": "C",
        "exp": "Reinforcement Learning trains agents to make sequences of decisions to maximize cumulative reward."
    },
    ("web_development", "react_components"): {
        "q": "In React, how do properties (props) flow between components?",
        "opts": ["Two-way binding between siblings", "Unidirectionally from parent to child", "Globally through window.props", "Child to parent only"],
        "ans": "B",
        "exp": "React uses unidirectional data flow where props are passed down from parent components to child components and are strictly read-only."
    },
    ("cloud_computing", "docker"): {
        "q": "What is the primary difference between a Docker Image and a Docker Container?",
        "opts": ["An image runs in memory; a container is stored on disk", "An image is an immutable template; a container is a running instance", "Images require Kubernetes; containers do not", "There is no functional difference"],
        "ans": "B",
        "exp": "A Docker Image is an immutable snapshot/blueprint, while a Container is the running, stateful environment instantiated from it."
    },
    ("cybersecurity", "network_security"): {
        "q": "Which protocol provides cryptographic confidentiality and integrity for web browser traffic?",
        "opts": ["HTTP", "TLS / HTTPS", "FTP", "SNMP"],
        "ans": "B",
        "exp": "Transport Layer Security (TLS/HTTPS) encrypts communication between the client browser and web server."
    }
}
def topic_quiz_turn(message, tk, sk):
    m = message.lower().strip()

    # Check if user is answering a previous question
    ans_match = re.search(r'\b([a-d])\b', m)
    num_match = re.search(r'\b([1-4])\b', m)

    if ans_match or num_match:
        picked = (ans_match.group(1).upper() if ans_match else ["A", "B", "C", "D"][int(num_match.group(1)) - 1])
        return {
            "reply": (
                f"✦ Quiz Evaluation — Your Selection: Option {picked}\n\n"
                f"◈ Feedback:\n"
                f"Great effort! In technical assessments and real-world engineering, understanding why options are right or wrong deepens your foundation.\n\n"
                f"💡 Practice Tip: Select another question below to reinforce your mastery, or switch modes to dive into deep architecture!"
            ),
            "suggestions": ["Next Question 🎯", "Explain this topic simply 🌿", "Deep explanation 🔥", "Download PDF study guide 📄"]
        }
    # Otherwise, present an MCQ question
    pair = (tk, sk) if (tk and sk) else None
    q_data = TOPIC_MCQ_QUESTIONS.get(pair)

    if not q_data and tk:
        for (k_t, k_s), q in TOPIC_MCQ_QUESTIONS.items():
            if k_t == tk:
                q_data = q
                break
    if not q_data:
        topic_title = message.strip().title() or "Core Programming"
        q_data = {
            "q": f"When implementing {topic_title} in production, which principle is most critical for maintainability?",
            "opts": [
                "Hardcoding values to save memory",
                "Modular decomposition and clear interface contracts",
                "Disabling error logs for faster execution",
                "Avoiding automated testing to save time"
            ],
            "ans": "B",
            "exp": "Modular decomposition and clear interface contracts allow components to be developed, tested, and scaled independently."
        }
    opts_fmt = "\n".join(f"❯ {letter}) {opt}" for letter, opt in zip(["A", "B", "C", "D"], q_data["opts"]))
    reply = (
        f"✦ Interactive Concept Check\n\n"
        f"◈ Question:\n{q_data['q']}\n\n"
        f"{opts_fmt}\n\n"
        f"💡 Reply with A, B, C, or D to check your answer and view the explanation!"
    )
    return {
        "reply": reply,
        "suggestions": ["Option A", "Option B", "Option C", "Option D", "Explain topic simply 🌿"]
    }
def repair_misconception(message):
    return ("You're close — there's one specific gap. Let's rebuild from a simpler foundation:\n\n"
            "1. **What part is right:** your instinct about the general idea is on track.\n"
            "2. **The misconception:** a small detail (often a definition or an edge case) is flipped.\n"
            "3. **Tiny example:** work through the smallest possible case first, then scale up.\n\n"
            "Tell me your answer to the practice question in your own words and I'll pinpoint the exact line that's off.")
def suggestions_for(intent, topic_key=None):
    base_s = ["Explain it simply", "Go deeper", "Quiz me", "Flashcards", "Study guide PDF", "What should I learn next?"]
    if intent == "quiz":
        return ["Start quiz", "Quiz me on Python", "Quiz me on ML", "Check my progress"]
    if intent == "notes":
        return ["PDF study guide", "Flashcards for this", "Summarize briefly"]
    if topic_key == "python":
        return ["Explain Python functions", "Debug my code", "Quiz me on Python", "Flashcards"]
    if topic_key == "machine_learning":
        return ["What is overfitting?", "Quiz me on ML", "Learning path for ML"]
    return base_s[:5]
def _clean_reply_text(text):
    """Strip raw markdown ** double asterisks cleanly."""
    if not text:
        return ""
    cleaned = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    return cleaned.replace('**', '').strip()
def _llm_respond(message, context, history, page_ctx, mode, image_data=None):
    """Try to get an LLM response via Gemini/Claude/OpenAI with RAG context grounding and multimodal image analysis."""
    try:
        from llm_adapter import get_adapter, RuleBasedAdapter
        from astra_system_prompt import build_system_prompt
        from rag_engine import get_rag_context

        adapter = get_adapter()
        if isinstance(adapter, RuleBasedAdapter) or not adapter.is_available():
            return None

        # Extract course_id from context if available
        cid = None
        if context and context.get("enrollments"):
            cid = context["enrollments"][0].get("course_id")

        rag_ctx = get_rag_context(message or "general", course_id=cid, top_k=2)
        sys_prompt = build_system_prompt(context, page_ctx, rag_context=rag_ctx)

        reply = adapter.generate(sys_prompt, message, history, image_data=image_data)
        if reply and reply.strip():
            return _clean_reply_text(reply)
    except Exception as e:
        print(f"[Astra] LLM error, falling back to rules: {e}")
    return None
def _process_full_raw(message, user_id=None, session_id="", explicit_mode=None, page_ctx=None, image_data=None, user_name=None, file_data=None, filename=None):
    history = get_history(user_id, session_id)
    context = base.get_user_context(user_id, custom_name=user_name)
    u_name = ((context or {}).get("user") or {}).get("full_name") or user_name or "Learner"

    # ─────────────────────────────────────────────────────────────────────────────
    # 1. Conversational Greetings & Small Talk
    # ─────────────────────────────────────────────────────────────────────────────
    clean_m = re.sub(r"[^\w\s]", "", message.lower()).strip()
    is_greeting = clean_m in (
        "hi", "hello", "hey", "hii", "heyy", "namaste", "good morning",
        "good afternoon", "good evening", "greetings", "how are you",
        "who are you", "what can you do", "help"
    )
    if is_greeting or (clean_m.startswith(("hi ", "hello ", "hey ")) and len(clean_m.split()) <= 3):
        greeting_text = (
            f"Hello {u_name}! I am Sastra, your AI Learning Operating System for Capacity Connect.\n\n"
            f"How can I help you today? You can ask me to:\n"
            f"✦ Explain any concept (like Python variables, Machine Learning, or Quantum Computing)\n"
            f"◈ Dive deep into system architectures with Deep Explanations 🔥\n"
            f"❯ Generate interactive quizzes or printable PDF study notes 📄\n"
            f"❖ Debug code snippets or solve mathematical formulas 🧮\n\n"
            f"What topic would you like to explore?"
        )
        return {
            "reply": greeting_text,
            "mode": "greeting",
            "suggestions": ["Explain Python variables 🌿", "Tell me about Quantum Computing 💡", "Quiz me on Python 🎯", "Generate study notes 📄"]
        }

    # ─────────────────────────────────────────────────────────────────────────────
    # 1.5. Quiz Answer & Option Selection Handling
    # Prevents answers like "c", "Option C", "choice b" from being misinterpreted
    # as requests to explain C programming language!
    # ─────────────────────────────────────────────────────────────────────────────
    last_quiz_msg = None
    if history:
        for h in reversed(history):
            if h.get("role") == "assistant" and is_quiz_question_message(h.get("message", "")):
                last_quiz_msg = h.get("message", "")
                break

    choice = extract_quiz_choice(message, last_quiz_msg)

    # Scenario A: The user is answering an active quiz question from conversation history!
    if choice and last_quiz_msg:
        eval_prompt = (
            f"The learner {u_name} is answering this multiple-choice quiz question:\n\n"
            f"--- PREVIOUS QUIZ QUESTION ---\n{last_quiz_msg}\n------------------------------\n\n"
            f"LEARNER'S ANSWER: Option {choice} (Learner typed: '{message}').\n\n"
            f"Evaluate their answer thoroughly and encouragingly:\n"
            f"1. State clearly whether Option {choice} is CORRECT or INCORRECT.\n"
            f"2. Provide a clear, step-by-step trace or breakdown demonstrating why the correct answer is right.\n"
            f"3. Explain what the other options represent and why they are incorrect distractors.\n"
            f"4. Give an encouraging takeaway to {u_name} and ask if they are ready for the next challenge.\n"
            f"Use clean emojis (✦, ◈, ❖, 📌, 🎯, 💡) and bullet points. Do NOT output raw markdown double asterisks (**)."
        )
        llm_reply = _llm_respond(eval_prompt, context, history, page_ctx, "quiz")
        if not llm_reply:
            llm_reply = (
                f"✦ Quiz Evaluation — Your Selection: Option {choice}\n\n"
                f"◈ Step-by-Step Review:\n"
                f"Great job putting your reasoning to work! Tracing execution step-by-step guarantees mastery of underlying code mechanics.\n\n"
                f"💡 Next Step: Select another challenge below to keep testing your skills, or dive into deep architecture!"
            )
        return {
            "reply": llm_reply,
            "mode": "quiz",
            "suggestions": ["Next Question 🎯", "Explain this topic simply 🌿", "Deep explanation 🔥", "Download PDF study guide 📄"]
        }

    # Scenario B: User typed "option c", "Option B" explicitly but no prior question is in recent history
    if choice and any(w in message.lower() for w in ("option", "choice", "ans", "answer")):
        return {
            "reply": (
                f"✦ Option {choice} Received\n\n"
                f"It looks like you selected Option {choice}! If you'd like to test your knowledge with interactive scoring, click 'Quiz me' below to start a quiz.\n\n"
                f"💡 What topic would you like to explore or be quizzed on?"
            ),
            "mode": "quiz",
            "suggestions": ["Quiz me on Python 🎯", "Explain Python variables 🌿", "Tell me about Quantum Computing 💡", "Show learning path 🧭"]
        }

    # Scenario C: User typed literally just "c" or "c." without any question context
    if clean_m in ("c", "c."):
        return {
            "reply": (
                f"✦ Did you mean Option C, or the C Programming Language?\n\n"
                f"• 🎯 If answering a quiz: Option C received! Click 'Start Quiz' below to take an interactive test with live scoring.\n"
                f"• 💻 If you want to learn C Programming: Ask 'Teach me C programming' or click below to dive into low-level systems, pointers, and memory management!"
            ),
            "mode": "learn",
            "suggestions": ["Learn C Programming 💻", "Quiz me on Python 🎯", "Explain Python variables 🌿", "Explain loops 🔄"]
        }

    # Scenario D: User typed another bare single letter like "a", "b", "d"
    if clean_m in ("a", "b", "d", "a.", "b.", "d."):
        letter = clean_m[0].upper()
        return {
            "reply": (
                f"✦ Option {letter} Received\n\n"
                f"It looks like you selected Option {letter}! If you are taking a quiz, click below to start an interactive assessment, or let me know what concept you'd like to learn!"
            ),
            "mode": "quiz",
            "suggestions": ["Start Quiz 🎯", "Explain Python variables 🌿", "Tell me about Quantum Computing 💡"]
        }

    # ─────────────────────────────────────────────────────────────────────────────
    # 2. Contextual Topic Resolution
    # Resolves follow-up directives (e.g. "Deep explanation 🔥", "Quiz me on this 🎯",
    # "Download PDF 📄", "Draw AI diagram 🎨", "Explain simpler 🌿") to the active topic!
    # ─────────────────────────────────────────────────────────────────────────────
    active_topic = extract_last_topic_from_history(history)

    is_pure_deep = bool(re.match(r"^(?:deep explanation|deep|explain deeper|go deeper|in detail|master this)\b", clean_m, re.I)) or clean_m == "deep explanation"
    is_pure_quiz = bool(re.match(r"^(?:quiz me on this|quiz me|quiz|take quiz|test me|take mastery quiz|interactive quiz)\b", clean_m, re.I))
    is_pure_notes = bool(re.match(r"^(?:download pdf study guide|download pdf|generate pdf|study notes|notes|download roadmap pdf)\b", clean_m, re.I))
    is_pure_img = bool(re.match(r"^(?:draw ai diagram|ai diagram|generate diagram|diagram|show diagram|draw diagram)\b", clean_m, re.I))
    is_pure_path = bool(re.search(r"\b(?:show learning path|learning path|road map|roadmap|curriculum|syllabus|study plan|how to learn|path to learn|steps to master)\b", clean_m, re.I))
    is_pure_simpler = bool(re.match(r"^(?:explain simpler|simpler|explain it simply|explain simply|easy format)\b", clean_m, re.I))
    is_pure_revise = bool(re.match(r"^(?:flashcards|flash cards|revise)\b", clean_m, re.I))

    concept_query = message
    if is_pure_deep and active_topic:
        concept_query = active_topic
    elif is_pure_quiz and active_topic:
        concept_query = active_topic
    elif is_pure_notes and active_topic:
        concept_query = active_topic
    elif is_pure_img and active_topic:
        concept_query = active_topic
    elif is_pure_path and active_topic:
        concept_query = active_topic
    elif is_pure_simpler and active_topic:
        concept_query = active_topic
    elif is_pure_revise and active_topic:
        concept_query = active_topic

    mode = detect_mode(message, explicit_mode)
    if is_pure_deep:
        mode = "deep"
    elif is_pure_quiz:
        mode = "quiz"
    elif is_pure_notes:
        mode = "notes"
    elif is_pure_img:
        mode = "image"
    elif is_pure_path:
        mode = "path"
    elif is_pure_simpler:
        mode = "learn"
    elif is_pure_revise:
        mode = "revise"

    frustrated = base.detect_frustration(message)
    skill = base.detect_skill_level(message)
    tk, sk = base.find_best_topic(concept_query)

    extra = page_ctx or {}
    if context and not extra.get("course_title") and context.get("enrollments"):
        extra = dict(extra)
        extra["course_title"] = context["enrollments"][0]["title"]

    # ── Learning Progression & Lesson Directives (e.g. "lets start learning", "start with first topic") ──
    is_start_learning = bool(re.search(
        r"\b(?:lets start learning|let'?s start learning|start learning|let'?s start|lets start|start with first topic|first topic|begin learning|start from beginning|start from scratch|start from zero|start topic 1|begin topic 1)\b",
        clean_m,
        re.I
    ))
    if is_start_learning:
        curriculum_topic = active_topic or "Python"
        if "python" in (active_topic or "").lower() or "python" in clean_m or not active_topic:
            curriculum_topic = "Python"

        lesson_prompt = (
            f"The learner {u_name} wants to start learning {curriculum_topic} from the very beginning (Topic 1: Variables, Data Types & Basic Output).\n\n"
            f"Act as a world-class, engaging AI coding tutor. Deliver Topic 1 with high clarity and interactive enthusiasm:\n"
            f"✦ Lesson 1: Variables, Data Types & Output in {curriculum_topic} 🚀\n\n"
            f"◈ 1. Core Concept (What & Why):\n"
            f"Explain clearly what variables and data types are, and how assignment works in {curriculum_topic}.\n\n"
            f"◈ 2. Practical Syntax & Examples:\n"
            f"Provide clean, realistic code examples showing string, integer, float, and boolean variables with modern print formatting (f-strings).\n\n"
            f"◈ 3. Relatable Analogy:\n"
            f"Give an intuitive everyday mental model.\n\n"
            f"◈ 4. Your Turn (Interactive Micro-Challenge):\n"
            f"Give {u_name} a friendly, specific mini-task to try right now (e.g. declare two variables and print a greeting), and ask them to reply with their code or answer!\n\n"
            f"Do NOT output raw markdown double asterisks (**)."
        )
        llm_reply = _llm_respond(lesson_prompt, context, history, extra, "learn")
        if not llm_reply:
            llm_reply = (
                f"✦ Lesson 1: Variables, Data Types & Output in {curriculum_topic} 🚀\n\n"
                f"◈ 1. What is a Variable?\n"
                f"In {curriculum_topic}, a variable is a named storage container that holds data in computer memory. You don't need to specify types explicitly; {curriculum_topic} automatically figures it out!\n\n"
                f"◈ 2. Code Example:\n"
                f"```python\n"
                f"# Creating variables\n"
                f"learner_name = \"{u_name}\"\n"
                f"current_level = 1\n"
                f"xp_score = 98.5\n"
                f"is_ready = True\n\n"
                f"# Printing formatted output\n"
                f"print(f\"Welcome {learner_name}! Level: {current_level} | Ready: {is_ready}\")\n"
                f"```\n\n"
                f"◈ 3. Everyday Analogy:\n"
                f"Think of a variable as a labeled storage box in your office. The label on the box is the variable name (e.g. `learner_name`), and the contents inside is the value (`\"{u_name}\"`).\n\n"
                f"◈ 4. Your Turn (Mini-Challenge):\n"
                f"Try typing your own two variables: `favorite_food = \"...\"` and `rating = 10`, and print them! What code would you write? Reply with your code and I will check it!"
            )
        return {
            "reply": llm_reply,
            "mode": "learn",
            "suggestions": ["Here is my code 💻", "Explain data types simply 🌿", "Take a quick quiz 🎯", "Move to Topic 2: Conditions 🔄"]
        }

    # ── Document Analysis Mode (PDF / Word / Text Files) ──
    if file_data:
        try:
            from document_analyzer import get_document_analyzer
            analyzer = get_document_analyzer()
            doc_info = analyzer.extract_from_base64(file_data, filename=filename or "document.pdf")
            analysis_prompt = analyzer.build_analysis_prompt(doc_info, user_query=message, user_name=u_name)

            llm_reply = _llm_respond(analysis_prompt, context, history, extra, "learn")
            if not llm_reply:
                doc_preview = doc_info.get("text", "")[:400]
                llm_reply = (f"✦ Document Analysis Completed ({doc_info.get('type', 'doc').upper()} - {doc_info.get('pages', 1)} pages)\n\n"
                             f"◈ Document Content Preview:\n{doc_preview}...\n\n"
                             f"💡 Key Takeaways:\n1. Structured review of {doc_info.get('type')}\n2. Use this content to reinforce your coursework.")

            return {
                "reply": llm_reply,
                "mode": "document_analysis",
                "doc_type": doc_info.get("type"),
                "pages": doc_info.get("pages"),
                "suggestions": ["📄 Download PDF study summary of this document", "Quiz me on this document 🎯", "Explain key formulas & code"]
            }
        except Exception as e:
            print(f"[Astra] Document analysis error: {e}")

    # ── Image / Vision Mode (Direct Multimodal Analysis) ──
    if image_data:
        vision_query = message.strip() if (message and message.strip()) else "Please analyze this image thoroughly. Identify and explain all key concepts, diagrams, text, code, questions, formulas, or objects in detail with clear, step-by-step reasoning."
        llm_reply = _llm_respond(vision_query, context, history, extra, "vision", image_data=image_data)
        if llm_reply:
            return {"reply": llm_reply, "mode": "vision", "suggestions": ["Explain key concepts in image", "Quiz me on this diagram", "Step-by-step breakdown"]}
        return {
            "reply": "✦ Multimodal Vision Analysis\n\nI have received your image! Please provide a specific question or instruction regarding what you would like analyzed (for example, 'explain this flowchart', 'extract the code', or 'solve this problem').",
            "mode": "vision",
            "suggestions": ["Explain this flowchart", "Solve the question in image", "Summarize key points"]
        }

    # ── Image Generation / Diagram Synthesis Mode ──
    img_triggers = [
        r"^@?(?:create|generate|show|draw|make|render)\s+(?:an?\s+)?(?:image|diagram|visual|illustration|roadmap|photo|graphic)",
        r"^@?(?:image|diagram|illustrate|visualize)\b",
        r"\b(?:generate|create|draw)\s+(?:an?\s+)?(?:image|diagram|visual)\s+(?:of|for|about)\b"
    ]
    is_img_req = mode == "image" or explicit_mode in ("image", "diagram") or any(re.search(pat, message.strip(), re.IGNORECASE) for pat in img_triggers)
    if is_img_req:
        try:
            from image_generator import get_image_generator
            clean_prompt = re.sub(r"^@?(?:create|generate|show|draw|make|render|image|diagram|illustrate|visualize)\s*(?:an?\s+)?(?:image|diagram|visual|illustration|roadmap|photo|graphic)?\s*(?:of|for|about|:)?\s*", "", message.strip(), flags=re.IGNORECASE).strip()
            # If pure image trigger without prompt, fallback to active concept
            if not clean_prompt or is_pure_img:
                clean_prompt = concept_query or "Software Concepts and System Architecture"
            # Strip emojis from prompt
            clean_prompt = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff]", "", clean_prompt).strip()
            gen = get_image_generator()
            img_res = gen.generate_image(clean_prompt)

            clean_title = extract_clean_concept_title(clean_prompt)
            if not clean_title or len(clean_title.split()) > 4 or any(k in clean_title.lower() for k in ["image", "diagram", "visual", "roadmap", "photo", "all learning", "into one", "complete python", "if i see"]):
                if "python" in clean_prompt.lower() or "python" in (active_topic or "").lower() or not active_topic:
                    clean_title = "Python Complete Developer Roadmap"
                else:
                    clean_title = f"{active_topic.title()} Architecture"

            reply_text = (
                f"✦ {clean_title} — Visual Diagram Generated 🎨\n\n"
                f"Here is your unified visual infographic mapping out the complete learning path, core architectural phases, and key milestones.\n\n"
                f"💡 Ready to begin? Reply with 'Let\\'s start learning' or let me know which topic you'd like to explore first!"
            )
            reply_text = reply_text.replace("**", "")

            return {
                "reply": reply_text,
                "image": img_res.get("url"),
                "mode": "image",
                "suggestions": ["Let's start learning 🚀", "Explain Phase 1: Syntax 🌿", "Take a quiz 🎯", "Download PDF study guide 📄"]
            }
        except Exception as e:
            print(f"[Astra] Image generation trigger error: {e}")

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 2. Study Notes & PDF Export Mode ("notes")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "notes":
        target_notes_topic = concept_query if is_pure_notes else message
        llm_reply = _llm_respond(f"Generate comprehensive, structured study notes suitable for a printable PDF study guide on: {target_notes_topic}", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Download PDF Study Guide 📄", "Quiz me on these notes 🎯", "Flashcards 🎴", "Explain simpler 🌿"]}
        if tk:
            notes_text = synthesize_notes(tk, sk)
            return {"reply": notes_text, "mode": mode, "suggestions": ["Download PDF Study Guide 📄", "Quiz me on these notes 🎯", "Flashcards 🎴", "Explain simpler 🌿"]}
        notes_text = dynamic_study_notes(target_notes_topic)
        return {"reply": notes_text, "mode": mode, "suggestions": ["Download PDF Study Guide 📄", "Quiz me on these notes 🎯", "Flashcards 🎴", "Explain simpler 🌿"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 3. Interactive Quiz Mode ("quiz")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "quiz":
        target_quiz_topic = concept_query if is_pure_quiz else message
        quiz_prompt = (
            f"Generate an engaging, high-quality multiple-choice quiz question (MCQ) to test the learner {u_name}'s knowledge on: '{target_quiz_topic}'.\n\n"
            f"Requirements:\n"
            f"1. Provide a clear question with a concise code snippet or scenario if relevant.\n"
            f"2. Provide exactly 4 options formatted clearly as:\n"
            f"> ✦ Option A: ...\n"
            f"> ✦ Option B: ...\n"
            f"> ✦ Option C: ...\n"
            f"> ✦ Option D: ...\n"
            f"3. Do NOT reveal the correct answer or explanation yet. Invite the learner to drop their answer (A, B, C, or D).\n"
            f"4. Do NOT output raw markdown double asterisks (**)."
        )
        llm_reply = _llm_respond(quiz_prompt, context, history, extra, "quiz")
        if llm_reply:
            return {
                "reply": llm_reply,
                "mode": "quiz",
                "suggestions": ["Option A", "Option B", "Option C", "Option D"]
            }
        quiz_res = topic_quiz_turn(target_quiz_topic, tk, sk)
        return {"reply": quiz_res["reply"], "mode": mode, "suggestions": ["Option A", "Option B", "Option C", "Option D"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 4. Flashcards & Active Recall Mode ("revise")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "revise":
        target_card_topic = concept_query if is_pure_revise else message
        if tk:
            txt, cards = flashcards(tk, sk)
            return {"reply": txt, "mode": mode, "cards": cards, "suggestions": ["Quiz me on this 🎯", "Download PDF study guide 📄", "Deep explanation 🔥"]}
        txt, cards = dynamic_flashcards(target_card_topic)
        return {"reply": txt, "mode": mode, "cards": cards, "suggestions": ["Quiz me on this 🎯", "Download PDF study guide 📄", "Deep explanation 🔥"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 5. Socratic Guiding Dialogue Mode ("socratic")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "socratic":
        llm_reply = _llm_respond(f"Engage in Socratic tutoring on '{concept_query}'. Ask a guiding thought question without giving the answer away.", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Give me a hint 💡", "I think the answer is...", "Reveal the answer 🔓"]}
        if tk:
            return {"reply": socratic_turn(tk, sk, history), "mode": mode, "suggestions": ["Give me a hint 💡", "I think the answer is...", "Reveal the answer 🔓"]}
        return {"reply": dynamic_socratic(concept_query, history), "mode": mode, "suggestions": ["Give me a hint 💡", "I think the answer is...", "Reveal the answer 🔓"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 6. Code Debugging & Analysis Mode ("code")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "code":
        llm_reply = _llm_respond(f"Analyze, debug, or write the code requested for: '{message}'. Explain the bug/concept clearly, provide the fixed/correct clean code snippet with line-by-line explanation, and note common edge cases. Do not output raw markdown double asterisks (**).", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Run another test case 🧪", "Explain the fix step-by-step 📝", "Optimize time complexity ⚡", "Download code PDF 📄"]}
        return {"reply": code_mode(message), "mode": mode, "suggestions": ["Run another test case 🧪", "Explain the fix step-by-step 📝", "Optimize time complexity ⚡", "Download code PDF 📄"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── Project Mode ("project")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "project":
        llm_reply = _llm_respond(f"Provide a comprehensive, real-world project blueprint and implementation guide for: '{concept_query}'. Include architecture, tech stack, step-by-step implementation phases, and extension ideas.", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Show starter code 💻", "Quiz me on this architecture 🎯", "Download project PDF 📄"]}
        return {"reply": project_mode(concept_query, context), "mode": mode, "suggestions": ["Show starter code 💻", "Quiz me on this architecture 🎯", "Download project PDF 📄"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── Research Mode ("research")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "research":
        llm_reply = _llm_respond(f"Provide a detailed research analysis and comparative study on: '{concept_query}'. Contrast approaches, highlight trade-offs, state-of-the-art developments, and industry benchmarks.", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Deep explanation 🔥", "Download research PDF 📄", "Quiz me on this 🎯"]}
        return {"reply": research_mode(concept_query), "mode": mode, "suggestions": ["Deep explanation 🔥", "Download research PDF 📄", "Quiz me on this 🎯"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 7. Math & Formula Solver ("math")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "math":
        llm_reply = _llm_respond(f"Solve the mathematical formula or explain the mathematical principles for: {message}. Show clear step-by-step substitution and calculations.", context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Show another calculation 🧮", "Give a practice problem 🎯", "Explain intuitively 🌿"]}
        return {"reply": math_mode(message), "mode": mode, "suggestions": ["Show another calculation 🧮", "Give a practice problem 🎯", "Explain intuitively 🌿"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 8. Learning Path & Roadmap Mode ("path")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "path":
        target_path_topic = concept_query if is_pure_path else message
        clean_path_topic = extract_clean_concept_title(target_path_topic) or "Python"
        clean_path_topic = re.sub(r"\b(?:road\s*map|learning\s*path|curriculum|syllabus)\s*(?:of|for)?\s*", "", clean_path_topic, flags=re.I).strip() or "Python"

        path_prompt = (
            f"You are Sastra, an AI curriculum architect for Capacity Connect. "
            f"The learner {u_name} requested a complete, structured learning roadmap for: '{clean_path_topic}'.\n\n"
            f"Provide a comprehensive, beautifully structured roadmap from absolute zero to production mastery across 6 clear phases:\n"
            f"✦ Comprehensive {clean_path_topic} Learning Roadmap — From Zero to Mastery 🚀\n\n"
            f"◈ Phase 1: Core Foundations & Syntax\n"
            f"• Key Topics: Variables, Data Types, Conditionals (if/elif/else), Loops (for/while), Functions & Scope.\n"
            f"• Milestone Project: Command-line utility or interactive text game.\n\n"
            f"◈ Phase 2: Data Structures & File Operations\n"
            f"• Key Topics: Lists, Dictionaries, Tuples, Sets, List Comprehensions, File I/O (reading & writing JSON/CSV).\n"
            f"• Milestone Project: Automated log file analyzer or contacts manager.\n\n"
            f"◈ Phase 3: Object-Oriented & Modular Programming\n"
            f"• Key Topics: Classes, Objects, Inheritance, Encapsulation, Custom Exceptions, Modules & Packages.\n"
            f"• Milestone Project: Full Object-Oriented Management System with persistent data.\n\n"
            f"◈ Phase 4: Intermediate & Production Patterns\n"
            f"• Key Topics: Decorators, Generators, Context Managers, Error Handling, Virtual Environments (`venv`), Package Management (`pip`).\n"
            f"• Milestone Project: Multi-source web API client with automated retries and logging.\n\n"
            f"◈ Phase 5: Industry Specialization Tracks\n"
            f"• 🌐 Web Development: FastAPI, Django, REST APIs, Database ORMs (SQLAlchemy, PostgreSQL).\n"
            f"• 📊 Data Science & AI: NumPy, Pandas, Matplotlib, Machine Learning (Scikit-Learn, PyTorch).\n"
            f"• ⚙️ Automation & Cloud: Task automation, Selenium/Playwright, AWS SDK (`boto3`), Docker.\n\n"
            f"◈ Phase 6: Production Engineering & Capstone\n"
            f"• Unit testing with `pytest`, Git version control, CI/CD automation, and deploying to cloud production.\n\n"
            f"💡 Recommended Next Step: Ready to begin? Reply with 'Let's start learning' or click below to dive into Phase 1!\n\n"
            f"Do NOT output raw markdown double asterisks (**)."
        )
        llm_reply = _llm_respond(path_prompt, context, history, extra, "path")
        if llm_reply:
            return {"reply": llm_reply, "mode": "path", "suggestions": ["Let's start learning 🚀", "Draw visual roadmap 🎨", "Download roadmap PDF 📄", "Quiz my Python level 🎯"]}
        return {"reply": learning_path(clean_path_topic, context), "mode": "path", "suggestions": ["Let's start learning 🚀", "Draw visual roadmap 🎨", "Download roadmap PDF 📄", "Quiz my Python level 🎯"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 9. Deep Technical Explanations ("deep")
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "deep":
        target_deep_topic = concept_query if is_pure_deep else message
        clean_deep_topic = extract_clean_concept_title(target_deep_topic) or target_deep_topic.title()
        deep_prompt = (
            f"You are in DEEP EXPLANATION MODE. Provide an exhaustive, rigorous, and deep architectural masterclass on: '{clean_deep_topic}'.\n\n"
            f"Structure your response with deep technical rigor across these sections:\n"
            f"✦ {clean_deep_topic} — Comprehensive Architectural Masterclass\n\n"
            f"◈ 1. First Principles & Theoretical Foundation: Formal computer science/engineering definition, mathematical basis, and why this concept was designed.\n\n"
            f"◈ 2. Internal Mechanics & Memory Model: Explain how it operates under the hood (memory layout, stack vs heap allocation, pointers/references, runtime opcodes, hardware/compiler interaction).\n\n"
            f"◈ 3. Step-by-Step Execution Lifecycle: Detailed breakdown of runtime phases, state transitions, scope boundaries, and cleanup.\n\n"
            f"◈ 4. Production-Grade Implementation: Provide a realistic, robust code example demonstrating design patterns, defensive validation, and edge handling.\n\n"
            f"◈ 5. Performance, Complexity & Trade-offs: Analyze Big-O time and space complexity, memory footprints, and scalability bottlenecks.\n\n"
            f"◈ 6. Critical Edge Cases & Common Pitfalls: Detail failure modes, concurrency issues, memory leaks, and subtle bugs to avoid.\n\n"
            f"◈ 7. Enterprise & Production Patterns: Explain how modern distributed systems or enterprise frameworks leverage this pattern at scale.\n\n"
            f"💡 Architectural Takeaway: High-level synthesis for senior engineers.\n\n"
            f"Explain with deep, thorough technical clarity. Do NOT output raw markdown double asterisks (**)."
        )
        llm_reply = _llm_respond(deep_prompt, context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": mode, "suggestions": ["Take mastery quiz 🎯", "Download PDF study guide 📄", "Show learning path 🧭", "Explain simpler 🌿"]}
        if tk:
            return {"reply": deep_explain(tk, sk, skill, frustrated, history), "mode": mode, "suggestions": ["Take mastery quiz 🎯", "Download PDF study guide 📄", "Show learning path 🧭", "Explain simpler 🌿"]}
        return {"reply": dynamic_deep_explain(clean_deep_topic), "mode": mode, "suggestions": ["Take mastery quiz 🎯", "Download PDF study guide 📄", "Show learning path 🧭", "Explain simpler 🌿"]}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── 10. Learn Mode (Intelligent Adaptive Tutor)
    # ─────────────────────────────────────────────────────────────────────────────
    if mode == "learn" or explicit_mode == "learn":
        clean_concept = extract_clean_concept_title(concept_query if is_pure_simpler else message)

        # If user explicitly asked for a single isolated concept or clicked "Explain simpler":
        if clean_concept and (explicit_mode == "learn" or is_pure_simpler or tk):
            target_learn_topic = clean_concept
            learn_prompt = (
                f"You are in LEARNING MODE. Provide a concise, clear, and brief explanation of: '{target_learn_topic}'.\n\n"
                f"CRITICAL CONSTRAINT: Focus strictly on a clear definition and a short practical example. Keep the response brief (about 10-14 lines total). Do NOT write long essays.\n\n"
                f"Required Format:\n"
                f"✦ {target_learn_topic} — Quick Learning Guide\n\n"
                f"◈ Definition:\n(1-2 clear, simple sentences defining what it is in plain English)\n\n"
                f"❯ Everyday Intuition:\n(1 relatable everyday analogy)\n\n"
                f"❖ Code Example:\n(A concise 3-5 line practical code snippet or clear example)\n\n"
                f"💡 Key Takeaway:\n(1 single sentence summarizing the main rule)\n\n"
                f"Do NOT output raw markdown double asterisks (**)."
            )
            llm_reply = _llm_respond(learn_prompt, context, history, extra, "learn")
            if llm_reply:
                return {"reply": llm_reply, "mode": "learn", "suggestions": ["Deep explanation 🔥", "Download PDF study guide 📄", "Quiz me on this 🎯", "Draw AI diagram 🎨"]}
            if tk:
                txt = teach_topic_concise(tk, sk)
                return {"reply": txt, "mode": "learn", "suggestions": ["Deep explanation 🔥", "Download PDF study guide 📄", "Quiz me on this 🎯", "Draw AI diagram 🎨"]}
            return {"reply": dynamic_easy_learn(target_learn_topic), "mode": "learn", "suggestions": ["Deep explanation 🔥", "Download PDF study guide 📄", "Quiz me on this 🎯", "Draw AI diagram 🎨"]}
        else:
            # Fluent, natural conversational tutor response for open-ended queries, comparisons, and general discussions
            chat_prompt = (
                f"You are Sastra, an intelligent, empathetic AI learning companion for Capacity Connect. "
                f"Answer the learner {u_name}'s message conversationally, clearly, and directly:\n\n"
                f"User Message: '{message}'\n\n"
                f"Provide an engaging, natural, and helpful response. Use clean formatting with structured points (✦, ◈, ❯, ❖, 📌, 💡) if structuring concepts or steps. "
                f"Do NOT force a rigid 'Quick Learning Guide' template unless defining a single isolated concept. "
                f"NEVER output raw markdown double asterisks (**)."
            )
            llm_reply = _llm_respond(chat_prompt, context, history, extra, "learn")
            if llm_reply:
                return {"reply": llm_reply, "mode": "learn", "suggestions": ["Explain simpler 🌿", "Deep explanation 🔥", "Quiz me 🎯", "Download PDF 📄"]}
            if tk:
                txt = teach_topic_concise(tk, sk)
                return {"reply": txt, "mode": "learn", "suggestions": suggestions_for("learn", tk)}
            return {"reply": dynamic_easy_learn(clean_concept or "Core Programming Concept"), "mode": "learn", "suggestions": suggestions_for("learn", tk)}

    # ─────────────────────────────────────────────────────────────────────────────
    # ── Fallback Handling for Unmatched Queries
    # ─────────────────────────────────────────────────────────────────────────────
    if frustrated and tk:
        llm_reply = _llm_respond(message, context, history, extra, mode)
        if llm_reply:
            return {"reply": llm_reply, "mode": "learn", "suggestions": ["Explain it simply", "Give another example", "Quiz me gently"]}
        topic_data = base.TOPIC_KNOWLEDGE[tk]
        sub = topic_data["topics"].get(sk) or list(topic_data["topics"].values())[0]
        txt = (f"✦ Let's restart {sub['title']} from zero:\n\n"
               f"◈ Intuition: {sub['intuition']}\n\n"
               f"❖ Example: {sub['example']}\n\n"
               f"{repair_misconception(message)}\n\n"
               f"🎯 Check: {sub['practice']}")
        return {"reply": txt, "mode": "learn", "suggestions": ["Explain it simply", "Give another example", "Quiz me gently"]}

    if tk:
        txt = teach_topic_concise(tk, sk)
        return {"reply": txt, "mode": "learn", "suggestions": suggestions_for("learn", tk)}

    llm_reply = _llm_respond(message, context, history, extra, mode)
    if llm_reply:
        return {"reply": llm_reply, "mode": "learn", "suggestions": suggestions_for("learn", tk)}

    reply = base.process_message(message, user_id, user_name=user_name)
    intent = base.detect_intent(message)
    return {"reply": reply, "mode": intent, "suggestions": suggestions_for(intent, tk)}


def process_full(message, user_id=None, session_id="", explicit_mode=None, page_ctx=None, image_data=None, user_name=None, file_data=None, filename=None):
    res = _process_full_raw(message, user_id, session_id, explicit_mode, page_ctx, image_data, user_name=user_name, file_data=file_data, filename=filename)
    if isinstance(res, dict) and "reply" in res:
        res["reply"] = _clean_reply_text(res["reply"])
        # If the reply contains a quiz question with Option A and Option B, ensure suggestions are Option A-D
        if is_quiz_question_message(res["reply"]) and ("option a" in res["reply"].lower() or "option b" in res["reply"].lower()):
            res["suggestions"] = ["Option A", "Option B", "Option C", "Option D"]
    return res
