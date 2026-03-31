from uuid import UUID
from sqlmodel import Field, Relationship
from app.models.tenant.base import MultiTenantBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

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

    user: "User" = Relationship(back_populates="cart_items")
