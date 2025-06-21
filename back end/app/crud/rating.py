from sqlalchemy.orm import Session
from app.models.rating import Rating
from app.schemas.rating import RatingCreate

def create_rating(db: Session, rater_id: int, rating: RatingCreate):
    new_rating = Rating(
        rater_id=rater_id,
        rated_user_id=rating.rated_user_id,
        exchange_id=rating.exchange_id,
        score=rating.score,
        comment=rating.comment
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

def get_ratings_for_user(db: Session, user_id: int):
    return db.query(Rating).filter(Rating.rated_user_id == user_id).all()

def calculate_average_rating(db: Session, user_id: int):
    from sqlalchemy import func
    avg = db.query(func.avg(Rating.score)).filter(Rating.rated_user_id == user_id).scalar()
    return round(avg or 0, 2)
