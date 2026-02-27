from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.runtime import START_TIME
from app.db.session import get_db
from app.schemas.health import (
    DatabaseStatus,
    HealthResponse,
    ServiceStatus,
)
from app.utils.time import format_uptime

router = APIRouter()


@router.get(
    "/",
    response_model=HealthResponse,
    summary="Healthcheck institucional completo",
)
def healthcheck(db: Annotated[Session, Depends(get_db)]):

    db_status = DatabaseStatus.unknown

    try:
        db.execute(text("SELECT 1"))
        db_status = DatabaseStatus.up
    except Exception:
        db_status = DatabaseStatus.down

    overall_status = (
        ServiceStatus.healthy
        if db_status == DatabaseStatus.up
        else ServiceStatus.degraded
    )

    now = datetime.now(timezone.utc)
    uptime_seconds = (now - START_TIME).total_seconds()

    return HealthResponse(
        status=overall_status,
        service=settings.PROJECT_NAME,
        database=db_status,
        timestamp=now,
        uptime_seconds=uptime_seconds,
        uptime_human=format_uptime(uptime_seconds),
        version=settings.VERSION,
        build=settings.BUILD_VERSION,
        commit=settings.COMMIT_HASH,
    )
