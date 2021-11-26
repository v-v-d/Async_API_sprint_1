import pytest
from fastapi import status
from fastapi.security import HTTPBasicCredentials

from app.main import app
from app.settings import settings
from app.utils import security


@pytest.fixture
def url_path():
    return "/api/docs"


@pytest.fixture
def valid_basic_auth():
    auth_obj = HTTPBasicCredentials(
        username=settings.BASIC_AUTH_USERNAME,
        password=settings.BASIC_AUTH_PASSWD,
    )
    app.dependency_overrides[security] = lambda: auth_obj


@pytest.fixture
def invalid_basic_auth():
    auth_obj = HTTPBasicCredentials(
        username="invalid username",
        password="invalid password",
    )
    app.dependency_overrides[security] = lambda: auth_obj


@pytest.mark.asyncio
async def test_film_details_ok(client, url_path, valid_basic_auth):
    response = await client.get(path=url_path)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_film_details_unauthorized(client, url_path, invalid_basic_auth):
    response = await client.get(path=url_path)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
