from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService
from tests.functional.testdata.api_films import (
    LIST_FILMS_ES_RESPONSE,
    EXPECTED_LIST_FILMS_RESPONSE,
)


@pytest.fixture
def valid_sort_asc_query(monkeypatch):
    return "rating"


@pytest.fixture
def valid_sort_desc_query(monkeypatch):
    return "-rating"


@pytest.fixture
def invalid_sort_query(monkeypatch):
    return "invalid"


@pytest.fixture
async def mocked_es_valid_response(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.return_value = LIST_FILMS_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_films_list_ok__default(client, v1_films_url, mocked_es_valid_response):
    response = await client.get(path=v1_films_url)

    assert response.status_code == status.HTTP_200_OK

    for idx, result_item in enumerate(response.json()):
        assert result_item == EXPECTED_LIST_FILMS_RESPONSE[idx]


@pytest.mark.asyncio
async def test_films_list_ok__query_sort_asc(
    client, v1_films_url, valid_sort_asc_query, mocked_es_valid_response
):
    response = await client.get(
        path=v1_films_url, query_string={"sort": valid_sort_asc_query}
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_films_list_ok__query_sort_desc(
    client, v1_films_url, valid_sort_desc_query, mocked_es_valid_response
):
    response = await client.get(
        path=v1_films_url, query_string={"sort": valid_sort_desc_query}
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_films_list__invalid_sort_query(
    client, v1_films_url, invalid_sort_query, mocked_es_valid_response
):
    response = await client.get(
        path=v1_films_url, query_string={"sort": invalid_sort_query}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_films_list__cached_result(
    client, v1_films_url, mocked_es_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=v1_films_url)
        assert response.status_code == status.HTTP_200_OK

        for idx, result_item in enumerate(response.json()):
            assert result_item == EXPECTED_LIST_FILMS_RESPONSE[idx]

    assert main.FilmsService._request_elastic.call_count == 1


@pytest.mark.asyncio
async def test_films_list__bad_es_response(
    client, v1_films_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=v1_films_url)


@pytest.mark.asyncio
async def test_films_list__es_error(
    client, v1_films_url, mocked_es_unexpected_exception
):
    response = await client.get(path=v1_films_url)
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
