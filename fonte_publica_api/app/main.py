from fastapi import FastAPI
from api.v1.router import api_router
from core.config import settings


app = FastAPI(
    title="Fonte Pública API",
    description="API pública de dados jornalísticos com foco em transparência, proveniência e correções",
    version="1.0.0",
    terms_of_service="https://fontepublica.org/termos",
    contact={
        "name": "Fonte Pública",
        "url": "https://fontepublica.org",
        "email": "contato@fontepublica.org",
    },
    license_info={
        "name": "CC BY 4.0",
        "url": "https://creativecommons.org/licenses/by/4.0/",
    },
)

app.include_router(api_router, prefix="/v1")
