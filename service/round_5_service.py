
import select
from sqlalchemy import select

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


load_dotenv()
from models.round_5 import Round_5




async def Admin_round_5_service(
    db: AsyncSession,
    Team_Name: str,
    
    score_5: int,
    
):
    result = await db.execute(select(Round_5).where(Round_5.Team_Name == Team_Name))
    event = result.scalar_one_or_none()

    if event:
        event.score_5 = score_5
        
        await db.commit()
        await db.refresh(event)

    return event



    