from app.services.schemas import ORJSONModel


class GenreSchema(ORJSONModel):
    id: str
    name: str
