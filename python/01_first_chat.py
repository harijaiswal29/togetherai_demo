"""Step 1 - Your first request: ask an open-source model one question.

Real-world example: a travel helper that suggests what to pack.
"""
from together import Together

from common import DEFAULT_MODEL, require_key

require_key()
client = Together()  # reads TOGETHER_API_KEY from the environment

response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[
        {"role": "system", "content": "You are a friendly travel assistant. Answer in 5 bullet points."},
        {"role": "user", "content": "I'm going to Goa in December for 4 days. What should I pack?"},
    ],
    temperature=0.7,  # 0 = predictable, 1+ = more creative
    max_tokens=300,  # cap on the length of the answer
)

print(response.choices[0].message.content)
print("\n--- usage (what you pay for) ---")
print(f"prompt tokens: {response.usage.prompt_tokens}, answer tokens: {response.usage.completion_tokens}")
