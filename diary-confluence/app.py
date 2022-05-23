import boto3
from chalice import Chalice, Cron

from chalicelib.common.client import Client
from chalicelib.common.settings import Settings
from chalicelib.functions import daily as daily_func

app = Chalice(app_name="diary-confluence", debug=True)
ssm = boto3.client("ssm")

settings = Settings(ssm)
client = Client(settings)

# TODO: Manually change the cron expression to match your needs.
# @app.schedule(Cron(0, 21, "*", "*", "?", "*"))
# def daily_event(event):
@app.route("/")
def index():
    daily_func(client, settings)
    return {"message": "success"}
