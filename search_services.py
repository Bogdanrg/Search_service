from constants import PHONES_INDEX, FOOD_INDEX
from schemas import PhoneModel, FoodModel
from elasticsearch import AsyncElasticsearch


class SearchService:

    @staticmethod
    async def add_phone(es: AsyncElasticsearch, document: PhoneModel) -> dict:
        response = await es.index(index=PHONES_INDEX, document=document.model_dump())
        return response['result']

    @staticmethod
    async def add_food(es: AsyncElasticsearch, document: FoodModel) -> dict:
        response = await es.index(index=FOOD_INDEX, document=document.model_dump())
        return response['result']
