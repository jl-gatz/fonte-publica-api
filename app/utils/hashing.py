import hashlib
import json


def generate_hash(payload: dict, encode=None) -> str:
    raw = (
        json.dumps(payload, sort_keys=True).encode(encode)
        if encode
        else json.dumps(payload, sort_keys=True).encode()
    )
    return hashlib.sha256(raw).hexdigest()
