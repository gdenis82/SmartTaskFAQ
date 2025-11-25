from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.get("/ask")
async def ask_question(request: QuestionRequest, db: Session = Depends(get_db)):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question is empty")

    return {"answer": "Smart FAQ is awesome!"}