from app.services.schemas import ORJSONModel


class PersonSchema(ORJSONModel):
    id: str
    full_name: str
    role: str
