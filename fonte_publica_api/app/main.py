from api.v1.router import api_router
from fastapi import FastAPI


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

app.include_router(api_router, prefix="/v1")
