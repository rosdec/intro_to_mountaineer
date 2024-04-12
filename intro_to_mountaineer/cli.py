from click import command, option
from mountaineer.cli import handle_runserver, handle_watch, handle_build
from mountaineer.database.cli import handle_createdb
from mountaineer.io import async_to_sync

from intro_to_mountaineer import models
from intro_to_mountaineer.config import AppConfig


@command()
@option("--port", default=5006, help="Port to run the server on")
def runserver(port: int):
    handle_runserver(
        package="intro_to_mountaineer",
        webservice="intro_to_mountaineer.main:app",
        webcontroller="intro_to_mountaineer.app:controller",
        port=port,
    )


@command()
def watch():
    handle_watch(
        package="intro_to_mountaineer",
        webcontroller="intro_to_mountaineer.app:controller",
    )


@command()
def build():
    handle_build(
        webcontroller="intro_to_mountaineer.app:controller",
    )


@command()
@async_to_sync
async def createdb():
    _ = AppConfig() # type: ignore

    await handle_createdb(models)