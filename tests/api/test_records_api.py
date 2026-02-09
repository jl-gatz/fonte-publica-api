# tests/api/test_records_api.py
from app.db.dependencies import get_db
from app.main import app
from tests.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)
