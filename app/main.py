from fastapi import FastAPI

from app.api.v1.routers import api_router
from app.core.config import settings
from app.db.engine import create_db_engine
from app.db.session import SessionLocal


def create_app(database_url: str | None = None) -> FastAPI:

    app = FastAPI(
        title="Fonte Pública API",
        description=(
            "API de dados públicos voltada a jornalismo, pesquisa e educação, "
            "com foco em transparência, proveniência e correções."
        ),
        version="0.1.0",
        terms_of_service="https://www.notion.so/Fonte-P-blica-Termos-de-uso-e-princ-pios-2f987579f47780099039d55270281d44",
        contact={
            "name": "Fonte Pública",
            "url": "https://github.com/jl-gatz/fonte-publica-api/issues",
        },
        license_info={
            "name": "Apache License 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    engine = create_db_engine(
        database_url or settings.DATABASE_URL,
        echo=settings.SQL_ECHO,
    )

    # Bind SessionLocal dinamicamente
    SessionLocal.configure(bind=engine)

    app.include_router(api_router, prefix=settings.API_V1_STR)
    # Apenas para DEBUG
    print("APP DO CLIENT:", id(app))

    return app


app = create_app()
