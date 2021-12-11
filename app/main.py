from fastapi import FastAPI
from typing import Optional
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/healthcheck")
async def health_check():
    msg = "ok"
    return {"msg": msg}

@app.get("/api/v1/wgewgages/")
async def wgewgages():
    """Get all raingages."""

    data = [
        {"wsid": 1, "gageid": 1},
        {"wsid": 2, "gageid": 2}

    ]
    return {"data": data}

@app.get("/api/v1/wgewgages/{wsid}/{gageid}")
async def wgewgages(wsid: int, gageid: int):
    """Get a raingage by watershed id and raingage id.
    """
    data = {"wsid": 1, "gageid": 1}
    return {"payload": data}

@app.get("/api/v1/wgewprecip/{wsid}/{gageid}")
async def wgewprecip(wsid: int, gageid: int):
    """Retrieves the specified watershed and raingage precip events.
    """

    data = []
    return {"data": data}