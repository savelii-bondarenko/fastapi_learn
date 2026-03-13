from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite')
session = sessionmaker(bind=engine,
                       autocommit=False,
                       autoflush=False)

Base = declarative_base()





