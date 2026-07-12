import json, re
from pathlib import Path
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.country import Country
from app.models.manufacturer import Manufacturer
from app.models.robot import Robot
from app.schemas.robot import RobotImport

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")

def import_robot_file(db: Session, file_path: Path) -> Robot:
    data = RobotImport.model_validate(json.loads(file_path.read_text(encoding="utf-8")))
    country = None
    if data.country:
        country = db.scalar(select(Country).where(Country.name == data.country))
        if country is None:
            country = Country(name=data.country, iso_code=data.country_iso)
            db.add(country); db.flush()
    manufacturer = db.scalar(select(Manufacturer).where(Manufacturer.name == data.manufacturer))
    if manufacturer is None:
        manufacturer = Manufacturer(name=data.manufacturer, slug=slugify(data.manufacturer), website=data.manufacturer_website, description=data.manufacturer_description, country=country)
        db.add(manufacturer); db.flush()
    robot = db.scalar(select(Robot).where(Robot.key == data.key))
    if robot is None:
        robot = Robot(key=data.key, name=data.name, slug=slugify(data.name), manufacturer=manufacturer, country=country)
        db.add(robot)
    robot.name = data.name; robot.slug = slugify(data.name); robot.manufacturer = manufacturer; robot.country = country
    for f in ("status","introduced_year","height_mm","weight_kg","payload_kg","speed_mps","dof","runtime_minutes","battery_type","charging_time_minutes","mobility_maturity","manipulation_maturity","ai_autonomy","commercial_readiness","developer_friendliness","deployment_readiness","description"):
        setattr(robot, f, getattr(data, f))
    db.commit(); db.refresh(robot); return robot
