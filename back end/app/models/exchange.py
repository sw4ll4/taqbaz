from sqlalchemy import Column, Integer, Srting, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class ExchangeStatus(str, enum.Enum):
    pending = "pending"
    rejected = "rejected"
    accepted = "accepted"
    negotiating = "negotiating"

class Exchange(Base):
    __tablename__ = "exchanges"

    id = Column(Integer, primary_key= True, index= True)
    requester_id = Column(Integer, ForeignKey("users.id"))
    responder_id = Column(Integer, ForeignKey("users.id"))
    offered_product_id = Column(Integer, ForeignKey("products.id"))
    requested_product_id = Column(Integer, ForeignKey("products.id"))
    status = Column(Enum(ExchangeStatus), default= ExchangeStatus.pending)

    requester = relationship("User", foreign_keys =[requester_id])
    responder = relationship("User", foreign_keys =[responder_id])
    offered_product = relationship("Product", foreign_keys =[offered_product_id])
    requested_product = relationship("Product", foreign_keys =[requested_product_id])
    