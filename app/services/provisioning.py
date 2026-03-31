from app.db.database import SessionLocal, engine
from sqlalchemy import text

# the shared "isolated" metadata instance all tenant tables inherit from
from app.models.tenant.base import organization_metadata

# import all tables that will be created so they are registered in the tenant_metadata
import app.models


def provision_organization(name: str, subdomain: str, schema_name: str):
    with SessionLocal() as session:
        # create the schema for the new organization
        session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
        session.commit()

        # new row detailing the new Organization in the public schema and its associated schema
        new_org = app.models.Organization(name=name, subdomain=subdomain, schema_name=schema_name)
        session.add(new_org)

        tables_to_create = []
        ''' go into the metadata and assign the new schema to all tables that don't already have 
        a schema (i.e. the public schema) and add them to a list of tables to create 
        for this organization'''
        for table in organization_metadata.tables.values():
            # 'table' is an object in the metadata with 'schema' as one of its attributes
            if table.schema is None:    
                table.schema = schema_name
                tables_to_create.append(table)
        
        organization_metadata.create_all(engine, tables=tables_to_create)

        ''' set the schema back to None for all tables in the metadata so that 
        they can be reused for future organizations without being tied to a specific schema'''
        for table in tables_to_create:
            table.schema = None

        session.commit()
        print(f"Successfully created schema for {name}")



