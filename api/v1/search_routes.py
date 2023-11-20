from fastapi import APIRouter, Depends
from schemas import PhoneModel, FoodModel
from core.es import get_es
from elasticsearch import AsyncElasticsearch
from search_service.search_services import SearchService


search_router = APIRouter(prefix="/api/v1/search", tags=["search_service"])


@search_router.post('/phone')
async def add_phone_document(phone_document: PhoneModel, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    result = await SearchService.add_phone(es, phone_document)
    return {'status': result}


@search_router.post('/food')
async def add_food_document(food_document: FoodModel, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    result = await SearchService.add_food(es, food_document)
    return {'status': result}


@search_router.get('/phone')
async def get_phone_document(document_id: str, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    result = await SearchService.get_phone(es, document_id)
    return {'status': result}


@search_router.get('/food')
async def get_food_document(document_id: str, es: AsyncElasticsearch = Depends(get_es)) -> dict:
    result = await SearchService.get_food(es, document_id)
    return {'status': result}
