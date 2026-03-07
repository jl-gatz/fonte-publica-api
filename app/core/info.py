from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()
settings = get_settings()


@router.get("")
def info():
    return {
        "PROJECT_NAME": settings.PROJECT_NAME,
        "DEBUG": settings.DEBUG,
        "DATABASE_URL": settings.DATABASE_URL,
    }
