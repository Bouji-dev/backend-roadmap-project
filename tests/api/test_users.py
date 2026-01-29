from fastapi.testclient import TestClient

from app.main import app
from app.core.dependencies import get_user_service


class FakeUserService:
    def get_user(self, user_id: int) -> dict:
        return {
            'id': user_id,
            'name': 'Test User'
        }
    
app.dependency_overrides[get_user_service] = lambda: FakeUserService()

client = TestClient(app)

def test_get_user_success():
    response = client.get('/api/v1/users/1')

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["id"] == 1
    assert data["data"]["name"] == "Ehsan"
    assert data["error"] is None

app.dependency_overrides.clear()    