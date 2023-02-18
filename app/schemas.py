from pydantic import BaseModel, EmailStr


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
        
        
class CreatePost(BaseModel):
    title : str
    content : str
    
class PostResponseModel(BaseModel):
    post_id : int
    title : str
    content : str
    
    
    class Config():
        orm_mode = True
        
class LoginCridentials(BaseModel):
    email: EmailStr
    password: str