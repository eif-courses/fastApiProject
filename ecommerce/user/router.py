from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ecommerce import db
from sqlalchemy.orm import Session

from . import schema
from . import services
from . import validator

router = APIRouter(tags=["Users"], prefix="/api/v1/users")


@router.get("/", response_model=List[schema.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.get_all_users(database)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_user(request: schema.User, database: Session = Depends(db.get_db)):
    # TODO PATIKRINTI EMAIL
    new_user = await services.new_user_register(request, database)
    return new_user


@router.delete("/{user_id}",
               status_code=status.HTTP_204_NO_CONTENT,
               response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_user_by_id(user_id, database)
