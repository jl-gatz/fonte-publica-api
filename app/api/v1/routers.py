from fastapi import APIRouter

from app.api.v1.endpoints import records

api_router = APIRouter()

api_router.include_router(records.router, prefix="/records", tags=["Records"])
# api_router.include_router(
#     sources.router, prefix="/sources", tags=["Sources"])
# api_router.include_router(
#     entities.router, prefix="/entities", tags=["Entities"])
