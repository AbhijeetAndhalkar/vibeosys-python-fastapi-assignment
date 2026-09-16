from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Category(str, Enum):
    FINISHED = "finished"
    SEMI_FINISHED = "semi-finished"
    RAW = "raw"


class UnitOfMeasure(str, Enum):
    MTR = "mtr"
    MM = "mm"
    LTR = "ltr"
    ML = "ml"
    CM = "cm"
    MG = "mg"
    GM = "gm"
    UNIT = "unit"
    PACK = "pack"


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=100)
    category: Category
    description: str | None = Field(default=None, max_length=250)
    product_image: str | None = None
    sku: str = Field(..., max_length=100)
    unit_of_measure: UnitOfMeasure
    lead_time: int = Field(..., ge=0)


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=100)
    category: Category | None = None
    description: str | None = Field(default=None, max_length=250)
    product_image: str | None = None
    sku: str | None = Field(default=None, max_length=100)
    unit_of_measure: UnitOfMeasure | None = None
    lead_time: int | None = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    name: str
    category: Category
    description: str | None
    product_image: str | None
    sku: str
    unit_of_measure: UnitOfMeasure
    lead_time: int
    created_date: datetime
    updated_date: datetime