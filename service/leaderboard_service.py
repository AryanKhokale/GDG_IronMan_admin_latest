from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select

load_dotenv()
from models.leaderboard import Leaderboard


async def get_leaderboard_entry(
    db: AsyncSession,
    Team_Name: str
    ):
    result = await db.execute(select(Leaderboard).where(Leaderboard.Team_Name == Team_Name))
    event = result.scalar_one_or_none()

    return event

async def get_current_leaderboard(db: AsyncSession):

    result = await db.execute(
        select(Leaderboard).order_by(desc(Leaderboard.team_score))
    )

    records = result.scalars().all()

    return records
