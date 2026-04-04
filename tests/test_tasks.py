import pytest
from fastapi.testclient import TestClient


def test_create_task(client: TestClient):
    response = client.post("/tasks/", json={
        "title": "Test title",
        "description": "Test description"
    })
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "Test title"
    assert data["id"] is not None
