from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("person_film_api_list.json")


@pytest.fixture
def person_id():
    return "33eb3b88-69f2-4f38-a26d-ff32f1feb1a1/films"


@pytest.fixture
async def person_film_list_url(v1_persons_url, person_id):
    return urljoin(v1_persons_url, person_id)


@pytest.fixture
async def mocked_es_person_film_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock(spec=FilmsService))
    mocked_data = load_fixture("person_film_list.json")
    main.FilmsService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_person_film__ok(
    client, person_film_list_url, mocked_es_person_film_valid_response, expected
):
    response = await client.get(
        path=person_film_list_url, query_string={"query": person_id}
    )

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.asyncio
async def test_person_film__cached_result(
    client, person_film_list_url, mocked_es_person_film_valid_response, expected
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(
            path=person_film_list_url, query_string={"query": person_id}
        )

        assert response.status_code == status.HTTP_200_OK

        result = response.json()

        assert len(result) == len(expected)
        assert result == expected

    assert main.FilmsService._execute.call_count == 1


@pytest.mark.asyncio
async def test_person_film__bad_es_response(
    client, person_film_list_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=person_film_list_url, query_string={"query": person_id})


@pytest.mark.asyncio
async def test_person_film__es_error(
    client, person_film_list_url, mocked_es_unexpected_exception
):
    response = await client.get(
        path=person_film_list_url, query_string={"query": person_id}
    )
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
