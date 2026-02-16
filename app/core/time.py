from datetime import datetime, timezone


def utc_now() -> datetime:
    """
    Returns a timezone-aware UTC datetime.
    """
    time = datetime.now(timezone.utc)
    return time


def ensure_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware")
    return dt.astimezone(timezone.utc)
