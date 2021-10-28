from unittest.mock import AsyncMock
from urllib.parse import urljoin

import pydantic
import pytest
from fastapi import status

from app.services.persons import main
from app.services.persons.main import PersonService
from tests.functional.testdata.api_persons import (
    PERSON_DETAILS_ES_RESPONSE,
    EXPECTED_PERSON_DETAILS_RESPONSE,
)


@pytest.fixture
def person_id():
    return "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a"


@pytest.fixture
async def person_details_url(v1_persons_url, person_id):
    return urljoin(v1_persons_url, person_id)


@pytest.fixture
async def mocked_es_person_valid_response(monkeypatch):
    monkeypatch.setattr(PersonService, "_request_elastic", AsyncMock())
    main.PersonService._request_elastic.return_value = PERSON_DETAILS_ES_RESPONSE  # noqa


@pytest.mark.asyncio
async def test_person_details__ok(client, person_details_url, mocked_es_person_valid_response):
    response = await client.get(path=person_details_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EXPECTED_PERSON_DETAILS_RESPONSE


@pytest.mark.asyncio
async def test_person_details__cached_result(
        client, person_details_url, mocked_es_person_valid_response
):
    method_call_count = 2

    for _ in range(method_call_count):
        response = await client.get(path=person_details_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == EXPECTED_PERSON_DETAILS_RESPONSE

    assert main.PersonService._request_elastic.call_count == 1


@pytest.mark.asyncio
async def test_person_details__bad_es_response(
        client, person_details_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(path=person_details_url)


@pytest.mark.asyncio
async def test_person_details__es_error(
        client, person_details_url, mocked_es_unexpected_exception
):
    response = await client.get(path=person_details_url)
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY


@pytest.mark.asyncio
async def test_person_details__not_found(
        client, person_details_url, mocked_es_not_found_error
):
    response = await client.get(path=person_details_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
