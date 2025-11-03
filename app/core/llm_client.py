import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def query_llm(prompt: str, history: list = None):
    """
    Sends a developer query to the LLM (Groq) using conversation context.
    """
    try:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing")

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        # Build message list with memory
        messages = [
            {
                "role": "system",
                "content": (
                    "You are **DocuLens**, an AI documentation assistant built for developers. "
                    "Your sole purpose is to explain and summarize *programming concepts, frameworks, APIs, and tools*. "
                    "You only respond to technical queries related to coding, software development, or engineering documentation. "
                    "If a question is not related to technology, politely decline by saying: "
                    "'I'm designed to assist with programming and developer documentation only.' "
                    "Keep your explanations concise (3–5 sentences) and include short code examples where relevant. "
                    "Use Markdown formatting for readability."
                )
            }
        ]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": prompt})

        payload = {"model": "llama-3.1-8b-instant", "messages": messages}

        async with httpx.AsyncClient(timeout=30) as client:
            res = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload,
            )
            res.raise_for_status()
            data = res.json()
            return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"💥 LLM Error: {e}")
        return None
