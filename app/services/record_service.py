import hashlib
import json
from datetime import datetime, timezone

from models.record import Record
from schemas.record import RecordCreate
from sqlalchemy.orm import Session


def generate_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()


def create_record(db: Session, data: RecordCreate) -> Record:
    payload = data.model_dump()
    record_hash = generate_hash(payload)

    record = Record(
        **payload, hash=record_hash, published_at=datetime.now(timezone.utc)
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record
