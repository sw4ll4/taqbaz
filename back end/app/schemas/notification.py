from pydantic import BaseModel

class NotificationCreate(BaseModel):
    user_id: int
    message: str

class NotificationOut(BaseModel):
    id: int
    user_id: int
    message: str
    is_read: bool

    class Config:
        orm_mode = True
