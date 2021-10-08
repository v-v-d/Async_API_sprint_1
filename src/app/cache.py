from enum import Enum

import jsonpickle
from aiocache import Cache
from aiocache.backends.redis import RedisCache
from aiocache.serializers import BaseSerializer
from app.settings import settings


class JsonPickleSerializer(BaseSerializer):
    def dumps(self, value):
        return jsonpickle.encode(value)

    def loads(self, value):
        if not value:
            return None

        return jsonpickle.decode(value)


CACHE_CONFIG = {
    "cache": RedisCache,
    "endpoint": settings.CACHE.REDIS_HOST,
    "port": settings.CACHE.REDIS_PORT,
    "serializer": JsonPickleSerializer(),
}

cache = Cache(
    cache_class=RedisCache,
    endpoint=CACHE_CONFIG["endpoint"],
    port=CACHE_CONFIG["port"],
    serializer=CACHE_CONFIG["serializer"]
)


class CacheNamespaceEnum(str, Enum):
    films = "films"
    persons = "persons"
    genres = "genres"


def build_cache_key(
    namespace: CacheNamespaceEnum, key: int | str
) -> str:
    return f"{namespace.value}:{key}"
