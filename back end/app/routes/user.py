from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, Userlogin, Token
from app.crud.user import Create_user, authenticate_user
from app.database import Sessionlocal
from app.utils.jwt import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register",response_model= UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return Create_user(user, db)

@router.post("/login", response_model= Token)
def Login(user: Userlogin,db:Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
