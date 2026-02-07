from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.record import RecordCreate, RecordResponse
from services.record_service import create_record
from sqlalchemy.orm import Session

router = APIRouter(prefix="/records", tags=["records"])


@router.post("/", response_model=RecordResponse, status_code=201)
def create_new_record(payload: RecordCreate, db: Session = Depends(get_db)):
    record = create_record(db, payload)
    return record
