from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from ecommerce.db import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    quantity = Column(Integer)
    description = Column(String(255))
    price = Column(Float)

    category_id = Column(Integer, ForeignKey('category.id', ondelete="CASCADE"))
    category = relationship("Category", back_populates="product")
    cart_items = relationship("CartItems", back_populates="products")



