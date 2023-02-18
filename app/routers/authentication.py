from fastapi import APIRouter,Depends,HTTPException,status,Response
from app.schemas import LoginCridentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import verify
from app import models

router = APIRouter(tags=["Authentication"])

@router.post("/login",status_code= status.HTTP_200_OK)
def login(credentials : LoginCridentials,db : Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == credentials.email).first()
    if not user or verify(c_password=credentials.password,h_password=user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Cridentials")
    else :
        return {"message" : "Loged in successfully"}