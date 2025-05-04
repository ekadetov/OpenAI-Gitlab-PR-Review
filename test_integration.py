import pytest
from main import app


@pytest.fixture(scope="module")
def test_client():
    with app.test_client() as client:
        yield client


def test_webhook(test_client):
    url = "/webhook"
    headers = {"Content-Type": "application/json", "X-Gitlab-Token": "123"}
    payload = {
        "object_kind": "merge_request",
        "object_attributes": {"action": "open", "iid": 6091},
        "project": {"id": 18752679},
    }

    response = test_client.post(url, json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json["message"] == "Webhook received"
