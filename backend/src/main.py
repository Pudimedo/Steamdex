from fastapi import FastAPI
from app.api import api_router
from models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SteamDex API")

app.include_router(api_router)