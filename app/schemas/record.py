from datetime import datetime as dt
from datetime import timezone as tz
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.source import SourceSchema


class RecordBase(BaseModel):
    type: str = Field(
        examples=["legislation", "jurisprudence", "administrative_act"]
    )
    title: str
    summary: Optional[str]
    source: SourceSchema
    attributes: Optional[Dict] = Field(default_factory=dict)
    collected_at: dt


class RecordCreate(RecordBase):
    published_at: Optional[dt] = Field(default_factory=lambda: dt.now(tz.utc))

    # @classmethod
    # @field_serializer("collected_at", "published_at")
    # def serialize_datetime(self, dt: dt, _info):
    #     return dt.isoformat()

    # @field_validator("collected_at")
    # @classmethod
    # def ensure_aware(cls, v: datetime):
    #     if v.tzinfo is None:
    #         raise ValueError("Datetime must be timezone-aware")
    #     return v.astimezone(timezone.utc)


class RecordResponse(RecordBase):
    id: UUID
    collected_at: dt
    published_at: dt
    status: str
    version: int
    hash: str

    model_config = ConfigDict(
        from_attributes=True,
    )


# class RecordListResponse(BaseModel):
#     records: list[RecordResponse]
