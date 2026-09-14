"""Universal Step-by-Step Learning Path & Curriculum Engine for Sastra AI Chatbot.
Generates comprehensive 5-phase learning roadmaps, milestones, hands-on projects,
and structured summary tables for ANY topic.
"""

import re


def generate_learning_path(topic_query: str, user_name: str = "Learner") -> str:
    """Construct a comprehensive step-by-step curriculum and learning path for any topic."""
    raw = topic_query.strip()
    clean_topic = re.sub(
        r"^(?:learning\s+path\s+(?:for|on|about)?|roadmap\s+(?:for|on|about)?|curriculum\s+(?:for|on)?|how\s+to\s+learn|path\s+(?:to|for)|syllabus\s+(?:for|of)?)\s*",
        "", raw, flags=re.IGNORECASE
    ).strip()
    clean_topic = re.sub(r"[?!.]+$", "", clean_topic).strip()
    title = clean_topic.title() if clean_topic else "Technology & Computer Science"
    t_lower = title.lower()

    # Domain Knowledge Profiles
    if any(k in t_lower for k in ["python", "py"]):
        domain = "Programming & Software Engineering"
        est_time = "8–10 Weeks (5–8 hrs/week)"
        prereqs = "None (Beginner Friendly)"
        phases = [
            {
                "num": 1, "name": "Python Foundations & Primitives", "time": "Weeks 1–2",
                "objectives": "Master core syntax, data structures, variables, control flow, and functions.",
                "skills": ["Variables, Types (int, float, str, bool)", "Control Flow (if/else, while, for loops)", "Collections (Lists, Tuples, Dictionaries, Sets)", "Function definitions, args, kwargs, scope"],
                "project": "CLI Personal Finance Expense Tracker & Budget Calculator",
                "drill": "Write a script that reads user expenses and outputs total spend grouped by category."
            },
            {
                "num": 2, "name": "Object-Oriented Design & Modular Architecture", "time": "Weeks 3–4",
                "objectives": "Write scalable, reusable Python modules with OOP, classes, and error handling.",
                "skills": ["Classes, Objects, Inheritance, Polymorphism", "Dunder/Magic methods (__init__, __str__, __repr__)", "File I/O (JSON, CSV, text processing)", "Exception handling (try/except/finally) & custom errors"],
                "project": "Object-Oriented Bank Account Management & Audit Logging System",
                "drill": "Create a `BankAccount` class with deposit, withdraw, and transaction history."
            },
            {
                "num": 3, "name": "Standard Library & Data Manipulation", "time": "Weeks 5–6",
                "objectives": "Work with high-performance collections, iterators, generators, and data analysis.",
                "skills": ["List & Dict Comprehensions", "Generators, Iterators, and `itertools`", "Virtual Environments (`venv`) & `pip` package manager", "Introduction to NumPy & Pandas DataFrames"],
                "project": "Automated Web Data Scraper & Tabular CSV Report Generator",
                "drill": "Extract structured articles from a public feed and clean columns using Pandas."
            },
            {
                "num": 4, "name": "APIs, Asynchronous Execution & Databases", "time": "Weeks 7–8",
                "objectives": "Build web APIs, communicate over HTTP, and connect to persistent SQL databases.",
                "skills": ["HTTP REST APIs with FastAPI or Flask", "Database integration with SQLite & SQLAlchemy ORM", "Asynchronous Python with `asyncio` & `aiohttp`", "Testing with `pytest` & type annotations (`mypy`)"],
                "project": "Full RESTful Task Management API with SQLite & JWT Authentication",
                "drill": "Implement 5 CRUD endpoints in FastAPI with input validation and pytest coverage."
            },
            {
                "num": 5, "name": "Production Deployment & Cloud Mastery", "time": "Weeks 9–10",
                "objectives": "Deploy production-grade Python services with Docker, CI/CD, and monitoring.",
                "skills": ["Containerization with Docker & Docker Compose", "CI/CD automated testing with GitHub Actions", "Cloud deployment (AWS / Render / Heroku / GCP)", "Performance profiling & memory optimization"],
                "project": "Production-Ready Microservice with Docker, Automated CI/CD & Cloud Hosting",
                "drill": "Write a Dockerfile and deploy your FastAPI app to a cloud platform."
            }
        ]
    elif any(k in t_lower for k in ["react", "web dev", "frontend", "javascript", "full stack"]):
        domain = "Modern Web Architecture & Frontend Engineering"
        est_time = "10–12 Weeks (6–8 hrs/week)"
        prereqs = "Basic HTML/CSS & Modern JavaScript (ES6+)"
        phases = [
            {
                "num": 1, "name": "HTML5, Modern CSS & JavaScript ES6+", "time": "Weeks 1–2",
                "objectives": "Build responsive layouts and master modern JavaScript primitives.",
                "skills": ["Semantic HTML5 & Responsive Flexbox / CSS Grid", "ES6+ Destructuring, Arrow Functions, Template Literals", "DOM Manipulation, Events & LocalStorage", "Async JavaScript: Promises & Fetch API"],
                "project": "Responsive Interactive Dashboard with Local Storage & Dark Mode",
                "drill": "Build a responsive grid layout that adapts cleanly from mobile to 4K desktop."
            },
            {
                "num": 2, "name": "React Core & Component Architecture", "time": "Weeks 3–4",
                "objectives": "Understand declarative UI, component lifecycles, and state reactivity.",
                "skills": ["JSX Syntax & Functional Components", "Core Hooks (`useState`, `useEffect`, `useRef`)", "Props, Children & Component Composition", "Forms, Controlled Inputs & Event Handling"],
                "project": "Interactive Kanban Project Board with Drag & Drop Filtering",
                "drill": "Build a multi-step form with live validation using controlled React state."
            },
            {
                "num": 3, "name": "State Management & Client-Side Routing", "time": "Weeks 5–6",
                "objectives": "Manage complex global state and multiple page routes.",
                "skills": ["React Router v6 Navigation & URL Parameters", "Context API & Custom React Hooks", "Zustand or Redux Toolkit Global State", "API fetching with TanStack React Query"],
                "project": "Full-Featured E-Commerce Product Catalog with Cart & Checkout",
                "drill": "Create a custom hook `useLocalStorageState` for seamless state synchronization."
            },
            {
                "num": 4, "name": "Backend Integration & Full-Stack APIs", "time": "Weeks 7–8",
                "objectives": "Connect frontend applications to RESTful and GraphQL backend services.",
                "skills": ["Node.js / Express or Next.js App Router API Routes", "JWT Authentication & Protected Route Guards", "PostgreSQL / MongoDB Database Integration", "Tailwind CSS & Framer Motion UI Polish"],
                "project": "Full-Stack Collaborative Learning Hub with Secure Authentication",
                "drill": "Implement JWT token exchange with refresh rotation and route guards."
            },
            {
                "num": 5, "name": "Performance, Testing & Production Deployment", "time": "Weeks 9–10",
                "objectives": "Optimize Web Vitals, write automated test suites, and deploy to the cloud.",
                "skills": ["Component Testing with Vitest & React Testing Library", "Lighthouse Performance & Core Web Vitals (LCP, FID, CLS)", "Vercel / Netlify Edge Deployment & Custom Domains", "CI/CD Automation & Sentry Error Monitoring"],
                "project": "High-Performance Production Web Application with 100% Lighthouse Score",
                "drill": "Profile and reduce bundle size using dynamic code splitting and lazy loading."
            }
        ]
    elif any(k in t_lower for k in ["machine learning", "ai", "deep learning", "data science"]):
        domain = "Artificial Intelligence & Data Science"
        est_time = "12–14 Weeks (8–10 hrs/week)"
        prereqs = "Python Programming & College Algebra"
        phases = [
            {
                "num": 1, "name": "Math Foundations & Data Analysis", "time": "Weeks 1–3",
                "objectives": "Master linear algebra, calculus, and tabular data manipulation.",
                "skills": ["Linear Algebra: Vectors, Matrices, Dot Products, Eigenvalues", "Multivariable Calculus: Gradients & Partial Derivatives", "NumPy Vectorized Operations & Matrix Math", "Pandas Exploratory Data Analysis & Matplotlib Visualization"],
                "project": "Exploratory Data Analysis (EDA) of Global Housing Price Dataset",
                "drill": "Compute feature correlation matrices and visualize distributions with Seaborn."
            },
            {
                "num": 2, "name": "Classical Supervised & Unsupervised ML", "time": "Weeks 4–6",
                "objectives": "Train and evaluate scikit-learn models for prediction and clustering.",
                "skills": ["Linear & Logistic Regression, Cost Functions", "Decision Trees, Random Forests, Gradient Boosting (XGBoost)", "K-Means Clustering & Principal Component Analysis (PCA)", "Model Evaluation: Accuracy, Precision, Recall, F1, ROC-AUC"],
                "project": "Customer Churn Prediction Engine with Feature Importance Breakdown",
                "drill": "Train an XGBoost classifier with 5-fold cross-validation and hyperparameter tuning."
            },
            {
                "num": 3, "name": "Deep Learning & Neural Networks", "time": "Weeks 7–9",
                "objectives": "Build neural network architectures using PyTorch.",
                "skills": ["Multi-Layer Perceptrons (MLPs) & Backpropagation", "Activation Functions (ReLU, Softmax, Sigmoid)", "PyTorch Tensors, Autograd & Custom Dataset Loaders", "Convolutional Neural Networks (CNNs) for Computer Vision"],
                "project": "Medical Image Classification System with Custom PyTorch CNN",
                "drill": "Construct a PyTorch training loop with Adam optimizer and validation metrics."
            },
            {
                "num": 4, "name": "Transformers, LLMs & Generative AI", "time": "Weeks 10–12",
                "objectives": "Master modern foundation models, attention mechanisms, and RAG architectures.",
                "skills": ["Scaled Dot-Product Attention & Transformer Encoder/Decoder", "Hugging Face Transformers & Pretrained Model Pipelines", "Retrieval-Augmented Generation (RAG) with Vector Databases (Chroma/FAISS)", "Prompt Engineering, Embedding Search & Fine-Tuning"],
                "project": "Enterprise Document QA Copilot with Vector Search & LLM Grounding",
                "drill": "Build a RAG pipeline that embeds PDF documents and answers domain queries."
            },
            {
                "num": 5, "name": "MLOps, Model Deployment & Production Scale", "time": "Weeks 13–14",
                "objectives": "Serve models over low-latency APIs with monitoring and containerization.",
                "skills": ["FastAPI Model Serving & ONNX Runtime Optimization", "Docker Containerization of ML Workflows", "Model Registry & Experiment Tracking (MLflow / Weights & Biases)", "Cloud Deployment to AWS SageMaker / GCP Vertex AI"],
                "project": "Production AI Microservice with Real-Time Inference & Latency Telemetry",
                "drill": "Containerize a PyTorch inference pipeline and benchmark throughput under load."
            }
        ]
    elif any(k in t_lower for k in ["cloud", "devops", "kubernetes", "docker", "aws"]):
        domain = "Cloud Infrastructure & DevOps Engineering"
        est_time = "10–12 Weeks (6–8 hrs/week)"
        prereqs = "Basic Linux CLI & Networking Fundamentals"
        phases = [
            {
                "num": 1, "name": "Linux Systems & Networking Essentials", "time": "Weeks 1–2",
                "objectives": "Master Linux system administration, shell scripting, and TCP/IP networking.",
                "skills": ["Linux File Permissions, Process Management (`ps`, `top`, `systemd`)", "Bash Shell Scripting & Automation", "TCP/IP, DNS, Subnets, Routing, CIDR blocks", "SSH Keys, Firewall rules (`ufw`, `iptables`), and TLS/SSL certificates"],
                "project": "Automated Linux Server Provisioning & Hardening Bash Script",
                "drill": "Configure an automated cron job that monitors disk/memory and alerts on thresholds."
            },
            {
                "num": 2, "name": "Containerization with Docker", "time": "Weeks 3–4",
                "objectives": "Package, isolate, and run multi-container microservice stacks.",
                "skills": ["Docker Architecture: Images, Containers, Registries", "Writing Optimized Multi-Stage Dockerfiles", "Docker Volumes, Port Mapping & Network Bridges", "Multi-Service Orchestration with Docker Compose"],
                "project": "Production Multi-Container Stack (Web UI + Node/Python API + Redis + Postgres)",
                "drill": "Optimize a Dockerfile down to an Alpine base image under 50MB."
            },
            {
                "num": 3, "name": "Core Cloud Architecture (AWS / GCP / Azure)", "time": "Weeks 5–6",
                "objectives": "Design fault-tolerant, scalable cloud networks and virtual servers.",
                "skills": ["Compute: EC2, Auto-Scaling Groups, Elastic Load Balancing", "Storage: S3 Buckets, IAM Policies, Principle of Least Privilege", "Networking: Virtual Private Clouds (VPC), Public/Private Subnets, NAT Gateways", "Serverless: AWS Lambda, API Gateway, CloudWatch Monitoring"],
                "project": "Highly Available 3-Tier Web Application on AWS VPC with Auto-Scaling",
                "drill": "Build a secure VPC with public/private subnets and route tables."
            },
            {
                "num": 4, "name": "Kubernetes Cluster Orchestration", "time": "Weeks 7–8",
                "objectives": "Deploy, manage, and scale containerized applications across clusters.",
                "skills": ["Kubernetes Architecture: Control Plane, Nodes, Kubelet", "Workloads: Pods, Deployments, StatefulSets, DaemonSets", "Services (ClusterIP, NodePort, LoadBalancer) & Ingress Controllers", "ConfigMaps, Secrets, PersistentVolumeClaims, and Helm Charts"],
                "project": "Production Microservices Cluster Deployed with Helm & Ingress Routing",
                "drill": "Write a Kubernetes Deployment with rolling update strategy and readiness probes."
            },
            {
                "num": 5, "name": "Infrastructure as Code (IaC) & CI/CD Pipelines", "time": "Weeks 9–10",
                "objectives": "Automate cloud provisioning with Terraform and CI/CD pipelines.",
                "skills": ["Terraform State, Providers, Modules & Resource Provisioning", "GitHub Actions CI/CD Automated Build, Test & Deploy Pipelines", "GitOps Workflows with ArgoCD / Flux", "Observability: Prometheus Metrics, Grafana Dashboards, OpenTelemetry"],
                "project": "Full GitOps Pipeline: Terraform IaC + GitHub Actions + Kubernetes Production",
                "drill": "Provision an S3 bucket and EC2 instance entirely via declarative Terraform HCL."
            }
        ]
    else:
        # Universal Dynamic Curriculum Generator
        domain = f"{title} Core Disciplines"
        est_time = "8–10 Weeks (5–7 hrs/week)"
        prereqs = "Fundamental Interest & Curiosity"
        phases = [
            {
                "num": 1, "name": f"{title} Foundations & Core Principles", "time": "Weeks 1–2",
                "objectives": f"Establish the mental model, baseline concepts, terminology, and primitives of {title}.",
                "skills": [f"Core Terminology & Historical Context of {title}", "Fundamental Principles & Governing Rules", "Tooling, Environment Setup & First Working Examples", "Essential Best Practices & Early Pitfalls to Avoid"],
                "project": f"Starter Milestone Project: Comprehensive Hands-On Exploration of {title}",
                "drill": f"Set up your workspace and construct a baseline implementation of {title} primitives."
            },
            {
                "num": 2, "name": f"Core Mechanics & Working Architecture", "time": "Weeks 3–4",
                "objectives": f"Deep dive into the underlying engine and operational mechanics of {title}.",
                "skills": [f"Deconstruct Primary Components of {title}", "Component Interactions, State Flow & Data Lifecycles", "Structuring Scalable Configurations & Workflows", "Diagnostic Debugging & Error Handling"],
                "project": f"Intermediate Application: Modular Implementation Harness for {title}",
                "drill": f"Build a modular prototype that isolates the core mechanism of {title}."
            },
            {
                "num": 3, "name": f"Applied Systems & Real-World Patterns", "time": "Weeks 5–6",
                "objectives": f"Apply {title} to industry scenarios, integration workflows, and complex challenges.",
                "skills": [f"Integration with External Services & Data Pipelines", "Industry Standards & Battle-Tested Architecture Patterns", "Handling Edge Cases, High Throughput & Stress Scenarios", "Automated Validation & Unit Testing"],
                "project": f"Integrated System: Enterprise Solution Leveraging {title}",
                "drill": f"Test edge-case boundaries and evaluate system throughput under heavy constraints."
            },
            {
                "num": 4, "name": f"Optimization, Security & Advanced Standards", "time": "Weeks 7–8",
                "objectives": f"Fine-tune performance, security posture, and production resilience.",
                "skills": [f"Latency & Memory Optimization in {title}", "Security Hardening, Access Controls & Audit Trails", "Refactoring Anti-Patterns into Clean Production Code", "Monitoring, Metrics Collection & Telemetry"],
                "project": f"Hardened Production Module with Comprehensive Benchmark Profiling",
                "drill": f"Profile execution bottlenecks and refactor for maximum efficiency."
            },
            {
                "num": 5, "name": f"Production Capstone & Portfolio Mastery", "time": "Weeks 9–10",
                "objectives": f"Deliver a flagship production-grade project proving end-to-end mastery of {title}.",
                "skills": [f"End-to-End Architecture Blueprinting", "Deployment, Maintenance & Production Documentation", "Code Review Standards & Open Source Contribution", "Continuous Learning & Advanced Specialization Tracks"],
                "project": f"Flagship Capstone: Full End-to-End Portfolio System Showcasing {title} Mastery",
                "drill": f"Publish your completed repository with comprehensive architecture documentation."
            }
        ]

    # Build Output
    out = []
    out.append(f"✦ Master Learning Path: {title} — From Zero to Mastery 🚀\n")
    out.append(f"- 🎓 Domain: {domain}")
    out.append(f"- ⏱️ Estimated Timeline: {est_time}")
    out.append(f"- 📋 Prerequisites: {prereqs}")
    out.append("\n---\n")

    out.append("📊 Master Roadmap Summary Table:")
    out.append("| Step # | Phase Name | Estimated Time | Core Skills & Topics | Hands-On Milestone Project |")
    out.append("| :--- | :--- | :--- | :--- | :--- |")
    for p in phases:
        skill_sample = ", ".join(p["skills"][:2])
        out.append(f"| Step {p['num']} | {p['name']} | {p['time']} | {skill_sample} | {p['project']} |")
    out.append("\n---\n")

    out.append("◈ Step-by-Step Learning Progression:\n")
    for p in phases:
        out.append(f"✦ Step {p['num']}: Phase {p['num']} — {p['name']} ({p['time']})")
        out.append(f"• 🎯 Learning Objective: {p['objectives']}")
        out.append("• 📚 Core Concepts to Master:")
        for s in p["skills"]:
            out.append(f"  ❯ {s}")
        out.append(f"• 🏆 Milestone Hands-On Project: {p['project']}")
        out.append(f"• 🛠️ Immediate Practice Drill: {p['drill']}\n")

    out.append("---\n")
    out.append("💡 Immediate Action Step:")
    out.append(f"Ready to begin Step 1 of {title}? Reply with 'Start Phase 1' or ask any introductory question to begin mastering Phase 1 today!")

    return "\n".join(out)
