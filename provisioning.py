from database import engine
from sqlmodel import SQLModel, Session
from sqlalchemy import text
from models import Organization, User, Memberships, UserRole, Products, CartItems, MultiTenantBase


def provision_organization(name: str, subdomain: str, schema_name: str):
    with Session(engine) as session:
        # create the schema for the new organization
        session.exec(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))

        # new row detailing the new Organization in the public schema and its associated schema
        new_org = Organization(name=name, subdomain=subdomain, schema_name=schema_name)
        session.add(new_org)

        tables_to_create = []
        ''' go into the metadata and assign the new schema to all tables that don't already have 
        a schema (i.e. the public schema) and add them to a list of tables to create 
        for this organization'''
        for table_name, table in SQLModel.metadata.tables.items():
            # 'table' is an object in the metadata with 'schema' as one of its attributes
            if table.schema is None:    
                table.schema = schema_name
                tables_to_create.append(table)
        
        SQLModel.metadata.create_all(engine, tables=tables_to_create)

        ''' set the schema back to None for all tables in the metadata so that 
        they can be reused for future organizations without being tied to a specific schema'''
        for table_name, table in SQLModel.metadata.tables.items():
            table.schema = None

        session.commit()
        print(f"Successfully created schema for {name}")



