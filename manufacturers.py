from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.core.database import get_db
from app.models.manufacturer import Manufacturer
from app.schemas.manufacturer import ManufacturerRead
router=APIRouter(prefix="/manufacturers", tags=["manufacturers"])
@router.get("", response_model=list[ManufacturerRead])
def list_manufacturers(db: Session = Depends(get_db)) -> list[Manufacturer]:
    q=select(Manufacturer).options(selectinload(Manufacturer.country)).order_by(Manufacturer.name)
    return list(db.scalars(q).all())
