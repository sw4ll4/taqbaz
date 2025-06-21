from pydantic import BaseModel
from typing import Optional

class RatingCreate(BaseModel):
    rated_user_id: int
    exchange_id: int
    score: int  # عدد بین 1 تا 5
    comment: Optional[str] = None

class RatingOut(BaseModel):
    id: int
    rater_id: int
    rated_user_id: int
    exchange_id: int
    score: int
    comment: Optional[str]

    class Config:
        orm_mode = True

