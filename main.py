from fastapi import FastAPI
from config import app_settings
from core.es import AsyncElasticClient
from api.v1.search_routes import search_router

app = FastAPI(title=app_settings.APP_TITLE)


@app.on_event("startup")
async def app_startup():
    client = AsyncElasticClient()
    await client.init()


@app.on_event("shutdown")
async def app_shutdown():
    client = AsyncElasticClient()
    await client.shutdown()


app.include_router(search_router)
