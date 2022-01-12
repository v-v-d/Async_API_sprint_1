import asyncio
from pathlib import Path

import aiocache
import pytest
from async_asgi_testclient import TestClient
from jose import jwt
from orjson import orjson
from pytest_mock import MockerFixture

from app.dependencies.auth import oauth2_scheme
from app.elastic import get_elastic
from app.main import app
from app.settings import settings

assert settings.TESTING, "You must set TESTING=True env for run the tests."

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/elastic_src")


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def disable_apm(session_mocker: MockerFixture):
    session_mocker.patch.object(settings.APM, "ENABLED", False)


@pytest.fixture(scope="session", autouse=True)
async def mocked_es():
    app.dependency_overrides[get_elastic] = lambda: None


@pytest.fixture
def load_fixture():
    def load(filename):
        with open(TEST_CONTAINER_SRC_DIR_PATH / filename, encoding="utf-8") as f:
            return orjson.loads(f.read())

    return load


@pytest.fixture(autouse=True)
def default_jwt_token():
    payload = {
        "is_admin": False,
        "roles": [],
    }
    token = jwt.encode(
        payload, settings.AUTH.SECRET_KEY, algorithm=settings.AUTH.ALGORITHM
    )
    app.dependency_overrides[oauth2_scheme] = lambda: token


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
