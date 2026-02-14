from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Dict, Optional

from sqlalchemy import JSON, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.db.mixins import TimestampMixin


class Record(Base, TimestampMixin):
    __tablename__ = "records"
    __table_args__ = {"extend_existing": True}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    summary: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
    )

    source: Mapped[Dict] = mapped_column(
        JSON,
        nullable=False,
    )

    collected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
        nullable=False,
        index=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
        index=True,
    )

    attributes: Mapped[Dict] = mapped_column(
        "metadata",
        JSON,
        default=dict,
        nullable=False,
    )
