from sqlmodel import Field, SQLModel, select

# 1. Define your model
class Product(SQLModel, table=True):

    __tablename__ = 'products'

    id: int | None = Field(default=None, primary_key=True, index=True)
    desc: str
    price: float
    quantity: int | None = None

