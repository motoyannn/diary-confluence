from atlassian import Confluence

from .settings import Settings

confluence = Confluence(
    url=Settings.CONFLUENCE["URL"],
    username=Settings.CONFLUENCE["USER"],
    password=Settings.CONFLUENCE["TOKEN"],
)
