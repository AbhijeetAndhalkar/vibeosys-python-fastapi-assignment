from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


def create_product(db: Session, product_data: ProductCreate):
    product = Product(
        name=product_data.name,
        category=product_data.category.value,
        description=product_data.description,
        product_image=product_data.product_image,
        sku=product_data.sku,
        unit_of_measure=product_data.unit_of_measure.value,
        lead_time=product_data.lead_time
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_products(db: Session, page: int):
    skip = (page - 1) * 10

    statement = (
        select(Product)
        .offset(skip)
        .limit(10)
    )

    return db.scalars(statement).all()


def get_product(db: Session, product_id: int):
    statement = select(Product).where(
        Product.product_id == product_id
    )

    return db.scalar(statement)


def update_product(
    db: Session,
    product: Product,
    product_data: ProductUpdate
):
    update_data = product_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        if hasattr(value, "value"):
            value = value.value

        setattr(product, field, value)

    product.updated_date = datetime.utcnow()

    db.commit()
    db.refresh(product)

    return product