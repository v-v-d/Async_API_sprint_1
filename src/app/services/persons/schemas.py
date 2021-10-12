from app.services.schemas import ORJSONModel


class InputPersonSchema(ORJSONModel):
    id: str
    full_name: str
    roles: list[str]
    film_ids: list[str]
