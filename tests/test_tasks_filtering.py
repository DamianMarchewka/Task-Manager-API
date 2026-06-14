import pytest
from fastapi.testclient import TestClient

def test_task_filtering_status(client: TestClient):
    response_1 = client.post("/tasks/", json={
        "title": "New title 1",
        "description": "New description 1",
    })
    response_2 = client.post("/tasks/", json={
        "title": "New title 2",
        "description": "New description 2",
    })
    client.post("/tasks/", json={
        "title": "New title 3",
        "description": "New description 3",
    })
    data_1 = response_1.json()
    task_id_1 = data_1["id"] 
    client.patch(f"/tasks/{task_id_1}", json={"status": "done"})

    data_2 = response_2.json()
    task_id_2 = data_2["id"] 
    client.patch(f"/tasks/{task_id_2}", json={"status": "done"})

    response = client.get("/tasks/?status=done")
    data = response.json()
    print(data)

    assert response.status_code == 200
    assert len(data) == 2
    assert all(task["status"] == "done" for task in data)

