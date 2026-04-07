from fastapi import FastAPI, Response, Depends
from sqlalchemy.orm import Session
from starlette.middleware.base import BaseHTTPMiddleware

from app.db.session import engine, get_db
from app.core.middleware import organization_schema_middleware

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=organization_schema_middleware)


# Just to eliminate the constant favicon errors in the logs
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) # 204 means "No Content"


