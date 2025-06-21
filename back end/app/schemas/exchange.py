from pydantic import BaseModel
from enum import Enum

class ExchangeStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    negotiating = "negotiating"

class ExchangeCreate(BaseModel):
    offered_product_id: int
    requested_product_id: int

class ExchangeOut(BaseModel):
    id: int
    requester_id: int
    responder_id:int
    offered_product_id: int
    requested_product_id: int
    status: ExchangeStatus

    class config:
        orm_mode = True

