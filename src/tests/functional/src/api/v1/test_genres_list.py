from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.genres import main
from app.services.genres.main import GenreService
from tests.functional.testdata.api_genres import (
    GENRE_LIST_ES_RESPONSE,
    EXPECTED_GENRE_LIST_RESPONSE,
)


@pytest.fixture
async def mocked_es_genre_valid_response(monkeypatch):
    monkeypatch.setattr(GenreService, "_execute", AsyncMock())
    main.GenreService._execute.return_value = GENRE_LIST_ES_RESPONSE


@pytest.mark.asyncio
async def test_films_list_ok__default(client, v1_genres_url, mocked_es_genre_valid_response):
    response = await client.get(path=v1_genres_url)

    assert response.status_code == status.HTTP_200_OK

    for idx, result_item in enumerate(response.json()):
        assert result_item == EXPECTED_GENRE_LIST_RESPONSE[idx]


@pytest.mark.asyncio
async def test_genre_list__cached_result(
        client, v1_genres_url, mocked_es_genre_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=v1_genres_url)
        assert response.status_code == status.HTTP_200_OK

        for idx, result_item in enumerate(response.json()):
            assert result_item == EXPECTED_GENRE_LIST_RESPONSE[idx]

    assert main.GenreService._execute.call_count == 1


@pytest.mark.asyncio
async def test_genre_list__bad_es_response(
        client, v1_genres_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=v1_genres_url)


@pytest.mark.asyncio
async def test_genre_list__es_error(
        client, v1_genres_url, mocked_es_unexpected_exception
):
    response = await client.get(path=v1_genres_url)
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
