"""Training Dataset Generator & Extractor for Astra AI Learning Agent.
Curated from:
1. LLaMA-Factory (https://github.com/hiyouga/LlamaFactory) — SFT, LoRA/QLoRA, DPO, ShareGPT format
2. Awesome-LLM (https://github.com/hannibal046/awesome-llm) — Architectures, Pre-training, Alignment
3. LLM-Training (https://github.com/topics/llm-training) — DeepSpeed, FSDP, FlashAttention, Distributed
4. SWE-bench Verified (https://www.swebench.com/verified.html) — Software engineering benchmarks & test harness
5. Awesome-LLM-Agents (https://github.com/kaushikb11/awesome-llm-agents) — ReAct, Memory, Tool Use, Multi-agent
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# ─── 1. LLaMA-Factory SFT Training Dataset (ShareGPT & Alpaca Format) ───
LLAMA_FACTORY_SFT_DATA = [
    {
        "instruction": "How do you fine-tune a LLaMA-3 model using LLaMA-Factory with LoRA and 4-bit QLoRA?",
        "input": "GPU: Single RTX 4090 (24GB VRAM), Target: Capacity Building Teaching Assistant",
        "output": "✦ **LLaMA-Factory 4-Bit QLoRA Fine-Tuning Guide** 🚀\n\n◈ **1. Environment Setup & Installation:**\n```bash\ngit clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git\ncd LLaMA-Factory\npip install -e '.[torch,metrics,bitsandbytes]'\n```\n\n◈ **2. Configuration `qlora_llama3.yaml`:**\n```yaml\nmodel_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct\nstage: sft\ndo_train: true\nfinetuning_type: lora\nlora_target: all\nquantization_bit: 4\nquantization_type: nf4\n\ndataset: astra_sft_data\ntemplate: llama3\ncutoff_len: 2048\nlearning_rate: 0.0002\nnum_train_epochs: 3.0\nper_device_train_batch_size: 4\ngradient_accumulation_steps: 4\nlr_scheduler_type: cosine\nwarmup_ratio: 0.1\nfp16: true\noutput_dir: saves/llama3-8b/lora/sft\n```\n\n◈ **3. Execution Command:**\n```bash\nllamafactory-cli train qlora_llama3.yaml\n```\n\n💡 **Key Advantages:** Reduces memory from 80GB to ~14GB VRAM while preserving 99% of full fine-tuning performance!"
    },
    {
        "instruction": "Explain the difference between SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) in modern LLM alignment.",
        "input": "",
        "output": "✦ **SFT vs DPO: Modern LLM Alignment Architecture** 🧠\n\n◈ **1. Supervised Fine-Tuning (SFT):**\n• **Objective:** Train model on high-quality `(Prompt, Response)` demonstration pairs.\n• **Loss Function:** Standard Cross-Entropy Next-Token Prediction:\n  $$\\mathcal{L}_{\\text{SFT}} = -\\sum \\log P_\\theta(y_t | y_{<t}, x)$$\n• **Purpose:** Imparts domain knowledge, persona, formatting, and instruction-following capability.\n\n◈ **2. Direct Preference Optimization (DPO):**\n• **Objective:** Align the model directly using binary preference pairs `(Prompt, Chosen_Response, Rejected_Response)` without requiring a separate reward model (unlike PPO).\n• **Loss Function:** Implicit reward optimization:\n  $$\\mathcal{L}_{\\text{DPO}}(\\pi_\\theta; \\pi_{\\text{ref}}) = -\\mathbb{E}_{(x, y_w, y_l)} \\left[ \\log \\sigma \\left( \\beta \\log \\frac{\\pi_\\theta(y_w|x)}{\\pi_{\\text{ref}}(y_w|x)} - \\beta \\log \\frac{\\pi_\\theta(y_l|x)}{\\pi_{\\text{ref}}(y_l|x)} \\right) \\right]$$\n• **Purpose:** Eliminates hallucinations, toxic outputs, and improves helpfulness."
    },
    {
        "instruction": "Explain the ReAct (Reasoning + Acting) pattern used in state-of-the-art LLM agents.",
        "input": "Provide an execution trace of a learning agent looking up course info.",
        "output": "✦ **ReAct Agent Architecture (Reasoning + Acting)** 🛠️\n\n◈ **Mechanism:** Interleaves verbal reasoning (*Thought*), environment interaction (*Action*), and sensory feedback (*Observation*).\n\n◈ **Execution Trace:**\n```text\nQuestion: Find the highest-rated Python course in Odisha Capacity Connect and check if I am eligible.\n\nThought 1: I need to query the database to list all Python courses sorted by rating.\nAction 1: db_query(\"SELECT title, difficulty, rating FROM courses WHERE category='Python' ORDER BY rating DESC LIMIT 1\")\nObservation 1: [{'title': 'Advanced Python Mastery', 'difficulty': 'intermediate', 'rating': 4.9, 'prereq': 'Basic Python'}]\n\nThought 2: The highest-rated course is 'Advanced Python Mastery'. Now I check the user's completed prerequisites.\nAction 2: check_user_progress(user_id=4, course_name='Basic Python')\nObservation 2: {'completed': True, 'score': 92}\n\nThought 3: The user has completed Basic Python with 92% score, satisfying the prerequisite.\nFinal Answer: 🎯 You are eligible for **Advanced Python Mastery** (4.9 ⭐). You already cleared the prerequisite 'Basic Python' with a 92% score! Would you like me to enroll you now?\n```"
    },
    {
        "instruction": "What is SWE-bench Verified, and how does it evaluate software engineering agents?",
        "input": "",
        "output": "✦ **SWE-bench Verified: Software Engineering Agent Benchmark** 🧪\n\n◈ **Overview:**\nSWE-bench Verified is a curated subset of 500 validated software engineering problems drawn from 12 real-world enterprise Python repositories (e.g. Django, SymPy, Scikit-learn, Sphinx, Flask).\n\n◈ **Evaluation Pipeline:**\n1. **Input:** The agent receives a real GitHub issue description (bug report / feature request) and the repository codebase.\n2. **Execution:** The agent navigates files, writes patches, and outputs a unified git diff `patch.diff`.\n3. **Docker Sandboxed Verification:**\n   - Applies the patch inside a reproducible Docker environment.\n   - Executes the pre-existing unit tests (`PASS_TO_PASS` test suite).\n   - Executes the issue-specific reproduction test suite (`FAIL_TO_PASS`).\n4. **Scoring:** The task is only marked `RESOLVED` if all `FAIL_TO_PASS` tests pass AND no regressions are introduced into `PASS_TO_PASS`!"
    }
]

# ─── 2. ShareGPT Multi-Turn Conversational Dataset ───
SHAREGPT_CONVERSATIONS = [
    {
        "conversations": [
            {"from": "human", "value": "How do plants convert sunlight into food? Explain using emojis and step-by-step logic."},
            {"from": "gpt", "value": "🌿 **Photosynthesis: The Plant Kitchen** ☀️\n\n✦ **Intuition:** Plants are nature's chefs—they use light energy to cook up sugar from air and water!\n\n◈ **The 3 Main Ingredients:**\n• ☀️ **Sunlight:** Absorbed by green **chlorophyll** pigment in leaves.\n• 💧 **Water (H₂O):** Drawn from soil through root xylem tubes.\n• 🍃 **Carbon Dioxide (CO₂):** Breathed in via microscopic leaf pores called **stomata**.\n\n🧪 **The Chemical Reaction:**\n$$6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{Sunlight} \\longrightarrow \\text{C}_6\\text{H}_{12}\\text{O}_6 (\\text{Glucose}) + 6\\text{O}_2 (\\text{Oxygen})$$\n\n🎯 **Outcome:**\n❯ 🍎 **Glucose:** Powers plant growth and cell repair.\n❯ 💨 **Oxygen:** Released into the air for us to breathe!"}
        ]
    }
]

# ─── 3. SWE-bench Style Agent Evaluation Problems ───
SWEBENCH_EVAL_PROBLEMS = [
    {
        "instance_id": "capacity_connect_quiz_session_ttl_001",
        "repo": "capacity-connect/backend",
        "problem_statement": "Issue: `QUIZ_SESSIONS` unbounded dictionary memory leak under high concurrent quiz takers. Need session timestamp TTL cleanup after 1800s.",
        "test_patch": "def test_quiz_session_cleanup():\n    cleanup_quiz_sessions()\n    assert len(QUIZ_SESSIONS) == 0\n",
        "difficulty": "medium",
        "resolved": True
    },
    {
        "instance_id": "capacity_connect_jwt_rbac_002",
        "repo": "capacity-connect/backend",
        "problem_statement": "Feature: Add `@require_role('admin')` decorator to protect `/api/users/pending` and user approval routes.",
        "test_patch": "def test_admin_rbac():\n    resp = client.get('/api/users/pending')\n    assert resp.status_code == 401\n",
        "difficulty": "easy",
        "resolved": True
    }
]


def export_all_datasets():
    """Write out training and evaluation datasets into data directory."""
    sft_file = os.path.join(DATA_DIR, "astra_llamafactory_sft.json")
    with open(sft_file, "w", encoding="utf-8") as f:
        json.dump(LLAMA_FACTORY_SFT_DATA, f, indent=2, ensure_ascii=False)

    sharegpt_file = os.path.join(DATA_DIR, "astra_sharegpt_train.json")
    with open(sharegpt_file, "w", encoding="utf-8") as f:
        json.dump(SHAREGPT_CONVERSATIONS, f, indent=2, ensure_ascii=False)

    swe_file = os.path.join(DATA_DIR, "swe_bench_agent_eval.json")
    with open(swe_file, "w", encoding="utf-8") as f:
        json.dump(SWEBENCH_EVAL_PROBLEMS, f, indent=2, ensure_ascii=False)

    print(f"[Dataset Generator] Exported SFT dataset: {sft_file}")
    print(f"[Dataset Generator] Exported ShareGPT dataset: {sharegpt_file}")
    print(f"[Dataset Generator] Exported SWE-bench eval dataset: {swe_file}")

    return {
        "sft_path": sft_file,
        "sharegpt_path": sharegpt_file,
        "swe_path": swe_file,
        "total_samples": len(LLAMA_FACTORY_SFT_DATA) + len(SHAREGPT_CONVERSATIONS) + len(SWEBENCH_EVAL_PROBLEMS)
    }


if __name__ == "__main__":
    export_all_datasets()
