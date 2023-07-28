from starlette.testclient import TestClient
import sys
sys.path.insert(1, '../app')

from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world!"}