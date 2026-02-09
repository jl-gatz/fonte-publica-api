from typing import Generator

from sqlalchemy.orm import Session

DbGenerator = Generator[Session, None, None]
