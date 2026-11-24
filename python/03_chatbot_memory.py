"""Step 3 - A tiny chatbot that remembers the conversation.

Models have no memory of their own. To 'remember', you resend the whole
conversation every time - like handing a new waiter your order history.
Type 'quit' to exit.
"""
from together import Together

from common import DEFAULT_MODEL, require_key

require_key()
client = Together()

history = [{"role": "system", "content": "You are a helpful cooking assistant. Keep answers short."}]

print(f"Chatting with {DEFAULT_MODEL}. Type 'quit' to exit.\n")
while True:
    user_text = input("You: ").strip()
    if user_text.lower() in {"quit", "exit", ""}:
        break
    history.append({"role": "user", "content": user_text})

    reply = client.chat.completions.create(model=DEFAULT_MODEL, messages=history, max_tokens=400)
    answer = reply.choices[0].message.content
    history.append({"role": "assistant", "content": answer})  # <- this line is the 'memory'
    print(f"Bot: {answer}\n")
