from app.services.schemas import ORJSONModel


class InputGenreSchema(ORJSONModel):
    id: str
    name: str
    description: str


class InputListGenreSchema(ORJSONModel):
    __root__: list[InputGenreSchema]

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)
