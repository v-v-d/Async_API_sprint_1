import orjson
import pytest

from app.dependencies.films import get_film_service
from tests.functional.testdata.service_films import (
    EXPECTED_QUERY_TO_ES__QUERY_NO_ARGS,
    EXPECTED_QUERY_TO_ES__GET_ALL,
    EXPECTED_QUERY_TO_ES__ONLY_QUERY,
    EXPECTED_QUERY_TO_ES__ONLY_GENRE_ID,
    EXPECTED_QUERY_TO_ES__ONLY_PERSON_ID,
    EXPECTED_QUERY_TO_ES__ONLY_SORT_ASC,
    EXPECTED_QUERY_TO_ES__ONLY_SORT_DESC,
    EXPECTED_QUERY_TO_ES__QUERY_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__GENRE_ID_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__PERSON_ID_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__QUERY_AND_PERSON_ID_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__GENRE_ID_AND_PERSON_ID_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__QUERY_AND_GENRE_ID_AND_PERSON_ID_AND_SORT_ASC,
    EXPECTED_QUERY_TO_ES__QUERY_AND_GENRE_ID_AND_PERSON_ID_AND_SORT_ASC_AND_UNSUBSCRIBED,
)


@pytest.fixture
def films_service(monkeypatch):
    return get_film_service()


@pytest.mark.asyncio
async def test_films_get_query__all(
    films_service,
):
    result = films_service.get_query(is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__GET_ALL


@pytest.mark.asyncio
async def test_films_get_query__no_args(films_service):
    result = films_service.get_query()
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__QUERY_NO_ARGS


@pytest.mark.asyncio
async def test_films_get_query__only_query(films_service):
    result = films_service.get_query(query="test", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__ONLY_QUERY


@pytest.mark.asyncio
async def test_films_get_query__only_genre_id(films_service):
    result = films_service.get_query(genre_id="test", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__ONLY_GENRE_ID


@pytest.mark.asyncio
async def test_films_get_query__only_person_id(films_service):
    result = films_service.get_query(person_id="test", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__ONLY_PERSON_ID


@pytest.mark.asyncio
async def test_films_get_query__only_sort_asc(films_service):
    result = films_service.get_query(sort="rating", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__ONLY_SORT_ASC


@pytest.mark.asyncio
async def test_films_get_query__only_sort_desc(films_service):
    result = films_service.get_query(sort="-rating", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__ONLY_SORT_DESC


@pytest.mark.asyncio
async def test_films_get_query__query_and_sort_asc(films_service):
    result = films_service.get_query(query="test", sort="rating", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__QUERY_AND_SORT_ASC


@pytest.mark.asyncio
async def test_films_get_query__genre_id_and_sort_asc(films_service):
    result = films_service.get_query(genre_id="test", sort="rating", is_subscriber=True)
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__GENRE_ID_AND_SORT_ASC


@pytest.mark.asyncio
async def test_films_get_query__person_id_and_sort_asc(films_service):
    result = films_service.get_query(
        person_id="test", sort="rating", is_subscriber=True
    )
    assert orjson.loads(result) == EXPECTED_QUERY_TO_ES__PERSON_ID_AND_SORT_ASC


@pytest.mark.asyncio
async def test_films_get_query__query_and_person_id_and_sort_asc(films_service):
    result = films_service.get_query(
        query="test", person_id="test", sort="rating", is_subscriber=True
    )
    assert (
        orjson.loads(result) == EXPECTED_QUERY_TO_ES__QUERY_AND_PERSON_ID_AND_SORT_ASC
    )


@pytest.mark.asyncio
async def test_films_get_query__genre_id_and_person_id_and_sort_asc(films_service):
    result = films_service.get_query(
        genre_id="test", person_id="test", sort="rating", is_subscriber=True
    )
    assert (
        orjson.loads(result)
        == EXPECTED_QUERY_TO_ES__GENRE_ID_AND_PERSON_ID_AND_SORT_ASC
    )


@pytest.mark.asyncio
async def test_films_get_query__query_and_genre_id_and_person_id_and_sort_asc(
    films_service,
):
    result = films_service.get_query(
        query="test",
        genre_id="test",
        person_id="test",
        sort="rating",
        is_subscriber=True,
    )
    assert (
        orjson.loads(result)
        == EXPECTED_QUERY_TO_ES__QUERY_AND_GENRE_ID_AND_PERSON_ID_AND_SORT_ASC
    )


@pytest.mark.asyncio
async def test_films_get_query__query_and_genre_id_and_person_id_and_sort_asc_and_unsubscribed(
    films_service,
):
    result = films_service.get_query(
        query="test", genre_id="test", person_id="test", sort="rating"
    )
    assert (
        orjson.loads(result)
        == EXPECTED_QUERY_TO_ES__QUERY_AND_GENRE_ID_AND_PERSON_ID_AND_SORT_ASC_AND_UNSUBSCRIBED
    )
