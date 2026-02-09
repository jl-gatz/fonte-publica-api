from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
)

TestingSessionLocal = sessionmaker(
    bind=engine_test,
    class_=Session,
    autocommit=False,
    autoflush=False,
)
