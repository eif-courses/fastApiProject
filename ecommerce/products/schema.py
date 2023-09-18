from pydantic import BaseModel, constr

from typing import Optional


class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class ListCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_orm: True


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    class Config:
        from_orm: True


class Product(ProductBase):
    category_id: int


class ProductListing(ProductBase):
    category: ListCategory

    class Confing:
        from_orm: True
