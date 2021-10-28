from unittest.mock import AsyncMock

import pytest

from app.services.base import BaseServiceError, NotFoundError
from app.services import base


@pytest.fixture
def v1_films_url():
    return "/api/v1/films/"


@pytest.fixture
def v1_genres_url():
    return "/api/v1/genres/"


@pytest.fixture
def v1_persons_url():
    return "/api/v1/persons/"


@pytest.fixture
def v1_search_persons_url():
    return "/api/v1/search/persons"


@pytest.fixture
def v1_search_film_url():
    return "/api/v1/search/films"


@pytest.fixture
async def mocked_es_invalid_response(monkeypatch):
    monkeypatch.setattr(base.BaseService, "_request_elastic", AsyncMock())
    base.BaseService._request_elastic.return_value = {}  # noqa


@pytest.fixture
async def mocked_es_unexpected_exception(monkeypatch):
    monkeypatch.setattr(base.BaseService, "_request_elastic", AsyncMock())
    base.BaseService._request_elastic.side_effect = BaseServiceError  # noqa


@pytest.fixture
async def mocked_es_not_found_error(monkeypatch):
    monkeypatch.setattr(base.BaseService, "_request_elastic", AsyncMock())
    base.BaseService._request_elastic.side_effect = NotFoundError  # noqa
