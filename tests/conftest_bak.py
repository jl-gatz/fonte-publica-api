import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

import app.db.base  # noqa: F401
from app.db.base_class import Base
from app.db.session import get_db
from app.main import app
from tests.db import TestingSessionLocal

DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(  # noqa: F811
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


# @pytest.fixture(scope="session", autouse=True)
# def create_test_tables():
#     Base.metadata.create_all(bind=engine_test)
#     yield
#     Base.metadata.drop_all(bind=engine_test)


@pytest.fixture
def db_session():
    print(Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
