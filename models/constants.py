from enum import Enum
from uuid import UUID
from sqlmodel import Field, Relationship
from .base import MultiTenantBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"

class Memberships(MultiTenantBase, table=True):
    __tablename__ = "memberships"

    user_id: UUID = Field(foreign_key="user.id", primary_key=True, index=True)
    org_id: UUID = Field(foreign_key="organization.id", primary_key=True, index=True)
    role: UserRole = Field(default=UserRole.CUSTOMER)
    
    user: "User" = Relationship(back_populates="memberships")