import pytest

from sentinel_dashboard.dashboard import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"SentinelPy Logs" in rv.data
