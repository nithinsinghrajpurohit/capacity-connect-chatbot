import os
from dotenv import load_dotenv

load_dotenv()

# Primary LLM Configuration (Google Gemini)
LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'gemini')  # 'gemini', 'bynara', 'openai', 'ollama', 'rule_based'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_BACKUP_KEY = os.getenv('GEMINI_BACKUP_KEY', '')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-3.5-flash')

# Bynara Claude Vision & Text Router Configuration
BYNARA_BASE_URL = os.getenv('ANTHROPIC_BASE_URL', 'https://router.bynara.id/v1').rstrip('/')
BYNARA_API_KEY = os.getenv('ANTHROPIC_AUTH_TOKEN', os.getenv('BYNARA_API_KEY', ''))
BYNARA_BACKUP_KEY = os.getenv('BYNARA_BACKUP_KEY', '')
BYNARA_MODEL = os.getenv('ANTHROPIC_DEFAULT_OPUS_MODEL', 'claude-opus-4.8-bynara')
BYNARA_PDF_KEY = os.getenv('BYNARA_PDF_KEY', '')

# General Fallback
FALLBACK_API_KEY = BYNARA_API_KEY
FALLBACK_MODEL = BYNARA_MODEL
FALLBACK_API_BASE = BYNARA_BASE_URL

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3')

# JWT Configuration
JWT_SECRET = os.getenv('JWT_SECRET', 'capacity-connect-dev-secret-change-in-production')
JWT_EXPIRY_HOURS = int(os.getenv('JWT_EXPIRY_HOURS', '24'))

# App Configuration
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
PORT = int(os.getenv('PORT', '5000'))
