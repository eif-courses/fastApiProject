import datetime

from sqlalchemy import Column, Integer, String, DateTime, ARRAY

from ecommerce.db import Base
from ecommerce.user import hashing


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(255))
    email = Column(String(255), unique=True)
    age = Column(Integer)
    permissions = Column(ARRAY(String(255)))
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __init_(self, username, password, email, *args, **kwargs):
        self.username = username
        self.password = hashing.get_password_hash(password)
        self.email = email

    def check_password(self, password):
        return hashing.verify_password(self.password, password)

