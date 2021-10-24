from unittest.mock import AsyncMock

import pytest

from app.services.base import BaseServiceError, NotFoundError
from app.services.films import main
from app.services.films.main import FilmsService


@pytest.fixture
def v1_films_url():
    return "/api/v1/films/"


@pytest.fixture
async def mocked_es_invalid_response(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.return_value = {}  # noqa


@pytest.fixture
async def mocked_es_unexpected_exception(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.side_effect = BaseServiceError  # noqa


@pytest.fixture
async def mocked_es_not_found_error(monkeypatch):
    monkeypatch.setattr(FilmsService, "_request_elastic", AsyncMock())
    main.FilmsService._request_elastic.side_effect = NotFoundError  # noqa