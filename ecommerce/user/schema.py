from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    username: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str


class DisplayUser(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_orm = True
