from typing import List

from sqlalchemy import select

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
load_dotenv()
from models.permission import Permission


async def permission_service(
    db: AsyncSession,
    Role: str,
    permission: str,
):


    result = await db.execute(select(Permission).where(Permission.User == Role))
    event = result.scalar_one_or_none()
    
    if event:
       # event.User = Role
        event.permission = permission
        await db.commit()
        await db.refresh(event)
        return event
    else:
       # new_permission = Permission(User=Role, permission=permission)
       # db.add(new_permission)
       # await db.commit()
       # await db.refresh(new_permission)
       # return new_permission
       return {"message": f"Role '{Role}' not found. No updates made."}

   

    

