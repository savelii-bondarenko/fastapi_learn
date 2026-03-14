from fastapi import FastAPI
from Data.db import engine
from Data import models
from Routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(todos.router)
app.include_router(auth.router)
