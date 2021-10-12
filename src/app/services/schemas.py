from typing import Any

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ORJSONModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class DocSchema(ORJSONModel):
    source: dict[str, Any] = Field(..., alias="_source")


class HitsSchema(ORJSONModel):
    hits: list[DocSchema]


class ResponseSchema(ORJSONModel):
    hits: HitsSchema
