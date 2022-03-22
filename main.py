from fastapi import FastAPI
from fastapi import HTTPException

from database import database as connection
from database import Product

from schemas import *

app = FastAPI(
    title='FastApi de la pagina web Berlinesa.com',
    description='Una API Rest',
    version='0,1'
)

@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([Product])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get("/")
async def index():
    return 'Hola Mundo'

@app.post('/products')
async def create_products(product_request: ProductRequestModel):
    product = Product.create(
        id=product_request.id,
        sku=product_request.sku,
        description=product_request.description,
        url_img=product_request.url_img,
        created_at=product_request.created_at,
        price=product_request.price,
        name=product_request.name
    )
    return product_request

@app.get('/products/{products_id}')
async def get_product(products_id):
    product = Product.select().where(Product.id == products_id).first()

    if product:
        return ProductResponseModel(
            id=product.id,
            sku=product.sku,
            description=product.description,
            url_img=product.url_img,
            created_at=product.created_at,
            price=product.price,
            name=product.name
            )

    else:
        return HTTPException(404, 'Product not found')

@app.delete('/products/{products_id}')
async def delete_product(products_id):
    product = Product.select().where(Product.id == products_id).first()

    if product:
        product.delete_instance()
        return True

    else:
        return HTTPException(404, 'Product not found')

@app.put('/products/{products_id}')
async def update_product(products_id, product_request: ProductRequestModel):
    product = Product.select().where(Product.id == products_id).first()

    if product:

        product = Product.update(
            id=product_request.id,
            sku=product_request.sku,
            description=product_request.description,
            url_img=product_request.url_img,
            created_at=product_request.created_at,
            price=product_request.price,
            name=product_request.name,
        )

    return product_request