import sys
import subprocess
from sqlalchemy import text
from app.db.database import engine

def get_schemas(target_schemas=None):
    """
    If target_schemas is provided (list), return it.
    Otherwise, fetch all from the DB.
    """
    if target_schemas:
        return target_schemas
        
    with engine.connect() as conn:
        # pick out only the schema names from the organizations table
        result = conn.execute(text("SELECT schema_name FROM public.organizations"))
        return [row[0] for row in result]

def run_upgrade(schema_name):
    print(f"--- Upgrading: {schema_name} ---")
    # Using -x to pass variables into env.py
    command = ["alembic", "-x", "tenant=true", "-x", f"schema={schema_name}", "upgrade", "head"]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    # Check if user passed specific schemas: python3 run_tenant_migrations.py tenant_a tenant_b
    user_args = sys.argv[1:] 
    
    targets = get_schemas(user_args if user_args else None)
    
    for schema in targets:
        try:
            run_upgrade(schema)
        except Exception as e:
            print(f"Failed on {schema}: {e}")