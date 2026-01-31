from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RecordBase(BaseModel):
    title: str
    summary: Optional[str]
    entity_id: Optional[str]
    source_id: Optional[str]


class RecordCreate(RecordBase):
    pass


class RecordOut(RecordBase):
    id: str
    created_at: datetime
    updated_at: datetime
    provenance_hash: str

    class Config:
        from_attributes = True
