from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import verify
from app import models, oauth2

router = APIRouter(tags=["Authentication"])

@router.post("/login",status_code= status.HTTP_200_OK)
def login(credentials : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == credentials.username).first()
    if not user or verify(c_password=credentials.password,h_password=user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Cridentials")
    else :
        return oauth2.create_jwt({"user_id" : user.user_id,"user_name" : user.user_name})