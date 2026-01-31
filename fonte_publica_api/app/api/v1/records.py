from typing import List

from core.permissions import Role
from core.security import require_role
from fastapi import APIRouter, Depends
from schemas.record import RecordCreate, RecordOut

router = APIRouter()


@router.get("/", response_model=List[RecordOut])
def list_records():
    return []


@router.post(
    "/",
    response_model=RecordOut,
    dependencies=[Depends(require_role(Role.contributor))],
)
def create_record(payload: RecordCreate):
    return {
        "id": "rec_123",
        **payload.dict(),
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-01T00:00:00Z",
        "provenance_hash": "sha256:abc123",
    }
