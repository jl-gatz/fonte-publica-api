from datetime import datetime
from uuid import UUID

from app.models.record import Record


def test_create_and_list_record(db_session):
    record = Record(
        type="document",
        title="Lei de Acesso à Informação",
        summary="Lei que regula o acesso a informações públicas",
        source={
            "name": "Planalto",
            "method": "download",
            "url": "https://www.planalto.gov.br",
        },
        collected_at=datetime.utcnow(),
        status="published",
        version=1,
        hash="testhash123",
        attributes={"tema": "transparência"},
    )

    db_session.add(record)
    db_session.commit()
    db_session.refresh(record)

    # Assert criação
    assert isinstance(record.id, UUID)
    assert record.title == "Lei de Acesso à Informação"

    # Assert listagem
    records = db_session.query(Record).all()

    assert len(records) == 1
    assert records[0].id == record.id
