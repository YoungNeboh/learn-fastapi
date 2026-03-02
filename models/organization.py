from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from.user import User, Memberships


class Organization(SQLModel, table=True):
    __tablename__ = "organization"

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    # I don't need "back_populates' here because I only need to view all the users associated 
    users: list["User"] = Relationship(back_populates="organizations", link_model=Memberships)
