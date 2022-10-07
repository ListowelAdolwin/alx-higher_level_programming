#!/usr/bin/python3
"""
Create a State class and map it to the states table
"""


from sqlalchemy import create_engine
from sql.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Column
import State


engine = create_engine(
      "mysql+pymysql://listo:passwd@localhost/db?host=localhost?port=3306")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class State(Base):
    __table__ = 'states'
    id = Column(integer, primary_key=True, unique=True,
                auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
