from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ProductCreate, ProductResponse, ProductUpdate
from app.crud import (
    create_product,
    get_products,
    get_product,
    update_product
)

router = APIRouter()


@router.post("/product/add", response_model=ProductResponse)
def add_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(db, product_data)


@router.get("/product/list", response_model=list[ProductResponse])
def list_products(
    page: int = 1,
    db: Session = Depends(get_db)
):
    if page < 1:
        raise HTTPException(
            status_code=400,
            detail="Page must be greater than 0"
        )

    return get_products(db, page)


@router.get("/product/{product_id}/info", response_model=ProductResponse)
def product_info(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put("/product/{product_id}/update", response_model=ProductResponse)
def update_product_info(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return update_product(db, product, product_data)