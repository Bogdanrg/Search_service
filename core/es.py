from typing import AsyncGenerator
from elasticsearch import AsyncElasticsearch
from config import settings
from mappings import food_mapping, phones_mapping
from constants import FOOD_INDEX, PHONES_INDEX


class AsyncElasticClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        if self._instance is None:
            self._es: None | AsyncElasticClient = None

    async def init(self) -> None:
        self._es = AsyncElasticsearch(
            [
                {'host': settings.es.HOST, 'port': settings.es.PORT, "scheme": settings.es.SCHEME},
            ]
        )
        if not await self._es.indices.exists(index=[FOOD_INDEX, PHONES_INDEX]):
            await self._es.indices.create(index=PHONES_INDEX, body=phones_mapping)
            await self._es.indices.create(index=FOOD_INDEX, body=food_mapping)

    async def shutdown(self) -> None:
        await self._es.close()

    @property
    def es(self) -> AsyncElasticsearch:
        return self._es


async def get_es() -> AsyncGenerator[AsyncElasticsearch, None]:
    client = AsyncElasticClient()
    yield client.es
