"""Step 5 - Already using the OpenAI library? Change two lines and you're on Together AI.

Real-world analogy: the same phone charger works because the socket shape is standard.
"""
import os

from openai import OpenAI

from common import DEFAULT_MODEL, require_key

require_key()
client = OpenAI(
    api_key=os.environ["TOGETHER_API_KEY"],  # change #1: your Together key
    base_url="https://api.together.ai/v1",  # change #2: point at Together
)

r = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Give me 3 name ideas for a chai cafe."}],
)
print(r.choices[0].message.content)
