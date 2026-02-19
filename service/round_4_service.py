import select
from sqlalchemy import select

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession 
from typing import List
from fastapi import UploadFile


load_dotenv()
from models.round_4 import  Round_4


async def submit_round_4_service(
    db: AsyncSession,
    Team_Name: str,
    
    status_4: str,
    
    score_4: int,
    feedback_4: str,
):   
    

    result = await db.execute(select(Round_4).where(Round_4.Team_Name == Team_Name))
    event = result.scalar_one_or_none()

    if event:
        event.status_4 = status_4
        event.score_4 = score_4
        event.feedback_4 = feedback_4
        await db.commit()
        await db.refresh(event)

    return event