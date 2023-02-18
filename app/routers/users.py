from fastapi import HTTPException, status, Depends,APIRouter
import sqlalchemy
from app.utils import hash 
from app.database import get_db
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas


router = APIRouter(prefix="/users",tags=["Users"])


@router.get("/", response_model=list[schemas.ResponseModel])
def get_users(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * from users")
    # users = cursor.fetchall()
    users = db.query(models.Users).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseModel)
def post_user(data: schemas.CreateUser, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT into users (name,password) VALUES (%s,%s) RETURNING * """, (data.name, data.password))
    # new_user = cursor.fetchone()
    # con.commit()
    h_password = hash(data.password)
    data.password = h_password
    new_user = models.Users(**data.dict())
    try:
        db.add(new_user)
        db.commit()
    except sqlalchemy.exc.IntegrityError :
       raise HTTPException(status_code=status.HTTP_226_IM_USED)
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=schemas.ResponseModel)
def getUserBy_id(user_id: int,db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()


@router.put("/{user_id}")
def update_user(user_id: int, data: schemas.CreateUser, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.user_id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # cursor.execute("""UPDATE users set name = %s, password = %s where user_id = %s""", (data.name, data.password, user_id))
    # con.commit()
    user.first().user_name = data.user_name
    user.first().password = data.password
    db.commit()
    return {"message": "user Successfully Updated!!!"}