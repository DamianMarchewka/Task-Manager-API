import pytest
from fastapi.testclient import TestClient


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
