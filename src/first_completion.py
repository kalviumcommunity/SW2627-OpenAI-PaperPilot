import os
import logging

from dotenv import load_dotenv
from openai import OpenAI
from openai import AuthenticationError, RateLimitError


load_dotenv()

logging.basicConfig(level=logging.INFO)

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

model = os.getenv("CHAT_MODEL")

messages = [
    {
        "role": "system",
        "content": "You are a concise academic research assistant."
    },
    {
        "role": "user",
        "content": "Explain what a research paper is in one sentence."
    }
]

try:
    logging.info("REQUEST: %s", messages)

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content

    logging.info("RESPONSE: %s", answer)
    logging.info("USAGE: %s", response.usage)

    print("\nAssistant:")
    print(answer)

except AuthenticationError:
    print("Auth failed (401): check OPENAI_API_KEY in your .env")

except RateLimitError:
    print("Rate limited (429): slow down and retry with backoff")

except Exception as e:
    print(f"An unexpected error occurred: {e}")