from datetime import datetime

from sqlalchemy import event
from sqlalchemy.orm import Mapper

from app.core.time import ensure_aware

print("EVENTS MODULE LOADED")


def _normalize_datetime_fields(mapper, target):
    for column in mapper.columns:
        if (
            hasattr(column.type, "python_type")
            and column.type.python_type is datetime
        ):
            value = getattr(target, column.key)
            if value is not None:
                setattr(target, column.key, ensure_aware(value))


@event.listens_for(Mapper, "mapper_configured")
def setup_listeners(mapper, class_):
    if not hasattr(class_, "__tablename__"):
        return

    @event.listens_for(class_, "before_insert")
    def before_insert(mapper, connection, target):
        print("BEFORE INSERT TRIGGERED", target, type(target))

        _normalize_datetime_fields(mapper, target)

    @event.listens_for(class_, "before_update")
    def before_update(mapper, connection, target):
        _normalize_datetime_fields(mapper, target)
