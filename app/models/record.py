from __future__ import annotations

import uuid
from datetime import datetime
from typing import Dict, Optional

from sqlalchemy import JSON, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.db.mixins import TimestampMixin


class Record(Base, TimestampMixin):
    __tablename__ = "records"
    __table_args__ = {"extend_existing": True}

    id: Mapped[str] = mapped_column(
        str(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
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
        nullable=True,
    )

    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
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
        JSON,
        default=dict,
        nullable=False,
    )
