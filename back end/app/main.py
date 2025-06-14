from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)



