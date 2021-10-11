from typing import Optional

from app.settings import settings

from app.services.schemas import ORJSONModel


class DefaultParamsSchema(ORJSONModel):
    page: int
    size: int


def get_default_query_params(
    page: Optional[int] = settings.ES.DEFAULT_PAGE,
    size: Optional[int] = settings.ES.DEFAULT_PAGE_SIZE,
) -> DefaultParamsSchema:
    return DefaultParamsSchema(page=page, size=size)
