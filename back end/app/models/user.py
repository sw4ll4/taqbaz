from sqlalchemy import Column, String, Integer, Text
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    bio = Column(Text, nullable=True)
    avatar_url = Column(String, nullable=True)


    products = relationship("Product", back_populates= "owner")

notifications = relationship("Notification", back_populates="user", cascade="all, delete")
