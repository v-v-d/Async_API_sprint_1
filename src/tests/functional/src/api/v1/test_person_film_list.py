from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.films import main
from app.services.films.main import FilmsService
from tests.functional.testdata.api_persons import (
    PERSON_FILM_LIST_ES_RESPONSE,
    EXPECTED_PERSON_FILM_LIST_RESPONSE,
)


@pytest.fixture
def person_id():
    return "33eb3b88-69f2-4f38-a26d-ff32f1feb1a1/films"


@pytest.fixture
async def person_film_list_url(v1_persons_url, person_id):
    return urljoin(v1_persons_url, person_id)


@pytest.fixture
async def mocked_es_person_film_valid_response(monkeypatch):
    monkeypatch.setattr(FilmsService, "_execute", AsyncMock())
    main.FilmsService._execute.return_value = PERSON_FILM_LIST_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_person_film__ok(client, person_film_list_url, mocked_es_person_film_valid_response):
    response = await client.get(path=person_film_list_url, query_string={"query": person_id})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_PERSON_FILM_LIST_RESPONSE


@pytest.mark.asyncio
async def test_person_film__cached_result(
        client, person_film_list_url, mocked_es_person_film_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=person_film_list_url, query_string={"query": person_id})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == EXPECTED_PERSON_FILM_LIST_RESPONSE

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
    response = await client.get(path=person_film_list_url, query_string={"query": person_id})
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY

