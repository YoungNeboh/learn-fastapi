from fastapi import FastAPI, Response, HTTPException
from models import Product

app = FastAPI()


ALBUMS = [
    {"id": 1, "name": "Hit Me Hard and Soft", "artist": "Billie Eilish", "genre": "Alternative"},
    {"id": 2, "name": "Essex Honey", "artist": "Blood Orange", "genre": "Alternative"},
    {"id": 3, "name": "Bicoastal", "artist": "Bathe", "genre": "R&B/Soul"},
    {"id": 4, "name": "It'll Be Fine", "artist": "Chase Shakur", "genre": "R&B/Soul"},
    {"id": 5, "name": "Blonde", "artist": "Frank Ocean", "genre": "Pop"},
]

products = [
        Product(id=1, desc="The fastest iPhone on the market", price=1399.99, quantity=200),
        Product(id=2, desc="Exceed your limits with the S25 Ultra", price=1299.99, quantity=780),
        Product(id=3, desc="Harness the power of the M4 on your lap", price=999.99, quantity=1000),
        Product(id=4, desc="Never miss a moment with the Meta Glasses", price=349.99, quantity=65),
        Product(id=5, desc="Let the GoPro Hero13 take you beyond your dreams", price=369.99, quantity=420)
    ]

# Just to eliminate the constant favicon errors in the logs
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) # 204 means "No Content"


# query parameter
@app.get("/blog")
def params(limit: int = 5, published: bool = False) -> dict[str, str]:
    if published:
        return {"data": f"All published blogs with limit: {limit}"}
    else:   
        return {"data": f"All blogs with limit: {limit}"}
    


@app.get("/albums/{album_id}")
def album(album_id: int) -> dict:
    album = next((album for album in ALBUMS if album["id"] == album_id), None)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@app.get("/albums/genre/{album_genre}")
def albums_by_genre(album_genre: str):
    albums = [album for album in ALBUMS if album["genre"].lower() == album_genre.lower()]
    return albums

@app.get("/products")
def all_products() -> list:
    return products

@app.get("/products/{product_id}")
async def product_by_id(product_id: int):
    product = next((prod for prod in products if prod.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="ID does not exist")
    return product


@app.post("/products")
async def create_product(product: Product):
    products.append(product)
    return product


@app.put("/products")
async def update_product(id: int, product: Product):
    for index, existing_prod in enumerate(products):
        if existing_prod.id == id:
            products[index] = product
            return product
        
    raise HTTPException(status_code=404, detail="ID does not exist")


@app.delete("/products")
async def remove_product(id: int):
    product = next((prod for prod in products if prod.id == id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="ID does not exist")
    
    products.remove(product)
    return {"message": "Item Removed Successfully"}



