from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    desc = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
