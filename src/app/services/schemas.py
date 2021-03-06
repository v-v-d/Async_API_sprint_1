from typing import Any, Union, List

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ORJSONModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class BaseListRootModel(ORJSONModel):
    __root__: List

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)


class MultiMatchQuerySchema(ORJSONModel):
    query: str
    fields: list[str]
    fuzziness: str = "AUTO"


class MultiMatchSchema(ORJSONModel):
    multi_match: MultiMatchQuerySchema


class MatchSchema(ORJSONModel):
    match: dict[str, Any]


class MustSchema(ORJSONModel):
    must: list[ORJSONModel]


class TermSchema(ORJSONModel):
    term: dict[str, Any]


class ShouldSchema(ORJSONModel):
    should: list[ORJSONModel]


class BoolSchema(ORJSONModel):
    bool: dict[str, list[ORJSONModel]]


class OrderSchema(ORJSONModel):
    order: str


class SortSchema(ORJSONModel):
    sort: dict[str, OrderSchema]


class QuerySchema(ORJSONModel):
    query: BoolSchema


class NestedSchema(ORJSONModel):
    path: str
    query: BoolSchema


class FilterSchema(ORJSONModel):
    nested: NestedSchema


class RootQuerySchema(ORJSONModel):
    __root__: dict[str, Union[BoolSchema, SortSchema]]


class DocSchema(ORJSONModel):
    source: dict[str, Any] = Field(..., alias="_source")


class HitsSchema(ORJSONModel):
    hits: list[DocSchema]


class ResponseSchema(ORJSONModel):
    hits: HitsSchema
