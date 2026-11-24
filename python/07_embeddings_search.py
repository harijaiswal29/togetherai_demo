"""Step 7 - Embeddings: find the FAQ answer that *means* the same thing as the question.

Embeddings turn text into a list of numbers (a 'location' on a map of meaning).
Texts with similar meaning land close together - even with zero shared words.
"""
import math

from together import Together

from common import require_key

require_key()
client = Together()
EMBED_MODEL = "BAAI/bge-base-en-v1.5"

faqs = [
    "How do I reset my password?",
    "What are your delivery charges?",
    "Can I return a product after 10 days?",
    "Do you ship outside India?",
]
question = "I forgot my login details"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


vectors = client.embeddings.create(model=EMBED_MODEL, input=faqs + [question]).data
faq_vecs, q_vec = [v.embedding for v in vectors[:-1]], vectors[-1].embedding

print(f'Question: "{question}"\n')
for faq, score in sorted(((f, cosine(q_vec, v)) for f, v in zip(faqs, faq_vecs)), key=lambda x: -x[1]):
    print(f"  {score:.3f}  {faq}")
