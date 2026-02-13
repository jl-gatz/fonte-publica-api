from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class SourceSchema(BaseModel):
    name: Optional[str] = Field(
        default=None,
        examples=[
            "Diário Oficial da União",
            "Tribunal de Justiça do Estado de São Paulo",
        ],
    )
    url: Optional[str] = Field(
        default=None, examples=["https://www.in.gov.br"]
    )
    method: str = Field(
        examples=["scraping", "download", "api"]
    )  # scraping | download | api
    license: Optional[str] = Field(None, examples=["CC-BY"])


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
