import pytest
from api.users_client import UsersClient


@pytest.mark.api
def test_get_existing_user_returns_expected_fields():
    client = UsersClient()
    res = client.get_user(1)

    assert res.status_code == 200
    body = res.json()
    assert body["id"] == 1
    assert "email" in body and "@" in body["email"]


@pytest.mark.api
def test_get_nonexistent_user_returns_404():
    client = UsersClient()
    # ID 999999 is outside seeded test records and should return Not Found
    res = client.get_user(999999)

    assert res.status_code == 404


@pytest.mark.api
def test_create_user_returns_201():
    client = UsersClient()
    payload = {"name": "Karthik Nair", "username": "karthik_qa", "email": "karthik@example.com"}
    res = client.create_user(payload)

    assert res.status_code == 201
    body = res.json()
    assert body["name"] == "Karthik Nair"
