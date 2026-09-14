import os
import json
import re
import urllib.request
import urllib.error
import base64
from abc import ABC, abstractmethod


class LLMAdapter(ABC):
    """Base class for LLM adapters."""
    
    @abstractmethod
    def generate(self, system_prompt, user_message, history=None, image_data=None, audio_data=None):
        """Generate a response. Accepts optional image_data and audio_data (base64 or data URL)."""
        pass
    
    def is_available(self):
        return True


class BynaraClaudeAdapter(LLMAdapter):
    """Bynara Claude Router Adapter (supporting text, voice transcription context, and multimodal vision)."""
    
    def __init__(self, api_key, backup_key=None, base_url="https://router.bynara.id/v1", model_name="claude-opus-4.8-bynara"):
        self.api_key = api_key
        self.backup_key = backup_key
        self.base_url = base_url.rstrip("/")
        self.model_name = model_name or "claude-opus-4.8-bynara"
        self.keys = [k for k in [
            api_key,
            backup_key,
            os.getenv("ANTHROPIC_AUTH_TOKEN"),
            os.getenv("BYNARA_API_KEY"),
            os.getenv("BYNARA_BACKUP_KEY")
        ] if k and isinstance(k, str) and k.strip()]
    
    def is_available(self):
        return len(self.keys) > 0
    
    def _call_anthropic(self, key, payload):
        endpoint = f"{self.base_url}/messages"
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "x-api-key": key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            content = res_data.get("content", [])
            if content and isinstance(content, list):
                return content[0].get("text", "").strip()
        return None

    def _call_openai(self, key, payload):
        endpoint = f"{self.base_url}/chat/completions"
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            choices = res_data.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "").strip()
        return None
    
    def generate(self, system_prompt, user_message, history=None, image_data=None, audio_data=None):
        if not self.keys:
            raise RuntimeError("Bynara API key not configured")
        
        # Build Anthropic Messages payload
        messages = []
        if history:
            for h in history:
                role = "user" if h.get("role") == "user" else "assistant"
                messages.append({"role": role, "content": h.get("message", "")})
        
        # User message parts
        if image_data:
            clean_b64 = image_data
            media_type = "image/jpeg"
            if "data:" in image_data and ";base64," in image_data:
                header, clean_b64 = image_data.split(";base64,")
                media_type = header.replace("data:", "")
            
            user_content = [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": clean_b64
                    }
                },
                {"type": "text", "text": user_message or "Analyze this image and explain in detail using rich emojis."}
            ]
        else:
            prompt_text = user_message or "Explain this concept in detail using rich emojis."
            if audio_data:
                prompt_text = f"🎤 [Voice Input Context]: {prompt_text}"
            user_content = prompt_text
            
        messages.append({"role": "user", "content": user_content})
        
        # Try keys across Anthropic & OpenAI wire endpoints
        last_error = None
        for key in self.keys:
            # 1. Anthropic wire format
            anthropic_payload = {
                "model": self.model_name,
                "system": system_prompt,
                "messages": messages,
                "max_tokens": 4096,
                "temperature": 0.7
            }
            try:
                reply = self._call_anthropic(key, anthropic_payload)
                if reply:
                    return self._enrich_symbols(reply)
            except Exception as e:
                last_error = e

            # 2. OpenAI wire format fallback
            openai_messages = [{"role": "system", "content": system_prompt}]
            for m in messages:
                openai_messages.append({"role": m["role"], "content": m["content"] if isinstance(m["content"], str) else user_message})
            openai_payload = {
                "model": self.model_name,
                "messages": openai_messages,
                "max_tokens": 4096,
                "temperature": 0.7
            }
            try:
                reply = self._call_openai(key, openai_payload)
                if reply:
                    return self._enrich_symbols(reply)
            except Exception as e:
                last_error = e

        if last_error:
            raise last_error
        return "✦ I am ready to help you learn."

    def _enrich_symbols(self, text):
        """Ensure rich emoji symbols are present and remove all ** raw markdown markers."""
        if not text:
            return ""
        replacements = [
            (r'\*\*Sunlight:\*\*', '☀️ Sunlight:'),
            (r'\*\*Water:\*\*', '💧 Water (H₂O):'),
            (r'\*\*Carbon Dioxide:\*\*', '🍃 Carbon Dioxide (CO₂):'),
            (r'\*\*Chlorophyll:\*\*', '🌿 Chlorophyll:'),
            (r'\*\*Glucose:\*\*', '🍎 Glucose (Sugar):'),
            (r'\*\*Oxygen:\*\*', '💨 Oxygen (O₂):'),
            (r'\*\*Formula:\*\*', '🧪 Formula:'),
            (r'\*\*Overview:\*\*', '✦ Overview:'),
            (r'\*\*Key Points:\*\*', '◈ Key Takeaways:'),
            (r'\*\*Practice:\*\*', '🧠 Practice Challenge:'),
            (r'\*\*Next Steps:\*\*', '🎯 Next Steps:'),
            (r'\*\*([^*]+)\*\*', r'\1'),
        ]
        out = text
        for pattern, repl in replacements:
            out = re.sub(pattern, repl, out, flags=re.I)
        return out.replace('**', '')


class GeminiAdapter(LLMAdapter):
    """Google Gemini adapter with native multimodal Vision, Voice, and advanced reasoning."""
    
    MODELS = [
        "gemini-3.5-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.6-flash",
        "gemini-flash-latest",
        "gemini-flash-lite-latest",
        "gemini-pro-latest"
    ]
    
    def __init__(self, api_key=None, preferred_model="gemini-3.6-flash", fallback_adapter=None):
        self.preferred_model = preferred_model or "gemini-3.6-flash"
        self.fallback_adapter = fallback_adapter
        import os
        keys_pool = [
            api_key,
            os.getenv('GEMINI_API_KEY'),
            os.getenv('GEMINI_BACKUP_KEY')
        ]
        self.keys = []
        for k in keys_pool:
            if k and isinstance(k, str):
                k = k.strip()
                if k and not k.startswith("your_") and k not in self.keys:
                    self.keys.append(k)
        self.api_key = self.keys[0] if self.keys else ""
    
    def is_available(self):
        return len(self.keys) > 0
    
    def _call_model(self, model_name, payload, key):
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={key}"
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "X-goog-api-key": key
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            candidates = res_data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return parts[0].get("text", "").strip()
        return None
    
    def generate(self, system_prompt, user_message, history=None, image_data=None, audio_data=None):
        if not self.api_key:
            if self.fallback_adapter and self.fallback_adapter.is_available():
                return self.fallback_adapter.generate(system_prompt, user_message, history, image_data, audio_data)
            return None
        
        if any(g in system_prompt for g in [
            "LEARN MODE GUIDELINES",
            "QUIZ MODE GUIDELINES",
            "STEP-BY-STEP MATHEMATICAL SOLVER GUIDELINES",
            "STEP-BY-STEP LEARNING PATH & ROADMAP GUIDELINES",
            "ACTIVE RECALL FLASHCARDS & REVISION GUIDELINES",
            "CODE DEBUGGING, EXPLANATION & SOFTWARE FIXING GUIDELINES",
            "STUDY NOTES & COMPLETE PDF STUDY MODE GUIDELINES"
        ]):
            sys_inst = system_prompt
        else:
            sys_inst = (
                f"{system_prompt}\n\n"
                "Respond as Sastra AI, an intelligent, empathetic, and highly capable learning companion for Capacity Connect. "
                "Explain concepts simply, clearly, and fluently — just like ChatGPT and Google Gemini. "
                "When explaining concepts like Deep Learning or Artificial Intelligence, provide natural, intuitive, and flowing explanations with relatable real-world analogies, concise practical code when helpful, and zero fluff. "
                "If an image is provided, examine it thoroughly, identify all shapes, diagrams, text, code snippets, questions, or formulas, and explain them accurately and in detail. "
                "NEVER output raw markdown double asterisks (**); instead use clean formatting with elegant bullet points and symbols (✦, ◈, ❯, ❖, 📌, ⚠️, 🎯, 💡)."
            )

        candidate_models = [self.preferred_model] + [m for m in self.MODELS if m != self.preferred_model]
        
        # 1. Primary path: Use Google Generative AI official Python SDK
        for key in self.keys:
            try:
                import google.generativeai as genai
                genai.configure(api_key=key, transport="rest")

                parts = []
                if image_data:
                    import base64
                    import io
                    from PIL import Image
                    clean_b64 = image_data
                    mime_type = "image/jpeg"
                    if "data:" in image_data and ";base64," in image_data:
                        header, clean_b64 = image_data.split(";base64,")
                        mime_type = header.replace("data:", "")
                    img_bytes = base64.b64decode(clean_b64)
                    try:
                        pil_img = Image.open(io.BytesIO(img_bytes))
                        parts.append(pil_img)
                    except Exception:
                        parts.append({"mime_type": mime_type, "data": img_bytes})

                prompt_text = user_message or "Analyze this image in detail and explain all concepts thoroughly."
                if audio_data:
                    prompt_text = f"🎤 [Voice Note]: {prompt_text}"
                parts.append(prompt_text)

                for model_name in candidate_models:
                    try:
                        model = genai.GenerativeModel(
                            model_name=model_name,
                            system_instruction=sys_inst
                        )
                        if history and not image_data:
                            chat_history = []
                            for h in (history or [])[-6:]:
                                role = "user" if h.get("role") == "user" else "model"
                                chat_history.append({"role": role, "parts": [h.get("message", "")]})
                            try:
                                chat = model.start_chat(history=chat_history)
                                resp = chat.send_message(prompt_text)
                                if resp and resp.text:
                                    return self._enrich_symbols(resp.text.strip())
                            except Exception:
                                pass

                        resp = model.generate_content(parts)
                        if resp and resp.text:
                            return self._enrich_symbols(resp.text.strip())
                    except Exception as model_err:
                        continue
            except Exception as key_err:
                continue

        # 2. REST Fallback
        for key in self.keys:
            for model_name in candidate_models[:2]:
                try:
                    payload = {
                        "system_instruction": {"parts": [{"text": sys_inst}]},
                        "contents": [{"role": "user", "parts": [{"text": user_message or "Explain this topic."}]}],
                        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 4096}
                    }
                    reply = self._call_model(model_name, payload, key)
                    if reply:
                        return self._enrich_symbols(reply)
                except Exception:
                    continue

        if self.fallback_adapter and self.fallback_adapter.is_available():
            try:
                fb_reply = self.fallback_adapter.generate(system_prompt, user_message, history, image_data, audio_data)
                if fb_reply:
                    return fb_reply
            except Exception:
                pass

        return None

    def _enrich_symbols(self, text):
        """Ensure rich emoji symbols are present and clean up raw markdown asterisks."""
        if not text:
            return ""
        # Remove bold markers like **text** -> text
        out = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        return out.replace('**', '')


class RuleBasedAdapter(LLMAdapter):
    """Fallback adapter using deterministic rules with rich symbols."""
    
    def generate(self, system_prompt, user_message, history=None, image_data=None, audio_data=None):
        raise NotImplementedError("Use astra_engine.process_message() directly")


# ─── Factory ───
_adapter_instance = None

def get_adapter():
    """Get configured LLM adapter with cascading vision, voice, and text fallback."""
    global _adapter_instance
    if _adapter_instance is not None:
        return _adapter_instance
    
    try:
        from config import (
            LLM_PROVIDER, GEMINI_API_KEY, GEMINI_MODEL,
            BYNARA_API_KEY, BYNARA_BACKUP_KEY, BYNARA_BASE_URL, BYNARA_MODEL
        )
    except ImportError:
        LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'gemini')
        GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
        GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
        BYNARA_API_KEY = os.getenv('ANTHROPIC_AUTH_TOKEN', os.getenv('BYNARA_API_KEY', ''))
        BYNARA_BACKUP_KEY = os.getenv('BYNARA_BACKUP_KEY', '')
        BYNARA_BASE_URL = os.getenv('ANTHROPIC_BASE_URL', 'https://router.bynara.id/v1')
        BYNARA_MODEL = os.getenv('ANTHROPIC_DEFAULT_OPUS_MODEL', 'claude-opus-4.8-bynara')
    
    bynara_adapter = None
    if BYNARA_API_KEY or BYNARA_BACKUP_KEY:
        bynara_adapter = BynaraClaudeAdapter(
            api_key=BYNARA_API_KEY,
            backup_key=BYNARA_BACKUP_KEY,
            base_url=BYNARA_BASE_URL,
            model_name=BYNARA_MODEL
        )
    
    # Primary: Google Gemini with native Multimodal Vision & ChatGPT/Gemini conversational intelligence
    if GEMINI_API_KEY or LLM_PROVIDER == 'gemini':
        adapter = GeminiAdapter(GEMINI_API_KEY, GEMINI_MODEL, fallback_adapter=bynara_adapter)
        if adapter.is_available():
            _adapter_instance = adapter
            print(f"[Astra] Connected to Google Gemini API ({GEMINI_MODEL}) with native Multimodal Vision")
            return _adapter_instance
    
    if bynara_adapter and bynara_adapter.is_available():
        _adapter_instance = bynara_adapter
        print(f"[Astra] Using Bynara Router ({BYNARA_MODEL})")
        return _adapter_instance
    
    _adapter_instance = RuleBasedAdapter()
    print(f"[Astra] Using rule-based engine")
    return _adapter_instance
