from pydantic import BaseModel

class Product(BaseModel):
    id: int
    desc: str
    price: float
    quantity: int
