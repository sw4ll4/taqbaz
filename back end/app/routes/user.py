from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, Userlogin, Token, UserUpdate
from app.crud.user import Create_user, authenticate_user, update_user, get_user_by_id
from app.database import Sessionlocal
from app.utils.jwt import create_access_token, get_current_user
from app.models.user import User
from app.dependencies import get_current_user_id
 
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

@router.get("/me", response_model= UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/profile", response_model=UserOut)
def edit_own_profile(
    update_data: UserUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    user = update_user(db, user_id, update_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/profile/{user_id}", response_model=UserOut)
def get_public_profile(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/user/{user_id}/products", response_model=List[ProductOut])
def get_user_products(user_id: int, db: Session = Depends(get_db)):
    return get_products_by_user(db, user_id)