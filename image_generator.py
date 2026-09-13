"""Vector SVG and Multi-Provider Visual Generation Engine for Astra.
Supports:
1. High-Definition Vector SVG Visuals (Concept cards with structured tables, neat explanations, roadmaps & blueprints)
2. Hugging Face Inference (FLUX.1-schnell / SDXL)
3. Stability AI (v2beta Core / SDXL v1)
4. OpenAI DALL-E 3
5. Together AI FLUX.1
6. Bynara Image API
"""

import os
import json
import urllib.request
import urllib.error
import urllib.parse
import base64
import re
import random
from config import BYNARA_API_KEY, BYNARA_BACKUP_KEY


class ImageGenerator:
    """Multi-provider image generation and diagram synthesis engine."""
    
    API_GENERATIONS = os.getenv("IMAGE_API_GENERATIONS", "https://api-images.bynara.id/v1/images/generations")
    API_EDITS = os.getenv("IMAGE_API_EDITS", "https://api-images.bynara.id/v1/images/edits")
    
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.together_key = os.getenv("TOGETHER_API_KEY", "").strip()
        self.hf_token = os.getenv("HUGGINGFACE_API_KEY", os.getenv("HF_TOKEN", "")).strip()
        self.stability_key = os.getenv("STABILITY_API_KEY", "").strip()
        self.bynara_key = os.getenv("BYNARA_API_KEY", "").strip()
        self.image_api_key = os.getenv("IMAGE_API_KEY", "").strip()
        self.keys = [k for k in [self.image_api_key, self.bynara_key, self.openai_key, self.hf_token] if k]

    def is_educational_diagram_request(self, prompt):
        """Check if user is asking for an educational roadmap, blueprint, scientific or computer science diagram."""
        p_lower = prompt.lower()
        diagram_cues = (
            "roadmap", "road map", "curriculum", "syllabus", "learning path", "study path",
            "cloud computing", "cloud", "devops", "aws", "kubernetes", "terraform",
            "python", "web development", "full stack", "fullstack", "frontend", "backend",
            "machine learning", "deep learning", "data science", "cybersecurity",
            "brain", "heart", "photosynthesis", "solar system",
            "flowchart", "flow chart", "architecture diagram", "uml", "wireframe",
            "memory model", "call stack", "loop lifecycle", "data structure diagram",
            "concept diagram", "concept architecture", "stack vs heap", "state diagram",
            "diagram", "labeled", "labels", "draw diagram", "show diagram",
            "subject", "subjects"
        )
        return any(cue in p_lower for cue in diagram_cues)

    def _build_enhanced_prompt(self, prompt, is_educational=False):
        """Build a richly detailed prompt optimized for AI image generation.
        
        ALWAYS incorporates the user's original prompt text so that different
        requests produce visually different images, even on the same topic.
        """
        clean = prompt.strip()
        p_lower = clean.lower()
        
        # Strip common instruction words to get the core concept
        core_topic = re.sub(r'\b(create|generate|draw|show|make|render|image|diagram|visual|illustration|picture|photo|of|for|about|a|an|the|ai|study|educational)\b', '', clean, flags=re.I).strip()
        if len(core_topic) < 3:
            core_topic = clean
        
        if is_educational:
            # Topic-specific visual STYLE hints (not full descriptions — the user's words drive the content)
            topic_style_map = {
                "python": "with Python logo colors (blue and gold), floating code snippets, data structure nodes, function graphs, in a futuristic dark blue digital workspace",
                "cloud": "with cloud server racks, glowing fiber optic cables, containerized microservices, load balancers, floating in a cosmic sky with aurora borealis",
                "devops": "with CI/CD pipeline conveyor belts, Docker containers, Kubernetes pods, monitoring dashboards, in a high-tech command center",
                "aws": "with AWS service icons (EC2, S3, Lambda), luminous data streams, auto-scaling groups, VPC networks in a digital cosmos",
                "kubernetes": "with pods, nodes, and clusters as glowing spheres in a hexagonal grid, deployment pipelines, service mesh networks",
                "machine learning": "with neural network layers, interconnected neurons, gradient descent paths, training loss curves, in a futuristic AI laboratory",
                "neural network": "with interconnected artificial neurons firing electrical impulses, multi-layer perceptron architecture, weight matrices, activation functions visualized as energy transformations",
                "deep learning": "with convolutional layers processing images, attention mechanisms, transformer blocks, backpropagation gradient flows in neon colors",
                "data science": "with holographic scatter plots, regression curves, clustering visualizations, DataFrames floating in 3D space",
                "artificial intelligence": "with a digital brain showing neural pathways, orbiting knowledge graphs, NLP embeddings, computer vision grids, robotic arms",
                "web development": "with HTML/CSS layers, JavaScript engines, React component trees, REST API connections, database schemas, responsive breakpoints",
                "frontend": "with React component hierarchy, CSS Grid layouts, DOM tree structures, responsive breakpoints between mobile and desktop",
                "backend": "with API gateways, microservices, message queues, database clusters, authentication flows, server pipelines",
                "cybersecurity": "with digital fortress, firewall shields, encrypted data streams, threat detection sensors, security operations center",
                "blockchain": "with cryptographic blocks forming a chain, distributed nodes, smart contracts, consensus mechanism animations",
                "react": "with component trees, useState/useEffect hooks as energy flows, virtual DOM diffing, component lifecycle stages",
                "java": "with JVM architecture, garbage collection zones, Spring Boot microservices, enterprise patterns",
                "javascript": "with event loop, call stack, callback queue, Web APIs as interconnected gears in steampunk-neon aesthetic",
                "database": "with relational tables, foreign key connections, SQL query plans, B-tree indexes, NoSQL document stores",
                "brain": "with labeled brain regions (cerebrum, cerebellum, brainstem, hippocampus), neural pathways, electrical impulses, synapses",
                "heart": "with four chambers, valves, aorta, pulmonary arteries, blood flow direction in red and blue",
                "photosynthesis": "with chloroplast cross-section, thylakoid membranes, light reactions, Calvin cycle, CO2 to glucose conversion",
                "solar system": "with all eight planets in orbits, asteroid belts, planetary rings, moons, deep space setting",
            }
            
            # Find matching style hints
            style_hint = ""
            for key, style in topic_style_map.items():
                if key in p_lower:
                    style_hint = style
                    break
            
            # Add randomized visual variation to prevent identical images
            variations = [
                "dramatic perspective, volumetric lighting",
                "bird's eye isometric view, glowing edges",
                "epic wide-angle composition, particle effects",
                "close-up detailed view, bokeh background",
                "split-screen cross-section, holographic overlays",
                "panoramic landscape composition, lens flare",
                "blueprint wireframe style with neon highlights",
                "floating island composition, ethereal atmosphere",
            ]
            variation = variations[random.randint(0, len(variations) - 1)]
            
            return f"A stunning, highly detailed 3D conceptual illustration of {core_topic} {style_hint}, {variation}, ultra-high detail, cinematic lighting, 8k resolution, vibrant colors, professional digital artwork"
        
        else:
            # Creative/artistic prompt enhancement
            art_enhancers = "masterpiece, cinematic lighting, 8k resolution, highly detailed, vibrant vivid colors, photorealistic digital artwork"
            return f"{clean}, {art_enhancers}"

    def generate_image(self, prompt, size="1024x1024", model="flux", force_ai=False):
        """Generate an educational concept diagram or high-definition visual illustration from prompt."""
        clean_p = prompt.strip()
        p_lower = clean_p.lower()

        # 1. Educational concept diagrams & table visuals: ALWAYS use the 100% vector SVG engine
        # This guarantees razor-sharp English text, structured comparison tables, and neat explanations!
        is_pure_art = any(k in p_lower for k in ("photorealistic", "cyberpunk neon", "3d pixar", "studio ghibli", "anime / manga", "oil painting", "wallpaper", "portrait", "scenery", "creative artwork"))
        if not is_pure_art:
            return self._generate_educational_diagram(clean_p)

        # 2. Pure creative art requests: Try authorized high-definition diffusion providers if available
        enhanced_prompt = self._build_enhanced_prompt(clean_p, is_educational=False)

        # Try Hugging Face (FLUX.1-schnell / SDXL)
        if self.hf_token:
            res = self._try_huggingface(enhanced_prompt, size)
            if res:
                return res

        # Try Stability AI Core
        if self.stability_key:
            res = self._try_stability_ai(enhanced_prompt, size)
            if res:
                return res

        # Try OpenAI DALL-E 3
        if self.openai_key:
            res = self._try_openai_dalle3(enhanced_prompt, size)
            if res:
                return res

        # Try Together AI FLUX.1
        if self.together_key:
            res = self._try_together_flux(enhanced_prompt, size)
            if res:
                return res

        # Try Bynara API
        if self.bynara_key or self.image_api_key:
            res = self._try_bynara(enhanced_prompt, size)
            if res:
                return res

        # Primary & Resilient Vector Fallback: ALWAYS synthesize crisp SVG vector image card
        return self._generate_educational_diagram(clean_p)

    def _try_huggingface(self, prompt, size="1024x1024"):
        """Generates image using Hugging Face Free Inference API with FLUX.1-schnell or SDXL."""
        models_to_try = [
            "black-forest-labs/FLUX.1-schnell",
            "stabilityai/stable-diffusion-xl-base-1.0"
        ]
        for model_id in models_to_try:
            try:
                url = f"https://router.huggingface.co/hf-inference/models/{model_id}"
                payload = {"inputs": prompt}
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={
                        "Authorization": f"Bearer {self.hf_token}",
                        "Content-Type": "application/json"
                    },
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=35) as resp:
                    content_type = resp.headers.get("Content-Type", "")
                    data = resp.read()
                    if "image" in content_type or (data and data[:4] in (b'\x89PNG', b'\xff\xd8\xff\xe0', b'\xff\xd8\xff\xe1', b'RIFF')):
                        b64 = base64.b64encode(data).decode("utf-8")
                        mime = content_type if "image" in content_type else "image/jpeg"
                        return {
                            "type": "base64",
                            "url": f"data:{mime};base64,{b64}",
                            "prompt": prompt,
                            "mode": "study_image",
                            "provider": f"huggingface_{model_id.split('/')[-1]}"
                        }
            except Exception as e:
                print(f"[ImageGen] Hugging Face {model_id} error: {e}")
        return None

    def _try_openai_dalle3(self, prompt, size="1024x1024"):
        """Generates image using OpenAI DALL·E 3 (Gold standard for prompt following & labels)."""
        try:
            url = "https://api.openai.com/v1/images/generations"
            payload = {
                "model": "dall-e-3",
                "prompt": prompt[:1000],
                "n": 1,
                "size": "1024x1024",
                "quality": "standard"
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {self.openai_key}",
                    "Content-Type": "application/json"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                items = data.get("data", [])
                if items and "url" in items[0]:
                    img_url = items[0]["url"]
                    proxy_url = f"/api/image/proxy?url={urllib.parse.quote(img_url)}"
                    return {
                        "type": "url",
                        "url": proxy_url,
                        "raw_url": img_url,
                        "prompt": prompt,
                        "mode": "study_image",
                        "provider": "openai_dalle3"
                    }
        except Exception as e:
            print(f"[ImageGen] OpenAI DALL-E 3 error: {e}")
        return None

    def _try_together_flux(self, prompt, size="1024x1024"):
        """Generates image using Together AI FLUX.1 (Top open model for photorealism & detail)."""
        try:
            url = "https://api.together.xyz/v1/images/generations"
            w, h = 1024, 1024
            payload = {
                "model": "black-forest-labs/FLUX.1-schnell",
                "prompt": prompt,
                "width": w,
                "height": h,
                "steps": 4,
                "n": 1
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {self.together_key}",
                    "Content-Type": "application/json"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                items = data.get("data", [])
                if items:
                    img_url = items[0].get("url")
                    if img_url:
                        proxy_url = f"/api/image/proxy?url={urllib.parse.quote(img_url)}"
                        return {
                            "type": "url",
                            "url": proxy_url,
                            "raw_url": img_url,
                            "prompt": prompt,
                            "mode": "study_image",
                            "provider": "together_flux"
                        }
                    elif "b64_json" in items[0]:
                        b64 = items[0]["b64_json"]
                        return {
                            "type": "base64",
                            "url": f"data:image/jpeg;base64,{b64}",
                            "prompt": prompt,
                            "mode": "study_image",
                            "provider": "together_flux"
                        }
        except Exception as e:
            print(f"[ImageGen] Together AI FLUX error: {e}")
        return None

    def _try_stability_ai(self, prompt, size="1024x1024"):
        """Generates image using Stability AI Stable Image Core (v2beta) with fallback to SDXL v1."""
        # 1. Primary: Stability AI v2beta Stable Image Core
        try:
            import requests
            url = "https://api.stability.ai/v2beta/stable-image/generate/core"
            r = requests.post(
                url,
                headers={"authorization": f"Bearer {self.stability_key}", "accept": "image/*"},
                files={"none": ""},
                data={"prompt": prompt, "output_format": "png"},
                timeout=35
            )
            if r.status_code == 200 and len(r.content) > 1000:
                b64 = base64.b64encode(r.content).decode("utf-8")
                return {
                    "type": "base64",
                    "url": f"data:image/png;base64,{b64}",
                    "prompt": prompt,
                    "mode": "creative_image",
                    "provider": "stability_ai_core"
                }
            else:
                print(f"[ImageGen] Stability v2 status {r.status_code}: {r.text[:200]}")
        except Exception as e:
            print(f"[ImageGen] Stability AI v2 error: {e}")

        # 2. Fallback: SDXL v1
        try:
            url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
            payload = {
                "text_prompts": [{"text": prompt, "weight": 1.0}],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {self.stability_key}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                artifacts = data.get("artifacts", [])
                if artifacts and "base64" in artifacts[0]:
                    b64 = artifacts[0]["base64"]
                    return {
                        "type": "base64",
                        "url": f"data:image/png;base64,{b64}",
                        "prompt": prompt,
                        "mode": "creative_image",
                        "provider": "stability_ai_sdxl"
                    }
        except Exception as e:
            print(f"[ImageGen] Stability AI v1 error: {e}")
        return None

    def _try_bynara(self, prompt, size="1024x1024"):
        """Generates image using Bynara image endpoint."""
        key = self.bynara_key or self.image_api_key
        try:
            payload = {
                "model": "flux",
                "prompt": prompt,
                "n": 1,
                "size": size
            }
            req = urllib.request.Request(
                self.API_GENERATIONS,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                items = data.get("data", [])
                if items and "url" in items[0]:
                    img_url = items[0]["url"]
                    proxy_url = f"/api/image/proxy?url={urllib.parse.quote(img_url)}"
                    return {
                        "type": "url",
                        "url": proxy_url,
                        "raw_url": img_url,
                        "prompt": prompt,
                        "mode": "study_image",
                        "provider": "bynara"
                    }
        except Exception as e:
            print(f"[ImageGen] Bynara error: {e}")
        return None



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
        """Synthesizes a 100% vector SVG diagram card containing:
        - Header banner with topic icon, title & domain badge
        - Neat explanation box (definition, how it works, why it matters, key benefit)
        - Intuitive mental model card (everyday analogy & core production rule)
        - 5-Column structured vector comparison/summary table (Component, Plain English, Analogy, Code/Syntax, Key Takeaway)
        - Bottom study mastery checklist & exam insight
        100% razor-sharp vector typography on all devices.
        """
        from svg_diagram_templates import build_topic_concept_table_svg
        svg = build_topic_concept_table_svg(prompt)

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
