import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine

import app.db.base  # noqa: F401
import app.db.session as session_module
from app.db.base_class import Base
from app.db.generators import DbGenerator
from app.main import app

# ---------------------------------------------------------
# Engine de teste (SQLite isolado)
# ---------------------------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


# TestingSessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

# 🔥 SOBRESCREVE O ENGINE GLOBAL DA APLICAÇÃO
session_module.engine = test_engine
session_module.SessionLocal.configure(bind=test_engine)


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
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def create_connection():
    connection = test_engine.connect()
    yield connection
    connection.close()


@pytest.fixture
def db_session(create_connection) -> DbGenerator:
    conn = create_connection
    transaction = conn.begin()
    session = session_module.SessionLocal(bind=conn)

    yield session
    session.close()
    transaction.rollback()


# @pytest.fixture(autouse=True)
# def clean_database(db_session: Generator[Session, Any, Any]):
#     """
#     Limpa os dados das tabelas entre os testes, mas mantém a estrutura.
#     """
#     yield
#     for table in reversed(Base.metadata.sorted_tables):
#         db_session.execute(table.delete())
#     db_session.commit()


# ---------------------------------------------------------
# Override da dependência get_db
# ---------------------------------------------------------


@pytest.fixture
def client(db_session: DbGenerator):
    """
    Injeta a sessão de teste no FastAPI via override.
    """

    def override_get_db():
        yield db_session

    print("Override do get_db com sessão de teste")
    print(id(db_session))
    app.dependency_overrides[session_module.get_db] = override_get_db

    print("TEST GET_DB:", session_module.get_db)
    print(app.dependency_overrides)
    print("APP NO OVERRIDE:", id(app))

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
