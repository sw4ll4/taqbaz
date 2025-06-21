from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user_id
from app.schemas.dashboard import DashboardOut
from app.crud.dashboard import get_user_dashboard_data

router = APIRouter()

@router.get("/dashboard", response_model=DashboardOut)
def get_dashboard(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return get_user_dashboard_data(db, user_id)