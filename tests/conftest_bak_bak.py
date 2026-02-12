import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

import app.db.base  # noqa: F401
from app.db.base_class import Base
from app.db.generators import DbGenerator
from app.db.session import get_db
from app.main import app

# ---------------------------------------------------------
# Engine de teste (SQLite isolado)
# ---------------------------------------------------------

SQLALCHEMY_DATABASE_URL = (
    "sqlite:///file:testdb?mode=memory&cache=shared&uri=true"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# ---------------------------------------------------------
# Criação e destruição das tabelas
# ---------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """
    Cria todas as tabelas antes da sessão de testes
    e remove após finalizar.
    """
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# ---------------------------------------------------------
# Sessão de banco para cada teste
# ---------------------------------------------------------


@pytest.fixture
def db_session(create_test_database) -> DbGenerator:
    """
    Cria uma nova transação por teste.
    Faz rollback ao final.
    """
    connection = engine.connect()
    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


# ---------------------------------------------------------
# Override da dependência get_db
# ---------------------------------------------------------


@pytest.fixture
def client(db_session: DbGenerator):
    """
    Injeta a sessão de teste no FastAPI via override.
    """

    # def override_get_db():
    #     yield db_session

    app.dependency_overrides[get_db] = lambda: db_session

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
