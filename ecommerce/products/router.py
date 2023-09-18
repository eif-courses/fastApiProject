from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ecommerce import db
from sqlalchemy.orm import Session

from . import schema
from . import services
from . import validator

router = APIRouter(tags=["Products"], prefix="/api/v1/products")


@router.post("/category", status_code=status.HTTP_201_CREATED)
async def create_new_category(request: schema.Category, database: Session = Depends(db.get_db)):
    category = await services.create_new_category(request, database)
    return category


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_product(request: schema.Product, database: Session = Depends(db.get_db)):
    # Category validator if exist

    product = await services.create_new_product(request, database)
    return product


@router.get("/", response_model=List[schema.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.gel_all_products(database)
