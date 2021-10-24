import asyncio
from unittest.mock import MagicMock

import aiocache
import pytest
from async_asgi_testclient import TestClient

from app.elastic import get_elastic
from app.main import app
from app.settings import settings

assert settings.TESTING, "You must set TESTING=True env for run the tests."


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def mocked_es():
    app.dependency_overrides[get_elastic] = lambda: MagicMock


@pytest.fixture
def client():
    client = TestClient(app)
    client.headers = {"Host": "0.0.0.0", "Content-Type": "application/json"}
    return client


@pytest.fixture(autouse=True)
async def clear_cache():
    yield
    cache = aiocache.caches.get("default")
    await cache.clear()
