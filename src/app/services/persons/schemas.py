from typing import Optional

from app.services.schemas import ORJSONModel, BaseListRootModel


class InputPersonSchema(ORJSONModel):
    id: str
    full_name: str
    roles: list[str]
    film_ids: list[str]


class InputFilmPersonSchema(ORJSONModel):
    id: str
    rating: Optional[float]
    title: str


class InputListFilmPersonSchema(BaseListRootModel):
    __root__: list[InputFilmPersonSchema]


class InputListPersonSchema(BaseListRootModel):
    __root__: list[InputPersonSchema]
