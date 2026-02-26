from typing import Optional
from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship


class MultiTenantBase(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    # 'foreign_key=organization.id' ensures every record belongs to an organization
    org_id: UUID = Field(foreign_key="organization.id", index=True)

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str

    memberships: list["Memberships"] = Relationship(back_populates="user")
    cart_items: list["CartItems"] = Relationship(back_populates="user")

class Organization(SQLModel, table=True):
    __tablename__ = "organization"

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"

class Memberships(MultiTenantBase, table=True):
    __tablename__ = "memberships"

    user_id: UUID = Field(foreign_key="user.id", index=True)
    role: UserRole = Field(default=UserRole.CUSTOMER)
    user: "User" = Relationship(back_populates="memberships")

class Products(MultiTenantBase, table=True):
    __tablename__ = "products"

    name: str
    price: float
    quantity: int

class CartItems(MultiTenantBase, table=True):
    __tablename__ = "cartitems"

    user_id: UUID = Field(foreign_key="user.id", index=True)
    product_id: UUID = Field(foreign_key="products.id", index=True)
    quantity: int

    user: User = Relationship(back_populates="cart_items")

