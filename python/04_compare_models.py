"""Step 4 - Same question, several open-source models. Swapping models = changing one string.

Real-world analogy: asking three different doctors for a second opinion.
"""
import time

from together import Together

from common import require_key

require_key()
client = Together()

# Edit this list freely - run 00_list_models.py to see what's available.
MODELS = [
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "Qwen/Qwen2.5-7B-Instruct-Turbo",
    "deepseek-ai/DeepSeek-V3",
]
QUESTION = "In one sentence: why is the sky blue?"

for model in MODELS:
    start = time.perf_counter()
    try:
        r = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": QUESTION}], max_tokens=100
        )
    except Exception as e:  # a model may be retired or need a dedicated endpoint
        print(f"\n[{model}] skipped: {e}")
        continue
    seconds = time.perf_counter() - start
    print(f"\n[{model}]  ({seconds:.1f}s, {r.usage.completion_tokens} tokens)")
    print("  " + r.choices[0].message.content.strip())
