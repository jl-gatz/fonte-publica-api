from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ServiceStatus(str, Enum):
    healthy = "healthy"
    degraded = "degraded"
    down = "down"


class DatabaseStatus(str, Enum):
    up = "up"
    down = "down"
    unknown = "unknown"


class HealthResponse(BaseModel):
    status: ServiceStatus = Field(..., description="Estado geral da aplicação")
    service: str = Field(..., description="Nome institucional do serviço")
    database: DatabaseStatus = Field(
        ..., description="Estado da conexão com o banco de dados"
    )
    timestamp: datetime = Field(
        ..., description="Momento da verificação em UTC"
    )
    uptime_seconds: float = Field(
        ..., description="Tempo de atividade da aplicação em segundos"
    )
    uptime_human: str = Field(
        ..., description="Tempo de atividade formatado em forma legível"
    )
    version: str = Field(..., description="Versão da aplicação")
    build: str = Field(..., description="Identificador do build")
    commit: str = Field(..., description="Hash do commit do deploy")

    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "healthy",
                "service": "farol-publico-api",
                "database": "up",
                "timestamp": "2026-02-16T20:45:00Z",
                "uptime_seconds": 1832.45,
            }
        }
    }
