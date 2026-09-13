"""High-Definition Vector SVG Blueprints and Subject Roadmap Generators for Sastra AI.
Generates 100% razor-sharp vector infographics with crystal-clear English typography,
color-coded phase progression, milestone cards, and zero blurriness.
"""

import re


def build_python_roadmap_svg():
    """Complete 6-Phase Python Developer S-Curve Pathway Roadmap (Zero to Mastery)."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" width="1000" height="640">
  <defs>
    <linearGradient id="pyBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070e1e"/>
      <stop offset="50%" stop-color="#0c1833"/>
      <stop offset="100%" stop-color="#081022"/>
    </linearGradient>
    <linearGradient id="pyBlueGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#387eb8"/>
      <stop offset="50%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1000" height="640" rx="24" fill="url(#pyBg)" stroke="rgba(56,126,184,0.3)" stroke-width="1.5"/>

  <!-- Subtle Tech Grid -->
  <path d="M 0,100 L 1000,100 M 0,200 L 1000,200 M 0,300 L 1000,300 M 0,400 L 1000,400 M 0,500 L 1000,500" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
  <path d="M 200,0 L 200,640 M 400,0 L 400,640 M 600,0 L 600,640 M 800,0 L 800,640" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>

  <!-- Header Section -->
  <g transform="translate(30, 22)">
    <rect width="940" height="58" rx="14" fill="rgba(15,23,42,0.85)" stroke="rgba(250,204,21,0.3)" stroke-width="1"/>
    <circle cx="36" cy="29" r="17" fill="#387eb8"/>
    <text x="36" y="36" text-anchor="middle" fill="#ffe873" font-family="Outfit, Arial, sans-serif" font-size="19">🐍</text>
    <text x="68" y="34" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">PYTHON DEVELOPER ROADWAY — COMPLETE JOURNEY</text>
    <text x="68" y="49" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">S-Curve Pathway: Syntax ➔ Data Structures ➔ OOP ➔ Concurrency ➔ Specialization ➔ Cloud Production</text>
    <rect x="785" y="14" width="140" height="30" rx="8" fill="rgba(250,204,21,0.12)" stroke="#facc15" stroke-width="1"/>
    <text x="855" y="34" text-anchor="middle" fill="#facc15" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Sastra AI Vector</text>
  </g>

  <!-- Dynamic S-Curve Track Connecting Path -->
  <path d="M 180,195 C 280,195 320,195 430,195 C 540,195 620,195 720,195 C 860,195 860,370 720,370 C 600,370 480,370 320,370 C 120,370 120,535 300,535 C 440,535 640,535 840,535" 
        fill="none" stroke="#172554" stroke-width="16" stroke-linecap="round" opacity="0.7"/>
  <path d="M 180,195 C 280,195 320,195 430,195 C 540,195 620,195 720,195 C 860,195 860,370 720,370 C 600,370 480,370 320,370 C 120,370 120,535 300,535 C 440,535 640,535 840,535" 
        fill="none" stroke="url(#pyBlueGold)" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="10 8"/>

  <!-- Stage 1: Syntax & Logic (Top Left) -->
  <g transform="translate(35, 105)" filter="url(#cardShadow)">
    <rect width="265" height="175" rx="14" fill="#091124" stroke="#387eb8" stroke-width="2"/>
    <rect width="265" height="32" rx="12" fill="#387eb8"/>
    <circle cx="22" cy="16" r="10" fill="#facc15"/>
    <text x="22" y="20" text-anchor="middle" fill="#080e1e" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">1</text>
    <text x="42" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">SYNTAX &amp; CONTROL FLOW</text>
    <text x="14" y="56" fill="#60a5fa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🌿 Core Language</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Variables &amp; Types (int, float, str, bool)</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Conditionals: if / elif / else &amp; Match</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Loops: for, while, break, continue</text>
    <text x="14" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Functions: def, *args, **kwargs, return</text>
    <rect x="12" y="142" width="241" height="24" rx="6" fill="rgba(56,126,184,0.15)" stroke="rgba(56,126,184,0.4)"/>
    <text x="132" y="158" text-anchor="middle" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="10" font-weight="bold">⚡ Milestone: Interactive CLI App</text>
  </g>

  <!-- Stage 2: Data Structures & Collections (Top Center) -->
  <g transform="translate(365, 105)" filter="url(#cardShadow)">
    <rect width="270" height="175" rx="14" fill="#091124" stroke="#06b6d4" stroke-width="2"/>
    <rect width="270" height="32" rx="12" fill="#06b6d4"/>
    <circle cx="22" cy="16" r="10" fill="#ffffff"/>
    <text x="22" y="20" text-anchor="middle" fill="#0891b2" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">2</text>
    <text x="42" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">DATA STRUCTURES &amp; I/O</text>
    <text x="14" y="56" fill="#22d3ee" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">📦 Collections &amp; Files</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Lists, Tuples &amp; Slicing Operations</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Dictionaries &amp; Hash Map Key Lookups</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Sets (Unions, Intersections, Diff)</text>
    <text x="14" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• File I/O: JSON, CSV &amp; with statement</text>
    <rect x="12" y="142" width="246" height="24" rx="6" fill="rgba(6,182,212,0.15)" stroke="rgba(6,182,212,0.4)"/>
    <text x="135" y="158" text-anchor="middle" fill="#67e8f9" font-family="Inter, Arial, sans-serif" font-size="10" font-weight="bold">⚡ Milestone: JSON/CSV Data Parser</text>
  </g>

  <!-- Stage 3: OOP & Modularity (Top Right) -->
  <g transform="translate(695, 105)" filter="url(#cardShadow)">
    <rect width="270" height="175" rx="14" fill="#091124" stroke="#facc15" stroke-width="2"/>
    <rect width="270" height="32" rx="12" fill="#eab308"/>
    <circle cx="22" cy="16" r="10" fill="#0f172a"/>
    <text x="22" y="20" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">3</text>
    <text x="42" y="21" fill="#0f172a" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">OOP &amp; ARCHITECTURE</text>
    <text x="14" y="56" fill="#fde047" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">⚙️ Object-Oriented Design</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Classes, Objects, __init__ &amp; self</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Inheritance, Polymorphism &amp; super()</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Encapsulation, @property &amp; dunder methods</text>
    <text x="14" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Custom Exceptions &amp; Modular Packages</text>
    <rect x="12" y="142" width="246" height="24" rx="6" fill="rgba(250,204,21,0.15)" stroke="rgba(250,204,21,0.4)"/>
    <text x="135" y="158" text-anchor="middle" fill="#fef08a" font-family="Inter, Arial, sans-serif" font-size="10" font-weight="bold">⚡ Milestone: Banking &amp; Inventory System</text>
  </g>

  <!-- Stage 4: Advanced Python & Async (Middle Right) -->
  <g transform="translate(545, 290)" filter="url(#cardShadow)">
    <rect width="280" height="165" rx="14" fill="#091124" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="280" height="32" rx="12" fill="#8b5cf6"/>
    <circle cx="22" cy="16" r="10" fill="#ffffff"/>
    <text x="22" y="20" text-anchor="middle" fill="#6d28d9" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">4</text>
    <text x="42" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">ADVANCED PYTHON &amp; ASYNC</text>
    <text x="14" y="56" fill="#c084fc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🔮 Concurrency &amp; Internals</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Decorators (@wraps) &amp; Closures</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Generators, yield &amp; Lazy Memory</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Asyncio: async / await &amp; Event Loops</text>
    <text x="14" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Context Managers (__enter__ / __exit__)</text>
    <rect x="12" y="138" width="256" height="20" rx="5" fill="rgba(139,92,246,0.15)"/>
    <text x="140" y="152" text-anchor="middle" fill="#d8b4fe" font-family="Inter, Arial, sans-serif" font-size="9.5" font-weight="bold">⚡ Milestone: High-Speed Async Web Scraper</text>
  </g>

  <!-- Stage 5: Specialization Tracks (Middle Left) -->
  <g transform="translate(175, 290)" filter="url(#cardShadow)">
    <rect width="280" height="165" rx="14" fill="#091124" stroke="#ec4899" stroke-width="2"/>
    <rect width="280" height="32" rx="12" fill="#ec4899"/>
    <circle cx="22" cy="16" r="10" fill="#ffffff"/>
    <text x="22" y="20" text-anchor="middle" fill="#be185d" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">5</text>
    <text x="42" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">CAREER SPECIALIZATION</text>
    <text x="14" y="56" fill="#f472b6" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🚀 Choose Your Industry Track</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• 🌐 Web Dev: FastAPI, Django, REST APIs</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• 📊 Data Science: Pandas, NumPy, Matplotlib</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• 🤖 AI/ML: Scikit-Learn, PyTorch, HuggingFace</text>
    <text x="14" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• ⚙️ Automation: Playwright, Selenium, Scripts</text>
    <rect x="12" y="138" width="256" height="20" rx="5" fill="rgba(236,72,153,0.15)"/>
    <text x="140" y="152" text-anchor="middle" fill="#fbcfe8" font-family="Inter, Arial, sans-serif" font-size="9.5" font-weight="bold">⚡ Milestone: Full-Stack Web App / ML Pipeline</text>
  </g>

  <!-- Stage 6: Production Engineering & Cloud Deploy (Bottom Center) -->
  <g transform="translate(180, 480)" filter="url(#cardShadow)">
    <rect width="640" height="135" rx="14" fill="#091124" stroke="#10b981" stroke-width="2"/>
    <rect width="640" height="30" rx="12" fill="#10b981"/>
    <circle cx="24" cy="15" r="10" fill="#064e3b"/>
    <text x="24" y="19" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">6</text>
    <text x="44" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">STAGE 6: PRODUCTION ENGINEERING &amp; CLOUD DEPLOYMENT</text>
    
    <g transform="translate(20, 40)">
      <text x="0" y="16" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🛡️ Quality &amp; Version Control</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Virtual Environments: venv, poetry, pip</text>
      <text x="0" y="52" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Unit &amp; Integration Testing with PyTest</text>
      <text x="0" y="70" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Git Workflows &amp; GitHub Actions CI/CD</text>
    </g>
    <g transform="translate(330, 40)">
      <text x="0" y="16" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">☁️ Containers &amp; Cloud Delivery</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Dockerizing Python Apps &amp; Compose</text>
      <text x="0" y="52" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Cloud Deployment: AWS EC2, Render, Docker Hub</text>
      <text x="0" y="70" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Production Logging &amp; Environment Secrets</text>
    </g>
  </g>

</svg>"""


def build_cloud_computing_roadmap_svg():
    """Complete 6-Phase Cloud Computing & DevOps Tiered Infrastructure Roadmap (Zero to Architect)."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" width="1000" height="640">
  <defs>
    <linearGradient id="cloudBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050c1e"/>
      <stop offset="50%" stop-color="#09142b"/>
      <stop offset="100%" stop-color="#040814"/>
    </linearGradient>
    <linearGradient id="cloudGradHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <filter id="cloudShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1000" height="640" rx="24" fill="url(#cloudBg)" stroke="rgba(56,189,248,0.3)" stroke-width="1.5"/>

  <!-- Network Circuit Lines -->
  <path d="M 500,100 L 500,600 M 260,240 L 740,240 M 260,420 L 740,420" stroke="rgba(56,189,248,0.15)" stroke-width="2" stroke-dasharray="6 4"/>
  <circle cx="500" cy="240" r="6" fill="#38bdf8"/>
  <circle cx="500" cy="420" r="6" fill="#f97316"/>

  <!-- Header Banner -->
  <g transform="translate(30, 20)">
    <rect width="940" height="58" rx="14" fill="rgba(15,23,42,0.85)" stroke="rgba(56,189,248,0.35)" stroke-width="1"/>
    <circle cx="36" cy="29" r="17" fill="#0284c7"/>
    <text x="36" y="36" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="18">☁️</text>
    <text x="68" y="34" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">CLOUD COMPUTING &amp; DEVOPS — TIERED INFRASTRUCTURE ROADMAP</text>
    <text x="68" y="49" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Tiered Architecture: Systems ➔ Cloud Core (AWS/GCP) ➔ Docker ➔ Kubernetes ➔ Terraform IaC ➔ GitOps CI/CD</text>
    <rect x="785" y="14" width="140" height="30" rx="8" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="1"/>
    <text x="855" y="34" text-anchor="middle" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Architect Track</text>
  </g>

  <!-- TIER 1: Foundations & Systems (Left Col, Row 1) -->
  <g transform="translate(35, 100)" filter="url(#cloudShadow)">
    <rect width="450" height="155" rx="14" fill="#0b152d" stroke="#3b82f6" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#2563eb"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 1: LINUX, NETWORKING &amp; SECURITY GATEWAYS</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#93c5fd" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🐧 OS &amp; CLI</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Linux Bash, Systemd, SSH Keys</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• User permissions, chown, chmod</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#93c5fd" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🌐 Network Protocol</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• TCP/IP, DNS, Subnets, CIDR</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Nginx Reverse Proxy, SSL/TLS</text>
    </g>
    <rect x="15" y="118" width="420" height="24" rx="6" fill="rgba(37,99,235,0.15)" stroke="rgba(37,99,235,0.3)"/>
    <text x="225" y="134" text-anchor="middle" fill="#60a5fa" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Production Linux VPS Hardening &amp; Nginx Setup</text>
  </g>

  <!-- TIER 2: Cloud Core AWS / GCP / Azure (Right Col, Row 1) -->
  <g transform="translate(515, 100)" filter="url(#cloudShadow)">
    <rect width="450" height="155" rx="14" fill="#0b152d" stroke="#f97316" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#ea580c"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 2: CLOUD INFRASTRUCTURE (AWS / AZURE / GCP)</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#fdba74" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">⚡ Compute &amp; Storage</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• EC2 / Virtual Machines, AutoScale</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• S3 Object Storage, EBS Volumes</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#fdba74" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🔒 IAM &amp; Virtual Private Cloud</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• VPC Public/Private Subnets &amp; NAT</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• IAM Roles, Policies &amp; RDS Database</text>
    </g>
    <rect x="15" y="118" width="420" height="24" rx="6" fill="rgba(234,88,12,0.15)" stroke="rgba(234,88,12,0.3)"/>
    <text x="225" y="134" text-anchor="middle" fill="#fb923c" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Multi-Tier Resilient VPC Architecture</text>
  </g>

  <!-- TIER 3: Containerization & Docker (Left Col, Row 2) -->
  <g transform="translate(35, 275)" filter="url(#cloudShadow)">
    <rect width="450" height="155" rx="14" fill="#0b152d" stroke="#06b6d4" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#0891b2"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 3: CONTAINERIZATION (DOCKER &amp; REGISTRIES)</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#67e8f9" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🐳 Docker Architecture</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Multi-Stage Dockerfiles (Lean)</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Docker Volumes &amp; Host Mounts</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#67e8f9" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">⚙️ Compose &amp; Registry</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Docker Compose Multi-Container</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Docker Hub &amp; AWS ECR Registries</text>
    </g>
    <rect x="15" y="118" width="420" height="24" rx="6" fill="rgba(8,145,178,0.15)" stroke="rgba(8,145,178,0.3)"/>
    <text x="225" y="134" text-anchor="middle" fill="#22d3ee" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Full-Stack Microservices in Docker Compose</text>
  </g>

  <!-- TIER 4: Kubernetes Orchestration (Right Col, Row 2) -->
  <g transform="translate(515, 275)" filter="url(#cloudShadow)">
    <rect width="450" height="155" rx="14" fill="#0b152d" stroke="#8b5cf6" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#7c3aed"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 4: CLUSTER ORCHESTRATION (KUBERNETES)</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#c084fc" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">☸️ K8s Core Objects</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Pods, Deployments &amp; ReplicaSets</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• ClusterIP, NodePort &amp; LoadBalancer</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#c084fc" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">📦 Helm &amp; Ingress</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Helm Package Manager Charts</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Ingress Controllers &amp; TLS Certs</text>
    </g>
    <rect x="15" y="118" width="420" height="24" rx="6" fill="rgba(124,58,237,0.15)" stroke="rgba(124,58,237,0.3)"/>
    <text x="225" y="134" text-anchor="middle" fill="#a78bfa" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Production K8s Cluster with Ingress &amp; Helm</text>
  </g>

  <!-- TIER 5: Infrastructure as Code & GitOps (Left Col, Row 3) -->
  <g transform="translate(35, 450)" filter="url(#cloudShadow)">
    <rect width="450" height="165" rx="14" fill="#0b152d" stroke="#ec4899" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#db2777"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 5: INFRASTRUCTURE AS CODE (TERRAFORM)</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#f472b6" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🏗️ Terraform HCL</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Providers, Resources &amp; Variables</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Remote State (S3 + DynamoDB Lock)</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#f472b6" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">⚙️ Modules &amp; Drift</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Reusable Modules across Staging/Prod</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Ansible Configuration Playbooks</text>
    </g>
    <rect x="15" y="128" width="420" height="24" rx="6" fill="rgba(219,39,119,0.15)" stroke="rgba(219,39,119,0.3)"/>
    <text x="225" y="144" text-anchor="middle" fill="#f472b6" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: 100% Code-Provisioned Multi-Region Cloud</text>
  </g>

  <!-- TIER 6: CI/CD Pipelines & Observability (Right Col, Row 3) -->
  <g transform="translate(515, 450)" filter="url(#cloudShadow)">
    <rect width="450" height="165" rx="14" fill="#0b152d" stroke="#10b981" stroke-width="1.8"/>
    <rect width="450" height="32" rx="12" fill="#059669"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEVEL 6: CI/CD PIPELINES &amp; OBSERVABILITY (SRE)</text>
    <g transform="translate(20, 48)">
      <text x="0" y="14" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">🚀 Automated Pipelines</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• GitHub Actions &amp; GitLab CI/CD</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• ArgoCD GitOps Automated Sync</text>
    </g>
    <g transform="translate(225, 48)">
      <text x="0" y="14" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">📊 SRE Observability</text>
      <text x="0" y="32" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Prometheus Metrics &amp; Grafana Alerts</text>
      <text x="0" y="50" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Distributed Tracing &amp; Loki Logs</text>
    </g>
    <rect x="15" y="128" width="420" height="24" rx="6" fill="rgba(5,150,105,0.15)" stroke="rgba(5,150,105,0.3)"/>
    <text x="225" y="144" text-anchor="middle" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Zero-Downtime End-to-End GitOps Pipeline</text>
  </g>

</svg>"""


def build_web_development_roadmap_svg():
    """Complete 6-Phase Full-Stack Web Development Roadmap (Zero to Architect)."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 610" width="960" height="610">
  <defs>
    <linearGradient id="bgGradWeb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="100%" stop-color="#0e172e"/>
    </linearGradient>
    <linearGradient id="wStep1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <linearGradient id="wStep2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
    <linearGradient id="wStep3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="wStep4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="wStep5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="wStep6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
  </defs>

  <rect width="960" height="610" rx="20" fill="url(#bgGradWeb)" stroke="rgba(249,115,22,0.25)"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(249,115,22,0.35)"/>
  <text x="45" y="44" fill="#fb923c" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ FULL-STACK WEB DEVELOPMENT ROADMAP — ZERO TO ARCHITECT</text>
  <text x="45" y="59" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">HTML5/CSS3 • Modern JavaScript ES6+ • React 19 &amp; Next.js • Node.js &amp; Express • SQL/NoSQL Databases • Cloud DevOps</text>
  <rect x="745" y="27" width="170" height="30" rx="8" fill="rgba(249,115,22,0.12)" stroke="#fb923c"/>
  <text x="830" y="47" text-anchor="middle" fill="#fb923c" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Sastra AI • All-in-One</text>

  <!-- Row 1: Phase 1, Phase 2, Phase 3 -->

  <!-- Phase 1: HTML5 & CSS3 -->
  <g transform="translate(25, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep1)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 1: WEB FOUNDATIONS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🌐 HTML5, CSS3 &amp; Responsive UI</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Semantic HTML Elements, Forms &amp; Accessibility (a11y)</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Modern CSS: Flexbox, CSS Grid &amp; Box Model</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Responsive Design: Media Queries &amp; Mobile-First</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• CSS Variables, Transitions, Keyframe Animations</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Modern Styling: Tailwind CSS &amp; PostCSS</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(249,115,22,0.12)" stroke="rgba(249,115,22,0.4)"/>
    <text x="22" y="194" fill="#fb923c" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Pixel-Perfect Responsive Portfolio Site</text>
  </g>

  <!-- Phase 2: JavaScript ES6+ -->
  <g transform="translate(335, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep2)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 2: MODERN JAVASCRIPT</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">⚡ DOM &amp; Asynchronous Logic</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Variables (let/const), Arrow Functions, Destructuring</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• DOM Manipulation, Event Listeners &amp; Bubbling</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Promises, async / await &amp; Fetch API for REST</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Array Methods: map, filter, reduce &amp; closures</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• ES Modules (import/export), LocalStorage &amp; Vite</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(234,179,8,0.12)" stroke="rgba(234,179,8,0.4)"/>
    <text x="22" y="194" fill="#facc15" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Interactive Weather Dashboard App</text>
  </g>

  <!-- Phase 3: Frontend Frameworks (React) -->
  <g transform="translate(645, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep3)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 3: FRONTEND (REACT / NEXT)</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">⚛️ Component Architecture</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• JSX, Props, State (useState, useEffect, useMemo)</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Component Lifecycle, Custom Hooks &amp; Context API</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Next.js App Router: SSR, SSG &amp; Server Components</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Global State: Zustand, Redux Toolkit, React Query</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• TypeScript: Static Types, Interfaces &amp; Generics</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(6,182,212,0.12)" stroke="rgba(6,182,212,0.4)"/>
    <text x="22" y="194" fill="#22d3ee" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Full-Featured E-Commerce UI Store</text>
  </g>

  <!-- Row 2: Phase 4, Phase 5, Phase 6 -->

  <!-- Phase 4: Backend Engineering -->
  <g transform="translate(25, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep4)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 4: BACKEND (NODE / PYTHON)</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🚀 RESTful APIs &amp; Microservices</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Node.js runtime, Event Loop, Express.js / FastAPI</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• REST API Design, Routing, Controllers &amp; Middleware</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Authentication: JWT Tokens, OAuth2 &amp; Password Hashing</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Realtime Communication: WebSockets &amp; Socket.io</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Input Validation (Zod/Joi), CORS &amp; Rate Limiting</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(16,185,129,0.12)" stroke="rgba(16,185,129,0.4)"/>
    <text x="22" y="194" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Production Auth &amp; CRUD API Server</text>
  </g>

  <!-- Phase 5: Databases & Caching -->
  <g transform="translate(335, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep5)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 5: DATABASES &amp; PERSISTENCE</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🗄️ SQL, NoSQL &amp; High-Speed Cache</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Relational SQL: PostgreSQL, Joins, Indexes &amp; Schemas</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Modern ORMs: Prisma, Drizzle, SQLAlchemy</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Document NoSQL: MongoDB, Collections &amp; Aggregations</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• In-Memory Caching: Redis Key-Value &amp; Session Store</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Database Migrations, ACID Transactions &amp; Pooling</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(139,92,246,0.12)" stroke="rgba(139,92,246,0.4)"/>
    <text x="22" y="194" fill="#c084fc" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Scalable Multi-Tenant Database Architecture</text>
  </g>

  <!-- Phase 6: DevOps & Cloud Deployment -->
  <g transform="translate(645, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#wStep6)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 6: CLOUD &amp; PRODUCTION</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🛡️ CI/CD, Docker &amp; Global Delivery</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Testing Suites: Vitest, Jest, Playwright E2E Testing</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Git Version Control &amp; GitHub Actions CI/CD Pipeline</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Dockerizing Frontend &amp; Backend with Docker Compose</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Cloud Deployment: Vercel, AWS ECS, Render &amp; VPS</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Monitoring: Sentry Error Tracking &amp; PostHog Analytics</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(236,72,153,0.12)" stroke="rgba(236,72,153,0.4)"/>
    <text x="22" y="194" fill="#f472b6" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Capstone: Production Full-Stack SaaS Application</text>
  </g>

  <!-- Bottom Exam Bar -->
  <rect x="25" y="544" width="910" height="52" rx="12" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="575" fill="#fb923c" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 Study Progression:</text>
  <text x="195" y="575" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">HTML/CSS Layouts ──▶ JavaScript Logic ──▶ React 19 / Next.js ──▶ Node/Express Backend ──▶ SQL/Redis ──▶ CI/CD Cloud</text>
</svg>"""


def build_ai_ml_roadmap_svg():
    """Complete 6-Phase Artificial Intelligence & Machine Learning Roadmap."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 610" width="960" height="610">
  <defs>
    <linearGradient id="bgGradAI" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070c20"/>
      <stop offset="100%" stop-color="#0e1333"/>
    </linearGradient>
    <linearGradient id="aiStep1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="aiStep2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="aiStep3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="aiStep4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="aiStep5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="aiStep6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="960" height="610" rx="20" fill="url(#bgGradAI)" stroke="rgba(139,92,246,0.25)"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(139,92,246,0.35)"/>
  <text x="45" y="44" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ ARTIFICIAL INTELLIGENCE &amp; MACHINE LEARNING ROADMAP — ZERO TO SPECIALIST</text>
  <text x="45" y="59" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">Linear Algebra &amp; Calculus • Data Wrangling (Pandas) • Scikit-Learn ML • PyTorch Deep Learning • LLMs &amp; RAG • MLOps</text>
  <rect x="745" y="27" width="170" height="30" rx="8" fill="rgba(139,92,246,0.12)" stroke="#a78bfa"/>
  <text x="830" y="47" text-anchor="middle" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Sastra AI • All-in-One</text>

  <!-- Row 1: Phase 1, Phase 2, Phase 3 -->

  <!-- Phase 1: Mathematics & Python -->
  <g transform="translate(25, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep1)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 1: MATH &amp; CORE PYTHON</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🧮 Numerical Foundations</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Linear Algebra: Vectors, Matrices &amp; Dot Products</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Calculus: Derivatives, Gradients &amp; Chain Rule</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Probability &amp; Statistics: Distributions, Bayes, Mean</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Python NumPy: Array Operations &amp; Vectorization</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Jupyter Notebooks &amp; Interactive Experimentation</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(59,130,246,0.12)" stroke="rgba(59,130,246,0.4)"/>
    <text x="22" y="194" fill="#60a5fa" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Gradient Descent Algorithm from Scratch</text>
  </g>

  <!-- Phase 2: Data Wrangling & EDA -->
  <g transform="translate(335, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep2)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 2: DATA &amp; EXPLORATION (EDA)</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">📊 Data Preprocessing &amp; Charts</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Pandas: DataFrames, Filtering, GroupBy &amp; Joins</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Data Cleaning: Missing Values, Outliers &amp; Encoding</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Visualizations: Matplotlib, Seaborn, Correlation Heatmaps</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Feature Engineering: Scaling, Normalization, PCA</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• SQL for Analytics: Window Functions &amp; Aggregates</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(6,182,212,0.12)" stroke="rgba(6,182,212,0.4)"/>
    <text x="22" y="194" fill="#22d3ee" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Real-World Dataset EDA &amp; Executive Report</text>
  </g>

  <!-- Phase 3: Classical Machine Learning -->
  <g transform="translate(645, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep3)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 3: MACHINE LEARNING (SKLEARN)</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🤖 Supervised &amp; Unsupervised Models</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Regression: Linear, Ridge, Lasso &amp; Polynomial</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Classification: Logistic Regression, Random Forest, SVM</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Boosting: XGBoost, LightGBM, Gradient Boosting</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Clustering: K-Means, Hierarchical, DBSCAN</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Metrics: ROC-AUC, Precision, Recall, F1-Score, Cross-Val</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(139,92,246,0.12)" stroke="rgba(139,92,246,0.4)"/>
    <text x="22" y="194" fill="#c084fc" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Customer Churn / Credit Risk Predictor</text>
  </g>

  <!-- Row 2: Phase 4, Phase 5, Phase 6 -->

  <!-- Phase 4: Deep Learning & PyTorch -->
  <g transform="translate(25, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep4)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 4: DEEP LEARNING (PYTORCH)</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🧠 Neural Networks &amp; Vision</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Perceptrons, Multi-Layer Perceptrons &amp; Backpropagation</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Activation Functions: ReLU, Sigmoid, GeLU, Softmax</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Loss Functions: Cross-Entropy, MSE &amp; Optimizers (Adam)</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• CNNs for Computer Vision: ResNet, Convolutions, Pooling</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Transfer Learning with Pretrained Models</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(236,72,153,0.12)" stroke="rgba(236,72,153,0.4)"/>
    <text x="22" y="194" fill="#f472b6" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Medical Image Classifier (98% Acc)</text>
  </g>

  <!-- Phase 5: Generative AI, LLMs & RAG -->
  <g transform="translate(335, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep5)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 5: GENERATIVE AI &amp; LLMS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🔮 Transformers, RAG &amp; Agents</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Self-Attention Mechanism &amp; Transformer Architecture</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Hugging Face Transformers: Tokenizers &amp; Pipelines</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Vector Databases: ChromaDB, Pinecone, FAISS, Embeddings</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Retrieval-Augmented Generation (RAG) Architecture</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Autonomous AI Agents: LangChain, Tool Calling &amp; Reasoning</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(245,158,11,0.12)" stroke="rgba(245,158,11,0.4)"/>
    <text x="22" y="194" fill="#fbbf24" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Production RAG Assistant with Custom Docs</text>
  </g>

  <!-- Phase 6: MLOps & Production -->
  <g transform="translate(645, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#aiStep6)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 6: MLOPS &amp; MODEL SERVING</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🛡️ High-Throughput Model APIs</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Model Serialization: ONNX, TorchScript, SafeTensors</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• FastAPI &amp; vLLM Model Serving Pipelines</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Experiment Tracking: MLflow, Weights &amp; Biases</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Dockerizing GPU Model Inference with CUDA</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Model Drift Monitoring, Retraining Pipelines &amp; Cloud</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(16,185,129,0.12)" stroke="rgba(16,185,129,0.4)"/>
    <text x="22" y="194" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Capstone: Enterprise Multimodal AI Service in Cloud</text>
  </g>

  <!-- Bottom Exam Bar -->
  <rect x="25" y="544" width="910" height="52" rx="12" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="575" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 Study Progression:</text>
  <text x="195" y="575" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">Math &amp; NumPy ──▶ Pandas EDA ──▶ Classical ML Models ──▶ PyTorch Deep Learning ──▶ LLMs &amp; RAG ──▶ Cloud MLOps</text>
</svg>"""


def build_universal_subject_roadmap_svg(subject_name):
    """Dynamic, color-coded 6-Phase Technical Subject Roadmap Generator."""
    clean_subj = re.sub(r'[^a-zA-Z0-9 ]', '', subject_name).strip()[:35].title() or "Computer Science"
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 610" width="960" height="610">
  <defs>
    <linearGradient id="bgGradUni" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070e24"/>
      <stop offset="100%" stop-color="#0b1636"/>
    </linearGradient>
    <linearGradient id="uStep1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="uStep2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="uStep3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="uStep4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="uStep5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="uStep6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="960" height="610" rx="20" fill="url(#bgGradUni)" stroke="rgba(56,189,248,0.25)"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(56,189,248,0.35)"/>
  <text x="45" y="44" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ COMPLETE {clean_subj.upper()} ROADMAP — ZERO TO MASTERY</text>
  <text x="45" y="59" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">Foundations • Core Architecture • Systems &amp; Data • Advanced Patterns • Specialization • Production Delivery</text>
  <rect x="745" y="27" width="170" height="30" rx="8" fill="rgba(56,189,248,0.12)" stroke="#38bdf8"/>
  <text x="830" y="47" text-anchor="middle" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Sastra AI • All-in-One</text>

  <!-- Row 1: Phase 1, Phase 2, Phase 3 -->

  <!-- Phase 1: Foundations -->
  <g transform="translate(25, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep1)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 1: CORE FOUNDATIONS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🌿 Syntax &amp; Mental Models</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Core Principles, Terminology &amp; Key Concepts</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Development Environment Setup &amp; Tooling</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Essential Syntax, Variables &amp; Control Flow</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Basic Problem Solving &amp; Algorithmic Thinking</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Code Conventions &amp; Clean Documentation</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(59,130,246,0.12)" stroke="rgba(59,130,246,0.4)"/>
    <text x="22" y="194" fill="#60a5fa" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Foundational Proof-of-Concept Project</text>
  </g>

  <!-- Phase 2: Core Architecture -->
  <g transform="translate(335, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep2)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 2: CORE ARCHITECTURE</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">⚙️ Structuring Systems</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Data Structures, Types &amp; Memory Schemas</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Modular Design, Encapsulation &amp; Reusability</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Error Handling, Edge Cases &amp; Validation</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Asynchronous Flow &amp; State Management</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Standard Libraries &amp; Utility Modules</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(6,182,212,0.12)" stroke="rgba(6,182,212,0.4)"/>
    <text x="22" y="194" fill="#22d3ee" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Multi-Component Engineered System</text>
  </g>

  <!-- Phase 3: Systems & Data -->
  <g transform="translate(645, 78)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep3)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 3: SYSTEMS &amp; PERSISTENCE</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">📦 Data I/O &amp; Integrations</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Database Modeling, Queries &amp; Persistence</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Working with APIs, External Services &amp; Protocols</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Caching, Session Management &amp; Data Pipeline</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Security Best Practices &amp; Input Sanitization</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Performance Benchmarking &amp; Optimization</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(139,92,246,0.12)" stroke="rgba(139,92,246,0.4)"/>
    <text x="22" y="194" fill="#c084fc" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Data-Backed Production Service</text>
  </g>

  <!-- Row 2: Phase 4, Phase 5, Phase 6 -->

  <!-- Phase 4: Advanced Patterns -->
  <g transform="translate(25, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep4)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 4: ADVANCED PATTERNS</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🔮 Concurrency &amp; Internals</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Concurrency, Multithreading &amp; Event-Driven Code</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Architectural Design Patterns (Factory, Observer, etc.)</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Memory Management &amp; Resource Lifecycle</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Unit, Integration &amp; Automated Regression Testing</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Profiling Bottlenecks &amp; High-Throughput Tuning</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(236,72,153,0.12)" stroke="rgba(236,72,153,0.4)"/>
    <text x="22" y="194" fill="#f472b6" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: High-Performance Concurrent Engine</text>
  </g>

  <!-- Phase 5: Industry Specialization -->
  <g transform="translate(335, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep5)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 5: INDUSTRY SPECIALIZATION</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🚀 Modern Industry Ecosystem</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Dominant Enterprise Frameworks &amp; Toolkits</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Microservices Architecture &amp; Distributed Patterns</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Cloud SDKs, Event Streaming (Kafka/RabbitMQ)</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Authentication, Encryption &amp; Zero-Trust Security</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Real-World Case Studies &amp; System Refactoring</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(245,158,11,0.12)" stroke="rgba(245,158,11,0.4)"/>
    <text x="22" y="194" fill="#fbbf24" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Milestone: Scalable Enterprise Application</text>
  </g>

  <!-- Phase 6: Production Delivery -->
  <g transform="translate(645, 312)">
    <rect width="290" height="220" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="290" height="32" rx="12" fill="url(#uStep6)"/>
    <text x="145" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">PHASE 6: CLOUD &amp; PRODUCTION</text>
    <text x="14" y="54" fill="#f8fafc" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">🛡️ Containerization &amp; DevOps</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Containerization: Dockerfiles &amp; Multi-Container Compose</text>
    <text x="14" y="92" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• CI/CD Pipelines: Automated Build, Test &amp; Deployment</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Cloud Hosting: AWS, GCP, Azure or Kubernetes</text>
    <text x="14" y="128" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Observability: Centralized Logging, Metrics &amp; Tracing</text>
    <text x="14" y="146" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• SRE Reliability: Health Checks, Alerts &amp; Auto-Scaling</text>
    <rect x="12" y="174" width="266" height="32" rx="8" fill="rgba(16,185,129,0.12)" stroke="rgba(16,185,129,0.4)"/>
    <text x="22" y="194" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Capstone: 100% Production-Deployed Cloud Solution</text>
  </g>

  <!-- Bottom Exam Bar -->
  <rect x="25" y="544" width="910" height="52" rx="12" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="575" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 Study Progression:</text>
  <text x="195" y="575" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">Phase 1 (Basics) ──▶ Phase 2 (Architecture) ──▶ Phase 3 (Data &amp; Systems) ──▶ Phase 4 (Patterns) ──▶ Phase 5 (Enterprise) ──▶ Phase 6 (Cloud Production)</text>
</svg>"""


def build_brain_svg():
    """Anatomical 6-Lobe Human Brain Diagram with Callout Cards."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="960" height="640">
  <defs>
    <linearGradient id="bgGradBrain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="100%" stop-color="#0b1329"/>
    </linearGradient>
    <linearGradient id="frontalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="parietalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="occipitalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="temporalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <linearGradient id="cerebellumGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="stemGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>

  <rect width="960" height="640" rx="20" fill="url(#bgGradBrain)" stroke="rgba(255,255,255,0.12)"/>
  
  <!-- Header Bar -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(56,189,248,0.3)"/>
  <text x="45" y="44" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ HUMAN BRAIN ANATOMY &amp; FUNCTIONAL LOBES — EDUCATIONAL STUDY DIAGRAM</text>
  <text x="915" y="44" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="12">100% Vector Study Guide</text>

  <!-- Central Brain Anatomical Diagram (Vector Illustration) -->
  <g transform="translate(480, 310)">
    <ellipse cx="0" cy="-20" rx="180" ry="140" fill="rgba(56,189,248,0.06)" filter="blur(20px)"/>

    <!-- 1. Frontal Lobe Path -->
    <path d="M -160 -10 C -170 -60 -130 -130 -60 -150 C -10 -160 20 -150 40 -120 C 10 -80 -10 -40 -40 -10 C -70 10 -120 10 -160 -10 Z" 
          fill="url(#frontalGrad)" stroke="#60a5fa" stroke-width="2.5" opacity="0.95"/>
    <text x="-90" y="-75" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">FRONTAL</text>
    <text x="-90" y="-58" fill="#bfdbfe" font-family="Inter, Arial, sans-serif" font-size="11" text-anchor="middle">LOBE</text>

    <!-- 2. Parietal Lobe Path -->
    <path d="M 40 -120 C 80 -150 140 -130 160 -70 C 170 -30 150 10 110 20 C 80 0 50 -50 40 -120 Z" 
          fill="url(#parietalGrad)" stroke="#a78bfa" stroke-width="2.5" opacity="0.95"/>
    <text x="115" y="-55" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">PARIETAL</text>
    <text x="115" y="-38" fill="#ddd6fe" font-family="Inter, Arial, sans-serif" font-size="11" text-anchor="middle">LOBE</text>

    <!-- 3. Occipital Lobe Path -->
    <path d="M 110 20 C 150 10 175 40 165 90 C 150 120 110 120 80 90 C 90 60 100 40 110 20 Z" 
          fill="url(#occipitalGrad)" stroke="#f472b6" stroke-width="2.5" opacity="0.95"/>
    <text x="128" y="70" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">OCCIPITAL</text>
    <text x="128" y="85" fill="#fbcfe8" font-family="Inter, Arial, sans-serif" font-size="10" text-anchor="middle">LOBE</text>

    <!-- 4. Temporal Lobe Path -->
    <path d="M -140 0 C -120 -20 -40 -10 -20 20 C -10 60 -50 90 -100 80 C -130 70 -150 40 -140 0 Z" 
          fill="url(#temporalGrad)" stroke="#22d3ee" stroke-width="2.5" opacity="0.95"/>
    <text x="-80" y="40" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">TEMPORAL</text>
    <text x="-80" y="56" fill="#cffafe" font-family="Inter, Arial, sans-serif" font-size="11" text-anchor="middle">LOBE</text>

    <!-- 5. Cerebellum -->
    <path d="M 15 80 C 40 70 80 80 95 120 C 90 155 40 165 0 145 C -10 120 0 95 15 80 Z" 
          fill="url(#cerebellumGrad)" stroke="#34d399" stroke-width="2.5" opacity="0.95"/>
    <path d="M 10 100 Q 50 105 85 115 M 5 120 Q 45 125 80 135 M 0 135 Q 35 140 65 148" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" fill="none"/>
    <text x="45" y="125" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CEREBELLUM</text>

    <!-- 6. Brainstem -->
    <path d="M -30 75 C -10 70 0 80 -5 120 C -10 160 -15 190 -25 210 C -40 210 -45 160 -40 120 C -40 90 -35 80 -30 75 Z" 
          fill="url(#stemGrad)" stroke="#fbbf24" stroke-width="2.5" opacity="0.95"/>
    <text x="-32" y="150" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">BRAIN</text>
    <text x="-32" y="166" fill="#fef3c7" font-family="Inter, Arial, sans-serif" font-size="10" text-anchor="middle">STEM</text>

    <!-- Sulci divider lines -->
    <path d="M 40 -120 Q 15 -60 -20 20" stroke="#ffffff" stroke-width="2.5" stroke-dasharray="3,3" fill="none"/>
    <path d="M -120 10 Q -50 5 15 80" stroke="#ffffff" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
  </g>

  <!-- CALLOUT CARDS -->

  <!-- Card 1: Frontal Lobe -->
  <g transform="translate(30, 85)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#3b82f6" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#1d4ed8"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">1. FRONTAL LOBE</text>
    <text x="14" y="52" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Higher Executive Functions:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Decision Making &amp; Reasoning</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Voluntary Motor Movement</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Broca's Area (Speech Production)</text>
    <path d="M 260 67 L 380 230" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="380" cy="230" r="4" fill="#3b82f6"/>
  </g>

  <!-- Card 2: Temporal Lobe -->
  <g transform="translate(30, 240)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#06b6d4" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#0e7490"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">2. TEMPORAL LOBE</text>
    <text x="14" y="52" fill="#67e8f9" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Memory &amp; Auditory Core:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Hearing &amp; Sound Processing</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Hippocampus (Long-term Memory)</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Wernicke's Area (Language Comprehension)</text>
    <path d="M 260 70 L 400 350" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="400" cy="350" r="4" fill="#06b6d4"/>
  </g>

  <!-- Card 3: Brainstem -->
  <g transform="translate(30, 395)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#b45309"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">3. BRAINSTEM</text>
    <text x="14" y="52" fill="#fde68a" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Autonomic Vital Life Control:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Heart Rate &amp; Blood Pressure</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Involuntary Breathing &amp; Respiration</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Midbrain, Pons &amp; Medulla Oblongata</text>
    <path d="M 260 67 L 440 450" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="440" cy="450" r="4" fill="#f59e0b"/>
  </g>

  <!-- Card 4: Parietal Lobe -->
  <g transform="translate(670, 85)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#6d28d9"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">4. PARIETAL LOBE</text>
    <text x="14" y="52" fill="#c4b5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Sensory &amp; Spatial Processing:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Somatosensory Cortex (Touch/Taste)</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Temperature &amp; Pain Sensation</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• 3D Spatial Awareness &amp; Geometry</text>
    <path d="M 0 67 L -70 230" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="600" cy="255" r="4" fill="#8b5cf6"/>
  </g>

  <!-- Card 5: Occipital Lobe -->
  <g transform="translate(670, 240)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#ec4899" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#be185d"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">5. OCCIPITAL LOBE</text>
    <text x="14" y="52" fill="#fbcfe8" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Visual Processing Center:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Primary Visual Cortex (V1)</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Color, Shape &amp; Motion Recognition</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Optical Nerve Inputs from Eyes</text>
    <path d="M 0 70 L -60 380" stroke="#ec4899" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="610" cy="380" r="4" fill="#ec4899"/>
  </g>

  <!-- Card 6: Cerebellum -->
  <g transform="translate(670, 395)">
    <rect width="260" height="135" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
    <rect width="260" height="30" rx="10" fill="#047857"/>
    <text x="14" y="20" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">6. CEREBELLUM</text>
    <text x="14" y="52" fill="#a7f3d0" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Coordination &amp; Balance:</text>
    <text x="14" y="72" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Fine Motor Muscle Control</text>
    <text x="14" y="90" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Posture, Equilibrium &amp; Balance</text>
    <text x="14" y="108" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Procedural Muscle Memory (Typing)</text>
    <path d="M 0 67 L -130 430" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="540" cy="430" r="4" fill="#10b981"/>
  </g>

  <!-- Bottom Exam Summary -->
  <rect x="25" y="550" width="910" height="70" rx="12" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="578" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 High-Yield Biology Exam Points:</text>
  <text x="45" y="602" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11.5">• Contralateral Control: The left hemisphere controls the right side of the body, and vice-versa.</text>
  <text x="495" y="602" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11.5">• Corpus Callosum: Thick nerve tract bridging both hemispheres for inter-hemispheric communication.</text>
</svg>"""


def build_photosynthesis_svg():
    """Complete Photosynthesis Biochemical Chloroplast Cycle."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="960" height="640">
  <defs>
    <linearGradient id="bgGradP" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#041510"/>
      <stop offset="100%" stop-color="#08281d"/>
    </linearGradient>
    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#eab308"/>
    </linearGradient>
    <linearGradient id="lightCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <linearGradient id="calvinCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14532d"/>
      <stop offset="100%" stop-color="#052e16"/>
    </linearGradient>
  </defs>

  <rect width="960" height="640" rx="20" fill="url(#bgGradP)" stroke="rgba(52,211,153,0.3)"/>

  <!-- Header -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(52,211,153,0.4)"/>
  <text x="45" y="44" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ PHOTOSYNTHESIS — COMPLETE BIOCHEMICAL STUDY DIAGRAM</text>
  <text x="915" y="44" text-anchor="end" fill="#a7f3d0" font-family="Inter, Arial, sans-serif" font-size="12">Chloroplast Mechanics</text>

  <!-- Large Chloroplast Boundary Container -->
  <rect x="35" y="85" width="890" height="420" rx="24" fill="rgba(6,78,59,0.3)" stroke="#10b981" stroke-width="2.5"/>
  <text x="55" y="115" fill="#6ee7b7" font-family="Outfit, Arial, sans-serif" font-size="14" font-weight="bold">CHLOROPLAST ORGANELLE (Double Membrane Enclosure)</text>

  <!-- Sun Energy Callout (Top-Left) -->
  <g transform="translate(50, 140)">
    <circle cx="45" cy="45" r="35" fill="url(#sunGrad)" filter="drop-shadow(0 0 15px rgba(250,204,21,0.6))"/>
    <text x="45" y="50" text-anchor="middle" fill="#713f12" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">LIGHT</text>
    <!-- Light Rays Arrow -->
    <path d="M 85 55 L 140 85" stroke="#facc15" stroke-width="3.5" stroke-dasharray="4,2"/>
    <polygon points="145,88 135,80 138,92" fill="#facc15"/>
    <text x="45" y="105" text-anchor="middle" fill="#fde047" font-family="Inter, Arial, sans-serif" font-size="11">Photons (hν)</text>
  </g>

  <!-- H2O Input Arrow (Left) -->
  <g transform="translate(50, 280)">
    <rect width="90" height="40" rx="10" fill="#0284c7" stroke="#38bdf8"/>
    <text x="45" y="25" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="14" font-weight="bold">H₂O</text>
    <text x="45" y="55" text-anchor="middle" fill="#7dd3fc" font-family="Inter, Arial, sans-serif" font-size="11">From Roots</text>
    <path d="M 95 20 L 140 20" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="145,20 135,15 135,25" fill="#38bdf8"/>
  </g>

  <!-- Stage 1: Light-Dependent Reactions (Thylakoid) -->
  <g transform="translate(195, 135)">
    <rect width="300" height="340" rx="18" fill="url(#lightCard)" stroke="#34d399" stroke-width="2"/>
    <rect width="300" height="34" rx="14" fill="#059669"/>
    <text x="150" y="22" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">STAGE 1: LIGHT REACTIONS</text>
    <text x="150" y="55" text-anchor="middle" fill="#a7f3d0" font-family="Inter, Arial, sans-serif" font-size="12" font-weight="bold">Location: Thylakoid Membrane (Grana)</text>

    <!-- Thylakoid Stack Illustration -->
    <g transform="translate(50, 70)">
      <ellipse cx="100" cy="15" rx="75" ry="12" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
      <ellipse cx="100" cy="35" rx="75" ry="12" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
      <ellipse cx="100" cy="55" rx="75" ry="12" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
      <text x="100" y="38" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">GRANUM STACK</text>
    </g>

    <!-- Key Biochemical Events -->
    <text x="18" y="165" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11">• Chlorophyll absorbs light energy</text>
    <text x="18" y="185" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11">• Photolysis of H₂O splits water:</text>
    <text x="32" y="205" fill="#fde047" font-family="Courier New, monospace" font-size="11">2H₂O ➔ 4H⁺ + 4e⁻ + O₂↑</text>
    <text x="18" y="230" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11">• Electron Transport Chain (ETC)</text>
    <text x="18" y="250" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11">• Synthesizes ATP &amp; NADPH</text>

    <!-- O2 Release Output -->
    <rect x="18" y="275" width="264" height="42" rx="10" fill="rgba(56,189,248,0.15)" stroke="#38bdf8"/>
    <text x="150" y="295" text-anchor="middle" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">BYPRODUCT RELEASED: O₂</text>
    <text x="150" y="310" text-anchor="middle" fill="#bfdbfe" font-family="Inter, Arial, sans-serif" font-size="10">Released into atmosphere via stomata</text>
  </g>

  <!-- Biochemical Energy Bridge (ATP & NADPH) -->
  <g transform="translate(505, 230)">
    <!-- ATP / NADPH Forward Arrow -->
    <path d="M 0 10 L 65 10" stroke="#facc15" stroke-width="3.5"/>
    <polygon points="70,10 60,5 60,15" fill="#facc15"/>
    <text x="35" y="0" text-anchor="middle" fill="#fde047" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">ATP + NADPH</text>
    <text x="35" y="26" text-anchor="middle" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="9">(Chemical Energy)</text>

    <!-- ADP / NADP+ Return Arrow -->
    <path d="M 65 80 L 0 80" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="4,2"/>
    <polygon points="-5,80 5,75 5,85" fill="#94a3b8"/>
    <text x="35" y="72" text-anchor="middle" fill="#cbd5e1" font-family="Outfit, Arial, sans-serif" font-size="10" font-weight="bold">ADP + NADP⁺</text>
    <text x="35" y="96" text-anchor="middle" fill="#64748b" font-family="Inter, Arial, sans-serif" font-size="9">(Recycled)</text>
  </g>

  <!-- Stage 2: Light-Independent Reactions (Calvin Cycle) -->
  <g transform="translate(585, 135)">
    <rect width="315" height="340" rx="18" fill="url(#calvinCard)" stroke="#34d399" stroke-width="2"/>
    <rect width="315" height="34" rx="14" fill="#15803d"/>
    <text x="157" y="22" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">STAGE 2: CALVIN CYCLE (DARK RXN)</text>
    <text x="157" y="55" text-anchor="middle" fill="#86efac" font-family="Inter, Arial, sans-serif" font-size="12" font-weight="bold">Location: Chloroplast Stroma (Fluid)</text>

    <!-- CO2 Input -->
    <rect x="25" y="70" width="265" height="35" rx="8" fill="rgba(255,255,255,0.08)" stroke="#a7f3d0"/>
    <text x="157" y="92" text-anchor="middle" fill="#fef08a" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">INPUT: CO₂ (From Stomata)</text>

    <!-- Calvin Cycle Steps -->
    <text x="18" y="135" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">1. Carbon Fixation (RuBisCO enzyme):</text>
    <text x="30" y="152" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">CO₂ binds to 5-carbon RuBP compound</text>

    <text x="18" y="180" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">2. Reduction Phase:</text>
    <text x="30" y="197" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">ATP &amp; NADPH convert 3-PGA into G3P sugar</text>

    <text x="18" y="225" fill="#ffffff" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">3. RuBP Regeneration:</text>
    <text x="30" y="242" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">Remaining G3P molecules rebuild RuBP</text>

    <!-- Final Output: Glucose -->
    <rect x="18" y="270" width="280" height="50" rx="10" fill="rgba(245,158,11,0.2)" stroke="#f59e0b"/>
    <text x="157" y="293" text-anchor="middle" fill="#fcd34d" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">SYNTHESIS: GLUCOSE (C₆H₁₂O₆)</text>
    <text x="157" y="310" text-anchor="middle" fill="#fde68a" font-family="Inter, Arial, sans-serif" font-size="10.5">Used for Plant Respiration, Starch &amp; Cellulose</text>
  </g>

  <!-- Bottom Chemical Equation Bar -->
  <rect x="25" y="525" width="910" height="95" rx="14" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="555" fill="#34d399" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">🌿 Balanced Biochemical Equation:</text>
  <text x="45" y="582" fill="#fde047" font-family="Courier New, monospace" font-size="16" font-weight="bold">6CO₂  +  6H₂O  +  Light Energy  ──────▶  C₆H₁₂O₆  +  6O₂↑</text>
  <text x="45" y="606" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11.5">• Carbon Dioxide + Water + Sunlight yields Glucose energy storage and Oxygen gas.</text>
</svg>"""


def build_human_heart_svg():
    """Human Heart 4-Chamber Circulatory Diagram."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="960" height="640">
  <defs>
    <linearGradient id="bgGradHeart" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180a0e"/>
      <stop offset="100%" stop-color="#280f17"/>
    </linearGradient>
    <linearGradient id="deoxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="oxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
  </defs>

  <rect width="960" height="640" rx="20" fill="url(#bgGradHeart)" stroke="rgba(239,68,68,0.3)"/>

  <!-- Header -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(239,68,68,0.4)"/>
  <text x="45" y="44" fill="#f87171" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ HUMAN HEART ANATOMY &amp; CIRCULATION — 4 CHAMBERS &amp; BLOOD FLOW</text>
  <text x="915" y="44" text-anchor="end" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="12">Cardiovascular Architecture</text>

  <!-- Deoxygenated vs Oxygenated Headers -->
  <rect x="50" y="85" width="410" height="32" rx="8" fill="rgba(30,64,175,0.25)" stroke="#3b82f6"/>
  <text x="255" y="106" text-anchor="middle" fill="#60a5fa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">RIGHT SIDE: DEOXYGENATED BLOOD (To Lungs)</text>

  <rect x="500" y="85" width="410" height="32" rx="8" fill="rgba(185,28,28,0.25)" stroke="#ef4444"/>
  <text x="705" y="106" text-anchor="middle" fill="#f87171" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">LEFT SIDE: OXYGENATED BLOOD (To Body)</text>

  <!-- Chamber 1: Right Atrium (Top-Left) -->
  <g transform="translate(50, 130)">
    <rect width="410" height="175" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
    <rect width="410" height="34" rx="12" fill="url(#deoxGrad)"/>
    <text x="20" y="23" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">1. RIGHT ATRIUM (RA)</text>
    <text x="390" y="22" text-anchor="end" fill="#bfdbfe" font-family="Inter, Arial, sans-serif" font-size="11">Deoxygenated (Blue)</text>
    <text x="20" y="60" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Receives blood from:</text>
    <text x="35" y="80" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">- Superior Vena Cava (upper body)</text>
    <text x="35" y="98" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">- Inferior Vena Cava (lower body)</text>
    <text x="20" y="125" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Pacemaker:</text>
    <text x="110" y="125" fill="#fde047" font-family="Inter, Arial, sans-serif" font-size="11">SA Node (Sinoatrial) starts electrical pulse</text>
    <text x="20" y="152" fill="#38bdf8" font-family="Inter, Arial, sans-serif" font-size="11">➔ Pumps through TRICUSPID VALVE into RV</text>
  </g>

  <!-- Chamber 2: Left Atrium (Top-Right) -->
  <g transform="translate(500, 130)">
    <rect width="410" height="175" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect width="410" height="34" rx="12" fill="url(#oxGrad)"/>
    <text x="20" y="23" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">2. LEFT ATRIUM (LA)</text>
    <text x="390" y="22" text-anchor="end" fill="#fecaca" font-family="Inter, Arial, sans-serif" font-size="11">Oxygenated (Red)</text>
    <text x="20" y="60" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Receives freshly oxygenated blood from:</text>
    <text x="35" y="80" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">- 4 Pulmonary Veins (from lungs)</text>
    <text x="20" y="110" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Structural Role:</text>
    <text x="35" y="130" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">Collects oxygen-rich blood during diastole</text>
    <text x="20" y="152" fill="#f87171" font-family="Inter, Arial, sans-serif" font-size="11">➔ Pumps through BICUSPID (MITRAL) VALVE into LV</text>
  </g>

  <!-- Chamber 3: Right Ventricle (Bottom-Left) -->
  <g transform="translate(50, 320)">
    <rect width="410" height="185" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
    <rect width="410" height="34" rx="12" fill="url(#deoxGrad)"/>
    <text x="20" y="23" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">3. RIGHT VENTRICLE (RV)</text>
    <text x="390" y="22" text-anchor="end" fill="#bfdbfe" font-family="Inter, Arial, sans-serif" font-size="11">Pumps to Lungs</text>
    <text x="20" y="60" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Wall Characteristics:</text>
    <text x="35" y="80" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">Thinner muscular wall than left ventricle</text>
    <text x="20" y="105" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Ejection Pathway:</text>
    <text x="35" y="125" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">Pumps blood through Pulmonary Valve</text>
    <text x="35" y="143" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">into Pulmonary Artery ➔ Left &amp; Right Lungs</text>
    <text x="20" y="168" fill="#38bdf8" font-family="Inter, Arial, sans-serif" font-size="11">⚡ Purpose: Oxygen uptake &amp; CO₂ removal</text>
  </g>

  <!-- Chamber 4: Left Ventricle (Bottom-Right) -->
  <g transform="translate(500, 320)">
    <rect width="410" height="185" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect width="410" height="34" rx="12" fill="url(#oxGrad)"/>
    <text x="20" y="23" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">4. LEFT VENTRICLE (LV)</text>
    <text x="390" y="22" text-anchor="end" fill="#fecaca" font-family="Inter, Arial, sans-serif" font-size="11">Pumps to Whole Body</text>
    <text x="20" y="60" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Wall Characteristics:</text>
    <text x="35" y="80" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">Thickest muscular myocardium (3x thicker)</text>
    <text x="20" y="105" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Ejection Pathway (Systole):</text>
    <text x="35" y="125" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">Forces blood through Aortic Valve</text>
    <text x="35" y="143" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">into AORTA at high systemic blood pressure</text>
    <text x="20" y="168" fill="#f87171" font-family="Inter, Arial, sans-serif" font-size="11">⚡ Purpose: Nourishes entire human body</text>
  </g>

  <!-- Bottom Systemic Blood Flow Summary -->
  <rect x="25" y="520" width="910" height="100" rx="14" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="548" fill="#f87171" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">🔄 Universal 2-Loop Circulatory Sequence:</text>
  <text x="45" y="572" fill="#60a5fa" font-family="Inter, Arial, sans-serif" font-size="11.5">• Pulmonary Circuit: Body ──▶ Vena Cava ──▶ Right Atrium ──▶ Right Ventricle ──▶ Pulmonary Artery ──▶ Lungs (Oxygenated)</text>
  <text x="45" y="594" fill="#f87171" font-family="Inter, Arial, sans-serif" font-size="11.5">• Systemic Circuit: Lungs ──▶ Pulmonary Veins ──▶ Left Atrium ──▶ Left Ventricle ──▶ Aorta ──▶ All Organs &amp; Tissues</text>
  <text x="45" y="612" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">• Cardiac Septum: Thick muscle wall preventing mixing of oxygenated and deoxygenated blood.</text>
</svg>"""


def build_solar_system_svg():
    """Solar System Planetary Architecture."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="960" height="640">
  <defs>
    <linearGradient id="bgGradS" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050814"/>
      <stop offset="100%" stop-color="#0a1128"/>
    </linearGradient>
    <linearGradient id="sunGradS" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <linearGradient id="jupiterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdba74"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
    <linearGradient id="saturnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
    <linearGradient id="earthGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#67e8f9"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="960" height="640" rx="20" fill="url(#bgGradS)" stroke="rgba(56,189,248,0.2)"/>

  <!-- Header -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(56,189,248,0.3)"/>
  <text x="45" y="44" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ SOLAR SYSTEM PLANETARY ARCHITECTURE — EDUCATIONAL STUDY DIAGRAM</text>
  <text x="915" y="44" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="12">Scale Order &amp; Classification</text>

  <!-- Classification Banners -->
  <rect x="135" y="85" width="280" height="30" rx="8" fill="rgba(59,130,246,0.15)" stroke="#3b82f6"/>
  <text x="275" y="105" text-anchor="middle" fill="#93c5fd" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">TERRESTRIAL ROCKY PLANETS</text>

  <rect x="445" y="85" width="480" height="30" rx="8" fill="rgba(245,158,11,0.15)" stroke="#f59e0b"/>
  <text x="685" y="105" text-anchor="middle" fill="#fde68a" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">JOVIAN GAS &amp; ICE GIANTS</text>

  <!-- Sun Section (Left) -->
  <g transform="translate(0, 130)">
    <path d="M 0 0 C 70 50 70 290 0 340 Z" fill="url(#sunGradS)" filter="drop-shadow(0 0 25px rgba(234,88,12,0.7))"/>
    <text x="25" y="175" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold" transform="rotate(-90, 25, 175)" text-anchor="middle">THE SUN</text>
  </g>

  <!-- 1. Mercury -->
  <g transform="translate(155, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="10" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="0" y="65" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">MERCURY</text>
    <text x="0" y="82" text-anchor="middle" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">0.39 AU</text>
    <text x="0" y="96" text-anchor="middle" fill="#64748b" font-family="Inter, Arial, sans-serif" font-size="9.5">0 Moons</text>
  </g>

  <!-- 2. Venus -->
  <g transform="translate(225, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="15" fill="#f59e0b" stroke="#fde68a" stroke-width="1.5"/>
    <text x="0" y="65" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">VENUS</text>
    <text x="0" y="82" text-anchor="middle" fill="#fcd34d" font-family="Inter, Arial, sans-serif" font-size="10">0.72 AU</text>
    <text x="0" y="96" text-anchor="middle" fill="#64748b" font-family="Inter, Arial, sans-serif" font-size="9.5">Hottest (CO₂)</text>
  </g>

  <!-- 3. Earth -->
  <g transform="translate(305, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="17" fill="url(#earthGrad)" stroke="#38bdf8" stroke-width="1.8"/>
    <circle cx="16" cy="16" r="4" fill="#e2e8f0"/>
    <text x="0" y="65" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">EARTH</text>
    <text x="0" y="82" text-anchor="middle" fill="#7dd3fc" font-family="Inter, Arial, sans-serif" font-size="10">1.00 AU</text>
    <text x="0" y="96" text-anchor="middle" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="9.5">1 Moon • Life</text>
  </g>

  <!-- 4. Mars -->
  <g transform="translate(385, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="12" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="0" y="65" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">MARS</text>
    <text x="0" y="82" text-anchor="middle" fill="#fca5a5" font-family="Inter, Arial, sans-serif" font-size="10">1.52 AU</text>
    <text x="0" y="96" text-anchor="middle" fill="#64748b" font-family="Inter, Arial, sans-serif" font-size="9.5">2 Moons • Iron</text>
  </g>

  <!-- Asteroid Belt Divider Line -->
  <g transform="translate(430, 250)">
    <line x1="0" y1="-100" x2="0" y2="180" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4,6"/>
    <text x="0" y="-115" text-anchor="middle" fill="#d8b4fe" font-family="Outfit, Arial, sans-serif" font-size="10" font-weight="bold">ASTEROID</text>
    <text x="0" y="-103" text-anchor="middle" fill="#d8b4fe" font-family="Outfit, Arial, sans-serif" font-size="10" font-weight="bold">BELT</text>
  </g>

  <!-- 5. Jupiter -->
  <g transform="translate(500, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="38" fill="url(#jupiterGrad)" stroke="#fed7aa" stroke-width="2"/>
    <ellipse cx="14" cy="40" rx="7" ry="4" fill="#991b1b"/>
    <text x="0" y="85" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12.5" font-weight="bold">JUPITER</text>
    <text x="0" y="102" text-anchor="middle" fill="#fdba74" font-family="Inter, Arial, sans-serif" font-size="10">5.20 AU</text>
    <text x="0" y="116" text-anchor="middle" fill="#fed7aa" font-family="Inter, Arial, sans-serif" font-size="9.5">Largest • 95 Moons</text>
  </g>

  <!-- 6. Saturn -->
  <g transform="translate(635, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <ellipse cx="0" cy="30" rx="46" ry="14" fill="none" stroke="#fef08a" stroke-width="4.5" opacity="0.8" transform="rotate(-18, 0, 30)"/>
    <circle cx="0" cy="30" r="30" fill="url(#saturnGrad)" stroke="#fef08a" stroke-width="1.8"/>
    <text x="0" y="85" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12.5" font-weight="bold">SATURN</text>
    <text x="0" y="102" text-anchor="middle" fill="#fef08a" font-family="Inter, Arial, sans-serif" font-size="10">9.58 AU</text>
    <text x="0" y="116" text-anchor="middle" fill="#fef08a" font-family="Inter, Arial, sans-serif" font-size="9.5">Ring System • 146 Moons</text>
  </g>

  <!-- 7. Uranus -->
  <g transform="translate(755, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="22" fill="#38bdf8" stroke="#bae6fd" stroke-width="1.8"/>
    <text x="0" y="75" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">URANUS</text>
    <text x="0" y="92" text-anchor="middle" fill="#7dd3fc" font-family="Inter, Arial, sans-serif" font-size="10">19.2 AU</text>
    <text x="0" y="106" text-anchor="middle" fill="#bae6fd" font-family="Inter, Arial, sans-serif" font-size="9.5">Tilted Axis • 28 Moons</text>
  </g>

  <!-- 8. Neptune -->
  <g transform="translate(855, 270)">
    <line x1="0" y1="-140" x2="0" y2="200" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
    <circle cx="0" cy="30" r="21" fill="#2563eb" stroke="#93c5fd" stroke-width="1.8"/>
    <text x="0" y="75" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">NEPTUNE</text>
    <text x="0" y="92" text-anchor="middle" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="10">30.1 AU</text>
    <text x="0" y="106" text-anchor="middle" fill="#bfdbfe" font-family="Inter, Arial, sans-serif" font-size="9.5">Fastest Winds • 16 Moons</text>
  </g>

  <!-- Bottom Exam Summary -->
  <rect x="25" y="530" width="910" height="90" rx="14" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="560" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 Exam Mnemonic &amp; Rules:</text>
  <text x="220" y="560" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12"><tspan font-weight="bold" fill="#ffffff">M</tspan>y <tspan font-weight="bold" fill="#ffffff">V</tspan>ery <tspan font-weight="bold" fill="#ffffff">E</tspan>ducated <tspan font-weight="bold" fill="#ffffff">M</tspan>other <tspan font-weight="bold" fill="#ffffff">J</tspan>ust <tspan font-weight="bold" fill="#ffffff">S</tspan>erved <tspan font-weight="bold" fill="#ffffff">U</tspan>s <tspan font-weight="bold" fill="#ffffff">N</tspan>oodles</text>
  <text x="45" y="588" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11.5">• Inner 4 (Terrestrial): High density, metallic core, few moons, solid silicate rock surface.</text>
  <text x="45" y="606" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11.5">• Outer 4 (Gas/Ice Giants): Massive volume, thick H/He/Methane atmospheres, ring systems, numerous natural satellites.</text>
</svg>"""


def build_database_architecture_svg(clean_title="System Architecture & Database Schema"):
    """4-Tier System Architecture & Database Schema Diagram."""
    clean_upper = re.sub(r'[^a-zA-Z0-9 &]', '', clean_title).strip().upper()
    safe_title = clean_upper.replace("&", "&amp;")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="960" height="640">
  <defs>
    <linearGradient id="bgGradD" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="960" height="640" rx="20" fill="url(#bgGradD)" stroke="rgba(255,255,255,0.12)"/>

  <!-- Header -->
  <rect x="25" y="16" width="910" height="52" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(56,189,248,0.3)"/>
  <text x="45" y="44" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="17" font-weight="bold">✦ {safe_title}</text>
  <text x="915" y="44" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="12">100% Vector Architecture</text>

  <!-- Tier 1: Client Layer (Left) -->
  <g transform="translate(35, 90)">
    <rect width="180" height="420" rx="16" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
    <rect width="180" height="36" rx="14" fill="#1d4ed8"/>
    <text x="90" y="23" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">1. CLIENT TIER</text>

    <!-- Client Box 1: Web App -->
    <rect x="15" y="55" width="150" height="70" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="80" fill="#60a5fa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Web Browser</text>
    <text x="25" y="100" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• React / Vite SPA</text>
    <text x="25" y="115" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• HTTPS / WSS Client</text>

    <!-- Client Box 2: Mobile -->
    <rect x="15" y="140" width="150" height="70" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="165" fill="#60a5fa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Mobile Apps</text>
    <text x="25" y="185" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• iOS / Android</text>
    <text x="25" y="200" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• JWT Authentication</text>

    <!-- Client Box 3: API Consumer -->
    <rect x="15" y="225" width="150" height="70" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="250" fill="#60a5fa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Partner APIs</text>
    <text x="25" y="270" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• RESTful Webhooks</text>
    <text x="25" y="285" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10.5">• HMAC Signatures</text>

    <rect x="15" y="315" width="150" height="85" rx="10" fill="rgba(59,130,246,0.1)" stroke="#3b82f6"/>
    <text x="25" y="340" fill="#93c5fd" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Traffic Protocols:</text>
    <text x="25" y="360" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• TLS 1.3 Encryption</text>
    <text x="25" y="378" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Gzip Compression</text>
  </g>

  <!-- Flow Arrow 1 -->
  <path d="M 215 300 L 255 300" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="260,300 250,295 250,305" fill="#38bdf8"/>

  <!-- Tier 2: API Gateway & Auth (Center-Left) -->
  <g transform="translate(265, 90)">
    <rect width="190" height="420" rx="16" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="190" height="36" rx="14" fill="#6d28d9"/>
    <text x="95" y="23" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">2. GATEWAY &amp; EDGE</text>

    <rect x="15" y="55" width="160" height="100" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="80" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">API Gateway</text>
    <text x="25" y="102" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Reverse Proxy (Nginx)</text>
    <text x="25" y="120" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Rate Limiting (Token Bucket)</text>
    <text x="25" y="138" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• SSL Termination</text>

    <rect x="15" y="170" width="160" height="100" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="195" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Security &amp; Auth</text>
    <text x="25" y="217" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• JWT Verification</text>
    <text x="25" y="235" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Role-Based Access (RBAC)</text>
    <text x="25" y="253" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• CORS Validation</text>

    <rect x="15" y="285" width="160" height="115" rx="10" fill="rgba(139,92,246,0.1)" stroke="#8b5cf6"/>
    <text x="25" y="310" fill="#c4b5fd" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">Observability:</text>
    <text x="25" y="330" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Prometheus Metrics</text>
    <text x="25" y="348" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Distributed Tracing</text>
    <text x="25" y="366" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Health Check Probes</text>
  </g>

  <!-- Flow Arrow 2 -->
  <path d="M 455 300 L 495 300" stroke="#a78bfa" stroke-width="3"/>
  <polygon points="500,300 490,295 490,305" fill="#a78bfa"/>

  <!-- Tier 3: Service Layer (Center-Right) -->
  <g transform="translate(505, 90)">
    <rect width="190" height="420" rx="16" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect width="190" height="36" rx="14" fill="#0e7490"/>
    <text x="95" y="23" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">3. BACKEND SERVICES</text>

    <rect x="15" y="55" width="160" height="100" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="80" fill="#22d3ee" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Flask / Python API</text>
    <text x="25" y="102" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Sastra AI Engine</text>
    <text x="25" y="120" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• RAG Knowledge Store</text>
    <text x="25" y="138" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Multimodal Vision Router</text>

    <rect x="15" y="170" width="160" height="100" rx="10" fill="#1e293b" stroke="rgba(255,255,255,0.1)"/>
    <text x="25" y="195" fill="#22d3ee" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Course Engine</text>
    <text x="25" y="217" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Progress Tracking</text>
    <text x="25" y="235" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• Interactive Quiz Grading</text>
    <text x="25" y="253" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">• PDF Report Generation</text>

    <rect x="15" y="285" width="160" height="115" rx="10" fill="rgba(6,182,212,0.1)" stroke="#06b6d4"/>
    <text x="25" y="310" fill="#a5f3fc" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">In-Memory Cache:</text>
    <text x="25" y="330" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Redis 7.0 Cache</text>
    <text x="25" y="350" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Session store &amp; locks</text>
    <text x="25" y="368" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10">• Sub-millisecond latency</text>
  </g>

  <!-- Flow Arrow 3 -->
  <path d="M 695 300 L 735 300" stroke="#22d3ee" stroke-width="3"/>
  <polygon points="740,300 730,295 730,305" fill="#22d3ee"/>

  <!-- Tier 4: Database & Storage (Right) -->
  <g transform="translate(745, 90)">
    <rect width="180" height="420" rx="16" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="180" height="36" rx="14" fill="#047857"/>
    <text x="90" y="23" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">4. DATABASE SCHEMA</text>

    <!-- Table 1: users -->
    <rect x="12" y="55" width="156" height="100" rx="8" fill="#1e293b" stroke="#10b981"/>
    <rect x="12" y="55" width="156" height="24" rx="6" fill="#059669"/>
    <text x="20" y="72" fill="#ffffff" font-family="Courier New, monospace" font-size="11" font-weight="bold">TABLE: users</text>
    <text x="20" y="93" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#facc15">id</tspan>: SERIAL PK</text>
    <text x="20" y="108" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• email: VARCHAR(255)</text>
    <text x="20" y="123" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• role: VARCHAR(50)</text>
    <text x="20" y="138" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• created_at: TIMESTAMP</text>

    <!-- Table 2: enrollments -->
    <rect x="12" y="170" width="156" height="105" rx="8" fill="#1e293b" stroke="#10b981"/>
    <rect x="12" y="170" width="156" height="24" rx="6" fill="#059669"/>
    <text x="20" y="187" fill="#ffffff" font-family="Courier New, monospace" font-size="11" font-weight="bold">TABLE: enrollments</text>
    <text x="20" y="208" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#facc15">id</tspan>: SERIAL PK</text>
    <text x="20" y="223" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#38bdf8">user_id</tspan>: FK(users)</text>
    <text x="20" y="238" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#38bdf8">course_id</tspan>: FK(courses)</text>
    <text x="20" y="253" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• progress_pct: INT</text>

    <!-- Table 3: quiz_scores -->
    <rect x="12" y="290" width="156" height="105" rx="8" fill="#1e293b" stroke="#10b981"/>
    <rect x="12" y="290" width="156" height="24" rx="6" fill="#059669"/>
    <text x="20" y="307" fill="#ffffff" font-family="Courier New, monospace" font-size="11" font-weight="bold">TABLE: quiz_scores</text>
    <text x="20" y="328" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#facc15">id</tspan>: SERIAL PK</text>
    <text x="20" y="343" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• <tspan fill="#38bdf8">user_id</tspan>: FK(users)</text>
    <text x="20" y="358" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• score: INT (0-100)</text>
    <text x="20" y="373" fill="#cbd5e1" font-family="Courier New, monospace" font-size="10">• completed: BOOLEAN</text>
  </g>

  <!-- Bottom Exam Summary -->
  <rect x="25" y="530" width="910" height="90" rx="14" fill="rgba(15,23,42,0.95)" stroke="rgba(255,255,255,0.1)"/>
  <text x="45" y="560" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">💡 Architectural Flow &amp; Relational Guarantees:</text>
  <text x="45" y="585" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11.5">• Separation of Concerns: Client ──▶ Edge Gateway ──▶ Stateless Services ──▶ Cached Relational Database.</text>
  <text x="45" y="605" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11.5">• ACID Transactions ensure zero state corruption across concurrent quiz submissions and progress updates.</text>
</svg>"""


def build_variables_memory_svg():
    """Variables & Memory Allocation Architecture (Stack vs Heap)."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
  <defs>
    <linearGradient id="bgGradVar" x1="0%" y1="0%" x2="100%" y2="100%">
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
  <rect width="760" height="380" rx="20" fill="url(#bgGradVar)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(59,130,246,0.3)"/>
  <text x="40" y="47" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold">✦ VARIABLES &amp; MEMORY ALLOCATION ARCHITECTURE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Stack References ➔ Heap Objects</text>

  <!-- Stack Column (Variable Names) -->
  <rect x="50" y="85" width="260" height="220" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
  <rect x="50" y="85" width="260" height="34" rx="12" fill="url(#stackGrad)"/>
  <text x="180" y="108" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">STACK (Variable References)</text>
  
  <rect x="68" y="132" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="155" fill="#f8fafc" font-family="monospace" font-size="12">username ➔ 0x7A1</text>

  <rect x="68" y="176" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="199" fill="#f8fafc" font-family="monospace" font-size="12">total_score ➔ 0x7A2</text>

  <rect x="68" y="220" width="224" height="36" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="243" fill="#f8fafc" font-family="monospace" font-size="12">is_enrolled ➔ 0x7A3</text>

  <rect x="68" y="264" width="224" height="32" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="80" y="285" fill="#38bdf8" font-family="monospace" font-size="11">course_list ➔ 0x7A4</text>

  <!-- Pointer Arrows -->
  <path d="M 292 150 L 440 150" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 292 194 L 440 194" stroke="#34d399" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 292 238 L 440 238" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 292 280 L 440 280" stroke="#f472b6" stroke-width="2" stroke-dasharray="4"/>

  <!-- Heap Column (Values & Objects in Memory) -->
  <rect x="450" y="85" width="260" height="220" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <rect x="450" y="85" width="260" height="34" rx="12" fill="url(#heapGrad)"/>
  <text x="580" y="108" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">HEAP (Actual Objects in RAM)</text>

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
  <text x="70" y="346" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">💡 Core Takeaway:</text>
  <text x="180" y="346" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">Variables are named labels pointing to memory objects, making reassignment instantaneous.</text>
</svg>"""


def build_quantum_svg():
    """Quantum Computing Architecture & Qubit Dynamics."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
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
  <text x="40" y="47" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold">✦ QUANTUM COMPUTING ARCHITECTURE &amp; QUBIT DYNAMICS</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Bloch Sphere ➔ Gate Synthesis ➔ QPU Readout</text>

  <!-- Step 1: Classical Bit vs Qubit -->
  <g transform="translate(45, 85)">
    <rect width="200" height="215" rx="14" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="200" height="32" rx="12" fill="url(#qGrad1)"/>
    <text x="100" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">1. QUBIT SUPERPOSITION</text>
    <text x="14" y="58" fill="#f8fafc" font-family="monospace" font-size="12">|ψ⟩ = α|0⟩ + β|1⟩</text>
    <text x="14" y="82" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Classical: Bit is 0 OR 1</text>
    <text x="14" y="102" fill="#38bdf8" font-family="Inter, Arial, sans-serif" font-size="11">• Quantum: 0 AND 1 simultaneously</text>
    <text x="14" y="122" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Complex amplitudes: |α|²+|β|²=1</text>
    <text x="14" y="146" fill="#fcd34d" font-family="monospace" font-size="11">Bloch Sphere: (θ, φ)</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• N Qubits = 2ⁿ state vector</text>
    <text x="14" y="195" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="11">Exponential State Expansion</text>
  </g>

  <!-- Connection Arrow 1 -->
  <path d="M 255 190 L 285 190" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 2: Unitary Quantum Gates -->
  <g transform="translate(295, 85)">
    <rect width="200" height="215" rx="14" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="200" height="32" rx="12" fill="url(#qGrad2)"/>
    <text x="100" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">2. UNITARY GATE LOGIC</text>
    <text x="14" y="58" fill="#f472b6" font-family="monospace" font-size="12">U† · U = I (Reversible)</text>
    <text x="14" y="82" fill="#38bdf8" font-family="Inter, Arial, sans-serif" font-size="11">• Hadamard (H): Superposition</text>
    <text x="14" y="102" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Pauli-X: Quantum NOT gate</text>
    <text x="14" y="122" fill="#a78bfa" font-family="Inter, Arial, sans-serif" font-size="11">• CNOT: Entangles 2 Qubits</text>
    <text x="14" y="146" fill="#f8fafc" font-family="monospace" font-size="11">Bell State: (|00⟩+|11⟩)/√2</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Interference cancels noise</text>
    <text x="14" y="195" fill="#ec4899" font-family="Inter, Arial, sans-serif" font-size="11">Amplifies Correct Answer</text>
  </g>

  <!-- Connection Arrow 2 -->
  <path d="M 505 190 L 535 190" stroke="#ec4899" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 3: Cryogenic QPU & Measurement -->
  <g transform="translate(545, 85)">
    <rect width="180" height="215" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="12" fill="url(#qGrad3)"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">3. QPU &amp; READOUT</text>
    <text x="14" y="58" fill="#34d399" font-family="monospace" font-size="12">Cryogenic: 15 mK</text>
    <text x="14" y="82" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Dilution Refrigerator</text>
    <text x="14" y="102" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Microwave pulse control</text>
    <text x="14" y="122" fill="#fcd34d" font-family="Inter, Arial, sans-serif" font-size="11">• Wavefunction collapse</text>
    <text x="14" y="146" fill="#38bdf8" font-family="monospace" font-size="11">Measure ➔ |0⟩ or |1⟩</text>
    <text x="14" y="170" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Sampling across shots</text>
    <text x="14" y="195" fill="#10b981" font-family="Inter, Arial, sans-serif" font-size="11">Classical Histogram Out</text>
  </g>

  <!-- Bottom Insight -->
  <rect x="45" y="315" width="680" height="45" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="65" y="342" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">💡 Core Takeaway:</text>
  <text x="180" y="342" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">Quantum machines compute by rotating state vectors in Hilbert space, evaluating vast solution spaces simultaneously.</text>
</svg>"""


def build_function_svg():
    """Function Call Stack & Execution Pipeline."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="760" height="380">
  <defs>
    <linearGradient id="bgGradFunc" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e21"/>
      <stop offset="100%" stop-color="#111c38"/>
    </linearGradient>
  </defs>
  <rect width="760" height="380" rx="20" fill="url(#bgGradFunc)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(139,92,246,0.3)"/>
  <text x="40" y="47" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold">✦ FUNCTION CALL STACK &amp; EXECUTION PIPELINE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Inputs ➔ Frame Scope ➔ Return Pipeline</text>

  <!-- Step 1: Input Arguments -->
  <g transform="translate(45, 90)">
    <rect width="180" height="190" rx="12" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="180" height="32" rx="10" fill="#2563eb"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">1. ARGUMENTS (Input)</text>
    <text x="16" y="60" fill="#f8fafc" font-family="monospace" font-size="12">def calculate(a, b):</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Parameters passed</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Positional / keyword</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Default args evaluated</text>
    <text x="16" y="165" fill="#38bdf8" font-family="monospace" font-size="11">calculate(10, 5)</text>
  </g>

  <!-- Flow 1 -->
  <path d="M 235 185 L 275 185" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 2: Function Stack Frame -->
  <g transform="translate(285, 90)">
    <rect width="190" height="190" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="10" fill="#7c3aed"/>
    <text x="95" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">2. LOCAL STACK FRAME</text>
    <text x="16" y="60" fill="#c084fc" font-family="monospace" font-size="12">result = a * 2 + b</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Isolated local scope</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Local vars created</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Logic executed</text>
    <text x="16" y="165" fill="#34d399" font-family="monospace" font-size="11">Frame destroyed on exit</text>
  </g>

  <!-- Flow 2 -->
  <path d="M 485 185 L 525 185" stroke="#34d399" stroke-width="3" stroke-dasharray="4"/>

  <!-- Step 3: Return Output -->
  <g transform="translate(535, 90)">
    <rect width="180" height="190" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="10" fill="#059669"/>
    <text x="90" y="21" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">3. RETURN VALUE (Output)</text>
    <text x="16" y="60" fill="#34d399" font-family="monospace" font-size="12">return result</text>
    <text x="16" y="90" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Sent back to caller</text>
    <text x="16" y="112" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• Can return tuple/dict</text>
    <text x="16" y="134" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">• None returned if omitted</text>
    <text x="16" y="165" fill="#facc15" font-family="monospace" font-size="11">output = 25</text>
  </g>

  <!-- Bottom Insight -->
  <rect x="45" y="300" width="670" height="50" rx="12" fill="rgba(15,23,42,0.9)" stroke="rgba(255,255,255,0.1)"/>
  <text x="65" y="330" fill="#a78bfa" font-family="Outfit, Arial, sans-serif" font-size="13" font-weight="bold">🎯 Clean Architecture Principle:</text>
  <text x="270" y="330" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="12">Functions are modular black boxes: predictable inputs in, clean transformed outputs out.</text>
</svg>"""


def build_loop_svg():
    """Loop Iteration Flowchart & Lifecycle."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" width="760" height="360">
  <defs>
    <linearGradient id="bgGradLoop" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e21"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="760" height="360" rx="20" fill="url(#bgGradLoop)" stroke="rgba(255,255,255,0.1)"/>
  <rect x="25" y="20" width="710" height="42" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(6,182,212,0.3)"/>
  <text x="40" y="47" fill="#22d3ee" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold">✦ LOOP CONTROL FLOW &amp; ITERATION LIFECYCLE</text>
  <text x="715" y="46" text-anchor="end" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Sequence ➔ Condition ➔ Body ➔ Next</text>

  <!-- Step 1: Start -->
  <circle cx="90" cy="170" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="90" y="175" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-weight="bold" font-size="12">START</text>

  <path d="M 125 170 L 195 170" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: Condition Diamond -->
  <polygon points="280,105 365,170 280,235 195,170" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="280" y="165" text-anchor="middle" fill="#fcd34d" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Condition</text>
  <text x="280" y="180" text-anchor="middle" fill="#fcd34d" font-family="Outfit, Arial, sans-serif" font-size="11">True?</text>

  <!-- True path -->
  <path d="M 365 170 L 440 170" stroke="#10b981" stroke-width="2"/>
  <text x="400" y="160" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">YES</text>

  <!-- Step 3: Loop Body -->
  <rect x="440" y="130" width="160" height="80" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="520" y="160" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">Execute Loop Body</text>
  <text x="520" y="180" text-anchor="middle" fill="#94a3b8" font-family="monospace" font-size="11">print(item) / update</text>

  <!-- Cycle back arrow -->
  <path d="M 520 130 L 520 85 L 280 85 L 280 105" fill="none" stroke="#22d3ee" stroke-width="2" stroke-dasharray="4"/>
  <text x="400" y="75" text-anchor="middle" fill="#22d3ee" font-family="sans-serif" font-size="10">Next Iteration</text>

  <!-- False path (Exit) -->
  <path d="M 280 235 L 280 290 L 630 290" fill="none" stroke="#ef4444" stroke-width="2"/>
  <text x="295" y="260" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">NO (Done)</text>

  <!-- Step 4: Finish -->
  <circle cx="665" cy="290" r="30" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
  <text x="665" y="295" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-weight="bold" font-size="11">EXIT</text>
</svg>"""


def _esc_xml(t):
    return (str(t or "")).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', '&quot;')


def build_topic_concept_table_svg(topic_query="Neural Networks"):
    """Generates a high-definition 1040x700 vector SVG diagram card containing:
    1. Header banner with icon & title
    2. Neat explanation box (definition, mechanism, why it matters, key benefit)
    3. Intuitive mental model card (everyday analogy, key production rule)
    4. Structured 5-column vector comparison/summary table (Component, Plain English, Analogy, Code, Takeaway)
    5. Bottom exam mastery & checklist bar
    """
    raw_topic = re.sub(r'^(?:draw|show|generate|create|render|visualize|diagram|visual|image|photo|table|roadmap|an?|the|of|for|about)\s+', '', str(topic_query).strip(), flags=re.I).strip()
    clean_topic = raw_topic.title() if raw_topic else "Concept Architecture"
    p_lower = str(topic_query).lower()

    # Pre-built curated domain profiles with high pedagogical precision
    if any(k in p_lower for k in ["photosynthesis", "chloroplast", "calvin cycle", "plant biology"]):
        title = "PHOTOSYNTHESIS & BIOCHEMICAL CELL CYCLE"
        icon = "🌿"
        badge = "Biological Science"
        definition = "The biochemical process converting solar photons, water, and CO2 into chemical glucose energy."
        how_it_works = "Light reactions generate ATP/NADPH in thylakoids; the Calvin cycle fixes CO2 into sugars in the stroma."
        why_it_matters = "Supplies Earth's oxygen atmosphere and forms the foundational energy base of almost all global food webs."
        benefit = "Produces storable high-energy sugars (glucose) and releases breathable O2 as an essential byproduct."
        analogy = "Solar panels charging batteries (Light Reactions) that power an automated sugar bakery (Calvin Cycle)!"
        rule = "Equation: 6 CO2 + 6 H2O + Solar Photons ➔ C6H12O6 (Glucose) + 6 O2 (Atmospheric Oxygen)."
        rows = [
            ("1. Light Reactions", "Thylakoid solar converters", "Splits H2O molecules using absorbed photons;", "generates high-energy ATP and NADPH carriers.", "Solar panel array", "charging backup batteries", "H2O + Photons ➔ O2 + ATP", "Releases O2", "Occurs in thylakoid membrane"),
            ("2. Photosystem II & I", "Chlorophyll pigment hubs", "Absorbs 680nm/700nm wavelength light to excite", "electrons through the electron transport chain.", "Quantum photon antennas", "harvesting solar waves", "P680 & P700 excitation", "Drives Proton Pump", "Generates H+ concentration gradient"),
            ("3. ATP Synthase", "Proton motor turbine", "Channels concentrated H+ protons across membrane,", "spinning catalytic head to synthesize cellular ATP.", "Hydroelectric dam turbine", "harnessing water pressure", "ADP + Pi ➔ ATP", "Universal Energy", "Powers the downstream Calvin cycle"),
            ("4. Calvin Cycle", "Stroma carbon fixation", "Rubisco enzyme binds atmospheric CO2 to RuBP,", "producing 3-PGA, then reduced to G3P sugars.", "Automated factory robot", "assembling carbon rings", "3 CO2 ➔ 1 G3P (sugar precursor)", "Light-Independent", "Consumes ATP & NADPH in stroma"),
            ("5. Glucose Synthesis", "Stable hexose energy store", "Two 3-carbon G3P molecules condense into stable", "C6H12O6 glucose, polymerized into starch.", "Packed survival emergency rations", "ready for long storage", "2 G3P ➔ C6H12O6 (Glucose)", "Chemical Storage", "Powers cellular respiration")
        ]
        checklist = "Mastery Sequence: Sunlight & H2O ➔ Thylakoid Photolysis ➔ ATP/NADPH ➔ Stroma Calvin Fixation ➔ Glucose & O2 Output."

    elif any(k in p_lower for k in ["brain", "cerebrum", "cerebellum", "neuroscience", "neuron"]) and "neural net" not in p_lower:
        title = "HUMAN BRAIN ANATOMY & NEURAL REGIONS"
        icon = "🧠"
        badge = "Neuroscience"
        definition = "The central nervous system organ governing cognition, sensory perception, motor control, and autonomic life support."
        how_it_works = "86 billion interconnected neurons transmit electrical action potentials and chemical neurotransmitters across synapses."
        why_it_matters = "Controls consciousness, memory retrieval, speech production, emotional regulation, and vital organ coordination."
        benefit = "Performs millisecond real-time sensorimotor processing with lifelong neuroplastic adaptability."
        analogy = "A supercomputing cluster: Cerebrum is the main CPU, Cerebellum is the motion stabilizer, Brainstem is the BIOS power supply!"
        rule = "Rule: Neurons that fire together wire together (Hebbian synaptic plasticity and long-term potentiation)."
        rows = [
            ("1. Frontal Lobe", "Executive control center", "Coordinates decision making, impulse control,", "abstract reasoning, and motor cortex output.", "Chief Executive Officer", "directing department operations", "Motor cortex & Broca's area", "Executive Function", "Primary seat of conscious personality"),
            ("2. Temporal Lobe", "Auditory & memory vault", "Decodes auditory signals, processes language comprehension", "(Wernicke's), and anchors episodic memory.", "Library catalog & speech audio desk", "indexing spoken words", "Hippocampus & Wernicke's", "Memory & Hearing", "Crucial for long-term memory encoding"),
            ("3. Parietal Lobe", "Somatosensory integration", "Maps bodily tactile touch, temperature, pressure,", "pain signals, and computes 3D spatial navigation.", "3D GPS sensory mapping console", "tracking bodily position", "Primary somatosensory strip", "Spatial Sense", "Synthesizes multi-sensory environment"),
            ("4. Occipital Lobe", "Visual processing engine", "Deconstructs optical nerve signals into edge orientation,", "color spectra, motion vectors, and facial recognition.", "High-speed optical GPU card", "decoding incoming video stream", "V1 to V5 visual cortices", "Visual Cortex", "Transforms light into mental imagery"),
            ("5. Cerebellum & Stem", "Motor tuning & vital reflexes", "Smooths balance and coordinated movements (cerebellum);", "regulates autonomic cardiac rhythm & respiration (stem).", "Gyroscope stabilizer & BIOS", "running vital survival systems", "Medulla, Pons, Cerebellum", "Autonomic Life", "Maintains survival without conscious effort")
        ]
        checklist = "Brain Architecture: Frontal (Decisions) ➔ Temporal (Memory/Speech) ➔ Parietal (Touch/Space) ➔ Occipital (Vision) ➔ Stem (Vitality)."

    elif any(k in p_lower for k in ["heart", "cardiac", "circulation", "cardiovascular"]) and "neural" not in p_lower:
        title = "HUMAN HEART ANATOMY & 4-CHAMBER CIRCULATION"
        icon = "❤️"
        badge = "Cardiovascular Medicine"
        definition = "Muscular pump driving continuous, synchronized dual-circuit blood circulation across the entire human body."
        how_it_works = "Sinoatrial node triggers electrical waves causing sequential atrial contraction followed by ventricular ejection."
        why_it_matters = "Delivers oxygen and nutrients to tissues while carrying away metabolic carbon dioxide and cellular waste."
        benefit = "Endlessly beats ~100,000 times daily with dynamic cardiac output scaling from 5 to 25+ liters/minute."
        analogy = "Dual-action plumbing pump: Right side pumps blood to the filtration plant (Lungs); Left side delivers purified water to the city (Body)!"
        rule = "Rule: Arteries carry blood Away from the heart; Veins return blood back toward the heart."
        rows = [
            ("1. Right Atrium", "Deoxygenated intake chamber", "Receives venous blood from Superior/Inferior Vena", "Cava; passes blood down through Tricuspid valve.", "Inbound receiving warehouse", "unloading returned empty containers", "Tricuspid Valve intake", "Low Pressure", "Collects oxygen-depleted systemic blood"),
            ("2. Right Ventricle", "Pulmonary circuit pump", "Propels deoxygenated blood through the Pulmonary", "valve into pulmonary arteries leading to the lungs.", "Booster pump to oxygen refinery", "dispatching blood to lung alveoli", "Pulmonary Semilunar Valve", "To Lungs", "Lower muscular wall thickness than left"),
            ("3. Left Atrium", "Oxygenated return receiver", "Collects freshly oxygen-rich blood returning from", "the lungs via four pulmonary veins into Bicuspid valve.", "Clean water reservoir", "holding purified fluid for distribution", "Mitral (Bicuspid) Valve", "Oxygen-Rich", "Prepares left ventricle for high-pressure fill"),
            ("4. Left Ventricle", "Systemic high-pressure driver", "Thickest muscular myocardium; contracts forcefully to", "eject blood through Aortic valve into systemic Aorta.", "High-pressure municipal water main", "pumping fluid to multi-story buildings", "Aorta (120 mmHg peak)", "Systemic Drive", "Powers entire bodily systemic circulation"),
            ("5. SA / AV Nodes", "Electrical conduction pacemaker", "Sinoatrial node generates rhythmic action potentials", "propagating down Bundle of His and Purkinje fibers.", "Digital clock quartz crystal", "setting tempo for industrial machinery", "SA ➔ AV ➔ Purkinje fibers", "Intrinsic Rhythm", "Coordinates synchronized lub-dub contractions")
        ]
        checklist = "Circulation Loop: Vena Cava ➔ Right Atrium ➔ Right Ventricle ➔ Lungs (Oxygenation) ➔ Left Atrium ➔ Left Ventricle ➔ Aorta."

    elif any(k in p_lower for k in ["os", "operating system", "kernel", "process management", "cpu scheduling"]):
        title = "OPERATING SYSTEM ARCHITECTURE & KERNEL DYNAMICS"
        icon = "💻"
        badge = "Systems & OS"
        definition = "Core system software mediating between application programs and underlying physical hardware resources."
        how_it_works = "Kernel manages CPU scheduling, virtual memory paging, device drivers, and system call hardware interrupts."
        why_it_matters = "Guarantees resource isolation, preemptive multitasking, fault tolerance, and secure abstract storage systems."
        benefit = "Allows concurrent applications to execute safely without memory corruption or unauthorized hardware access."
        analogy = "Air traffic controller & runway coordinator: schedules hundreds of flights with zero mid-air collisions or gridlock!"
        rule = "Rule: User applications must execute system calls (syscalls) to transition from Ring 3 (User) to Ring 0 (Kernel)."
        rows = [
            ("1. Kernel & Syscalls", "Privileged hardware bridge", "Provides secure API interface for user programs to", "request low-level I/O, networking, and memory.", "Embassy border security checkpoint", "verifying diplomatic travel credentials", "sys_read(), sys_write()", "Ring 0 Privilege", "Enforces memory and execution boundaries"),
            ("2. Process & Threads", "Execution workload units", "Process holds isolated virtual address space;", "threads share process memory for lightweight concurrency.", "Independent office rooms (processes)", "with shared collaborative desks (threads)", "fork(), clone(), pthread_create()", "Memory Isolation", "Threads share heap; have private stacks"),
            ("3. CPU Scheduler", "Clock cycle arbitrator", "Preemptively allocates CPU time slices using", "algorithms like Linux CFS (Completely Fair Scheduler).", "Traffic light signal timer", "allocating green lights fairly across lanes", "sched_yield(), context_switch()", "Fair Allocation", "Minimizes latency and prevents starvation"),
            ("4. Virtual Memory & MMU", "Hardware address translation", "Translates virtual page addresses to physical RAM", "frames using page tables; handles disk page swapping.", "Postal mail forwarding bureau", "mapping recipient alias to real physical door", "mprotect(), mmap(), page_fault", "Page Tables", "Enables demand paging and process isolation"),
            ("5. File System & VFS", "Hierarchical block storage", "Abstracts raw disk sectors into directories, inodes,", "permissions, buffers, and journaling transactions.", "Master library filing index", "locating books by unique catalog codes", "open(), read(), write(), fsync()", "ACID File Safety", "Journaling prevents corruption on sudden crash")
        ]
        checklist = "OS Stack Flow: User App ➔ Syscall (Ring 0) ➔ Kernel Subsystems (Scheduler/VFS/MMU) ➔ Hardware Drivers ➔ Physical CPU/RAM/Disk."

    elif any(k in p_lower for k in ["database", "sql", "dbms", "rdbms", "relational", "nosql"]):
        title = "DATABASE MANAGEMENT SYSTEMS & SQL ARCHITECTURE"
        icon = "🗄️"
        badge = "Database Engineering"
        definition = "Engineered data storage systems guaranteeing durable persistence, ACID transactions, and sub-millisecond query retrieval."
        how_it_works = "Parses SQL queries into relational algebra ASTs, cost-optimizes execution plans, and queries indexed B-trees on disk."
        why_it_matters = "Ensures mission-critical financial, user, and analytical records are never lost, duplicated, or corrupted."
        benefit = "Sub-millisecond record lookups and atomic rollback protection against sudden power failure or software crashes."
        analogy = "High-security financial ledger vault where every transaction is double-checked and audited before permanent stamping!"
        rule = "Rule: Index columns frequently filtered (WHERE) or joined (JOIN); beware excessive write penalty on secondary indexes."
        rows = [
            ("1. Tables & Schema", "Relational record definitions", "Defines strict data types, primary keys, foreign", "key constraints, and normalization rules.", "Standardized official ledger form", "with labeled required entry blanks", "CREATE TABLE users (...)", "Data Integrity", "Primary key guarantees record uniqueness"),
            ("2. Query Optimizer", "Execution plan cost evaluator", "Evaluates index scans vs sequential scans based on", "table row cardinality statistics and disk page cost.", "GPS navigation satellite", "picking fastest highway vs local streets", "EXPLAIN ANALYZE SELECT ...", "Cost-Based Opt", "Picks optimal join algorithms (Hash vs Loop)"),
            ("3. B+ Tree Indexing", "Balanced logarithmic search tree", "Stores sorted keys in leaf nodes connected by", "linked list for O(log N) point and range queries.", "Thumb-tabbed dictionary index", "flipping directly to target word letter", "CREATE INDEX idx_user_email", "O(log N) Search", "Dramatically accelerates SELECT query filters"),
            ("4. ACID Engine", "Reliability transaction contract", "Atomicity (all-or-nothing), Consistency, Isolation", "(MVCC), and Durability (WAL write-ahead logging).", "Legally binding signed bank contract", "reversing all steps if any transfer fails", "BEGIN; ... COMMIT; ROLLBACK;", "Zero Corruption", "Protects against partial writes during crashes"),
            ("5. Write-Ahead Log", "Crash recovery journal", "Appends changes sequentially to disk WAL before", "updating in-memory RAM buffer pool dirty pages.", "Airplane indestructible black-box recorder", "logging every action before execution", "WAL flush & Checkpointing", "Durability (D)", "Guarantees zero data loss on unexpected power cut")
        ]
        checklist = "Database Lifecycle: SQL Query ➔ AST Parser ➔ Cost Optimizer ➔ B+ Tree Index Scan ➔ MVCC Isolation ➔ WAL Commit."

    elif any(k in p_lower for k in ["docker", "container", "containerization", "kubernetes", "k8s"]):
        title = "DOCKER & CONTAINERIZATION ARCHITECTURE"
        icon = "🐳"
        badge = "DevOps & Containers"
        definition = "Standardized lightweight packaging bundling code with all system dependencies into immutable, isolated runtimes."
        how_it_works = "Leverages Linux kernel namespaces (isolation) and cgroups (resource limits) over a shared underlying host kernel."
        why_it_matters = "Completely eliminates 'it works on my machine' defects and enables reproducible deployments across cloud environments."
        benefit = "Near-instant startup times (milliseconds) with a tiny memory footprint compared to full virtual machines (VMs)."
        analogy = "Standardized cargo shipping containers: packed once with goods and loaded seamlessly onto cargo ships, trains, or trucks!"
        rule = "Rule: Keep container images lightweight and immutable: one process per container, use multi-stage Docker builds."
        rows = [
            ("1. Dockerfile", "Declarative build recipe", "Plaintext configuration defining base OS image,", "dependencies, environment variables, and entrypoint.", "Culinary baking recipe", "specifying exact ingredients and bake steps", "FROM python:3.11-slim", "Reproducible", "Pin exact base image tags for stability"),
            ("2. Container Image", "Immutable layered filesystem", "Read-only stacked UnionFS layers cached and", "pushed to Docker Hub or private cloud registries.", "Frozen TV dinner tray", "pre-assembled and ready to heat instantly", "docker build -t app:v1 .", "Layer Caching", "Multi-stage builds strip compile tools"),
            ("3. Container Runtime", "Isolated execution sandbox", "Active running process restricted by PID, network,", "and mount namespaces with CPU/RAM cgroup limits.", "Operating kitchen appliance", "running safely on dedicated electrical circuit", "docker run -d -p 8080:80 app", "Ephemeral Life", "Containers are stateless and easily replaced"),
            ("4. Volumes & Mounts", "Persistent storage decoupling", "Binds persistent host filesystem directories to the", "container, preserving data across restarts.", "Plug-in external solid-state drive", "keeping files safe when computer reboots", "-v /host/data:/app/data", "Data Persistence", "Keeps database files intact on container stop"),
            ("5. Docker Compose", "Multi-container coordinator", "Declares multi-service architectures (app, redis, db)", "and internal bridge networks in a single YAML file.", "General construction contractor", "orchestrating plumbing, electrical, & carpentry", "docker compose up -d", "Local Full-Stack", "Spins up entire multi-tier environment in one click")
        ]
        checklist = "Container Pipeline: Dockerfile ➔ Image Layers ➔ Container Runtime ➔ Volume Mounts ➔ Compose / K8s Pod Orchestration."

    elif any(k in p_lower for k in ["security", "cyber", "cybersecurity", "encryption", "firewall", "jwt"]):
        title = "CYBERSECURITY & DEFENSE-IN-DEPTH ARCHITECTURE"
        icon = "🛡️"
        badge = "Security Engineering"
        definition = "Multi-layered defensive engineering safeguarding identities, networks, data integrity, and computing infrastructure."
        how_it_works = "Applies Zero Trust verification, cryptographic encryption, least-privilege RBAC, and telemetry anomaly detection."
        why_it_matters = "Prevents catastrophic data breaches, ransomware paralysis, unauthorized exfiltration, and compliance penalties."
        benefit = "Limits attack blast radius and provides full forensic auditability across distributed modern systems."
        analogy = "A medieval fortress: moat and drawbridge (Firewall), biometric gate passes (IAM), and underground vault ciphers (Encryption)!"
        rule = "Rule: Never trust, always verify (Zero Trust); enforce the principle of least privilege across all service tokens."
        rows = [
            ("1. Identity & IAM", "Authentication & Access Control", "Verifies caller identity via MFA/OAuth2 and enforces", "strict role-based access control (RBAC) permissions.", "Biometric keycard security badge", "checking authorization at every doorway", "OAuth 2.0 / OIDC / RBAC", "Least Privilege", "Only grant minimum permissions needed for role"),
            ("2. Network Firewall & WAF", "Traffic perimeter filtration", "Inspects IP packets, blocks SQL injection/XSS,", "and isolates cloud VPC private database subnets.", "Fortress moat & drawbridge portcullis", "inspecting all incoming wagons for weapons", "AWS WAF / iptables / Security Group", "Perimeter Defense", "Default-deny policy for all inbound traffic"),
            ("3. Cryptography (TLS/AES)", "Data encryption at rest & transit", "Encrypts payload transmissions with TLS 1.3 and", "secures database records with AES-256 block ciphers.", "Unbreakable military cipher codebook", "protecting messages even if intercepted", "AES-GCM-256 / RSA / ECC", "Confidentiality", "Protects against eavesdropping and packet sniffing"),
            ("4. Vulnerability & SAST", "Static analysis & CVE scanning", "Continuously audits source code and container dependencies", "for published CVE exploits and buffer overflows.", "Building structural safety inspector", "spotting hidden cracks before bridge opens", "Trivy / Snyk / SonarQube / Semgrep", "Shift Left", "Patch high and critical CVEs in CI/CD pipeline"),
            ("5. SIEM & Threat SOC", "Telemetry logging & incident response", "Correlates access logs, flags unusual egress spikes,", "and triggers automated quarantine upon compromise.", "24/7 central security monitoring room", "watching live cameras for intruder movement", "Splunk / Datadog / Elastic SIEM", "Rapid Containment", "Enables sub-hour containment of active threats")
        ]
        checklist = "Defense Layers: Zero Trust IAM ➔ Perimeter WAF ➔ TLS/AES Encryption ➔ SAST Dependency Audit ➔ SIEM SOC Monitoring."

    elif any(k in p_lower for k in ["solar system", "planet", "astronomy", "sun", "jupiter", "earth"]):
        title = "SOLAR SYSTEM & PLANETARY ORBITAL ARCHITECTURE"
        icon = "☀️"
        badge = "Astrophysics"
        definition = "The gravitationally bound celestial system comprising the Sun and the astronomical bodies orbiting within its heliosphere."
        how_it_works = "Solar gravitational mass governs elliptical Keplerian orbits and conservation of angular momentum across all planets."
        why_it_matters = "Our cosmic habitat: illuminates planetary accretion, habitable goldilocks zones, and celestial orbital mechanics."
        benefit = "Continuous solar thermonuclear fusion provides predictable solar irradiance sustaining terrestrial life and climates."
        analogy = "A cosmic merry-go-round: central massive pillar spins and pulls four inner rocky carts and four outer gas leviathans!"
        rule = "Rule: Kepler's 3rd Law: The square of orbital period is proportional to cube of semi-major axis (P² = a³)."
        rows = [
            ("1. The Sun (Sol)", "G-type main sequence star", "Contains 99.86% of total system mass; powers the", "heliosphere via proton-proton hydrogen fusion.", "Central nuclear fusion generator", "anchoring all orbital paths with gravity", "4H ➔ He + 2e+ + 2v + Energy", "Gravitational Anchor", "Nuclear core reaches 15 million Kelvin"),
            ("2. Terrestrial Worlds", "Inner rocky silicate planets", "Mercury, Venus, Earth, Mars: dense metallic iron cores", "surrounded by silicate mantles; high density.", "Compact inner rocky residential block", "closest to the warm central furnace", "Mercury, Venus, Earth, Mars", "Goldilocks Zone", "Earth possesses liquid water and protective magnetosphere"),
            ("3. Asteroid Belt", "Planetary accretion debris ring", "Millions of rocky and metallic planetesimals between", "Mars and Jupiter; contains dwarf planet Ceres.", "Construction gravel rubble zone", "prevented from coalescing by Jupiter's gravity", "Ceres, Vesta, Pallas", "Boundary Line", "Separates inner rocky planets from outer gas giants"),
            ("4. Gas & Ice Giants", "Outer massive fluid leviathans", "Jupiter & Saturn (H/He gas giants); Uranus &", "Neptune (water/ammonia/methane ice giants).", "Outer massive industrial storage towers", "commanding vast rings and dozens of moons", "Jupiter, Saturn, Uranus, Neptune", "Gravitational Shield", "Jupiter's massive gravity deflects rogue comets"),
            ("5. Kuiper Belt & Oort", "Trans-Neptunian icy reservoir", "Icy planetesimals, dwarf planets (Pluto, Eris), and", "spherical Oort cloud reservoir of long-period comets.", "Outer frozen cosmic perimeter fence", "holding primordial solar nebula remnants", "Pluto, Haumea, Cometary nuclei", "Deep Reservoir", "Extends nearly a light-year into interstellar space")
        ]
        checklist = "Solar System Architecture: Sun (Core) ➔ Inner Terrestrial ➔ Asteroid Belt ➔ Gas Giants ➔ Kuiper Belt & Oort Cloud."

    elif any(k in p_lower for k in ["quantum", "qubit", "superposition", "quantum computing"]):
        title = "QUANTUM COMPUTING & QUBIT MECHANICS"
        icon = "⚛️"
        badge = "Quantum Information"
        definition = "Advanced computational paradigm leveraging quantum mechanical phenomena (superposition, entanglement) for intractable problems."
        how_it_works = "Manipulates probability amplitudes across 2^N quantum state vectors using reversible unitary matrix logic gates."
        why_it_matters = "Enables exponential speedups for integer factorization (Shor's), chemical simulations, and combinatorial optimization."
        benefit = "Explores vast multidimensional solution landscapes simultaneously rather than sequential trial-and-error."
        analogy = "A spinning coin: while spinning, it exists in a blend of heads and tails simultaneously until slapped onto the tabletop!"
        rule = "Rule: Quantum measurement collapses the superposition into a single deterministic classical state (0 or 1)."
        rows = [
            ("1. Qubit (Quantum Bit)", "Two-state quantum vector", "State represented as |ψ⟩ = α|0⟩ + β|1⟩ where the", "squared amplitudes (|α|² + |β|²) must sum to 1.", "Spinning weighted coin in mid-air", "before it settles onto the table surface", "q = QuantumRegister(1)", "Superposition", "Holds continuous probability amplitudes"),
            ("2. Hadamard Gate (H)", "Superposition initiator", "Rotates classical computational basis state |0⟩ into", "an equal superposition state (|0⟩ + |1⟩)/√2.", "Flicking stationary coin into a spin", "creating 50/50 probability", "qc.h(0)", "Equal Parallelism", "Core building block of all quantum algorithms"),
            ("3. Entanglement (CNOT)", "Non-local quantum correlation", "Couples two qubits into a unified Bell state where", "measuring one instantly determines the other's state.", "Pair of magical interconnected dice", "always landing on identical values", "qc.cx(control, target)", "Non-Local Link", "Powers quantum teleportation and exponential speedup"),
            ("4. Unitary Quantum Gates", "Reversible state rotations", "Applies unitary matrices (Phase, X, Y, Z, Toffoli)", "rotating state vectors around the Bloch sphere.", "Precision lens realigning light beams", "preserving total beam energy", "qc.rz(theta, 0)", "Reversible Logic", "Zero information loss before final measurement"),
            ("5. Decoherence & Shield", "Quantum fidelity preservation", "Protects delicate qubits from environmental thermal noise", "and electromagnetic interference using dilution fridges.", "Delicate crystal sculpture in vault", "shielded from slightest ground vibration", "Cryostat (< 15 millikelvin)", "Fault Tolerance", "Requires quantum error correction surface codes")
        ]
        checklist = "Quantum Circuit: Initialize Qubits ➔ Hadamard Superposition ➔ Entanglement Gates ➔ Phase Kickback ➔ Collapse Measurement."

    elif any(k in p_lower for k in ["dsa", "data structure", "algorithm", "linked list", "binary search", "sorting", "stack", "queue"]):
        title = "DATA STRUCTURES & ALGORITHMIC COMPLEXITY"
        icon = "🌲"
        badge = "Computer Science Core"
        definition = "Systematic techniques for organizing, storing, and accessing data paired with deterministic computational procedures."
        how_it_works = "Structures govern memory layout; algorithms manipulate data with provable Big-O Time and Space asymptotic bounds."
        why_it_matters = "The fundamental bedrock of software efficiency: turns unscalable O(N²) bottlenecks into lightning O(log N) speed."
        benefit = "Ensures systems scale from 10 records to 100,000,000 records smoothly without crashing CPU or exhausting memory."
        analogy = "Selecting the right kitchen tool: chopping vegetables with a sharp chef's knife vs attempting to use a plastic spoon!"
        rule = "Rule: Master the Space-Time trade-off: caching or hash lookups consume extra RAM to save precious CPU compute time."
        rows = [
            ("1. Array & Dynamic List", "Contiguous linear memory", "Fixed or dynamic contiguous memory blocks; delivers", "instant O(1) random index access but O(N) insertions.", "Row of numbered lockers in a gym", "walking straight to locker #42 instantly", "arr[i] ➔ O(1) read", "Cache Locality", "Ideal for sequential reads and fixed-size lists"),
            ("2. Hash Map (Dictionary)", "Key-value hash bucket mapping", "Computes hash code of key to jump directly to array", "bucket; delivers O(1) average lookup, insert, delete.", "Alphabetical postal sorting boxes", "filing letters directly into labeled slots", "map[key] = value ➔ O(1)", "O(1) Avg Speed", "Handle hash collisions via separate chaining"),
            ("3. Stack & Queue", "LIFO & FIFO linear buffers", "Stack enforces Last-In-First-Out (push/pop);", "Queue enforces First-In-First-Out (enqueue/dequeue).", "Stack of cafeteria trays vs grocery line", "taking the top tray / serving first customer", "stack.pop() / queue.popleft()", "Order Guarantee", "Stacks power call trees; Queues power BFS & tasks"),
            ("4. Binary Search Tree", "Sorted hierarchical node tree", "Left child < Parent < Right child; delivers O(log N)", "search, insert, delete when balanced (AVL/Red-Black).", "Decision flowchart tree", "eliminating half the possibilities at every step", "tree.search(target) ➔ O(log N)", "Balanced Trees", "Unbalanced BSTs degrade to slow O(N) linked lists"),
            ("5. Graph & BFS / DFS", "Vertices and edge networks", "Models interconnected networks (social, road, dependency);", "traverses nodes using Queue (BFS) or Stack/Recursion (DFS).", "Airline flight route connection map", "finding shortest route between airports", "bfs(graph, start) ➔ O(V + E)", "Pathfinding", "BFS finds shortest path; DFS explores all depths")
        ]
        checklist = "DSA Analysis: Identify Data Structure ➔ Inspect Worst-Case Time O(N) ➔ Inspect Memory Space O(N) ➔ Optimize Bottlenecks."

    elif any(k in p_lower for k in ["neural", "deep learning", "ai", "machine learning", "perceptron", "artificial intelligence", "ml"]):
        title = "NEURAL NETWORKS & DEEP LEARNING ARCHITECTURE"
        icon = "🧠"
        badge = "AI & ML Architecture"
        definition = "A computational learning system transforming numerical signals across weighted layers."
        how_it_works = "Linear transformations (W·x + b) are passed through non-linear activation functions."
        why_it_matters = "Enables models to discover complex, non-linear representations directly from data."
        benefit = "Learns abstract features automatically without manual feature engineering."
        analogy = "Think of an assembly line committee: Station 1 detects edges, Station 2 identifies shapes, and Station 3 classifies objects!"
        rule = "Rule: Multi-layer networks require activation gates to avoid linear collapse."
        rows = [
            ("1. Input Layer", "Raw sensory entry point", "Ingests raw numerical features (e.g. pixels,", "tokens, normalized audio frequencies).", "Sensory organs", "(eyes/ears receiving stimuli)", "x = tensor([2.5, 1.8])", "Must be normalized", "to [0, 1] or std-normal"),
            ("2. Weights & Biases", "Learnable linear coefficients", "Multiplies inputs to calibrate feature influence;", "bias shifts activation threshold along axis.", "Volume equalizer dials", "adjusting each instrument", "y = W @ x + b", "Updated by SGD", "during backprop pass"),
            ("3. Activation Function", "Non-linear firing gate", "Applies non-linearity so multi-layer networks", "do not collapse into a single linear regression.", "Circuit electrical fuse", "triggering above voltage", "a = torch.relu(y)", "ReLU is default", "Avoids vanishing grad"),
            ("4. Hidden Layers", "Deep latent feature space", "Hierarchically aggregates low-level features", "into complex high-level contextual concepts.", "Executive committee", "synthesizing department reports", "h2 = layer2(h1)", "More depth = power", "Use Dropout to prevent overfit"),
            ("5. Loss & Optimizer", "Error calculation & updates", "Calculates deviation between prediction & truth;", "calculates partial gradients to adjust all weights.", "Coach reviewing game film", "and guiding technique", "loss.backward(); opt.step()", "Adam Optimizer", "Adaptive learning rates")
        ]
        checklist = "Review each column from Left to Right: Inputs ➔ Weighted Sums ➔ Non-Linear Activation ➔ Latent Representations ➔ Backprop Optimization."

    elif any(k in p_lower for k in ["variable", "data type", "python variable", "datatype"]):
        title = "PYTHON VARIABLES & CORE DATA TYPES"
        icon = "🐍"
        badge = "Python Foundations"
        definition = "Named references pointing to dynamically allocated objects stored in computer memory."
        how_it_works = "Python assigns variable identifiers to heap objects without requiring explicit static typing."
        why_it_matters = "Allows flexible, readable data storage and manipulation across all algorithms."
        benefit = "Automatic garbage collection and dynamic typing speed up rapid software development."
        analogy = "A variable is like a sticky label attached to a storage box: you can reattach the label to a new box anytime!"
        rule = "Rule: Everything in Python is an object; variable assignment creates a reference, not a copy."
        rows = [
            ("1. String (str)", "Textual character sequence", "Immutable sequence of Unicode characters;", "supports slicing, formatting, and regex.", "Written message on card", "cannot be edited in-place", "name = 'Sastra AI'", "Immutable in Python", "Indexed with [0], [-1]"),
            ("2. Integer (int)", "Unbounded whole numbers", "Stores positive, negative, and zero integers;", "supports arbitrary precision arithmetic.", "Counting beads on abacus", "exact discrete counts", "count = 42", "Arbitrary precision", "Never overflows in Python 3"),
            ("3. Float (float)", "Real decimal numbers", "IEEE 754 double-precision floating point;", "handles scientific fractions and calculations.", "Markings on metric ruler", "fractional measurements", "score = 98.65", "Watch precision", "Use Decimal for currency"),
            ("4. Boolean (bool)", "Logical truth states", "Binary evaluation flags (True or False);", "subclass of integer where True == 1.", "Light on/off wall switch", "binary circuit decision", "is_ready = True", "Conditional logic", "Powers if/elif branching"),
            ("5. List & Dict", "Collections & hash maps", "Ordered mutable lists [ ] and key-value dicts { };", "essential for storing compound records.", "Expandable filing cabinet", "organized by labeled folders", "data = {'id': 1, 'items': []}", "Mutable collections", "Dict lookup is O(1) avg")
        ]
        checklist = "Mastery Rule: Know your types! Primitive immutables (str, int, float, bool) vs mutable containers (list, dict, set)."

    elif any(k in p_lower for k in ["cloud", "devops", "aws", "kubernetes", "docker", "terraform"]):
        title = "CLOUD COMPUTING & DEVOPS INFRASTRUCTURE"
        icon = "☁️"
        badge = "Cloud & Infrastructure"
        definition = "On-demand delivery of IT resources (compute, storage, networking) over the internet."
        how_it_works = "Hardware is virtualized and provisioned via declarative APIs and container engines."
        why_it_matters = "Eliminates physical data centers, enabling infinite elasticity and zero downtime."
        benefit = "Pay-as-you-go cost model with global high-availability across multiple regions."
        analogy = "Plugging into the municipal power grid: you draw electricity as needed without owning the power station!"
        rule = "Rule: Treat servers as cattle, not pets: automate all infrastructure with Infrastructure as Code."
        rows = [
            ("1. Compute (IaaS)", "Virtual machines & CPUs", "On-demand virtual server instances with configurable", "RAM, vCPU, and OS operating systems.", "Renting office floor space", "pay monthly for capacity", "AWS EC2 / GCP Compute", "Elastic Scaling", "Auto-scale behind LB"),
            ("2. Storage (S3)", "Durable object storage", "Scalable cloud storage for files, backups, and", "static media assets with 11 9's durability.", "Infinite safety deposit vault", "storing files by unique ID", "boto3.upload_file(bucket)", "99.999999999%", "Ultra-high durability"),
            ("3. Containers", "Isolated app packages", "Packages application code with all runtime libraries", "into lightweight immutable images.", "Standardized shipping box", "fits any cargo ship or train", "docker run -p 80:80 app", "Immutable runtime", "Runs identical everywhere"),
            ("4. Kubernetes", "Container orchestration", "Automates container deployment, scaling, health", "checks, load balancing, and self-healing.", "Airport traffic controller", "routing and scheduling planes", "kubectl apply -f deploy.yaml", "Self-Healing", "Replaces failed pods"),
            ("5. CI/CD & IaC", "Automated delivery pipelines", "Codifies infrastructure in Terraform and triggers", "automated test & deployment upon git push.", "Automated factory robot", "assembling and testing cars", "terraform apply & git push", "Zero Downtime", "GitOps version control")
        ]
        checklist = "Architecture Flow: Linux Systems ➔ Cloud Core (AWS/GCP) ➔ Docker Containers ➔ Kubernetes Pods ➔ Terraform IaC."

    elif any(k in p_lower for k in ["web", "react", "frontend", "backend", "full stack", "fullstack", "api"]):
        title = "FULL-STACK WEB ARCHITECTURE & REST APIS"
        icon = "🌐"
        badge = "Web Systems"
        definition = "End-to-end web software integrating UI components, server routes, and databases."
        how_it_works = "Clients dispatch HTTP requests over REST/GraphQL; servers process and query databases."
        why_it_matters = "Powers modern distributed SaaS applications and interactive user experiences."
        benefit = "Clean separation of concerns allows frontend and backend to scale independently."
        analogy = "A dining restaurant: Customer is the Frontend, Waiter is the API, Kitchen is the Backend Database!"
        rule = "Rule: Never trust client input: validate all payloads on the backend server before processing."
        rows = [
            ("1. Client UI (React)", "Component tree & state", "Renders dynamic DOM interfaces reactively when", "internal component state or props change.", "Restaurant dining room", "interactive visual menu", "const [val, setVal] = useState()", "Virtual DOM diff", "Re-renders on change"),
            ("2. REST API / HTTP", "Stateless request protocol", "Standardized HTTP methods (GET, POST, PUT, DELETE)", "carrying JSON payloads across networks.", "Waiter taking orders", "between customer & kitchen", "POST /api/chat HTTP/1.1", "HTTP Status Codes", "200 OK, 400 Bad, 500 Err"),
            ("3. Backend (Flask)", "Server logic & routing", "Handles business logic, middleware auth tokens,", "validation, and database transactions.", "Head chef in kitchen", "preparing requested dishes", "@app.route('/api/chat', methods=...)", "Controller Layer", "Validates inputs & auth"),
            ("4. Database (SQL)", "Persistent tabular storage", "ACID-compliant relational database storing", "records with foreign keys and indexes.", "Organized pantry warehouse", "shelves labeled by category", "SELECT * FROM users WHERE id=?", "ACID Transactions", "Index foreign keys"),
            ("5. Auth (JWT)", "Stateless security tokens", "Cryptographically signed tokens proving caller", "identity and permission roles.", "VIP club wristband", "checked at secure gates", "jwt.encode(payload, secret)", "Stateless Auth", "Store in HttpOnly cookie")
        ]
        checklist = "Full-Stack Protocol: UI Interaction ➔ State Dispatch ➔ HTTP REST Payload ➔ Backend Auth & DB ➔ JSON Response."

    else:
        # Universal Smart Generator for any technical topic
        title = f"{clean_topic.upper()} — CONCEPT ARCHITECTURE"
        icon = "⚙️"
        badge = "Technical Architecture"
        definition = f"{clean_topic} is a core technology paradigm engineered to solve computational and structural challenges reliably."
        how_it_works = f"Processes inputs through defined modular interfaces, executing core logic deterministically."
        why_it_matters = f"Provides standardized patterns for reliability, scalability, and maintainability in software systems."
        benefit = f"Minimizes structural complexity while maximizing throughput and fault tolerance."
        analogy = f"Think of {clean_topic} as a precision engine: each modular gear performs one job with zero wasted energy!"
        rule = f"Rule: Follow high cohesion and low coupling when architecting systems around {clean_topic}."
        rows = [
            ("1. Core Interface", "Foundational entry contract", f"Declares baseline abstractions, interface contracts,", "and initial configuration parameters.", "Front doorway gate", "standardized entry point", "init_config(params)", "Explicit Contracts", "Document inputs cleanly"),
            ("2. Working Engine", "Core operational mechanics", f"Executes primary algorithmic workload,", "transforming raw input into structured state.", "Engine combustion chamber", "generating mechanical drive", "process_pipeline(data)", "Deterministic", "Pure functional logic"),
            ("3. Data State", "Storage & memory layout", f"Maintains transient and persistent state variables", "with thread-safe consistency guarantees.", "Secure storage locker", "retrieving items by key", "state.update(key, value)", "Thread Safety", "Guarantees integrity"),
            ("4. Error Defense", "Validation & fault tolerance", f"Guards against invalid inputs, timeout failures,", "and handles edge cases gracefully.", "Automobile airbags", "protecting on unexpected shock", "try: run() except Err: heal()", "Defensive Coding", "Catch exceptions early"),
            ("5. Output & Scale", "Production delivery & metrics", f"Emits transformed results, writes audit telemetry,", "and scales horizontally under load.", "High-speed conveyor belt", "delivering finished product", "export_result(payload)", "Production Ready", "Monitor system metrics")
        ]
        checklist = f"Mastery Checklist: Core Concept ➔ Working Mechanism ➔ Syntax / Implementation ➔ Error Handling ➔ Production Scale."

    # Build SVG XML
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 700" width="1040" height="700">
  <defs>
    <linearGradient id="bgGradTbl" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="50%" stop-color="#0c1833"/>
      <stop offset="100%" stop-color="#081022"/>
    </linearGradient>
    <linearGradient id="thGradTbl" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="cardShadowTbl" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1040" height="700" rx="24" fill="url(#bgGradTbl)" stroke="rgba(56,189,248,0.3)" stroke-width="1.5"/>

  <!-- Tech Grid Lines -->
  <path d="M 0,85 L 1040,85 M 0,240 L 1040,240 M 0,615 L 1040,615" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>

  <!-- Top Header Bar -->
  <g transform="translate(30, 18)">
    <rect width="980" height="56" rx="14" fill="rgba(15,23,42,0.85)" stroke="rgba(56,189,248,0.35)" stroke-width="1"/>
    <circle cx="35" cy="28" r="16" fill="#0284c7"/>
    <text x="35" y="34" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="16">{_esc_xml(icon)}</text>
    <text x="65" y="32" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="16" font-weight="bold">{_esc_xml(title)} — EXPLANATION &amp; TABLE</text>
    <text x="65" y="47" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="11">Sastra AI Pedagogical Vector Architecture • Structured Knowledge Matrix • 100% Vector Fidelity</text>
    <rect x="815" y="13" width="150" height="30" rx="8" fill="rgba(56,189,248,0.12)" stroke="#38bdf8"/>
    <text x="890" y="33" text-anchor="middle" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">{_esc_xml(badge)}</text>
  </g>

  <!-- Top Left: Neat Explanation Card -->
  <g transform="translate(30, 88)" filter="url(#cardShadowTbl)">
    <rect width="590" height="138" rx="14" fill="#0b152d" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="590" height="32" rx="12" fill="#1e3a8a"/>
    <text x="20" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">◈ NEAT TOPIC EXPLANATION: CORE CONCEPTS &amp; MECHANICS</text>
    <g transform="translate(20, 42)">
      <text x="0" y="16" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• What it is:</text>
      <text x="75" y="16" fill="#e2e8f0" font-family="Inter, Arial, sans-serif" font-size="11">{_esc_xml(definition[:85])}</text>
      <text x="0" y="38" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• How it works:</text>
      <text x="90" y="38" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(how_it_works[:85])}</text>
      <text x="0" y="60" fill="#93c5fd" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">• Why it matters:</text>
      <text x="98" y="60" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(why_it_matters[:85])}</text>
      <text x="0" y="82" fill="#34d399" font-family="Inter, Arial, sans-serif" font-size="10.5" font-weight="bold">⚡ Key Benefit: {_esc_xml(benefit[:75])}</text>
    </g>
  </g>

  <!-- Top Right: Intuitive Mental Model Card -->
  <g transform="translate(635, 88)" filter="url(#cardShadowTbl)">
    <rect width="375" height="138" rx="14" fill="#0b152d" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="375" height="32" rx="12" fill="#5b21b6"/>
    <text x="18" y="21" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">💡 INTUITIVE MENTAL MODEL</text>
    <g transform="translate(18, 44)">
      <text x="0" y="16" fill="#c084fc" font-family="Inter, Arial, sans-serif" font-size="11" font-weight="bold">Everyday Analogy:</text>
      <text x="0" y="36" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(analogy[:52])}</text>
      <text x="0" y="52" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(analogy[52:108])}</text>
      <rect x="0" y="66" width="338" height="22" rx="5" fill="rgba(139,92,246,0.15)" stroke="rgba(139,92,246,0.3)"/>
      <text x="10" y="81" fill="#e9d5ff" font-family="Inter, Arial, sans-serif" font-size="10" font-weight="bold">{_esc_xml(rule[:48])}</text>
    </g>
  </g>

  <!-- Main Section: Structured Vector Table Card -->
  <g transform="translate(30, 240)" filter="url(#cardShadowTbl)">
    <rect width="980" height="365" rx="16" fill="#091124" stroke="#06b6d4" stroke-width="1.8"/>
    
    <!-- Table Header Row -->
    <rect width="980" height="38" rx="14" fill="url(#thGradTbl)" stroke="#06b6d4" stroke-width="1"/>
    <text x="25" y="24" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">COMPONENT / FEATURE</text>
    <line x1="205" y1="0" x2="205" y2="38" stroke="rgba(6,182,212,0.3)"/>
    <text x="220" y="24" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">WHAT IT DOES (PLAIN ENGLISH)</text>
    <line x1="495" y1="0" x2="495" y2="38" stroke="rgba(6,182,212,0.3)"/>
    <text x="510" y="24" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">EVERYDAY INTUITION</text>
    <line x1="710" y1="0" x2="710" y2="38" stroke="rgba(6,182,212,0.3)"/>
    <text x="725" y="24" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">CODE / SYNTAX</text>
    <line x1="865" y1="0" x2="865" y2="38" stroke="rgba(6,182,212,0.3)"/>
    <text x="880" y="24" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="11.5" font-weight="bold">KEY TAKEAWAY</text>
"""

    colors = ["#60a5fa", "#22d3ee", "#f472b6", "#a78bfa", "#34d399"]
    for i, r in enumerate(rows):
        y_offset = 38 + (i * 62)
        c_name = colors[i % len(colors)]
        bg = "rgba(6,182,212,0.03)" if (i % 2 == 1) else "rgba(255,255,255,0.015)"
        h = 78 if (i == 4) else 62
        svg += f"""
    <!-- Row {i+1}: {r[0]} -->
    <g transform="translate(0, {y_offset})">
      <rect width="980" height="{h}" fill="{bg}"/>
      {"<line x1='0' y1='62' x2='980' y2='62' stroke='rgba(255,255,255,0.06)'/>" if i < 4 else ""}
      <text x="25" y="26" fill="{c_name}" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">{_esc_xml(r[0])}</text>
      <text x="25" y="44" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">{_esc_xml(r[1])}</text>
      <line x1="205" y1="0" x2="205" y2="{h}" stroke="rgba(255,255,255,0.05)"/>
      <text x="220" y="26" fill="#e2e8f0" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(r[2])}</text>
      <text x="220" y="44" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(r[3])}</text>
      <line x1="495" y1="0" x2="495" y2="{h}" stroke="rgba(255,255,255,0.05)"/>
      <text x="510" y="26" fill="#a78bfa" font-family="Inter, Arial, sans-serif" font-size="10.5">{_esc_xml(r[4])}</text>
      <text x="510" y="44" fill="#94a3b8" font-family="Inter, Arial, sans-serif" font-size="10">{_esc_xml(r[5])}</text>
      <line x1="710" y1="0" x2="710" y2="{h}" stroke="rgba(255,255,255,0.05)"/>
      <text x="725" y="34" fill="#34d399" font-family="monospace" font-size="11">{_esc_xml(r[6])}</text>
      <line x1="865" y1="0" x2="865" y2="{h}" stroke="rgba(255,255,255,0.05)"/>
      <text x="880" y="26" fill="#fde047" font-family="Inter, Arial, sans-serif" font-size="10" font-weight="bold">{_esc_xml(r[7])}</text>
      <text x="880" y="44" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="9.5">{_esc_xml(r[8])}</text>
    </g>"""

    svg += f"""
  </g>

  <!-- Bottom Insight & Exam Mastery Bar -->
  <g transform="translate(30, 618)">
    <rect width="980" height="64" rx="14" fill="rgba(15,23,42,0.95)" stroke="rgba(56,189,248,0.25)" stroke-width="1"/>
    <circle cx="28" cy="32" r="14" fill="#0369a1"/>
    <text x="28" y="37" text-anchor="middle" fill="#ffffff" font-family="Outfit, Arial, sans-serif" font-size="14">🎯</text>
    <text x="54" y="27" fill="#38bdf8" font-family="Outfit, Arial, sans-serif" font-size="12" font-weight="bold">STUDY MASTERY CHECKLIST &amp; EXAM INSIGHT:</text>
    <text x="54" y="46" fill="#cbd5e1" font-family="Inter, Arial, sans-serif" font-size="11">{_esc_xml(checklist[:130])}</text>
    <rect x="805" y="16" width="160" height="32" rx="8" fill="rgba(34,197,94,0.15)" stroke="#22c55e" stroke-width="1"/>
    <text x="885" y="36" text-anchor="middle" fill="#4ade80" font-family="Outfit, Arial, sans-serif" font-size="11" font-weight="bold">✓ 100% Vector Crisp</text>
  </g>
</svg>"""
    return svg


