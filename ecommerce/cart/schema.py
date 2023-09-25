import datetime
from typing import List

from pydantic import BaseModel

from ecommerce.products.schema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    created_at: datetime.datetime

    class Config:
        from_orm = True


class ShowCart(BaseModel):
    id: int
    cart_items: List[ShowCartItems] = []

    class Config:
        from_orm = True
