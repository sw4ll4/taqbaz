from sqlalchemy import Column, String, Integer
from app.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    hashed_password = Column(String)

    products = relationship("Product", back_populates= "owner")
