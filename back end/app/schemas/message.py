from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    exchange_id: int
    content: str

class MessageOut(BaseModel):
    id: int
    sender_id: int
    exchange_id: int
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

