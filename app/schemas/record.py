from datetime import datetime, timezone
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from app.schemas.source import SourceSchema


class RecordBase(BaseModel):
    type: str = Field(
        examples=["legislation", "jurisprudence", "administrative_act"]
    )
    title: str
    summary: Optional[str]
    source: SourceSchema
    attributes: Optional[Dict] = Field(default_factory=dict)


class RecordCreate(RecordBase):
    collected_at: datetime

    @field_validator("collected_at")
    @classmethod
    def ensure_aware(cls, v: datetime):
        if v.tzinfo is None:
            raise ValueError("Datetime must be timezone-aware")
        return v.astimezone(timezone.utc)


class RecordResponse(RecordBase):
    id: UUID
    collected_at: datetime
    published_at: datetime
    status: str
    version: int
    hash: str

    class Config:
        from_attributes = True


# class RecordListResponse(BaseModel):
#     records: list[RecordResponse]
