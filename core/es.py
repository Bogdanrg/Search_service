from typing import AsyncGenerator
from elasticsearch import AsyncElasticsearch
from config import app_settings
from mappings import food_mapping, phones_mapping
from constants import FOOD_INDEX, PHONES_INDEX


class AsyncElasticClient:

    def __init__(self) -> None:
        self.es: None | AsyncElasticClient = None

    async def init(self) -> None:
        self.es = AsyncElasticsearch(
            [
                {'host': app_settings.ES_HOST, 'port': app_settings.ES_PORT, "scheme": "http"},
            ]
        )
        if not await self.es.indices.exists(index=[FOOD_INDEX, PHONES_INDEX]):
            await self.es.indices.create(index=PHONES_INDEX, body=phones_mapping)
            await self.es.indices.create(index=FOOD_INDEX, body=food_mapping)


client = AsyncElasticClient()


async def get_es() -> AsyncGenerator[client.es, None]:
    yield client.es
