from fastapi.testclient import TestClient

from api.app import app
from database.database import create_tables

create_tables()

client = TestClient(app)


def test_get_books():
    response = client.get("/books")

    assert response.status_code == 200
