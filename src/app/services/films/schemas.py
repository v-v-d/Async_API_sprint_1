from app.services.schemas import ORJSONModel


class FilmSchema(ORJSONModel):
    id: str
    title: str
    description: str
