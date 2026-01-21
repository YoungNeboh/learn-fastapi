from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data": {"firstName": "Young"}}

@app.get("/about")
def about():
    return {"data": "This is the about page."}