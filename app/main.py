import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from config.config import settings
from routes import api_router

app = FastAPI(
    title="Modara API",
    description="API para a plataforma de consulta de vestimentas e acessórios Modara.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Modara API"}

print("DATABASE_URL carregada:", settings.DATABASE_URL)

@app.on_event("startup")
async def startup_event():
    retries = 10
    for i in range(retries):
        try:
            await Tortoise.init(
                db_url=settings.DATABASE_URL,
                modules={"models": ["models.models"]}
            )
            await Tortoise.generate_schemas()
            return
        except Exception as e:
            await asyncio.sleep(5)
    raise Exception("Não foi possível conectar ao banco.")

@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()
