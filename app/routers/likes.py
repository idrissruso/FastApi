from fastapi import HTTPException, status, Depends,APIRouter
from sqlalchemy.exc import IntegrityError
from app.utils import hash 
from app.database import get_db
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas
from oauth2 import get_current_user

router = APIRouter(prefix="/likes",tags=["Likes"])

@router.post("")
def like_post(data : schemas.LikeModel,db : Session = Depends(get_db),current_user : int = Depends(get_current_user)):
    post = db.query(models.Likes).filter(models.Likes.post_id == data.post_id).first()
    if not post :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No Post with such id that you provided")
    else : 
        #dir == 0 : like
        #dir == 1 : remove like
        if data.diraction == 0 :
            try:
                new_like = models.Likes(user_id = current_user,post_id = data.post_id)
                db.add(new_like)
                db.commit()
                db.refresh(new_like)
                return schemas.LikeResponseModel(message="Successfully added the like",**new_like.__dict__)
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_226_IM_USED,detail="You can't like a post twice")
        elif data.diraction == 1 :
            like = db.query(models.Likes).filter(models.Likes.post_id == data.post_id,models.Likes.user_id == current_user).first()
            db.delete(like)
            db.commit()
            return schemas.LikeResponseModel(message="Successfully removed the like",**like.__dict__)
            