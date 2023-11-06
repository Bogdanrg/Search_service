from fastapi import APIRouter, Depends
from schemas import PhoneModel, FoodModel
from core.es import get_es
from elasticsearch import AsyncElasticsearch
from constants import FOOD_INDEX, PHONES_INDEX


search_router = APIRouter(prefix="/api/search", tags=["search_service"])


@search_router.post('/phone')
async def add_phone_document(phone_document: PhoneModel, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    response = await es.index(index=PHONES_INDEX, document=phone_document.model_dump())
    return {'status': response['result']}


@search_router.post('/food')
async def add_food_document(food_document: FoodModel, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    response = await es.index(index=FOOD_INDEX, document=food_document.model_dump())
    return {'status': response['result']}
