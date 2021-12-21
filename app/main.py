from fastapi import FastAPI, Depends
from typing import Optional
import graphql
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
graphql_app = GraphQLRouter(schemas.schema)
app.include_router(graphql_app, prefix="/graphql")

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
async def wgewgages(db: Session = Depends(get_db)):
    """Get all raingages.
    """
    
    data = crud.get_wgew_raingages(db)
    return {"data": data}

@app.get("/api/v1/wgewgages/{wsid}/{gageid}")
async def wgewgages(wsid: int, gageid: int, db: Session = Depends(get_db)):
    """Get a raingage by watershed id and raingage id.
    """

    data = crud.get_wgew_watershed_raingage(db, wsid, gageid)
    return {"data": data}

@app.get("/api/v1/wgewprecip/{wsid}/{gageid}")
async def wgewprecip(wsid: int, gageid: int, db: Session = Depends(get_db)):
    """Retrieves the specified watershed and raingage precip events.
    """

    data = crud.get_wgew_watershed_gage_precip(db, wsid, gageid)
    return {"data": data}