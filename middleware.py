from fastapi import Request, HTTPException
from sqlalchemy import text
from .database import SessionLocal
from .models import Organization


async def organization_schema_middleware(request: Request, call_next):
    
    # get the subdomain from the header object
    host = request.headers.get("host", "")
    subdomain = host.split(".")[0]


    with SessionLocal() as session:
        # in the public domain(Organization), find the organization associated with the subdomain
        organization = session.query(Organization).filter(Organization.subdomain == subdomain).first()

        if not organization:
            raise HTTPException(status_code=404, detail="Store not found")
        
        # set our search_path to the schema associated with the organization
        session.execute(text(f"SET search_path TO {organization.schema_name}, public"))

        '''
        attach the schema name to the request.state object so that we can access it
          in our route handlers (endpoints) without re-querying the database to verify 
          the schema every time for the duration of the request.
        '''
        request.state.schema_name = organization.schema_name

        response = await call_next(request)
        return response
        