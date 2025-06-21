from sqlalchemy.orm import Session
from app.models.message import Message
from app.schemas.message import MessageCreate

def send_message(db: Session, sender_id: int, message: MessageCreate):
    new_message = Message(
        sender_id=sender_id,
        exchange_id=message.exchange_id,
        content=message.content
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_messages_for_exchange(db: Session, exchange_id: int):
    return db.query(Message).filter(Message.exchange_id == exchange_id).order_by(Message.timestamp).all()
