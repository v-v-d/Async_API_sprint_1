import typer
import uvicorn
from IPython import embed

from app.settings import settings

app = typer.Typer()


@app.command()
def shell():
    embed()


@app.command()
def runserver():
    uvicorn.run(**settings.UVICORN.dict())


if __name__ == "__main__":
    app()
