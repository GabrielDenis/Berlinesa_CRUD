from datetime import datetime
from pydantic import BaseModel

class ProductRequestModel(BaseModel):
    id: str
    sku: str
    description: str
    url_img: str
    created_at: datetime
    price: float
    name: str

class ProductResponseModel(ProductRequestModel):
    id: str
    sku: str
    description: str
    url_img: str
    created_at: datetime
    price: float
    name: str