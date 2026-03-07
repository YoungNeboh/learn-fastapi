from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from sqlalchemy import MetaData

# create an isolated metadata instance for all models that inherit from MultiTenantBase
# this prevents clashes with the default metadata used by the public schema 
tenant_metadata = MetaData()

class MultiTenantBase(SQLModel):
    metadata = tenant_metadata
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    # 'foreign_key=organization.id' ensures every record belongs to an organization
    # org_id: UUID = Field(foreign_key="organization.id", index=True)
