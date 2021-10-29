from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("film_api_list.json")


@pytest.fixture
def valid_sort_asc_query():
    return "rating"


@pytest.fixture
def valid_sort_desc_query():
    return "-rating"


@pytest.fixture
def invalid_sort_query():
    return "invalid"


@pytest.fixture
async def mocked_es_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock(spec=FilmsService))
    mocked_data = load_fixture("films_list.json")
    main.FilmsService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_films_list_ok__default(
    client, v1_films_url, mocked_es_valid_response, expected, load_fixture
):
    response = await client.get(path=v1_films_url)

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result) == len(expected)

    for idx, result_item in enumerate(result):
        assert result_item == expected[idx]


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
    client, v1_films_url, mocked_es_valid_response, expected
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=v1_films_url)
        assert response.status_code == status.HTTP_200_OK

        result = response.json()

        assert len(result) == len(expected)

        for idx, result_item in enumerate(result):
            assert result_item == expected[idx]

    assert main.FilmsService._execute.call_count == 1


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
