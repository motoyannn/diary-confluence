from atlassian import Confluence

from .confluence import create_page


def daily(confluence: Confluence):
    create_page(confluence)
