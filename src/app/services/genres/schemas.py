from app.services.schemas import ORJSONModel


class InputGenreSchema(ORJSONModel):
    id: str
    name: str
    description: str


