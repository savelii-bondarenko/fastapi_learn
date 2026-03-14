from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Data/DB.sqlite')
session = sessionmaker(bind=engine,
                       autocommit=False,
                       autoflush=False)

Base = declarative_base()

def db_delete(data):
    db = session()
    db.delete(data)
    db.commit()
    db.close()

def db_add(data):
    db = session()
    db.add(data)
    db.commit()
    db.close()


def get_all(table):
    db = session()
    data = db.query(table).all()
    db.close()
    return data


def find_by_id(table, get_id):
    db = session()
    data = db.query(table).filter(table.id==get_id).first()
    db.close()
    return data

def db_update():
    db = session()
    db.commit()
    db.close()
