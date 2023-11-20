from constants import PHONES_INDEX, FOOD_INDEX
from schemas import PhoneModel, FoodModel
from elasticsearch import AsyncElasticsearch
from search_service.producer import AIOProducer


class SearchService:

    @staticmethod
    async def add_phone(es: AsyncElasticsearch, document: PhoneModel) -> dict:
        response = await es.index(index=PHONES_INDEX,
                                  document=document.model_dump(exclude={'id'}),
                                  id=document.id)
        producer = AIOProducer()
        message = document.model_dump()
        message['action'] = 'add_phone'
        await producer.send_data(message)
        return response['result']

    @staticmethod
    async def add_food(es: AsyncElasticsearch, document: FoodModel) -> dict:
        response = await es.index(index=FOOD_INDEX,
                                  document=document.model_dump(exclude={'id'}),
                                  id=document.id)
        producer = AIOProducer()
        message = document.model_dump()
        message['action'] = 'add_food'
        await producer.send_data(message)
        return response['result']

    @staticmethod
    async def get_phone(es: AsyncElasticsearch, document_id: str) -> dict:
        response = await es.get(index=PHONES_INDEX, id=document_id)
        producer = AIOProducer()
        message = {"id": document_id, "action": "search_phone"}
        await producer.send_data(message)
        return response['_source']

    @staticmethod
    async def get_food(es: AsyncElasticsearch, document_id: str) -> dict:
        response = await es.get(index=FOOD_INDEX, id=document_id)
        producer = AIOProducer()
        message = {"id": document_id, "action": "search_food"}
        await producer.send_data(message)
        return response['_source']
