import jsonpickle
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
    "ttl": settings.CACHE.TTL,
}
