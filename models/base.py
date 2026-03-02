from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field


class MultiTenantBase(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    # 'foreign_key=organization.id' ensures every record belongs to an organization
    org_id: UUID = Field(foreign_key="organization.id", index=True)
