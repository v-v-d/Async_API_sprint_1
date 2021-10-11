from typing import Optional

from app.services.schemas import ORJSONModel


class InputItemSchema(ORJSONModel):
    id: str
    name: str


class InputFilmSchema(ORJSONModel):
    id: str
    rating: Optional[float]
    title: str
    description: str
    genres: list[InputItemSchema]
    directors: list[InputItemSchema]
    actors: list[InputItemSchema]
    writers: list[InputItemSchema]
    actors_names: list[str]
    writers_names: list[str]
    directors_names: list[str]


class InputListFilmSchema(ORJSONModel):
    __root__: list[InputFilmSchema]

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)


class QuerySchema(ORJSONModel):
    query: str
    fields: list[str] = ["title", "description"]


class MatchSchema(ORJSONModel):
    multi_match: QuerySchema
