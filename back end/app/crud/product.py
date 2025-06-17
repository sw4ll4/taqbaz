from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.models.product import Product

def create_product(db: Session, product: ProductCreate, user_id: int):
    db_product= Product(**product.dict(), owner_id = user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product(db: Session, product_id: int, user_id: int):
    product = db.query(Product).filter(Product.id == product_id, Product.owner_id == user_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product
