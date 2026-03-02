from datetime import timedelta


def format_uptime(seconds: float) -> str:
    delta = timedelta(seconds=int(seconds))

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []

    if days:
        parts.append(f"{days}d")
    if hours or days:
        parts.append(f"{hours:02}h")
    if minutes or hours or days:
        parts.append(f"{minutes:02}m")

    parts.append(f"{seconds:02}s")

    return " ".join(parts)
