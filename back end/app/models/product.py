from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = column(Integer, primary_key= True, index= True )
    title = column(String, index= True)
    description = column(String)
    image_url = Column(String, nullable= True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates= "products")
