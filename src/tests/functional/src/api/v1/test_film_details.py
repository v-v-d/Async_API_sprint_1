from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status
from jose import jwt

from app.dependencies.auth import oauth2_scheme
from app.main import app
from app.services.films import main
from app.services.films.main import FilmsService
from app.settings import settings


@pytest.fixture
def expected(load_fixture):
    return load_fixture("film_api_details.json")


@pytest.fixture
def film_id():
    return "a801e84c-316a-4c0c-a5a5-cc024234b2cb"


@pytest.fixture
async def film_details_url(v1_films_url, film_id):
    return urljoin(v1_films_url, film_id)


@pytest.fixture
async def mocked_es_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock(spec=FilmsService))
    mocked_data = load_fixture("film_details.json")
    main.FilmsService._execute.return_value = mocked_data  # noqa


@pytest.fixture
async def mocked_es_valid_subscription_response(monkeypatch, load_fixture):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock(spec=FilmsService))
    mocked_data = load_fixture("film_details_subscription.json")
    main.FilmsService._execute.return_value = mocked_data  # noqa


@pytest.fixture
def invalid_jwt_token():
    token = jwt.encode({}, "invalid_secret_key", algorithm=settings.AUTH.ALGORITHM)
    app.dependency_overrides[oauth2_scheme] = lambda: token


@pytest.fixture
def jwt_token_invalid_payload():
    payload = {"invalid": True}
    token = jwt.encode(
        payload, settings.AUTH.SECRET_KEY, algorithm=settings.AUTH.ALGORITHM
    )
    app.dependency_overrides[oauth2_scheme] = lambda: token


@pytest.mark.asyncio
async def test_film_details_ok(
    client, film_details_url, mocked_es_valid_response, expected
):
    response = await client.get(path=film_details_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.asyncio
async def test_film_details_invalid_jwt(client, invalid_jwt_token, film_details_url):
    response = await client.get(path=film_details_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_film_details_invalid_jwt_payload(
    client, jwt_token_invalid_payload, film_details_url
):
    response = await client.get(path=film_details_url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_film_details_forbidden(
    client, film_details_url, mocked_es_valid_subscription_response
):
    response = await client.get(path=film_details_url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_film_details__cached_result(
    client, film_details_url, mocked_es_valid_response, expected
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=film_details_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected

    assert main.FilmsService._execute.call_count == 1


@pytest.mark.asyncio
async def test_film_details__bad_es_response(
    client, film_details_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=film_details_url)


@pytest.mark.asyncio
async def test_film_details__es_error(
    client, film_details_url, mocked_es_unexpected_exception
):
    response = await client.get(path=film_details_url)
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY


@pytest.mark.asyncio
async def test_film_details__not_found(
    client, film_details_url, mocked_es_not_found_error
):
    response = await client.get(path=film_details_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
