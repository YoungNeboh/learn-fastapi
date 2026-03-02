from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from .base import MultiTenantBase
from .shopping import CartItems
from .constants import UserRole
from .organization import Organization

class UserOrgLink(SQLModel, table=True):
    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    org_id: UUID = Field(foreign_key="organization.id", primary_key=True)

class Memberships(MultiTenantBase, table=True):
    __tablename__ = "memberships"

    user_id: UUID = Field(foreign_key="user.id", primary_key=True, index=True)
    org_id: UUID = Field(foreign_key="organization.id", primary_key=True, index=True)
    role: UserRole = Field(default=UserRole.CUSTOMER)
    
    user: "User" = Relationship(back_populates="memberships")

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str

    memberships: list["Memberships"] = Relationship(back_populates="user")
    cart_items: list["CartItems"] = Relationship(back_populates="user")
    organizations: list["Organization"] = Relationship(back_populates="users", link_model=Memberships)


