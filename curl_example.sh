#!/usr/bin/env bash
# The raw HTTP request - no SDK at all. Every SDK does exactly this under the hood.
curl -s https://api.together.ai/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "messages": [{"role": "user", "content": "Explain APIs to a 10 year old in 2 lines."}]
  }'
