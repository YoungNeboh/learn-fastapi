from fastapi import FastAPI, Response
from database import engine
from sqlmodel import Session


app = FastAPI()


# Just to eliminate the constant favicon errors in the logs
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) # 204 means "No Content"


