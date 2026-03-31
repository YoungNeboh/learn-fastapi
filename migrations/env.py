from logging.config import fileConfig

from sqlalchemy import engine_from_config, text
from sqlalchemy import pool

from alembic import context

# from sqlmodel import SQLModel
from app.db.base import SQLModel, MultiTenantBase



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    # Check if we are targeting a tenant or the public schema
    # Usage: alembic -x tenant=true upgrade head
    args = context.get_x_argument(as_dictionary=True)
    is_tenant = args.get("tenant") == "true"
    # Get the specific schema name passed from our loop script
    schema_name = args.get("schema", "public") 

    # Select the correct metadata and target schema based on the context
    if is_tenant:
        target_metadata = MultiTenantBase.metadata
    else:
        target_metadata = SQLModel.metadata

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # 4. Tell Alembic to look ONLY at this schema
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # IMPORTANT: This tells Alembic which schema to "look" at
            version_table_schema=schema_name, # Keeps migration history isolated on a per-schema basis
            include_schemas=True,            
        )

        # This forces all 'CREATE TABLE' statements to include the schema prefix
        connection.execute(text(f"SET search_path TO {schema_name}"))

        with context.begin_transaction():
            context.run_migrations()

# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.

#     """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
