from app.services.schemas import ORJSONModel, BaseListRootModel


class InputGenreSchema(ORJSONModel):
    id: str
    name: str
    description: str


class InputListGenreSchema(BaseListRootModel):
    __root__: list[InputGenreSchema]
