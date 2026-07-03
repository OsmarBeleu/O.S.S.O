from fastapi import FastAPI
from app.api.v1.routes import auth

app = FastAPI(title="OSSO API")

app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "OSSO API rodando"}
