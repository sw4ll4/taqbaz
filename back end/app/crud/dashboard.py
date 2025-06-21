from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.exchange import Exchange
from app.models.message import Message
from app.models.notification import Notification

def get_user_dashboard_data(db: Session, user_id: int):
    products = db.query(Product).filter(Product.owner_id == user_id).all()
    sent_exchanges = db.query(Exchange).filter(Exchange.sender_id == user_id).all()
    received_exchanges = db.query(Exchange).filter(Exchange.receiver_id == user_id).all()
    messages = db.query(Message).filter(Message.sender_id == user_id).all()
    notifications = db.query(Notification).filter(Notification.user_id == user_id).all()

    return {
        "products": products,
        "sent_exchanges": sent_exchanges,
        "received_exchanges": received_exchanges,
        "messages": messages,
        "notifications": notifications,
    }
