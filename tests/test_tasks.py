import pytest
from fastapi.testclient import TestClient


# === SUCCESS TESTS ===

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


# === ERROR TESTS ===

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


# === PAGINATION TEST ===

def test_tasks_with_pagination(client: TestClient):
    client.post("/tasks/", json={
        "title": "task-01",
        "description": "description-01"
    })
    client.post("/tasks/", json={
        "title": "task-02",
        "description": "description-02"
    })
    client.post("/tasks/", json={
        "title": "task-03",
        "description": "description-03"
    })
    client.post("/tasks/", json={
        "title": "task-04",
        "description": "description-04"
    })
    client.post("/tasks/", json={
        "title": "task-05",
        "description": "description-05"
    })
    response_01 = client.get("/tasks/?limit=2&offset=0")
    first_page = response_01.json()
    response_02 = client.get("/tasks/?limit=2&offset=2")
    second_page = response_02.json()
    response_03 = client.get("/tasks/?limit=2&offset=4")
    third_page = response_03.json()

    assert response_01.status_code == 200
    assert len(first_page) == 2

    assert response_02.status_code == 200
    assert len(second_page) == 2

    assert response_03.status_code == 200
    assert len(third_page) == 1

    first_ids = [item["id"] for item in first_page]
    second_ids = [item["id"] for item in second_page]
    third_ids = [item["id"] for item in third_page]

    assert first_ids != second_ids
    assert third_ids == [5]
