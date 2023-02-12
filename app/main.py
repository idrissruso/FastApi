from typing import Union
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from random import randrange


class Post_Model(BaseModel):
    name: str
    password: str
    id: int


users = [{
    "name": "Nasra",
    "password": "Nasra@abkar@2014",
    "id": 274404
}, {
    "name": "Nasra",
    "password": "Nasra@abkar@2014",
    "id": 845092
}]


def getUserBy_id(id: int):
    for user in users:
        print(type(user))
        if user.get("id") == id:
            return user
        else :
            return None


def del_user(id):
    for user in users:
        if user.get("id") == id:
            users.remove(user)


app = FastAPI()


@app.get("/")
def home():
    return {"Message": "Hello wordl"}


@app.get("/posts")
def get_users():
    return {"users": users}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post_user(data: Post_Model):
    data_dict = data.dict()
    data_dict["id"] = randrange(0, 1000000)
    users.append(data_dict)
    return {"message": "New User Added successfylu"}




@app.get("/posts/{id}")
def getUserById(id: int):
    user = getUserBy_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"user": user}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usre(id: int):
    if not getUserBy_id(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del_user(id)


@app.put("/posts/{id}")
def update_user(id: int, data: Post_Model):
    user = getUserBy_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for user in users:
        if 'id' in user and user['id'] == id:
            index = users.index(user)
            users[index] = data.dict()
    return {"message" : "user Successfully Updated"}