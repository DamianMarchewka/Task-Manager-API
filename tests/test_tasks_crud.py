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


def test_get_task(client: TestClient):
    response = client.post("/tasks/", json={
        "title": "Test title",
        "description": "Test description"
    })
    data = response.json()
    task_id = data["id"]
    result = client.get(f"/tasks/{task_id}")
    result_data = result.json()
    assert result.status_code == 200
    assert result_data["id"] == task_id
    assert result_data["title"] == "Test title"
    assert result_data["description"] == "Test description"


def test_list_tasks_empty(client: TestClient):
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_with_data(client: TestClient):
    client.post("/tasks/", json={
        "title": "First test task",
        "description": "First test description"
    })
    client.post("/tasks/", json={
        "title": "Second test task",
        "description": "Second test description"
    })
    response = client.get("/tasks/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2

    assert all("id" in i for i in data)
    assert all("created_at" in i for i in data)
    assert all(item["status"] == "todo" for item in data)

    titles = [item["title"] for item in data]
    descriptions = [item["description"] for item in data]

    assert "First test task" in titles
    assert "Second test task" in titles

    assert "First test description" in descriptions
    assert "Second test description" in descriptions


def test_update_task(client: TestClient):
    response = client.post("/tasks/", json={
        "title": "Test title",
        "description": "Test description"
    })
    data = response.json()
    task_id = data["id"]
    update_response = client.patch(f"/tasks/{task_id}", json={
        "title": "New test title"
    })
    update_data = update_response.json()
    assert update_response.status_code == 200
    assert update_data["title"] == "New test title"
    assert update_data["description"] == "Test description"


def test_delete_task(client: TestClient):
    response = client.post("/tasks/", json={
        "title": "Test title",
        "description": "Test description"
    })
    data = response.json()
    task_id = data["id"]
    delete_response = client.delete(f"/tasks/{task_id}")
    get_response = client.get(f"/tasks/{task_id}")
    assert delete_response.status_code == 204
    assert get_response.status_code == 404
