import pytest
from fastapi.testclient import TestClient


def test_get_task_not_found(client: TestClient):
    response = client.get("/tasks/9999")
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Task not found"


def test_update_task_not_found(client: TestClient):
    response = client.patch("/tasks/9999", json={
        "title": "New title"
    })
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Task not found"


def test_update_task_empty_body(client: TestClient):
    response = client.post("/tasks/", json={
        "title": "Test title",
        "description": "Test description"
    })
    data = response.json()
    task_id = data["id"]
    response_patch = client.patch(f"/tasks/{task_id}", json={})
    data_patch = response_patch.json()
    assert response_patch.status_code == 400
    assert data_patch["detail"] == "Empty data"


def test_delete_task_not_found(client: TestClient):
    response = client.delete("/tasks/9999")
    assert response.status_code == 404
