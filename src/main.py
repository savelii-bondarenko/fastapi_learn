from typing import Annotated

from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session

import models
from models import Todos
from db import engine, session
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todos/{todo_id}")
async def get_todo_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todos).filter(Todos.id==todo_id).first()
    if todo is not None:
        return todo 
    return "Todo is not found"
    
