from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import chat, auth

app = FastAPI(
    title="NeuroSync AI Assistant API",
    description="Async AI assistant backend with WebSocket streaming, session memory, and provider routing.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
