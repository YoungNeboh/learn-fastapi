from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
import sqlalchemy as sa
from .base import MultiTenantBase
# from .constants import Memberships # not in the type_checking block because it's required at runtime for the link_model
from .constants import UserRole

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .shopping import CartItems
    # from .organization import Organization

class User(MultiTenantBase, table=True):
    __tablename__ = "user"

    name: str
    email: str = Field(index=True)
    hashed_password: str
    # make sure PostGreSQL doesn't try to create a native enum type. Let Python handle the enum instead
    role: UserRole = Field(sa_column=sa.Column(sa.Enum(UserRole, native_enum=False)))
    is_active: bool = Field(default=True)

    # memberships: list["Memberships"] = Relationship(back_populates="user")
    cart_items: list["CartItems"] = Relationship(back_populates="user")
    # organizations: list["Organization"] = Relationship(back_populates="users", link_model=Memberships)


