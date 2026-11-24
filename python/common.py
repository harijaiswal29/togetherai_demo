"""Shared setup for every demo: load the API key and pick a default model."""
import os
import sys

try:
    from dotenv import load_dotenv  # reads TOGETHER_API_KEY from a .env file

    load_dotenv()
except ImportError:
    pass

# Model IDs change over time. Run `python python/00_list_models.py` to see what is live today.
DEFAULT_MODEL = os.environ.get("TOGETHER_MODEL", "meta-llama/Llama-3.3-70B-Instruct-Turbo")


def require_key() -> None:
    if not os.environ.get("TOGETHER_API_KEY"):
        sys.exit(
            "TOGETHER_API_KEY is not set.\n"
            "  1. Create a key at https://api.together.ai/settings/api-keys\n"
            "  2. Copy .env.example to .env and paste the key there\n"
            "     (or run: export TOGETHER_API_KEY=your-key)"
        )
