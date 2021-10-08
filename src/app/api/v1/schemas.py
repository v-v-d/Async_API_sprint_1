from pydantic import BaseModel


class FilmSchema(BaseModel):
    id: str
    title: str
