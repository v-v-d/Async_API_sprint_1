import jsonpickle
from aiocache import cached
from aiocache.backends.redis import RedisCache
from aiocache.serializers import BaseSerializer

from app.apm import traced
from app.settings import settings


class JsonPickleSerializer(BaseSerializer):  # pragma: no cover
    def dumps(self, value):
        return jsonpickle.encode(value)

    def loads(self, value):
        if not value:
            return None

        return jsonpickle.decode(value)


DEFAULT_CACHE_CONFIG = {
    "cache": RedisCache,
    "endpoint": settings.CACHE.REDIS_HOST,
    "port": settings.CACHE.REDIS_PORT,
    "serializer": JsonPickleSerializer(),
    "ttl": settings.CACHE.TTL,
}

CACHE_CONFIG = {} if settings.TESTING else DEFAULT_CACHE_CONFIG


def cached_and_traced(func):
    """
    Decorator that allow to cache and trace aiocache requests.
    """
    return traced("aiocache")(cached(**CACHE_CONFIG)(func))
