from sqlalchemy.orm import Session
from app.models.exchange import Exchange, ExchangeStatus
from app.schemas.exchange import ExchangeCreate
from app.models.product import Product

def create_exchange(db: Session, user_id: int, data: ExchangeCreate):
    requested_product = db.query(Product).filter(Product.id == data.requested_product_id).first()
    if not requested_product:
        return None
    exchange = Exchange(
        requester_id = user_id,
        responder_id = requested_product.owner_id,
        offered_product_id = data.offered_product_id,
        requested_product_id = data.requested_product
    )
    db.add(exchange)
    db.commit()
    db.refresh(exchange)
    return exchange

def get_exchange_by_user(db: Session, user_id: int):
    return db.query(Exchange).filter((Exchange.requester_id == user_id) | (Exchange.responder_id == user_id)).all()
    
def update_exchange_status(db: Session, exchange_id: int, new_status: ExchangeStatus):
    exchange = db.query(Exchange).filter(Exchange.id == exchange_id).first()
    if exchange:
        Exchange.status = new_status
        db.commit()
        db.refresh(exchange)
    return exchange
