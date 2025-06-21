from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.message import MessageCreate, MessageOut
from app.crud.message import send_message, get_messages_for_exchange
from app.database import get_db
from app.dependencies import get_current_user_id  # برای گرفتن user از JWT

router = APIRouter()

@router.post("/messages", response_model=MessageOut)
def create_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return send_message(db, user_id, message)

@router.get("/messages/{exchange_id}", response_model=List[MessageOut])
def get_chat_messages(
    exchange_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return get_messages_for_exchange(db, exchange_id)
