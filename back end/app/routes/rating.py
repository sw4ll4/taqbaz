from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.rating import RatingCreate, RatingOut
from app.crud.rating import create_rating, get_ratings_for_user, calculate_average_rating
from app.dependencies import get_current_user_id

router = APIRouter()

@router.post("/ratings", response_model=RatingOut)
def rate_user(
    rating: RatingCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return create_rating(db, user_id, rating)

@router.get("/ratings/{user_id}", response_model=List[RatingOut])
def get_user_ratings(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_ratings_for_user(db, user_id)

@router.get("/ratings/{user_id}/average")
def get_user_average_rating(
    user_id: int,
    db: Session = Depends(get_db)
):
    return {"average_score": calculate_average_rating(db, user_id)}

