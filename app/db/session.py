from sqlalchemy.orm import sessionmaker

from app.db.engine import create_db_engine

engine = create_db_engine()

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    bind=engine,
)
