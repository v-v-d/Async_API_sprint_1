from app.services.schemas import ORJSONModel


class ErrorSchema(ORJSONModel):
    detail: str
