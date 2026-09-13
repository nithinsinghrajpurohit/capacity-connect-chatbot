# ✦ Sastra AI — Digital Capacity Building Operating System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask 3.1](https://img.shields.io/badge/flask-3.1.1-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Sastra AI (Capacity Connect)** is a state-of-the-art multimodal AI learning companion and course-aware assistant engineered for LMS integration. It combines deep pedagogical reasoning, multimodal vision, interactive quizzes, dynamic concept diagrams, automated study notes, and A4 PDF study guide generation.

---

## 🚀 Key Capabilities

- 🧠 **Concise Learn & Deep Mastery Modes**:
  - **Learn Mode**: Delivers punchy, crystal-clear explanations (definition + intuitive analogy + code example) tailored for fast grasp.
  - **Deep Mode**: Comprehensive, academic deep dives (intuition, architecture, deep technical mechanics, best practices, edge cases).
- 🎨 **Visual Concept & Vector Diagrams**: Generates dynamic educational SVG diagrams directly in chat (architecture flowcharts, memory models, data structures).
- 👁️ **Multimodal Vision & Document Analysis**: Upload screenshots, handwritten diagrams, code snippets, or PDF/DOCX course documents for instant structured breakdown.
- 🧪 **Interactive Adaptive Quizzes**: Course-tailored quizzes with instant evaluation and natural option disambiguation (e.g. Option A/B/C/D).
- 📄 **Instant Study Notes & PDF Generator**: Clean, branded A4 study guide export with zero third-party branding.
- 🗄️ **Zero-Friction Local Database**: Automatic SQLite schema creation and demo seed on startup.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask, Gunicorn, SQLite, ReportLab
- **AI Models**: Google Gemini 2.5 Flash / 1.5 Flash, OpenAI GPT-4o, Ollama, with rule-based fallback
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons, Vite
- **Deployment**: Docker, Render, Railway, Vercel

---

## ⚡ Quick Start (Local Setup)

### 1. Clone & Set Up Backend

```bash
# Clone the repository
git clone https://github.com/nithinsinghrajpurohit/capacity-connect-chatbot.git
cd capacity-connect-chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the sample environment file:
```bash
cp .env.example .env
```
Edit `.env` to configure your API keys:
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
PORT=5000
```
*(Get a free key at [Google AI Studio](https://aistudio.google.com/apikey). If left unset, Astra seamlessly falls back to its offline rule-based knowledge engine.)*

### 3. Run the Server

```bash
python app.py
```
Open **http://localhost:5000** in your browser to interact with the full Sastra AI interface!

---

## 🌐 Deployment Guide

### Recommended Stack: Backend on Render + Frontend on Vercel

---

### Step 1: Deploy Backend to Render

1. Go to **[render.com](https://render.com/)** and log in with GitHub.
2. Click **New +** → **Web Service**.
3. Connect your repository: `https://github.com/nithinsinghrajpurohit/capacity-connect-chatbot`.
4. Configure the settings:
   - **Name**: `capacity-connect-backend` (or `capacity-connect-chatbot`)
   - **Language / Runtime**: `Python 3`
   - **Region**: Choose closest to you (e.g. *Singapore / Frankfurt / Oregon*)
   - **Branch**: `main`
   - **Root Directory**: *(leave blank)*
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Under **Environment Variables**, add:
   - `GEMINI_API_KEY` = `your_gemini_api_key` *(from [Google AI Studio](https://aistudio.google.com/apikey))*
   - `LLM_PROVIDER` = `gemini`
   - `JWT_SECRET` = `your_random_secret_string`
   - `FLASK_DEBUG` = `false`
6. Click **Create Web Service**.
7. Once deployed, copy your Render URL (e.g., `https://capacity-connect-backend.onrender.com`).

---

### Step 2: Deploy Frontend to Vercel

1. Go to **[vercel.com](https://vercel.com/)** and sign in with GitHub.
2. Click **Add New…** → **Project**.
3. Select `capacity-connect-chatbot` from your repositories.
4. In the configuration screen:
   - **Framework Preset**: `Vite`
   - **Root Directory**: Click *Edit* and select **`frontend`**
   - **Build Command**: `npm run build` *(default)*
   - **Output Directory**: `dist` *(default)*
5. Open **Environment Variables** and add:
   - **Key**: `VITE_API_BASE_URL`
   - **Value**: `https://capacity-connect-backend.onrender.com` *(paste your Render backend URL from Step 1, without trailing slash)*
6. Click **Deploy**.
7. Vercel will build and launch your high-performance frontend with global CDN edge caching!

---

### Option 2: Deploy to Railway

1. Go to [railway.app](https://railway.app) and sign in.
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select `nithinsinghrajpurohit/capacity-connect-chatbot`.
4. Railway will automatically detect the `Procfile` and `requirements.txt`.
5. Go to **Variables** and add:
   - `GEMINI_API_KEY` = `your_gemini_api_key`
   - `LLM_PROVIDER` = `gemini`
6. Click **Deploy**. Railway will assign a public domain under Settings → Networking.

---

### Option 3: Deploy with Docker

A production-ready `Dockerfile` is included:

```bash
# Build the Docker image
docker build -t sastra-ai-chatbot .

# Run the container
docker run -d -p 5000:5000 \
  -e GEMINI_API_KEY="your_api_key_here" \
  -e LLM_PROVIDER="gemini" \
  --name sastra-ai \
  sastra-ai-chatbot
```

Access the app at **http://localhost:5000**.

---

## 📂 Project Architecture

```
capacity-connect-chatbot/
├── app.py                     # Primary Flask REST API & SPA static router
├── astra_engine.py            # Offline rule-based NLP engine & fallback knowledge base
├── astra_full.py              # Multimodal AI engine (11 learning modes, quiz engine, RAG)
├── astra_system_prompt.py     # Adaptive context & pedagogical prompt engineer
├── llm_adapter.py             # Unified connector for Gemini, OpenAI, and Ollama
├── image_generator.py         # Dynamic visual SVG diagram generator
├── pdf_generator.py           # ReportLab A4 study guide generator
├── document_analyzer.py       # PDF / Word / Text document extractor
├── database.py                # SQLite schema management & demo data seeds
├── config.py                  # Environment config loader
├── requirements.txt           # Python production dependencies
├── Procfile                   # Process file for Render / Railway / Heroku
├── Dockerfile                 # Production container definition
├── dist/                      # Production-ready React SPA bundle
├── frontend/                  # React + TypeScript + Tailwind source code
└── static/                    # PDFs and downloadable resources
```

---

## 🔑 Demo Credentials

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| Trainer | `trainer_priya` | `trainer123` |
| Trainee | `sneha` | `trainee123` |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
