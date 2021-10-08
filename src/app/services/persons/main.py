from logging import getLogger

logger = getLogger(__name__)


class PersonsService:
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic
