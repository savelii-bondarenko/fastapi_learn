from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from fastapi import Depends

engine = create_engine('sqlite:///Data/DB.sqlite')
session = sessionmaker(bind=engine,
                       autocommit=False,
                       autoflush=False)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] #for routers

def db_delete(data, db: Session):
    db.delete(data)
    db.commit()

def db_add(data, db: Session):
    db.add(data)
    db.commit()

def get_all(table, db: Session):
     return db.query(table).all()

def find_by_id(table, get_id, db: Session):
     return db.query(table).filter(table.id==get_id).first()

def db_update(db: Session):
    db.commit()
