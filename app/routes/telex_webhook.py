from fastapi import APIRouter, Request, Body
from app.services.telex_response import build_response
from app.core.llm_client import query_llm
from app.core.summarizer import summarize_text
from app.core.memory import add_to_memory, get_memory


router = APIRouter(tags=["Telex Webhook"])

@router.post("/")
async def telex_webhook(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message", "")
        channel_id = str(data.get("channel_id", "default"))  # Telex chat channel or fallback

        if not user_message:
            return build_response("❌ No message received.")

        # Save user message to memory
        add_to_memory(channel_id, "user", user_message)

        # Get conversation context
        history = get_memory(channel_id)

        # Generate LLM response
        response = await query_llm(user_message, history=history)

        if not response:
            return build_response("⚠️ DocuLens couldn’t find a suitable explanation. Try again later.")

        # Summarize if needed (for long responses)
        response_summary = await summarize_text(response)

        # Save assistant response to memory
        add_to_memory(channel_id, "assistant", response_summary)

        # Return Telex message
        message = f"📘 **DocuLens AI Response:**\n\n{response_summary}"
        return build_response(message)

    except Exception as e:
        return build_response(f"⚠️ Internal Error: {str(e)}")


@router.post("/query")
async def query_docs(user_message: str = Body(..., embed=True)):
    """
    Accepts a user query directly via API (for local or external testing).
    Example JSON:
    {
        "message": "How do I use FastAPI BackgroundTasks?"
    }
    """
    try:
        if not user_message:
            return build_response("❌ No message received.")

        # Use a fixed 'local' channel_id for local testing memory
        channel_id = "local_test"

        # Save user query to memory
        add_to_memory(channel_id, "user", user_message)

        # Retrieve recent context
        history = get_memory(channel_id)

        # Query LLM with context
        response = await query_llm(user_message, history=history)

        if not response:
            return build_response("⚠️ DocuLens couldn’t find a suitable explanation. Try again later.")

        # Summarize for brevity
        response_summary = await summarize_text(response)

        # Store assistant reply
        add_to_memory(channel_id, "assistant", response_summary)

        # Build and return formatted response
        message = f"📘 **DocuLens AI Response:**\n\n{response_summary}"
        return build_response(message)

    except Exception as e:
        return build_response(f"⚠️ Internal Error: {str(e)}")