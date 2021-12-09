from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def health_check():
    msg = None
    return {
        "msg": msg
    }

