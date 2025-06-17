from fastapi import HTTPException,status, APIRouter, Depends
from typing import List
from app.database import Sessionlocal
from app.crud import product as crud_product
from app.schemas.product import ProductCreate, ProductOut
from app.routes.user import get_current_user
from app.models.user import User
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/product", response_model=ProductOut)
def create_new_product(product: ProductCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) 
    ):
    return crud_product.get_product(db, product, current_user.id)

@router.get("/products", response_model=List[ProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_product.get_products(db, skip=skip, limit=limit)

@router.get("/products/{product_id}", response_model=ProductOut)
def product_detail(product_id: int, db: Session = Depends(get_db)):
    db_product=crud_product.get_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code= 404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user= Depends(get_current_user)):
    product = crud_product.delete_product(db, product_id, current_user.id)
    if not product:
        raise HTTPException(status_code= 404, detail="Product not found or not owned by user")
    return product
