from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.genres import main
from app.services.genres.main import GenreService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("genre_api_list.json")


@pytest.fixture
async def mocked_es_genre_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(GenreService, "_execute", AsyncMock(spec=GenreService))
    mocked_data = load_fixture("genre_list.json")
    main.GenreService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_genre_list_ok__default(
    client, v1_genres_url, mocked_es_genre_valid_response, expected
):
    response = await client.get(path=v1_genres_url)

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result) == len(expected)

    for idx, result_item in enumerate(response.json()):
        assert result_item == expected[idx]


@pytest.mark.asyncio
async def test_genre_list__cached_result(
    client, v1_genres_url, mocked_es_genre_valid_response, expected
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=v1_genres_url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()

        assert len(result) == len(expected)

        for idx, result_item in enumerate(response.json()):
            assert result_item == expected[idx]

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
