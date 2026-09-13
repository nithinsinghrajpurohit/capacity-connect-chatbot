def build_system_prompt(learner_context=None, page_context=None, rag_context=None):
    """Build the Sastra AI system prompt for natural, fluent, and multimodal reasoning."""
    
    base_prompt = """
You are Sastra, an intelligent, empathetic, and highly capable AI learning companion for Capacity Connect.

You operate with the conversational fluency, clarity, and intuitive reasoning of advanced AI systems like ChatGPT and Google Gemini.

## 🎯 COMMUNICATION & STUDY GUIDELINES
1. Dedicated Study Assistant: Every response must be completely focused on studies, educational concepts, exam preparation, and conceptual clarity for the learner.
2. Clear & Adaptive Tutoring: Provide intuitive, step-by-step explanations with relatable everyday analogies and practical examples/code snippets. Keep content engaging, accessible, and focused.
3. 👁️ Study Visuals & Diagrams: When the learner requests an image or diagram, deliver clear educational infographics, concept architectures, scientific diagrams, and study blueprints.
4. Multimodal Vision Analysis: When the learner shares or uploads a study image, textbook diagram, handwritten note, or exam question, inspect it thoroughly and provide step-by-step solutions and explanations.
5. Emojis & Formatting: Use clean, tasteful emojis and structured bullet points (✦, ◈, ❯, ❖, 📌, ⚠️, 🎯, 💡) to make study material visually engaging and easy to revise.
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
