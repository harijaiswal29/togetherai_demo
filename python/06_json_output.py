"""Step 6 - Get structured JSON back instead of free text.

Real-world example: turn a messy customer email into fields your app can store.
"""
import json

from together import Together

from common import DEFAULT_MODEL, require_key

require_key()
client = Together()

email = """Hi, this is Priya Sharma. My order #A-1042 arrived with a broken
mug. I'd like a replacement, not a refund. Call me on 98200 12345."""

r = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[
        {
            "role": "system",
            "content": "Extract fields from the email. Reply with JSON only, using keys: "
            "name, order_id, problem, wants (refund|replacement|other), phone.",
        },
        {"role": "user", "content": email},
    ],
    response_format={"type": "json_object"},
    temperature=0,  # we want the same answer every time
)

data = json.loads(r.choices[0].message.content)
print(json.dumps(data, indent=2))
