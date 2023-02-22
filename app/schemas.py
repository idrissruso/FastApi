from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class User(BaseModel):
    user_name: str
    email: EmailStr
    password: str


class CreateUser(User):
    pass


class ResponseModel(BaseModel):
    user_id: int
    user_name: str

    class Config:
        orm_mode = True
        
        
class UserResponseModel(BaseModel):
    user_name: str
    email: str

    class Config:
        orm_mode = True
        
        
class CreatePost(BaseModel):
    title : str
    content : str
    owner_id : Optional[int] = None
    
    class Config:
        orm_mode = True
    

class PostResponseModel(BaseModel):
    title : str
    content : str
    owner_id : Optional[int] = None
    owner: Optional[UserResponseModel] = None
    
    class Config:
        orm_mode = True
        
class LoginCridentials(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token : str
    token_type : str
    
    
    class Config():
        orm_mode = True
        
class TokenData(BaseModel):
    user_id : Optional[str] = None
    user_name : Optional[str] = None

class LikeModel(BaseModel):
    post_id : int
    diraction : conint(le=1)

class LikeResponseModel(BaseModel):
    message : str
    post_id : int
    user_id : int
    