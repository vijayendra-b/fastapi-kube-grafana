from sqlalchemy import *
from app.database import Base
class Product(Base):
 __tablename__="products"
 id=Column(Integer,primary_key=True)
 name=Column(String(100))
 price=Column(Float)
 quantity=Column(Integer)
class Order(Base):
 __tablename__="orders"
 id=Column(Integer,primary_key=True)
 product_id=Column(Integer)
 quantity=Column(Integer)
