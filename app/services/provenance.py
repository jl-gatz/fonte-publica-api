from datetime import datetime, timezone

from app.utils.hashing import generate_hash


def generate_provenance(payload: dict) -> str:
    material = {
        "payload": payload,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return generate_hash(material, encode="utf-8")
