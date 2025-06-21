from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    rater_id = Column(Integer, ForeignKey("users.id"))
    rated_user_id = Column(Integer, ForeignKey("users.id"))
    exchange_id = Column(Integer, ForeignKey("exchanges.id"))
    score = Column(Integer)  # امتیاز بین ۱ تا ۵
    comment = Column(Text, nullable=True)

    rater = relationship("User", foreign_keys=[rater_id], backref="given_ratings")
    rated_user = relationship("User", foreign_keys=[rated_user_id], backref="received_ratings")
