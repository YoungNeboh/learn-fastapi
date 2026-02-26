from fastapi import FastAPI, Response, HTTPException
# from pydantic_models import Product
from database import engine
from sqlmodel import Session
from sql_models import Product


app = FastAPI()

def create_product():
    products = [Product(desc="Exceed your limits with the S25 Ultra", price=1299.99, quantity=780), 
                Product(desc="Harness the power of the M4 on your lap", price=999.99, quantity=1000), 
                Product(desc="Never miss a moment with the Meta Glasses", price=349.99, quantity=65), 
                Product(desc="Let the GoPro Hero13 take you beyond your dreams", price=369.99, quantity=420) 
                ]
   
    
    with Session(engine) as session:
        try:
            session.add_all(products) # Cleaner than a manual loop
            session.commit()
            for product in products:
                session.refresh(product)
                print(f"Created product: {product.id}")
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    create_product()




# Just to eliminate the constant favicon errors in the logs
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) # 204 means "No Content"

