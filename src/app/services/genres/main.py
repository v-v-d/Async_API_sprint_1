from logging import getLogger

logger = getLogger(__name__)


class GenresService:
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic
