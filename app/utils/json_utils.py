import json
from datetime import datetime


def dump_datas(data):
    return json.dumps(data, indent=4, sort_keys=True, default=str)


def load_datas(data):
    return json.loads(data)


def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Converte para string ISO 8601
    raise TypeError("Tipo não serializável")
