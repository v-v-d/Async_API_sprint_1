from app.services.schemas import ORJSONModel
from typing import Optional


class InputPersonSchema(ORJSONModel):
    id: str
    full_name: str
    roles: list[str]
    film_ids: list[str]


class InputFilmPersonSchema(ORJSONModel):
    id: str
    rating: Optional[float]
    title: str


class InputListFilmPersonSchema(ORJSONModel):
    __root__: list[InputFilmPersonSchema]

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)


class InputListPersonSchema(ORJSONModel):
    __root__: list[InputPersonSchema]

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)
