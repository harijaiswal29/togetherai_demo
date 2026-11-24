"""Step 2 - Streaming: print the answer word-by-word as it is generated.

Real-world analogy: watching a live cricket score vs. reading tomorrow's newspaper.
"""
from together import Together

from common import DEFAULT_MODEL, require_key

require_key()
client = Together()

stream = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Write a 4-line poem about monsoon rain in Mumbai."}],
    stream=True,
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
