from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data": {"firstName": "Young"}}

@app.get("/about")
def about():
    return {"data": "This is the about page."}

@app.get("/about/{id}")
def show(id: int):
    return {"data": "Let's work with id: {id}".format(id=id),
            "data2": id}
