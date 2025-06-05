import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def test_client():
    """
    Create a test client for the FastAPI application.
    Share a single client across the entire test module.
    """
    with TestClient(app) as client:
        yield client
