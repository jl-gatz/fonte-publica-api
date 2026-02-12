from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from app.db.types import DbSession
from app.schemas.record import RecordCreate, RecordResponse
from app.services.record_service import create_record, list_records_service

router = APIRouter()

# fake_db = []


@router.post(
    "/", status_code=HTTPStatus.CREATED, response_model=RecordResponse
)
def create_new_record(payload: RecordCreate, db: DbSession):
    record = create_record(db, payload)
    return record


@router.get(
    "",
    response_model=List[RecordResponse],
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
