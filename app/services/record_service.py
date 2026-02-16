from datetime import datetime

from sqlalchemy.orm import Session

from app.models.record import Record
from app.schemas.record import RecordCreate, RecordResponse
from app.utils.hashing import generate_hash


def create_record(data: RecordCreate, db: Session, now: datetime) -> Record:
    payload = data.model_dump(exclude={"published_at"})
    hash_input = data.model_dump(mode="json", exclude={"published_at"})
    record_hash = generate_hash(hash_input)

    # Converte now para naive (remove tzinfo)
    naive_now = now.replace(tzinfo=None)

    # Garante que collected_at também seja naive, se vier com timezone
    if "collected_at" in payload and payload["collected_at"] is not None:
        if (
            hasattr(payload["collected_at"], "tzinfo")
            and payload["collected_at"].tzinfo is not None
        ):
            payload["collected_at"] = payload["collected_at"].replace(
                tzinfo=None
            )

    # Cria o record com os objetos datetime (naive)
    record = Record(**payload, hash=record_hash, published_at=naive_now)

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def list_records_service(db: Session) -> list[RecordResponse]:
    records = db.query(Record).all()

    # Mesmo vazio, retorna lista
    return [RecordResponse.model_validate(record) for record in records]
