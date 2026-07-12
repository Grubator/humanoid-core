# Humanoid Core

Python backend for the Humanoid Intelligence robotics database.

## Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

Use `POST /robots/import/sample`, then `GET /robots`.
