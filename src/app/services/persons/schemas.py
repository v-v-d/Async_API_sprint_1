from app.services.schemas import ORJSONModel


class InputPersonSchema(ORJSONModel):
    id: str
    full_name: str
    roles: list[str]
    film_ids: list[str]


class InputListPersonSchema(ORJSONModel):
    __root__: list[InputPersonSchema]

    def __iter__(self):
        return self.__root__.__iter__()

    def __getitem__(self, item):
        return self.__root__.__getitem__(item)