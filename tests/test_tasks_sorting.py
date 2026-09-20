import pytest
from fastapi.testclient import TestClient

def test_task_sorting_title_asc(client: TestClient):
    client.post("/tasks/", json={
        "title": "C task",
        "description": "test description"
    })
    client.post("/tasks/", json={
        "title": "A task",
        "description": "test description"
    })
    client.post("/tasks/", json={
        "title": "B task",
        "description": "test description"
    })

    response = client.get("/tasks/?sort_by=title&order=asc")
    data = response.json()
    titles = [task["title"] for task in data]

    assert response.status_code == 200
    assert len(data) == 3
    assert titles == ["A task", "B task", "C task"]


def test_task_sorting_title_desc(client: TestClient):
    client.post("/tasks/", json={
        "title": "C task",
        "description": "test description"
    })
    client.post("/tasks/", json={
        "title": "A task",
        "description": "test description"
    })
    client.post("/tasks/", json={
        "title": "B task",
        "description": "test description"
    })

    response = client.get("/tasks/?sort_by=title&order=desc")
    data = response.json()
    titles = [task["title"] for task in data]

    assert response.status_code == 200
    assert len(data) == 3
    assert titles == ["C task", "B task", "A task"]