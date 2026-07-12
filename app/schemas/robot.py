from pydantic import BaseModel, ConfigDict, Field
from app.schemas.country import CountryRead
from app.schemas.manufacturer import ManufacturerRead

class RobotImport(BaseModel):
    key: str
    name: str
    manufacturer: str
    country: str | None = None
    country_iso: str | None = None
    status: str | None = None
    introduced_year: int | None = None
    height_mm: int | None = None
    weight_kg: float | None = None
    payload_kg: float | None = None
    speed_mps: float | None = None
    dof: int | None = None
    runtime_minutes: int | None = None
    battery_type: str | None = None
    charging_time_minutes: int | None = None
    mobility_maturity: int | None = Field(default=None, ge=1, le=5)
    manipulation_maturity: int | None = Field(default=None, ge=1, le=5)
    ai_autonomy: int | None = Field(default=None, ge=1, le=5)
    commercial_readiness: int | None = Field(default=None, ge=1, le=5)
    developer_friendliness: int | None = Field(default=None, ge=1, le=5)
    deployment_readiness: int | None = Field(default=None, ge=1, le=5)
    description: str | None = None
    manufacturer_website: str | None = None
    manufacturer_description: str | None = None

class RobotRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    key: str
    name: str
    slug: str
    status: str | None = None
    introduced_year: int | None = None
    height_mm: int | None = None
    weight_kg: float | None = None
    payload_kg: float | None = None
    speed_mps: float | None = None
    dof: int | None = None
    runtime_minutes: int | None = None
    battery_type: str | None = None
    charging_time_minutes: int | None = None
    mobility_maturity: int | None = None
    manipulation_maturity: int | None = None
    ai_autonomy: int | None = None
    commercial_readiness: int | None = None
    developer_friendliness: int | None = None
    deployment_readiness: int | None = None
    description: str | None = None
    manufacturer: ManufacturerRead
    country: CountryRead | None = None
