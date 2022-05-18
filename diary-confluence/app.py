from datetime import datetime

from atlassian import Confluence
from chalice import Chalice, Cron
from dateutil import tz

from chalicelib import Settings

app = Chalice(app_name="diary-confluence", debug=True)


# TODO: Manually change the cron expression to match your needs.
@app.schedule(Cron(0, 21, "*", "*", "?", "*"))
def daily_event():
    # https://atlassian-python-api.readthedocs.io/confluence.html
    confluence = Confluence(
        url=Settings.CONFLUENCE["URL"],
        username=Settings.CONFLUENCE["USER"],
        password=Settings.CONFLUENCE["TOKEN"],
    )
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
        parent_id=2350252104,
        type="page",
        representation="storage",
        editor="v2",
    )
    return {"message": "success"}
