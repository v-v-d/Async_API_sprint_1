from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("film_search_api_list.json")


@pytest.fixture
def film_title():
    return "2011 NBA All-Star Game"


@pytest.fixture
async def mocked_es_film_search_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock(spec=FilmsService))
    mocked_data = load_fixture("film_search_list.json")
    main.FilmsService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_search_films__ok(
    client,
    v1_search_film_url,
    film_title,
    mocked_es_film_search_valid_response,
    expected,
):
    response = await client.get(
        path=v1_search_film_url, query_string={"query": film_title}
    )

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result) == len(expected)
    assert response.json() == expected


@pytest.mark.asyncio
async def test_film__bad_es_response(
    client, v1_search_film_url, film_title, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=v1_search_film_url, query_string={"query": film_title})


@pytest.mark.asyncio
async def test_film__es_error(
    client, v1_search_film_url, film_title, mocked_es_unexpected_exception
):
    response = await client.get(
        path=v1_search_film_url, query_string={"query": film_title}
    )
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
