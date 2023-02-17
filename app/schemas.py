from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class CreateUser(User):
    pass


class ResponseModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
