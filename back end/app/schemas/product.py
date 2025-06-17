from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductOut(ProductCreate):
    id: int
    owner_id: int
    price: Optional[int]
    class config:
        orm_mode = True
