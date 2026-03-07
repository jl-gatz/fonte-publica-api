from datetime import datetime
from typing import Annotated

from fastapi import Depends

from app.core.time import utc_now


def get_now() -> datetime:
    """
    FastAPI dependency that provides current UTC time.
    """
    return utc_now()


UTCNow = Annotated[datetime, Depends(get_now)]
