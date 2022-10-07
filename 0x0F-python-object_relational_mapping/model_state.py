#!/usr/bin/python3
"""
Create a State class and map it to the states table
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Column


engine = create_engine(
      "mysql+pymysql://root:passwd@localhost/db?host=localhost?port=3306")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class State(Base):
    """
    States class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
