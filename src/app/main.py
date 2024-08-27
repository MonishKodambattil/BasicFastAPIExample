from fastapi import FastAPI
from src.app.api import users, items
from src.app.db import models
from src.app.db.session import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)