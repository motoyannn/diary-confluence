from datetime import datetime

from atlassian import Confluence
from chalicelib.common.settings import Settings
from dateutil import tz


def create_page(confluence: Confluence):
    """
    Create a new page in Confluence.

    :param confluence: Confluence client
    :return: None
    """
    JST = tz.gettz("Asia/Tokyo")
    title = datetime.now(JST).strftime("test__%Y-%m-%d_")
    body = """
    ## やること

    ### RevComm

    ### Kal

    ### Private
    """
    confluence.create_page(
        space=Settings.CONFLUENCE["SPACE"],
        title=title,
        body=body,
        parent_id=Settings.CONFLUENCE["PARENT_PAGE"],
        type="page",
        representation="storage",
        editor="v2",
    )
