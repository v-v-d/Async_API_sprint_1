from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService
from tests.functional.testdata.api_films import (
    FILM_DETAILS_ES_RESPONSE,
    EXPECTED_FILM_DETAILS_RESPONSE,
)


@pytest.fixture
def film_id():
    return "a801e84c-316a-4c0c-a5a5-cc024234b2cb"


@pytest.fixture
async def film_details_url(v1_films_url, film_id):
    return urljoin(v1_films_url, film_id)


@pytest.fixture
async def mocked_es_valid_response(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.return_value = FILM_DETAILS_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_film_details_ok(client, film_details_url, mocked_es_valid_response):
    response = await client.get(path=film_details_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_FILM_DETAILS_RESPONSE


@pytest.mark.asyncio
async def test_film_details__cached_result(
    client, film_details_url, mocked_es_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=film_details_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == EXPECTED_FILM_DETAILS_RESPONSE

    assert main.FilmsService._request_elastic.call_count == 1


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

