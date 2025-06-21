from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user
from app.routes import product

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(exchange.router, prefix="/exchanges", tags=["Exchanges"])
app.include_router(message.router, prefix="/messages", tags=["Messages"])
app.include_router(notification.router, prefix="/notifications", tags=["Notifications"])
app.include_router(rating.router, prefix="/ratings", tags=["Ratings"])
app.include_router(profile.router, prefix="/profiles", tags=["Profiles"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])