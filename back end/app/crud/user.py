from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, Userlogin, UserUpdate
from app.utils.security import hash_password
from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

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

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def update_user(db: Session, user_id: int, update_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    update_fields = update_data.dict(exclude_unset=True)
    for key, value in update_fields.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
