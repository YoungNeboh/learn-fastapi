from typing import Optional, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
# from .constants import Memberships # not in the type_checking block because it's required at runtime for the link_model

if TYPE_CHECKING:
    from .user import User

class Organization(SQLModel, table=True):
    __tablename__ = "organization"
    __table_args__ = {"schema": "public"}

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    subdomain: str = Field(index=True, unique=True)
    schema_name: str = Field(unique=True)

    # users: list["User"] = Relationship(back_populates="organizations", link_model=Memberships)
