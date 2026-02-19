from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import UploadFile
from sqlalchemy import select

load_dotenv()
from models.round_2 import Round_2


async def admin_round_2_service(
    db: AsyncSession,
    Team_Name: str,
    status: str,
    score_2: int,
    feedback_2: str):
    result = await db.execute(select(Round_2).where(Round_2.Team_Name == Team_Name))
    event = result.scalar_one_or_none()

    if event:
        event.status = status
        event.score_2 = score_2
        event.feedback_2 = feedback_2
        await db.commit()
        await db.refresh(event)

    return event
