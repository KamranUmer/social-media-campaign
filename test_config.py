import os

from dotenv import load_dotenv

# Keys come from a local .env file (see .env.example). Never hardcode them here.
load_dotenv()
for name in ("GEMINI_API_KEY", "RAPID_API_KEY", "UNSPLASH_API_KEY"):
    if not os.getenv(name):
        raise RuntimeError(f"Set {name} in your .env file")
