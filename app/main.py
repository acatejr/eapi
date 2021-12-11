from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/healthcheck")
async def health_check():
    msg = "ok" 
    return {"msg": msg}

@app.get("/api/v1/gages/")
async def gages():
    """Get all raingages."""

    payload = [
        {"wsid": 1, "gageid": 1},
        {"wsid": 2, "gageid": 2}

    ]
    return {"payload": payload}

@app.get("/api/v1/gages/{wsid}/{gageid}")
async def gages(wsid: int, gageid: int):
    """Get a raingage by watershed id and raingage id.
    """
    payload = {"wsid": 1, "gageid": 1}
    return {"payload": payload}
