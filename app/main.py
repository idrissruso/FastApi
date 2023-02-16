from fastapi import FastAPI, HTTPException, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from app.database import engine, get_db
from sqlalchemy.orm import Session, sessionmaker
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas


# db: Session = Depends(get_db)

models.Base.metadata.create_all(bind=engine)

while True:
    try:
        with psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='idris2014',
                              cursor_factory=RealDictCursor) as con:
            print("Successfully connected to database")
            cursor = con.cursor()
            break
    except Exception as error:
        print(error)


def getUserBy_id(id: int):
    # cursor.execute(""" SELECT * from users where id = (%s)""", (id,))
    # user = cursor.fetchone()
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(models.Users).filter(models.Users.id == id).first()
    return user


def del_user(id):
    cursor.execute(""" DELETE from users where id = %s""", (id,))
    con.commit()


app = FastAPI()


@app.get("/")
def home():
    return {"Message": "Hello wordl"}


@app.get("/posts")
def get_users(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * from users")
    # users = cursor.fetchall()
    users = db.query(models.Users).all()
    return {"users": users}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post_user(data: schemas.CreateUser, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT into users (name,password) VALUES (%s,%s) RETURNING * """, (data.name, data.password))
    # new_user = cursor.fetchone()
    # con.commit()
    new_user = models.Users(**data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"new_user": new_user}


@app.get("/posts/{id}")
def getUserById(id: int, db: Session = Depends(get_db)):
    user = getUserBy_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"user": user}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usre(id: int, db: Session = Depends(get_db)):
    user = getUserBy_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()


@app.put("/posts/{id}")
def update_user(id: int, data: schemas.CreateUser, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # cursor.execute("""UPDATE users set name = %s, password = %s where id = %s""", (data.name, data.password, id))
    # con.commit()
    user.first().name = data.name
    user.first().password = data.password
    db.commit()
    return {"message": "user Successfully Updated!!!"}
