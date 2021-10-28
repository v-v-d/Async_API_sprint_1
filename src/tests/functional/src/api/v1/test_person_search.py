from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.persons import main
from app.services.persons.main import PersonService
from tests.functional.testdata.api_persons import (
    PERSON_LIST_ES_RESPONSE,
    EXPECTED_PERSON_LIST_RESPONSE,
)


@pytest.fixture
def person_name():
    return "Linda Park"


@pytest.fixture
async def mocked_es_person_valid_response(monkeypatch):
    monkeypatch.setattr(PersonService, "_request_elastic", AsyncMock())
    main.PersonService._request_elastic.return_value = PERSON_LIST_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_search_person__ok(client, v1_search_persons_url, mocked_es_person_valid_response):
    response = await client.get(path=v1_search_persons_url, query_string={"query": person_name})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_PERSON_LIST_RESPONSE


@pytest.mark.asyncio
async def test_person_details__bad_es_response(
        client, v1_search_persons_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=v1_search_persons_url, query_string={"query": person_name})


@pytest.mark.asyncio
async def test_person_details__es_error(
        client, v1_search_persons_url, mocked_es_unexpected_exception
):
    response = await client.get(path=v1_search_persons_url, query_string={"query": person_name})
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY

