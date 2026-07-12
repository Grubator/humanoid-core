from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Country(Base):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    iso_code: Mapped[str | None] = mapped_column(String(3), unique=True, nullable=True)
    region: Mapped[str | None] = mapped_column(String(120), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    manufacturers: Mapped[list["Manufacturer"]] = relationship(back_populates="country")
    robots: Mapped[list["Robot"]] = relationship(back_populates="country")
