import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def summarize_text(text: str):
    """
    Summarizes long documentation text using Groq API.
    """
    if not GROQ_API_KEY:
        return text[:400] + "..." if len(text) > 400 else text

    prompt = f"Summarize the following documentation in 2 short sentences:\n\n{text}"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": prompt}]}

    async with httpx.AsyncClient() as client:
        res = await client.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        data = res.json()
        return data["choices"][0]["message"]["content"].strip()
