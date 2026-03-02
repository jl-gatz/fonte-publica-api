from fastapi import APIRouter

from app.api.v1.endpoints import health, records
from app.core import info

api_router = APIRouter()

api_router.include_router(records.router, prefix="/records", tags=["Records"])
api_router.include_router(info.router, prefix="/info", tags=["Info"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
# api_router.include_router(
#     sources.router, prefix="/sources", tags=["Sources"])
# api_router.include_router(
#     entities.router, prefix="/entities", tags=["Entities"])
