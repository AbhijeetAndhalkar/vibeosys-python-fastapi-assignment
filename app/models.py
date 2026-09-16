from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        Enum("finished", "semi-finished", "raw"),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(250),
        nullable=True
    )

    product_image: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    unit_of_measure: Mapped[str] = mapped_column(
        Enum(
            "mtr",
            "mm",
            "ltr",
            "ml",
            "cm",
            "mg",
            "gm",
            "unit",
            "pack"
        ),
        nullable=False
    )

    lead_time: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    created_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )