"""Step 0 - See the 'menu': every serverless model you can call right now.

Real-world analogy: before ordering, you look at the restaurant menu.
"""
from collections import Counter

from together import Together

from common import require_key

require_key()
client = Together()

# GET /v1/models returns the public catalog as JSON (a list of model objects).
models = client.get("/v1/models", cast_to=object)

by_type = Counter(m.get("type", "unknown") for m in models)
print(f"{len(models)} models available. By type: {dict(by_type)}\n")

print("A few chat models (id  |  $ per 1M input / output tokens):")
for m in [m for m in models if m.get("type") == "chat"][:20]:
    price = m.get("pricing") or {}
    print(f"  - {m['id']:<60} ${price.get('input', '?')} / ${price.get('output', '?')}")
