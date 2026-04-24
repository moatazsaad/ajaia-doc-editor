from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_update_and_read_document():
    create_response = client.post(
        "/documents",
        json={
            "title": "Test Doc",
            "owner_id": 1,
        },
    )

    assert create_response.status_code == 200

    document = create_response.json()
    document_id = document["id"]

    update_response = client.put(
        f"/documents/{document_id}",
        json={
            "title": "Updated Test Doc",
            "content": "<p>Hello from test</p>",
        },
    )

    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Test Doc"

    read_response = client.get(f"/documents/{document_id}")

    assert read_response.status_code == 200
    assert read_response.json()["content"] == "<p>Hello from test</p>"