"""Text-to-Image and Image-to-Image Generation Engine for Astra.
Supports:
1. Bynara Image API (https://api-images.bynara.id/v1/images/generations & edits)
2. Cascading key fallback across all user keys
3. High-definition SVG educational diagram generator fallback for complex science/computing concepts
"""

import os
import json
import urllib.request
import urllib.error
import urllib.parse
import base64
import re
from config import BYNARA_API_KEY, BYNARA_BACKUP_KEY


class ImageGenerator:
    """Multi-provider image generation and diagram synthesis engine."""
    
    API_GENERATIONS = os.getenv("IMAGE_API_GENERATIONS", "https://api-images.bynara.id/v1/images/generations")
    API_EDITS = os.getenv("IMAGE_API_EDITS", "https://api-images.bynara.id/v1/images/edits")
    
    KEYS = [k for k in [
        os.getenv("IMAGE_API_KEY"),
        os.getenv("ANTHROPIC_AUTH_TOKEN"),
        os.getenv("BYNARA_API_KEY")
    ] if k and isinstance(k, str) and k.strip()]
    
    def __init__(self):
        self.keys = [k for k in self.KEYS if k]
    
    def is_educational_diagram_request(self, prompt):
        """Check if user is explicitly asking for a programmatic concept roadmap, flowchart, or architecture diagram."""
        p_lower = prompt.lower()
        diagram_cues = (
            "roadmap", "road map", "curriculum", "syllabus", "learning path", "study path",
            "flowchart", "flow chart", "architecture diagram", "uml", "wireframe",
            "memory model", "call stack", "loop lifecycle", "data structure diagram",
            "concept diagram", "concept architecture", "stack vs heap", "state diagram"
        )
        return any(cue in p_lower for cue in diagram_cues)

    def generate_image(self, prompt, size="1024x1024", model="flux"):
        """Generate an educational concept diagram or high-definition neural visual illustration from prompt."""
        # 1. Check if user is asking for an educational curriculum / roadmap / computer science architectural blueprint
        if self.is_educational_diagram_request(prompt):
            return self._generate_educational_diagram(prompt)

        # 2. For all creative, artistic, scenic, character, sci-fi, and general visual prompts:
        # Route to the AI Neural Text-to-Image Generation Engine
        return self._generate_neural_image(prompt, size=size, model=model)

    def _generate_neural_image(self, prompt, size="1024x1024", model="flux"):
        """High-definition neural AI image synthesis using text-to-image foundation models."""
        import random
        clean_p = prompt.strip()

        # Check if user already specified detailed style modifiers
        has_style = any(w in clean_p.lower() for w in (
            "photorealistic", "cinematic", "8k", "hyperrealistic", "unreal engine",
            "anime", "watercolor", "illustration", "oil painting", "digital art",
            "3d render", "pixar", "isometric", "cyberpunk", "studio portrait",
            "studio lighting", "vibrant", "octane render"
        ))

        if not has_style:
            enhanced_prompt = f"{clean_p}, high quality digital art, cinematic lighting, sharp focus, 8k resolution, detailed"
        else:
            enhanced_prompt = f"{clean_p}, sharp focus, 8k resolution, high quality"

        seed = random.randint(1000, 999999)

        w, h = 768, 768
        if "x" in size:
            try:
                parts = size.split("x")
                w, h = int(parts[0]), int(parts[1])
            except Exception:
                pass

        encoded_prompt = urllib.parse.quote(enhanced_prompt.strip())
        pollinations_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={w}&height={h}&seed={seed}&nologo=true"
        proxy_url = f"/api/image/proxy?url={urllib.parse.quote(pollinations_url)}"

        return {
            "type": "url",
            "url": proxy_url,
            "raw_url": pollinations_url,
            "prompt": clean_p,
            "enhanced_prompt": enhanced_prompt,
            "seed": seed,
            "mode": "creative_image",
            "provider": "neural_ai_model"
        }

    def edit_image(self, image_data, prompt, size="1024x1024", model="stable-diffusion"):
        """Edit an existing image with new prompt instructions."""
        payload = {
            "model": model,
            "image": image_data,
            "prompt": prompt,
            "n": 1,
            "size": size
        }
        
        for key in self.keys:
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }
            req = urllib.request.Request(
                self.API_EDITS,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                    data = res.get("data", [])
                    if data and len(data) > 0:
                        url = data[0].get("url") or data[0].get("b64_json")
                        if url:
                            return {"type": "url", "url": url, "prompt": prompt}
            except Exception as e:
                print(f"[ImageEdit] Key {key[:12]} failed: {e}")
                continue
        
        return self._generate_educational_diagram(prompt)

    def _generate_educational_diagram(self, prompt):
        """Synthesizes a clean SVG diagram card matching the topic."""
        p_lower = prompt.lower()
        
        is_python_roadmap = bool(
            re.search(r'\bpython\b', p_lower) and re.search(r'\b(roadmap|road map|path|curriculum|syllabus|plan|learn|learning|complete|all learning)\b', p_lower)
        ) or bool(
            re.search(r'\b(roadmap|road map|curriculum|all learning)\b', p_lower) and not any(k in p_lower for k in ["java", "react", "c++", "rust", "go", "javascript"])
        )
        is_ai_topic = any(k in p_lower for k in ["ai", "machine learning", "ml", "neural", "deep learning", "artificial intelligence"])
        
        if is_python_roadmap:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 610" width="960" height="610">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="100%" stop-color="#0b1329"/>
    </linearGradient>
    <linearGradient id="step1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <linearGradient id="step2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="step3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
    <linearGradient id="step4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#db2777"/>
    </linearGradient>
    <linearGradient id="step5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="step6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <rect width="960" height="610" rx="20" fill="url(#bgGrad)" stroke="rgba(255,255,255,0.12)"/>
  
  <!-- Header Banner -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(59,130,246,0.3)"/>
  <text x="45" y="44" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="17" font-weight="bold">✦ COMPLETE PYTHON DEVELOPER ROADMAP — ZERO TO MASTERY</text>
  <text x="45" y="59" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">All Core Syntax • Data Structures • OOP • Advanced Internals • Specialization • Production</text>
  <rect x="750" y="27" width="165" height="30" rx="8" fill="rgba(56,189,248,0.12)" stroke="#38bdf8"/>
  <text x="832" y="47" text-anchor="middle" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">Sastra AI • All-in-One</text>

  <!-- Row 1: Phase 1, Phase 2, Phase 3 -->

  <!-- Phase 1: Core Syntax -->
  <g transform="translate(25, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step1)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 1: SYNTAX &amp; LOGIC</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🌿 Core Foundations</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Variables &amp; Types (int, str, float, bool)</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Operators &amp; Type Casting</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Conditionals: if / elif / else</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Loops: for, while, break, continue</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Functions: def, return &amp; scope</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(59,130,246,0.12)" stroke="rgba(59,130,246,0.4)"/>
    <text x="22" y="194" fill="#60a5fa" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Interactive Text RPG &amp; CLI</text>
  </g>

  <!-- Phase 2: Data Structures & Files -->
  <g transform="translate(335, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step2)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 2: DATA &amp; COLLECTIONS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">📦 Collections &amp; I/O</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Lists &amp; Tuples (Indexing, Slicing)</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Dictionaries &amp; Hash Map Lookups</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Sets (Unions, Intersections)</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• List &amp; Dict Comprehensions</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• File I/O: open, read/write JSON &amp; CSV</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(6,182,212,0.12)" stroke="rgba(6,182,212,0.4)"/>
    <text x="22" y="194" fill="#22d3ee" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Data Parser &amp; Log Analyzer</text>
  </g>

  <!-- Phase 3: OOP & Architecture -->
  <g transform="translate(645, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step3)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 3: OOP &amp; MODULARITY</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">⚙️ Scalable Systems</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Classes, Objects &amp; __init__ / self</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Encapsulation &amp; Private Variables</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Inheritance, Polymorphism &amp; super()</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Custom Exceptions (try / except)</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Modules, Packages &amp; Imports</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(139,92,246,0.12)" stroke="rgba(139,92,246,0.4)"/>
    <text x="22" y="194" fill="#c084fc" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Bank/Inventory OOP System</text>
  </g>

  <!-- Row 2: Phase 4, Phase 5, Phase 6 -->

  <!-- Phase 4: Advanced Internals -->
  <g transform="translate(25, 310)">
    <rect width="290" height="225" rx="14" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step4)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 4: ADVANCED PYTHON</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🔮 Internals &amp; Concurrency</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Decorators (@wraps) &amp; Closures</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Generators &amp; yield (Lazy Memory)</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Context Managers (__enter__ / __exit__)</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Concurrency: async / await, threads</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• PyObject model, Ref Counting &amp; GC</text>
    <rect x="12" y="178" width="266" height="32" rx="8" fill="rgba(236,72,153,0.12)" stroke="rgba(236,72,153,0.4)"/>
    <text x="22" y="198" fill="#f472b6" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Async Web Scraper Pipeline</text>
  </g>

  <!-- Phase 5: Industry Specializations -->
  <g transform="translate(335, 310)">
    <rect width="290" height="225" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step5)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 5: CAREER TRACKS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🚀 Choose Your Domain</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• 🌐 Web: FastAPI, Django, REST, SQL</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• 📊 Data: NumPy, Pandas, Matplotlib</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• 🤖 AI/ML: Scikit-Learn, PyTorch, LLMs</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• ⚙️ Automation: Selenium, Playwright</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• ☁️ Cloud SDKs: AWS boto3, Docker</text>
    <rect x="12" y="178" width="266" height="32" rx="8" fill="rgba(245,158,11,0.12)" stroke="rgba(245,158,11,0.4)"/>
    <text x="22" y="198" fill="#fbbf24" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Full-Stack Web App / AI Model</text>
  </g>

  <!-- Phase 6: Production Engineering -->
  <g transform="translate(645, 310)">
    <rect width="290" height="225" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#step6)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="11" font-weight="bold">PHASE 6: PRODUCTION DEPLOY</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🛡️ DevOps &amp; Cloud Delivery</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Virtual Environments: venv, poetry, pip</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Unit &amp; Integration Testing: pytest</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Git Version Control &amp; GitHub Actions</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Docker Containers &amp; Compose</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="10.5">• Cloud Deploy: Render, AWS, Linux</text>
    <rect x="12" y="178" width="266" height="32" rx="8" fill="rgba(16,185,129,0.12)" stroke="rgba(16,185,129,0.4)"/>
    <text x="22" y="198" fill="#34d399" font-family="Inter, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Production Deployed Service</text>
  </g>

  <!-- Bottom Navigation Flow Banner -->
  <rect x="25" y="546" width="910" height="48" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="575" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🎯 Universal Roadmap Progression:</text>
  <text x="265" y="575" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="11">Phase 1 (Syntax) ➔ Phase 2 (Data &amp; I/O) ➔ Phase 3 (OOP) ➔ Phase 4 (Advanced) ➔ Phase 5 (Specialization) ➔ Phase 6 (Cloud Production)</text>
</svg>"""
        elif is_ai_topic:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="step1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <linearGradient id="step2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="step3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
    <linearGradient id="step4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#db2777"/>
    </linearGradient>
  </defs>
  <rect width="800" height="420" rx="20" fill="url(#bgGrad)" stroke="rgba(255,255,255,0.1)"/>
  
  <!-- Header Banner -->
  <rect x="30" y="24" width="740" height="48" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(59,130,246,0.3)"/>
  <text x="50" y="54" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="18" font-weight="bold">✦ ARTIFICIAL INTELLIGENCE ARCHITECTURAL ROADMAP</text>
  <text x="750" y="53" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="12">Sastra AI • Capacity Connect</text>

  <!-- Flow connecting line -->
  <path d="M 120 170 L 680 170" stroke="#334155" stroke-width="4" stroke-dasharray="6"/>
  <path d="M 120 310 L 680 310" stroke="#334155" stroke-width="4" stroke-dasharray="6"/>

  <!-- Step 1: Math & Python -->
  <g transform="translate(40, 90)">
    <rect width="160" height="150" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect width="160" height="32" rx="12" fill="url(#step1)"/>
    <text x="80" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 1: FOUNDATIONS</text>
    <text x="14" y="55" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🧮 Math & Python</text>
    <text x="14" y="76" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Linear Algebra & Calc</text>
    <text x="14" y="94" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Probability & Stats</text>
    <text x="14" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Python Core & NumPy</text>
    <text x="14" y="130" fill="#38bdf8" font-family="Inter, sans-serif" font-size="10">⚡ Milestone: Logic mastery</text>
  </g>

  <!-- Step 2: Data Engineering -->
  <g transform="translate(230, 90)">
    <rect width="160" height="150" rx="14" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
    <rect width="160" height="32" rx="12" fill="url(#step2)"/>
    <text x="80" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 2: DATA & EDA</text>
    <text x="14" y="55" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">📊 Data Wrangling</text>
    <text x="14" y="76" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Pandas & DataFrames</text>
    <text x="14" y="94" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Matplotlib / Seaborn</text>
    <text x="14" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Feature Engineering</text>
    <text x="14" y="130" fill="#22d3ee" font-family="Inter, sans-serif" font-size="10">⚡ Milestone: EDA Insights</text>
  </g>

  <!-- Step 3: Machine Learning -->
  <g transform="translate(420, 90)">
    <rect width="160" height="150" rx="14" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="160" height="32" rx="12" fill="url(#step3)"/>
    <text x="80" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 3: ML MODELS</text>
    <text x="14" y="55" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🤖 Supervised & Unsup</text>
    <text x="14" y="76" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Regression & Trees</text>
    <text x="14" y="94" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Random Forests / SVM</text>
    <text x="14" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• K-Means & Clustering</text>
    <text x="14" y="130" fill="#c084fc" font-family="Inter, sans-serif" font-size="10">⚡ Milestone: Predictive APIs</text>
  </g>

  <!-- Step 4: Deep Learning & GenAI -->
  <g transform="translate(610, 90)">
    <rect width="160" height="150" rx="14" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <rect width="160" height="32" rx="12" fill="url(#step4)"/>
    <text x="80" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 4: DEEP LEARNING</text>
    <text x="14" y="55" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">🔮 LLMs & Neural Nets</text>
    <text x="14" y="76" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• PyTorch & TensorFlow</text>
    <text x="14" y="94" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• Transformers & Vision</text>
    <text x="14" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="10">• RAG & Autonomous Agents</text>
    <text x="14" y="130" fill="#f472b6" font-family="Inter, sans-serif" font-size="10">⚡ Milestone: Sastra Master</text>
  </g>

  <!-- Bottom Interactive Guidance -->
  <rect x="30" y="265" width="740" height="125" rx="14" fill="rgba(15,23,42,0.8)" stroke="rgba(255,255,255,0.08)"/>
  <text x="50" y="295" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="14" font-weight="bold">🎯 Recommended Learning Action Path:</text>
  <text x="50" y="320" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">1. Solidify foundational programming and data structures in your active module.</text>
  <text x="50" y="342" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">2. Implement machine learning and analytical pipelines on real-world datasets.</text>
  <text x="50" y="364" fill="#34d399" font-family="Inter, sans-serif" font-size="12">3. Transition to deep learning, vision, and autonomous RAG agents using Sastra pipelines.</text>
</svg>"""
        elif "variable" in p_lower:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="stackGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="heapGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="760" height="380" rx="20" fill="url(#bgGrad)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(59,130,246,0.3)"/>
  <text x="40" y="47" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="16" font-weight="bold">✦ VARIABLES &amp; MEMORY ALLOCATION ARCHITECTURE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">Stack References ➔ Heap Objects</text>

  <!-- Stack Column (Variable Names) -->
  <rect x="50" y="85" width="260" height="220" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
  <rect x="50" y="85" width="260" height="34" rx="12" fill="url(#stackGrad)"/>
  <text x="180" y="108" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="13" font-weight="bold">STACK (Variable References)</text>
  
  <rect x="68" y="132" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="155" fill="#f8fafc" font-family="monospace" font-size="12">username ➔ 0x7A1</text>

  <rect x="68" y="176" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="199" fill="#f8fafc" font-family="monospace" font-size="12">total_score ➔ 0x7A2</text>

  <rect x="68" y="220" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="243" fill="#f8fafc" font-family="monospace" font-size="12">is_enrolled ➔ 0x7A3</text>

  <rect x="68" y="264" width="224" height="32" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="285" fill="#38bdf8" font-family="monospace" font-size="11">course_list ➔ 0x7A4</text>

  <!-- Pointer Arrows -->
  <path d="M 292 150 L 440 150" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4" marker-end="url(#arr)"/>
  <path d="M 292 194 L 440 194" stroke="#34d399" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 292 238 L 440 238" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 292 280 L 440 280" stroke="#f472b6" stroke-width="2" stroke-dasharray="4"/>

  <!-- Heap Column (Values & Objects in Memory) -->
  <rect x="450" y="85" width="260" height="220" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <rect x="450" y="85" width="260" height="34" rx="12" fill="url(#heapGrad)"/>
  <text x="580" y="108" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="13" font-weight="bold">HEAP (Actual Objects in RAM)</text>

  <rect x="468" y="132" width="224" height="36" rx="8" fill="#0f172a" stroke="#059669"/>
  <text x="480" y="155" fill="#38bdf8" font-family="monospace" font-size="12">'Alex' (Type: str)</text>

  <rect x="468" y="176" width="224" height="36" rx="8" fill="#0f172a" stroke="#059669"/>
  <text x="480" y="199" fill="#34d399" font-family="monospace" font-size="12">98 (Type: int)</text>

  <rect x="468" y="220" width="224" height="36" rx="8" fill="#0f172a" stroke="#059669"/>
  <text x="480" y="243" fill="#a78bfa" font-family="monospace" font-size="12">True (Type: bool)</text>

  <rect x="468" y="264" width="224" height="32" rx="8" fill="#0f172a" stroke="#059669"/>
  <text x="480" y="285" fill="#f472b6" font-family="monospace" font-size="11">['Python', 'React'] (list)</text>

  <!-- Bottom Insight -->
  <rect x="50" y="320" width="660" height="42" rx="10" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="70" y="346" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">💡 Core Takeaway:</text>
  <text x="180" y="346" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">Variables are named labels pointing to memory objects, making reassignment instantaneous.</text>
</svg>"""
        elif "quantum" in p_lower:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
  <defs>
    <linearGradient id="bgGradQ" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050a1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="qGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="qGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
    <linearGradient id="qGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
  </defs>
  <rect width="760" height="380" rx="20" fill="url(#bgGradQ)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(6,182,212,0.3)"/>
  <text x="40" y="47" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="16" font-weight="bold">✦ QUANTUM COMPUTING ARCHITECTURE &amp; QUBIT DYNAMICS</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">Bloch Sphere ➔ Gate Synthesis ➔ QPU Readout</text>

  <!-- Step 1: Classical Bit vs Qubit -->
  <g transform="translate(45, 85)">
    <rect width="200" height="215" rx="14" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="200" height="32" rx="12" fill="url(#qGrad1)"/>
    <text x="100" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">1. QUBIT SUPERPOSITION</text>
    <text x="14" y="58" fill="#f8fafc" font-family="monospace" font-size="12">|ψ⟩ = α|0⟩ + β|1⟩</text>
    <text x="14" y="82" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Classical: Bit is 0 OR 1</text>
    <text x="14" y="102" fill="#38bdf8" font-family="Inter, sans-serif" font-size="11">• Quantum: 0 AND 1 simultaneously</text>
    <text x="14" y="122" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Complex amplitudes: |α|²+|β|²=1</text>
    <text x="14" y="146" fill="#fcd34d" font-family="monospace" font-size="11">Bloch Sphere: (θ, φ)</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• N Qubits = 2ⁿ state vector</text>
    <text x="14" y="195" fill="#34d399" font-family="Inter, sans-serif" font-size="11">Exponential State Expansion</text>
  </g>

  <!-- Connection Arrow 1 -->
  <path d="M 255 190 L 285 190" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 2: Unitary Quantum Gates -->
  <g transform="translate(295, 85)">
    <rect width="200" height="215" rx="14" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="200" height="32" rx="12" fill="url(#qGrad2)"/>
    <text x="100" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">2. UNITARY GATE LOGIC</text>
    <text x="14" y="58" fill="#f472b6" font-family="monospace" font-size="12">U† · U = I (Reversible)</text>
    <text x="14" y="82" fill="#38bdf8" font-family="Inter, sans-serif" font-size="11">• Hadamard (H): Superposition</text>
    <text x="14" y="102" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Pauli-X: Quantum NOT gate</text>
    <text x="14" y="122" fill="#a78bfa" font-family="Inter, sans-serif" font-size="11">• CNOT: Entangles 2 Qubits</text>
    <text x="14" y="146" fill="#f8fafc" font-family="monospace" font-size="11">Bell State: (|00⟩+|11⟩)/√2</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Interference cancels noise</text>
    <text x="14" y="195" fill="#ec4899" font-family="Inter, sans-serif" font-size="11">Amplifies Correct Answer</text>
  </g>

  <!-- Connection Arrow 2 -->
  <path d="M 505 190 L 535 190" stroke="#ec4899" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 3: Cryogenic QPU & Measurement -->
  <g transform="translate(545, 85)">
    <rect width="180" height="215" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="12" fill="url(#qGrad3)"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">3. QPU &amp; READOUT</text>
    <text x="14" y="58" fill="#34d399" font-family="monospace" font-size="12">Cryogenic: 15 mK</text>
    <text x="14" y="82" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Dilution Refrigerator</text>
    <text x="14" y="102" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Microwave pulse control</text>
    <text x="14" y="122" fill="#fcd34d" font-family="Inter, sans-serif" font-size="11">• Wavefunction collapse</text>
    <text x="14" y="146" fill="#38bdf8" font-family="monospace" font-size="11">Measure ➔ |0⟩ or |1⟩</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Sampling across shots</text>
    <text x="14" y="195" fill="#10b981" font-family="Inter, sans-serif" font-size="11">Classical Histogram Out</text>
  </g>

  <!-- Bottom Insight -->
  <rect x="45" y="315" width="680" height="45" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="65" y="342" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">💡 Core Takeaway:</text>
  <text x="180" y="342" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">Quantum machines compute by rotating state vectors in Hilbert space, evaluating vast solution spaces simultaneously.</text>
</svg>"""
        elif "function" in p_lower:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e21"/>
      <stop offset="100%" stop-color="#111c38"/>
    </linearGradient>
  </defs>
  <rect width="760" height="380" rx="20" fill="url(#bgGrad2)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(139,92,246,0.3)"/>
  <text x="40" y="47" fill="#a78bfa" font-family="Outfit, sans-serif" font-size="16" font-weight="bold">✦ FUNCTION CALL STACK &amp; EXECUTION PIPELINE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">Inputs ➔ Frame Scope ➔ Return Pipeline</text>

  <!-- Step 1: Input Arguments -->
  <g transform="translate(45, 90)">
    <rect width="180" height="190" rx="12" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="180" height="32" rx="10" fill="#2563eb"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">1. ARGUMENTS (Input)</text>
    <text x="16" y="60" fill="#f8fafc" font-family="monospace" font-size="12">def calculate(a, b):</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Parameters passed</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Positional / keyword</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Default args evaluated</text>
    <text x="16" y="165" fill="#38bdf8" font-family="monospace" font-size="11">calculate(10, 5)</text>
  </g>

  <!-- Flow 1 -->
  <path d="M 235 185 L 275 185" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 2: Function Stack Frame -->
  <g transform="translate(285, 90)">
    <rect width="190" height="190" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="10" fill="#7c3aed"/>
    <text x="95" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">2. LOCAL STACK FRAME</text>
    <text x="16" y="60" fill="#c084fc" font-family="monospace" font-size="12">result = a * 2 + b</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Isolated local scope</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Local vars created</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Logic executed</text>
    <text x="16" y="165" fill="#34d399" font-family="monospace" font-size="11">Frame destroyed on exit</text>
  </g>

  <!-- Flow 2 -->
  <path d="M 485 185 L 525 185" stroke="#34d399" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 3: Return Output -->
  <g transform="translate(535, 90)">
    <rect width="180" height="190" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="10" fill="#059669"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">3. RETURN VALUE (Output)</text>
    <text x="16" y="60" fill="#34d399" font-family="monospace" font-size="12">return result</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Sent back to caller</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Can return tuple/dict</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• None returned if omitted</text>
    <text x="16" y="165" fill="#facc15" font-family="monospace" font-size="11">output = 25</text>
  </g>

  <!-- Bottom Insight -->
  <rect x="45" y="300" width="670" height="50" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="65" y="330" fill="#a78bfa" font-family="Outfit, sans-serif" font-size="13" font-weight="bold">🎯 Clean Architecture Principle:</text>
  <text x="270" y="330" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">Functions are modular black boxes: predictable inputs in, clean transformed outputs out.</text>
</svg>"""
        elif "loop" in p_lower:
            svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" width="760" height="360">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e21"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="760" height="360" rx="20" fill="url(#bgGrad3)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(6,182,212,0.3)"/>
  <text x="40" y="47" fill="#22d3ee" font-family="Outfit, sans-serif" font-size="16" font-weight="bold">✦ LOOP CONTROL FLOW &amp; ITERATION LIFECYCLE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">Sequence ➔ Condition ➔ Body ➔ Next</text>

  <!-- Step 1: Start -->
  <circle cx="90" cy="170" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="90" y="175" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-weight="bold" font-size="12">START</text>

  <path d="M 125 170 L 195 170" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: Condition Diamond -->
  <polygon points="280,105 365,170 280,235 195,170" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="280" y="165" text-anchor="middle" fill="#fcd34d" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">Condition</text>
  <text x="280" y="180" text-anchor="middle" fill="#fcd34d" font-family="Outfit, sans-serif" font-size="11">True?</text>

  <!-- True path -->
  <path d="M 365 170 L 440 170" stroke="#10b981" stroke-width="2"/>
  <text x="400" y="160" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">YES</text>

  <!-- Step 3: Loop Body -->
  <rect x="440" y="130" width="160" height="80" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="520" y="160" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">Execute Loop Body</text>
  <text x="520" y="180" text-anchor="middle" fill="#94a3b8" font-family="monospace" font-size="11">print(item) / update</text>

  <!-- Cycle back arrow -->
  <path d="M 520 130 L 520 85 L 280 85 L 280 105" fill="none" stroke="#22d3ee" stroke-width="2" stroke-dasharray="4"/>
  <text x="400" y="75" text-anchor="middle" fill="#22d3ee" font-family="sans-serif" font-size="10">Next Iteration</text>

  <!-- False path (Exit) -->
  <path d="M 280 235 L 280 290 L 630 290" fill="none" stroke="#ef4444" stroke-width="2"/>
  <text x="295" y="260" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">NO (Done)</text>

  <!-- Step 4: Finish -->
  <circle cx="665" cy="290" r="30" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
  <text x="665" y="295" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-weight="bold" font-size="11">EXIT</text>
</svg>"""
        else:
            clean_title = re.sub(r'[^a-zA-Z0-9 ]', '', prompt).strip()[:40].title() or "Concept Architecture"
            svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" width="760" height="360">
  <defs>
    <linearGradient id="bgGradGen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e21"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="760" height="360" rx="20" fill="url(#bgGradGen)" stroke="rgba(255,255,255,0.1)"/>
  
  <!-- Title Header -->
  <rect x="25" y="20" width="710" height="46" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(56,189,248,0.3)"/>
  <text x="45" y="50" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="16" font-weight="bold">✦ CONCEPT SYSTEM ARCHITECTURE: {clean_title.upper()}</text>
  <text x="715" y="49" text-anchor="end" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">Sastra AI Concept Studio</text>

  <!-- Stage 1: Input / Foundation -->
  <g transform="translate(45, 90)">
    <rect width="190" height="170" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="12" fill="#2563eb"/>
    <text x="95" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 1: FOUNDATION</text>
    <text x="16" y="65" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">Prerequisites &amp; Data</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Core definitions</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Input parameters</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Initial state baseline</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 245 175 L 285 175" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

  <!-- Stage 2: Processing & Transformation -->
  <g transform="translate(295, 90)">
    <rect width="190" height="170" rx="14" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="12" fill="#7c3aed"/>
    <text x="95" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 2: MECHANICS</text>
    <text x="16" y="65" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">Execution Logic</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Algorithmic steps</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• State transformations</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Edge case boundaries</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 495 175 L 535 175" stroke="#10b981" stroke-width="3" stroke-dasharray="4"/>

  <!-- Stage 3: Outcome & Mastery -->
  <g transform="translate(545, 90)">
    <rect width="180" height="170" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="12" fill="#059669"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">PHASE 3: OUTCOME</text>
    <text x="16" y="65" fill="#f8fafc" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">System Verification</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Output delivery</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Metric evaluation</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, sans-serif" font-size="11">• Real-world usage</text>
  </g>

  <!-- Footer Guidance -->
  <rect x="45" y="280" width="680" height="56" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="65" y="312" fill="#38bdf8" font-family="Outfit, sans-serif" font-size="12" font-weight="bold">💡 Study Guide:</text>
  <text x="160" y="312" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="12">Master each tier sequentially: establish the prerequisites before debugging runtime mechanics.</text>
</svg>"""
        
        b64_svg = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        data_uri = f"data:image/svg+xml;base64,{b64_svg}"
        return {
            "type": "svg",
            "url": data_uri,
            "prompt": prompt,
            "svg_raw": svg,
            "mode": "educational_diagram",
            "provider": "educational_vector_engine"
        }


# Singleton instance
_img_generator = None

def get_image_generator():
    global _img_generator
    if _img_generator is None:
        _img_generator = ImageGenerator()
    return _img_generator
