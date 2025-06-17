from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key= True, index= True )
    title = Column(String, index= True)
    description = Column(String)
    image_url = Column(String, nullable= True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates= "products")
