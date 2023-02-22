from fastapi import HTTPException, status, Depends,APIRouter
import sqlalchemy
from app.utils import hash 
from app.database import get_db
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas
from oauth2 import get_current_user

router = APIRouter(prefix="/likes",tags=["Likes"])

@router.get("")
def like_post(data : dict,db : Session = Depends(get_db),current_user : int = Depends(get_current_user)):
    pass
