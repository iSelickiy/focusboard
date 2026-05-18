from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routers import health

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FocuBoard API",
    description="A simple personal task tracker API built with FastAPI.",
    version="0.1.0"
)

app.include_router(health.router)