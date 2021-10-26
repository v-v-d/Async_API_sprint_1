from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.genres import main
from app.services.genres.main import GenreService
from tests.functional.testdata.api_genres import (
    GENRE_DETAILS_ES_RESPONSE,
    EXPECTED_GENRE_DETAILS_RESPONSE,
)


@pytest.fixture
def genre_id():
    return "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff"


@pytest.fixture
async def genre_details_url(v1_genres_url, genre_id):
    return urljoin(v1_genres_url, genre_id)


@pytest.fixture
async def mocked_es_genre_valid_response(monkeypatch):
    monkeypatch.setattr(GenreService, "_request_elastic", AsyncMock())
    main.GenreService._request_elastic.return_value = GENRE_DETAILS_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_genres_details__ok(client, genre_details_url, mocked_es_genre_valid_response):
    response = await client.get(path=genre_details_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_GENRE_DETAILS_RESPONSE


@pytest.mark.asyncio
async def test_genre_details__cached_result(
        client, genre_details_url, mocked_es_genre_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=genre_details_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == EXPECTED_GENRE_DETAILS_RESPONSE

    assert main.GenreService._request_elastic.call_count == 1


@pytest.mark.asyncio
async def test_genre_details__bad_es_response(
        client, genre_details_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=genre_details_url)


@pytest.mark.asyncio
async def test_genre_details__es_error(
        client, genre_details_url, mocked_es_unexpected_exception
):
    response = await client.get(path=genre_details_url)
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY


@pytest.mark.asyncio
async def test_genre_details__not_found(
        client, genre_details_url, mocked_es_not_found_error
):
    response = await client.get(path=genre_details_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
