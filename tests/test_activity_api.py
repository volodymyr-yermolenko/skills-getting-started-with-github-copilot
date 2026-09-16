from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 200

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
