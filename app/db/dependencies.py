from app.db.generators import DbGenerator
from app.db.session import SessionLocal


def get_db() -> DbGenerator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
