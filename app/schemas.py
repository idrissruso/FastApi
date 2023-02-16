from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    password: str
    id: Optional[int] = None


class CreateUser(User):
    pass
