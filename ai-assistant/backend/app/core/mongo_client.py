from datetime import datetime
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client["neurosync_ai"]


async def append_message(session_id: str, role: str, content: str) -> None:
    if not content:
        return
    await db.messages.insert_one(
        {
            "session_id": session_id,
            "role": role,
            "content": content,
            "created_at": datetime.utcnow(),
        }
    )


async def get_session_messages(session_id: str) -> List[dict]:
    cursor = db.messages.find({"session_id": session_id}).sort("created_at", 1)
    documents = await cursor.to_list(length=200)
    return [
        {
            "role": item["role"],
            "content": item["content"],
            "timestamp": item["created_at"].isoformat() if item.get("created_at") else None,
        }
        for item in documents
    ]


async def clear_session(session_id: str) -> None:
    await db.messages.delete_many({"session_id": session_id})
