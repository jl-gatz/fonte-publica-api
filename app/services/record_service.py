import hashlib
import json
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.record import Record
from app.schemas.record import RecordCreate, RecordResponse


def generate_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()


def create_record(db: Session, data: RecordCreate, now: datetime) -> Record:
    payload = data.model_dump()
    record_hash = generate_hash(payload)

    record = Record(
        **payload, hash=record_hash, published_at=datetime.now(timezone.utc)
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_records_service(db: Session) -> list[RecordResponse]:
    records = db.query(Record).all()

    # Mesmo vazio, retorna lista
    return [RecordResponse.model_validate(record) for record in records]
