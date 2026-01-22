from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    age: int

@app.get("/")
def index():
    return {"data": {"firstName": "Young"}}

@app.get("/about")
def about():
    return {"data": "This is the about page."}


# path parameter
@app.get("/about/{id}")
def show(id: int) -> dict[str, str | int]:
    return {"data": "Let's work with id: {id}".format(id=id),
            "data2": id}


# query parameter
@app.get("/blog")
def params(limit: int = 5, published: bool = False) -> dict[str, str]:
    if published:
        return {"data": f"All published blogs with limit: {limit}"}
    else:   
        return {"data": f"All blogs with limit: {limit}"}
    

@app.post("/signup")
def userinfo(user: User):
    return f"The user is {user.username}, age is {user.age}"