from pydantic import BaseModel
from typing import List
from app.schemas.product import ProductOut
from app.schemas.exchange import ExchangeOut
from app.schemas.message import MessageOut
from app.schemas.notification import NotificationOut

class DashboardOut(BaseModel):
    products: List[ProductOut]
    sent_exchanges: List[ExchangeOut]
    received_exchanges: List[ExchangeOut]
    messages: List[MessageOut]
    notifications: List[NotificationOut]
