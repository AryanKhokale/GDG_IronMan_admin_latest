from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, FastAPI, Body, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from service.round_2_service import admin_round_2_service
from schemas.round_2_schema import admin_2_submit
from service.round_3_service import admin_round_3_service
from schemas.round_3_schema import admin_3_submit
from schemas.round_4_schema import Admin_4_Submit
from service.round_4_service import submit_round_4_service
from service.round_5_service import Admin_round_5_service
from schemas.round_5_schema import Admin_5_Submit

app = FastAPI()

@app.post("/judge_round_2")
async def judge_round_2_endpoint(
    round_2: admin_2_submit,
    db: AsyncSession = Depends(get_db)
):

    event = await admin_round_2_service(
        db=db,
        Team_Name=round_2.Team_Name,
        status=round_2.status,
        score_2=round_2.score_2,
        feedback_2=round_2.feedback_2
    )

    return {
        "message": "Judged successfully",
        "event": event
    }

@app.post("/judge_round_3")
async def judge_round_3_endpoint(  
    round_3: admin_3_submit,
    db: AsyncSession = Depends(get_db)
):

    event = await admin_round_3_service(
        db=db,
        Team_Name=round_3.Team_Name,
        status_3=round_3.status_3,
        feedback_3=round_3.feedback_3,
        score_3=round_3.score_3
    )

    return {
        "message": "Judged successfully",
        "event": event
    }

@app.post("/submit_round_4")
async def submit_round_4(result: Admin_4_Submit, db: AsyncSession = Depends(get_db)):
    return await submit_round_4_service(
        db=db,
        Team_Name=result.Team_Name,
        status_4=result.status_4,
        score_4=result.score_4,
        feedback_4=result.feedback_4
    )
@app.post("/submit_round_5")
async def submit_round_5(result: Admin_5_Submit, db: AsyncSession = Depends(get_db)):
    return await Admin_round_5_service(
        db=db,
        Team_Name=result.Team_Name,

        score_5=result.score_5,
       
    )
    
    