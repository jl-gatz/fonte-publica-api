import hashlib
import json
from datetime import datetime


def generate_provenance(payload: dict) -> str:
    material = {"payload": payload, "timestamp": datetime.utcnow().isoformat()}
    raw = json.dumps(material, sort_keys=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
