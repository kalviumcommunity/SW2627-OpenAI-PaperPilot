import os

from dotenv import load_dotenv


load_dotenv()

print("Base URL:", os.getenv("OPENAI_BASE_URL"))
print("Chat Model:", os.getenv("CHAT_MODEL"))
print("Embedding Model:", os.getenv("EMBED_MODEL"))

if os.getenv("OPENAI_API_KEY"):
    print("API key: configured")
else:
    print("API key: not configured")