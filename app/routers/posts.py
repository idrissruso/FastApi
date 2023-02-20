from fastapi import HTTPException, status, Depends,APIRouter
from app import oauth2
from app.database import get_db
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas


router = APIRouter(prefix="/posts",tags=["Posts"])



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponseModel)
def create_post(post:schemas.CreatePost,db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    post_dict = post.dict(exclude_unset=True)
    new_post = models.Post(owner_id = current_user,**post_dict)
    try:
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    except Exception :
        raise HTTPException(status_code=status.HTTP_226_IM_USED)
    return new_post


@router.get("/{post_id}",response_model=schemas.PostResponseModel)
def get_post_by_id(post_id : int,db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post

@router.delete("/{post_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_post(post_id : int,db : Session = Depends(get_db)):
   post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
   if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
   db.delete(post)
   db.commit()
   
@router.get("/",response_model=list[schemas.PostResponseModel])
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.put("/{post_id}",response_model=schemas.PostResponseModel)
def update_post(data : schemas.CreatePost,post_id : int,db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED)
    else : 
        post.first().title = data.title
        post.first().content = data.content
        db.commit()
        new_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
        return new_post
        
    