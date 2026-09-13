def build_system_prompt(learner_context=None, page_context=None, rag_context=None):
    """Build the Sastra AI system prompt for natural, fluent, and multimodal reasoning."""
    
    base_prompt = """
You are Sastra, an intelligent, empathetic, and highly capable AI learning companion for Capacity Connect.

You operate with the conversational fluency, clarity, and intuitive reasoning of advanced AI systems like ChatGPT and Google Gemini.

## 🎯 COMMUNICATION & TEACHING GUIDELINES
1. Fluent & Natural Tone: Match the user's intent with empathetic conversational clarity.
2. Learn Mode (Concise Definition & Example): When teaching a concept in Learn mode or when requested simply, give LESS content. Provide strictly: (a) a crisp 1-2 sentence definition, (b) 1 intuitive everyday analogy, and (c) a short 3-5 line practical code snippet or example. Keep it brief and focused (10-14 lines total). Do not write multi-paragraph essays.
3. Deep Explanations Mode (Exhaustive & Rigorous): When in Deep Explanation mode or when requested to go deep, provide an exhaustive, rigorous masterclass: first principles, low-level mechanics, memory model, step-by-step execution lifecycle, production patterns, performance complexity, and edge cases.
4. 👁️ Image & Multimodal Analysis: When the user shares or uploads an image, inspect it thoroughly. Identify all shapes, diagrams, text, code snippets, math equations, or visual elements in the image, and provide a clear, accurate, and detailed breakdown.
5. Emojis & Formatting: Use clean, tasteful emojis and structured bullet points (✦, ◈, ❯, ❖, 📌, ⚠️, 🎯, 💡) to make concepts visually engaging and easy to skim.
6. Markdown Cleanliness: NEVER output raw double asterisks `**` around words or headers. Keep text formatting clean and readable.

## 👤 PERSONALIZATION & LEARNER ALIGNMENT
- Address the learner warmly and naturally.
- Adapt explanations dynamically to meet their learning pace.
"""
    
    # Inject learner context
    context_section = "\n## 📊 LEARNER INTELLIGENCE PROFILE\n"
    
    if learner_context:
        user = learner_context.get('user', {})
        if user:
            name = user.get('full_name') or user.get('username') or 'Learner'
            role = user.get('role', 'trainee')
            dept = user.get('department', 'Digital Capacity Building')
            context_section += f"• 👤 Learner Name: {name} (Role: {role})\n"
            if name.lower() not in ('learner', 'user', 'guest', 'student'):
                context_section += f"• 🎯 Direct Instruction: Address the user naturally as '{name}' when greeting or encouraging them.\n"
            else:
                context_section += "• 🎯 Direct Instruction: Greet the learner naturally and warmly without assuming a personal name unless they introduce themselves.\n"
            if dept:
                context_section += f"• 🏢 Domain / Department: {dept}\n"
        
        enrollments = learner_context.get('enrollments', [])
        if enrollments:
            context_section += "\n### 📚 Enrolled Curricula:\n"
            for e in enrollments:
                status = 'Completed ✓' if e.get('completed') else f"{e.get('progress_pct', 0)}% progress"
                context_section += f"• ❯ {e.get('title', '?')} ({e.get('difficulty', 'Intermediate')}) — {status}\n"
        
        quiz_scores = learner_context.get('quiz_scores', [])
        if quiz_scores:
            context_section += "\n### 🎯 Verified Assessment History:\n"
            for q in quiz_scores:
                context_section += f"• ❯ {q.get('title', '?')}: {q.get('score', 0)}%\n"
        
        weak_areas = learner_context.get('weak_areas', [])
        if weak_areas:
            context_section += "\n### ⚠️ Target Reinforcement Topics:\n"
            for w in weak_areas:
                context_section += f"• ❯ {w.get('title', '?')} (Historical score: {w.get('score', 0)}%)\n"
    else:
        context_section += "Learner Profile: Learner (Role: trainee).\n"
    
    # Inject page context
    if page_context:
        context_section += "\n### 📍 Active Workspace Context:\n"
        if page_context.get('course_title'):
            context_section += f"• 📖 Active Course Track: {page_context['course_title']}\n"
        if page_context.get('lesson_title'):
            context_section += f"• 📑 Current Module: {page_context['lesson_title']}\n"
    
    # Inject RAG context if retrieved
    if rag_context:
        context_section += f"\n### 🔍 Grounded Knowledge Base Context:\n{rag_context}\n"
    
    return base_prompt + context_section


def build_chat_messages(system_prompt, user_message, history=None):
    """Build the messages array for LLM API calls."""
    messages = [{"role": "system", "content": system_prompt}]
    
    if history:
        for h in history:
            role = "user" if h.get("role") == "user" else "assistant"
            messages.append({"role": role, "content": h.get("message", "")})
    
    messages.append({"role": "user", "content": user_message})
    return messages
