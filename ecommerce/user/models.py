import datetime

from sqlalchemy import Column, Integer, String, DateTime, ARRAY

from ecommerce.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(255))
    email = Column(String(255), unique=True)
    age = Column(Integer)
    permissions = Column(ARRAY(String(255)))
    created_at = Column(DateTime, default=datetime.datetime.now())
