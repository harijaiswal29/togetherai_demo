# Together AI demo: open-source models, explained visually

A beginner-friendly guide to calling open-source AI models (Llama, DeepSeek, Qwen, Mistral, FLUX…) through [Together AI](https://www.together.ai), plus small runnable demos.

**Start here:** open [`index.html`](index.html) in your browser. It's a single self-contained page with diagrams, an interactive temperature slider, a token/cost calculator and a streaming animation.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then paste your key from https://api.together.ai/settings/api-keys
python python/01_first_chat.py
```

## Demos (run in order)

| Script | What it teaches |
|---|---|
| `python/00_list_models.py` | List live models and prices (the "menu") |
| `python/01_first_chat.py` | First request: system + user messages, temperature, max_tokens, usage |
| `python/02_streaming.py` | Print the answer word-by-word |
| `python/03_chatbot_memory.py` | Interactive chatbot; memory = resending history |
| `python/04_compare_models.py` | Same question to several models, timing compared |
| `python/05_openai_sdk.py` | Use the OpenAI Python library with Together (2-line change) |
| `python/06_json_output.py` | Extract structured JSON from a messy email |
| `python/07_embeddings_search.py` | Semantic FAQ search with embeddings |
| `python/08_generate_image.py` | Text-to-image with FLUX, saved as PNG |
| `javascript/chat.mjs`, `stream.mjs` | Same ideas in Node.js (`cd javascript && npm install`) |
| `curl_example.sh` | The raw HTTP request, no SDK |

Change the default chat model for all demos with `TOGETHER_MODEL=...` in `.env`.
Model IDs change over time, so run `00_list_models.py` to see what's currently available.
