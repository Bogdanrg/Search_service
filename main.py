from fastapi import FastAPI
from config import app_settings
from core.es import AsyncElasticClient
from api.v1.search_routes import search_router
from search_service.producer import AIOProducer

app = FastAPI(title=app_settings.APP_TITLE)


@app.on_event("startup")
async def app_startup():
    producer = AIOProducer()
    client = AsyncElasticClient()
    await client.init()
    await producer.init_producer()
    await producer.start()


@app.on_event("shutdown")
async def app_shutdown():
    producer = AIOProducer()
    client = AsyncElasticClient()
    await client.shutdown()
    await producer.stop()


app.include_router(search_router)
