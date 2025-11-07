from fastapi import FastAPI
from app.routes.telex_webhook import router as telex_router

app = FastAPI(
    title="DocuLens AI Agent",
    description="AI-powered documentation fetcher and summarizer for Telex.im",
    version="1.0.0"
)

app.include_router(telex_router)

@app.get("/")
def root():
    return {"message": "DocuLens API is running 🚀"}
