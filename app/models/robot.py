from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Robot(Base):
    __tablename__ = "robots"
    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(180), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(180), index=True)
    slug: Mapped[str] = mapped_column(String(180), unique=True, index=True)
    status: Mapped[str | None] = mapped_column(String(120), nullable=True)
    introduced_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    height_mm: Mapped[int | None] = mapped_column(Integer, nullable=True)
    weight_kg: Mapped[float | None] = mapped_column(Float, nullable=True)
    payload_kg: Mapped[float | None] = mapped_column(Float, nullable=True)
    speed_mps: Mapped[float | None] = mapped_column(Float, nullable=True)
    dof: Mapped[int | None] = mapped_column(Integer, nullable=True)
    runtime_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    battery_type: Mapped[str | None] = mapped_column(String(180), nullable=True)
    charging_time_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    mobility_maturity: Mapped[int | None] = mapped_column(Integer, nullable=True)
    manipulation_maturity: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ai_autonomy: Mapped[int | None] = mapped_column(Integer, nullable=True)
    commercial_readiness: Mapped[int | None] = mapped_column(Integer, nullable=True)
    developer_friendliness: Mapped[int | None] = mapped_column(Integer, nullable=True)
    deployment_readiness: Mapped[int | None] = mapped_column(Integer, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id", ondelete="RESTRICT"))
    country_id: Mapped[int | None] = mapped_column(ForeignKey("countries.id", ondelete="SET NULL"), nullable=True)
    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="robots")
    country: Mapped["Country | None"] = relationship(back_populates="robots")
