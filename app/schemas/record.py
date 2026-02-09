from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class SourceSchema(BaseModel):
    name: str = Field(..., example="Diário Oficial da União")
    url: Optional[str] = Field(None, example="https://www.in.gov.br")
    method: str = Field(..., example="scraping")  # scraping | download | api
    license: Optional[str] = Field(None, example="CC-BY")


class RecordBase(BaseModel):
    type: str = Field(..., example="document")
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
