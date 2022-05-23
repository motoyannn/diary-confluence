from ..common.client import Client
from ..common.settings import Settings
from .confluence import create_page


def daily(client: Client, settings: Settings):
    create_page(client.confluence, settings)
