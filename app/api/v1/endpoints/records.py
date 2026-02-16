from datetime import datetime
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.time import utc_now
from app.db.dependencies import get_db
from app.db.types import DbSession
from app.schemas.record import RecordCreate, RecordResponse
from app.services.record_service import create_record, list_records_service

router = APIRouter()

# fake_db = []


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_model=RecordResponse,
)
def create_new_record(
    payload: RecordCreate,
    db: Annotated[Session, Depends(get_db)],
    now: Annotated[datetime, Depends(utc_now)],
):
    record = create_record(payload, db, now=now)
    return RecordResponse.model_validate(record)


@router.get(
    "",
    response_model=list[RecordResponse],
    status_code=HTTPStatus.OK,
)
def list_records(db: DbSession):
    return list_records_service(db)


# @router.get(
#     "",
#     response_model=RecordListResponse,
#     status_code=HTTPStatus.OK,
# )
# def list_records(db: DbSession):
#     return {"records": fake_db}
