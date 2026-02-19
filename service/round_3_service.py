from sqlalchemy import select

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import UploadFile

load_dotenv()
from models.round_3 import Round_3


async def admin_round_3_service(
    db: AsyncSession,
    Team_Name: str,
    status_3: str ,
    feedback_3: str,
    score_3: int,
):


    result = await db.execute(select(Round_3).where(Round_3.Team_Name == Team_Name))
    event = result.scalar_one_or_none()

    if event:
        event.status_3 = status_3
        event.score_3 = score_3
        event.feedback_3 = feedback_3
        await db.commit()
        await db.refresh(event)

    return event
