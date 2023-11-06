from fastapi import FastAPI
from config import app_settings
from core.es import client
from search_routes import search_router

app = FastAPI(title=app_settings.APP_TITLE)


@app.on_event("startup")
async def app_startup():
    await client.init()


@app.on_event("shutdown")
async def app_shutdown():
    await client.es.close()


app.include_router(search_router)
