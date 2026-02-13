from typing import Optional

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
