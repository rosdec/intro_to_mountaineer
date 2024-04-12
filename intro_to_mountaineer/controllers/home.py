from mountaineer import ControllerBase

class HomeController(ControllerBase):
    url = "/"
    view_path = "/app/home/page.tsx"

    async def render(
        self
    ) -> None:
        pass
 