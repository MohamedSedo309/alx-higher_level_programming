#!/usr/bin/python3
"""
linking a python class to a database table
first - define a class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class State; instance of Base
    acting as MySQL table "states"
    """
    __tablename__ = "states"
    id = Column(Ineger, nullable=false, primary_key=true)
    name = Column(String(128), nullable=false)
