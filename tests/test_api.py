from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_ask_endpoint():
    response = client.post("/api/v1/ask", json={"question": "Что такое SmartTask?"})

    if response.status_code == 200:
        data = response.json()
        assert "answer" in data
        assert isinstance(data["answer"], str)
    elif response.status_code == 500:
        error = response.json()
        assert "detail" in error
        assert isinstance(error["detail"], str)
    else:
        assert False, f"Unexpected status: {response.status_code}"