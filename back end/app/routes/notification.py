from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.notification import NotificationOut, NotificationCreate
from app.crud.notification import (
    create_notification, get_user_notifications, mark_as_read
)
from app.database import get_db
from app.dependencies import get_current_user_id
from typing import List

router = APIRouter()

@router.post("/notifications", response_model=NotificationOut)
def create_new_notification(
    notif: NotificationCreate,
    db: Session = Depends(get_db)
):
    return create_notification(db, notif)

@router.get("/notifications", response_model=List[NotificationOut])
def get_my_notifications(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return get_user_notifications(db, user_id)

@router.put("/notifications/{notif_id}/read", response_model=NotificationOut)
def mark_notification_read(
    notif_id: int,
    db: Session = Depends(get_db)
):
    return mark_as_read(db, notif_id)
