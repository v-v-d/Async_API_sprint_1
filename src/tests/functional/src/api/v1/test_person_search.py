from unittest.mock import AsyncMock

import pydantic
import pytest
from fastapi import status

from app.services.persons import main
from app.services.persons.main import PersonService


@pytest.fixture
def expected(load_fixture):
    return load_fixture("person_api_list.json")


@pytest.fixture
def person_name():
    return "Linda Park"


@pytest.fixture
async def mocked_es_person_valid_response(monkeypatch, load_fixture):
    monkeypatch.setattr(PersonService, "_execute", AsyncMock(spec=PersonService))
    mocked_data = load_fixture("person_list.json")
    main.PersonService._execute.return_value = mocked_data  # noqa


@pytest.mark.asyncio
async def test_search_person__ok(
    client, v1_search_persons_url, mocked_es_person_valid_response, expected
):
    response = await client.get(
        path=v1_search_persons_url, query_string={"query": person_name}
    )

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.asyncio
async def test_person_details__bad_es_response(
    client, v1_search_persons_url, mocked_es_invalid_response
):
    with pytest.raises(pydantic.ValidationError):
        await client.get(
            path=v1_search_persons_url, query_string={"query": person_name}
        )


@pytest.mark.asyncio
async def test_person_details__es_error(
    client, v1_search_persons_url, mocked_es_unexpected_exception
):
    response = await client.get(
        path=v1_search_persons_url, query_string={"query": person_name}
    )
    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
