from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

def Create_user(db: Session, user: UserCreate):
    db_user = User(
        username = user.username,
        hashed_password = hash_password(user.password),
        email = user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
