"""Production RAG & Multi-LLM Benchmark Suite for Astra Chatbot.
Tests:
1. RAG Knowledge Indexing and Top-K Semantic Retrieval
2. Live Google Gemini generation with RAG context
3. Automatic Fallback LLM Adapter configuration (Claude / Proxy)
4. Pedagogical scenarios (Socratic dialogue, Code debugging, Math logic, Course queries)
"""

import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')

from rag_engine import get_retriever, get_rag_context
from llm_adapter import get_adapter, GeminiAdapter, FallbackProxyAdapter
from astra_full import process_full
import astra_engine as base


def run_benchmark():
    print("=" * 60)
    print("🚀 ASTRA PRODUCTION RAG AGENT BENCHMARK & TEST SUITE")
    print("=" * 60)

    # ── Test 1: RAG Indexing & Retrieval ──
    print("\n[TEST 1] RAG Knowledge Indexing & Retrieval...")
    retriever = get_retriever()
    print(f"✓ Indexed {len(retriever.documents)} documents across courses, modules, and quizzes.")
    
    rag_test_query = "How do React hooks work with state?"
    docs = retriever.retrieve(rag_test_query, top_k=2)
    print(f"✓ Query '{rag_test_query}' retrieved {len(docs)} relevant items:")
    for d in docs:
        print(f"   • [{d['type']}] {d['title']}")
    
    assert len(docs) > 0, "RAG retrieval returned 0 documents"

    # ── Test 2: Multi-Model & Fallback Adapter ──
    print("\n[TEST 2] Adapter & Fallback Configuration...")
    adapter = get_adapter()
    print(f"✓ Active Primary LLM: {type(adapter).__name__}")
    if isinstance(adapter, GeminiAdapter) and adapter.fallback_adapter:
        fb = adapter.fallback_adapter
        print(f"✓ Secondary Fallback Configured: {type(fb).__name__} (Model: {fb.model_name})")

    # ── Test 3: RAG-Augmented Query Generation ──
    test_cases = [
        ("General Concept", "What is an API in simple terms?"),
        ("Code Debugging", "fix error: TypeError: 'int' object is not subscriptable in x = 5; print(x[0])"),
        ("Course-Specific Grounding", "What is covered in the React course on this portal?"),
        ("Math / Reasoning", "If training accuracy is 99% and test accuracy is 60%, what is the issue?"),
    ]

    print("\n[TEST 3] Running Pedagogical Test Cases...")
    for label, query in test_cases:
        print(f"\n--- Scenario: {label} ---")
        print(f"User: {query}")
        
        t0 = time.time()
        res = process_full(query, user_id=4)
        elapsed = round(time.time() - t0, 2)
        
        reply = res.get("reply", "")
        mode = res.get("mode", "general")
        print(f"Astra ({mode} mode, {elapsed}s):\n{reply[:250]}...\n")
        assert len(reply) > 20, f"Empty reply for scenario: {label}"

    print("=" * 60)
    print("✅ ALL RAG & AGENT BENCHMARK TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmark()
