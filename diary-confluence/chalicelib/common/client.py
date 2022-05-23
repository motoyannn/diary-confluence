from atlassian import Confluence

from .settings import Settings


class Client:
    def __init__(self, settings: Settings):
        self._confluence = Confluence(
            url=settings.CONFLUENCE["URL"],
            username=settings.CONFLUENCE["USER"],
            password=settings.CONFLUENCE["TOKEN"],
        )

    @property
    def confluence(self):
        return self._confluence
