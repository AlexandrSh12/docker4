from fastapi import APIRouter, status, Response, Path, Depends, HTTPException
from typing import Union, List, Dict
from app.schemas.default_response import DefaultResponse
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
import json

from app.schemas.product import Product as ProductScehma, CreateProduct

router = APIRouter(
    prefix="/api", 
    tags=["products"]
)

store: Dict[int, ProductScehma] = {}

@router.post("/products")
def create_product(product: CreateProduct):
    product.id = len(store) + 1

    store[product.id] = product

    return JSONResponse(
        content={"id": product.id},
        status_code=status.HTTP_201_CREATED
    )

@router.get("/products/{id}")
def get_product(id: int):
    if id not in store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    return jsonable_encoder(store[id])

@router.get("/products_download")
def products_download():
    products = list(store.values())

    with open("products.json", "w") as f:
        json.dump(jsonable_encoder(products), f, indent=4)

    return FileResponse(
        "products.json",
        content_disposition_type="attachment",
        filename="all_products.json"
    )