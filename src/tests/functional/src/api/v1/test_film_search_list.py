from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService
from tests.functional.testdata.api_films import (
    LIST_FILMS_SEARCH_ES_RESPONSE,
    EXPECTED_LIST_SEARCH_FILMS_RESPONSE,
)


@pytest.fixture
def film_title():
    return "2011 NBA All-Star Game"


@pytest.fixture
async def mocked_es_film_search_valid_response(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.return_value = LIST_FILMS_SEARCH_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_search_films__ok(client, v1_search_film_url, mocked_es_film_search_valid_response):
    response = await client.get(path=v1_search_film_url, query_string={"query": film_title})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_LIST_SEARCH_FILMS_RESPONSE


@pytest.mark.asyncio
async def test_search_film__cached_result(
        client, v1_search_film_url, mocked_es_film_search_valid_response
):
    method_call_count = 1

    for _ in range(method_call_count):
        response = await client.get(path=v1_search_film_url, query_string={"query": film_title})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == EXPECTED_LIST_SEARCH_FILMS_RESPONSE

    assert main.FilmsService._request_elastic.call_count == 1


@pytest.mark.asyncio
async def test_film__bad_es_response(
        client, v1_search_film_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=v1_search_film_url, query_string={"query": film_title})


@pytest.mark.asyncio
async def test_film__es_error(
        client, v1_search_film_url, mocked_es_unexpected_exception
):
    response = await client.get(path=v1_search_film_url, query_string={"query": film_title})
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
