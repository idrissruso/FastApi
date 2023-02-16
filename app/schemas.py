from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    password: str
    id: Optional[int] = None


class CreateUser(User):
    pass


class ResponseModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
