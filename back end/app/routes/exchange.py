from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.exchange import ExchangeCreate, ExchangeOut, ExchangeStatus
from app.crud.exchange import create_exchange, get_exchange_by_user, update_exchange_status
from app.database import SessionLocal
from app.utils.jwt import get_current_user_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/exchange",response_model = ExchangeOut)
def send_exchange(data: ExchangeCreate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    result = create_exchange(db, user_id, data)
    if not result:
        raise HTTPException(status_code=404, detail = "Requested product not found")
    return result
    
@router.get("/exchange",response_model = List[ExchangeOut])
def my_exchanges(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return get_exchange_by_user(db, user_id)

@router.put("/exchange/{exchange_id}/{new_status}", response_model= ExchangeOut)
def update_status(
    new_status: ExchangeStatus,
    exchange_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    exchange= update_exchange_status(db, new_status, exchange_id)
    if not exchange:
        raise HTTPException(status_code = 404, detail="exchange not found")
    return exchange
