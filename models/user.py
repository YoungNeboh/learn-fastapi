from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from .constants import Memberships # not in the type_checking block because it's required at runtime for the link_model

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .shopping import CartItems
    from .organization import Organization

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str

    memberships: list["Memberships"] = Relationship(back_populates="user")
    cart_items: list["CartItems"] = Relationship(back_populates="user")
    organizations: list["Organization"] = Relationship(back_populates="users", link_model=Memberships)


