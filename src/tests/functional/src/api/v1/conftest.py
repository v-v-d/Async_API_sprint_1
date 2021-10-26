from unittest.mock import AsyncMock

import pytest

from app.services.base import BaseServiceError, NotFoundError
from app.services import base


@pytest.fixture
def v1_films_url():
    return "/api/v1/films/"


@pytest.fixture
async def mocked_es_invalid_response(monkeypatch):
    monkeypatch.setattr(base.ElasticsearchService, "_execute", AsyncMock())
    base.ElasticsearchService._execute.return_value = {}  # noqa


@pytest.fixture
async def mocked_es_unexpected_exception(monkeypatch):
    monkeypatch.setattr(base.ElasticsearchService, "_execute", AsyncMock())
    base.ElasticsearchService._execute.side_effect = BaseServiceError  # noqa


@pytest.fixture
async def mocked_es_not_found_error(monkeypatch):
    monkeypatch.setattr(base.ElasticsearchService, "_execute", AsyncMock())
    base.ElasticsearchService._execute.side_effect = NotFoundError  # noqa
