from mountaineer.app import AppController
from mountaineer.js_compiler.postcss import PostCSSBundler
from mountaineer.render import LinkAttribute, Metadata

from intro_to_mountaineer.config import AppConfig
from intro_to_mountaineer.controllers.home import HomeController

controller = AppController(
    config=AppConfig(),  # type: ignore

)

controller.register(HomeController())
