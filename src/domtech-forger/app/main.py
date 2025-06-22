from fastapi import FastAPI
from app.api.api import api_router
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PoliticaMente API",
    description="Backend para a plataforma PoliticaMente.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do PoliticaMente"}