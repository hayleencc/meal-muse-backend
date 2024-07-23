import pytest
from fastapi.testclient import TestClient

from api import create_app


@pytest.fixture
def client_session():
    app = create_app()
    with TestClient(app) as client:
        yield client
