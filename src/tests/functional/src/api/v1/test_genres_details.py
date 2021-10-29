from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.genres import main
from app.services.genres.main import GenreService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("genre_api_details.json")


@pytest.fixture
def genre_id():
    return "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff"


@pytest.fixture
async def genre_details_url(v1_genres_url, genre_id):
    return urljoin(v1_genres_url, genre_id)


@pytest.fixture
async def mocked_es_genre_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(GenreService, "_execute", AsyncMock(spec=GenreService))
    mocked_data = load_fixture("genre_details.json")
    main.GenreService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_genres_details__ok(
    client, genre_details_url, mocked_es_genre_valid_response, expected
):
    response = await client.get(path=genre_details_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.asyncio
async def test_genre_details__cached_result(
    client, genre_details_url, mocked_es_genre_valid_response, expected
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=genre_details_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected

    assert main.GenreService._execute.call_count == 1


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
