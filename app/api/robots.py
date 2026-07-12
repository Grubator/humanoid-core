from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.core.database import get_db
from app.models.robot import Robot
from app.schemas.robot import RobotRead
from app.services.importer import import_robot_file
router = APIRouter(prefix="/robots", tags=["robots"])
@router.get("", response_model=list[RobotRead])
def list_robots(db: Session = Depends(get_db)) -> list[Robot]:
    q=select(Robot).options(selectinload(Robot.manufacturer),selectinload(Robot.country)).order_by(Robot.name)
    return list(db.scalars(q).all())
@router.get("/{robot_key}", response_model=RobotRead)
def get_robot(robot_key: str, db: Session = Depends(get_db)) -> Robot:
    q=select(Robot).where(Robot.key==robot_key).options(selectinload(Robot.manufacturer),selectinload(Robot.country))
    robot=db.scalar(q)
    if robot is None: raise HTTPException(status_code=404, detail="Robot not found")
    return robot
@router.post("/import/sample", response_model=RobotRead)
def import_sample(db: Session = Depends(get_db)) -> Robot:
    p=Path("data/robots/optimus.json")
    if not p.exists(): raise HTTPException(status_code=500, detail="Sample file is missing")
    return import_robot_file(db,p)
