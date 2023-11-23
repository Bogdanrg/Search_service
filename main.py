from fastapi import FastAPI
from config import settings
from core.es import AsyncElasticClient
from search_service.producer import AIOProducer
from api.api_routes import api_router


app = FastAPI(title=settings.app.TITLE)


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


app.include_router(api_router)
