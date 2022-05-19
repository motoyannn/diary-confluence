from chalice import Chalice, Cron

from chalicelib.common.client import confluence
from chalicelib.functions import daily as daily_func

app = Chalice(app_name="diary-confluence", debug=True)


# TODO: Manually change the cron expression to match your needs.
# @app.schedule(Cron(0, 21, "*", "*", "?", "*"))
# def daily_event(event):
@app.route("/")
def index():
    daily_func(confluence)
    return {"message": "success"}
