from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.manufacturers import router as manufacturers_router
from app.api.robots import router as robots_router
from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Humanoid Core API",
    version="0.1.0",
    description="Structured API and importer for humanoid robotics data.",
    lifespan=lifespan,
)

app.include_router(robots_router)
app.include_router(manufacturers_router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Humanoid Core API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
