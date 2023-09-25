from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ecommerce import db
from sqlalchemy.orm import Session

from . import schema
from . import services
from . import validator

router = APIRouter(tags=["Cart"], prefix="/cart")


@router.post("/add")
async def add_to_cart(product_id: int, database: Session = Depends(db.get_db)):
    result = await services.add_to_cart(product_id, database)
    return result
