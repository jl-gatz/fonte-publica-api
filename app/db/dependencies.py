from typing import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a SQLAlchemy Session
    and ensures it's closed after use.
    Yields:
        Session: A SQLAlchemy Session instance.
    """
    db = None
    try:
        print("CRIANDO SESSION")
        db = SessionLocal()
        print("SESSION OK:", db)
        yield db
    except Exception:
        import traceback  # noqa: PLC0415

        print("ERRO NA DEPENDÊNCIA:")
        traceback.print_exc()
        raise
    finally:
        print("FINALLY EXECUTANDO")
        try:
            if db is not None:
                db.close()
        except Exception as e:
            print("ERRO NO CLOSE:", e)
