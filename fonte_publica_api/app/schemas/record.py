from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

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
        orm_mode = True
