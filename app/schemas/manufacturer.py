from pydantic import BaseModel, ConfigDict
from app.schemas.country import CountryRead
class ManufacturerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    slug: str
    founded_year: int | None = None
    website: str | None = None
    description: str | None = None
    country: CountryRead | None = None
