from fastapi import APIRouter
from api.v1.search.search_routes import search_router


v1_router = APIRouter(prefix='/v1')
v1_router.include_router(search_router)
