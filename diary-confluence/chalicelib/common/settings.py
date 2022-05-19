import os

import boto3

ssm = boto3.client("ssm")


class Settings:

    ENV = os.environ.get("ENV", "local")

    CONFLUENCE = (
        {
            # NOTE: run locally
            "URL": os.environ["CONFLUENCE_URL"],
            "TOKEN": os.environ["CONFLUENCE_TOKEN"],
            "USER": os.environ["CONFLUENCE_USER"],
            "SPACE": os.environ["CONFLUENCE_SPACE"],
            "PARENT_PAGE": os.environ["CONFLUENCE_PARENT_PAGE"],
        }
        if ENV == "local"
        else {
            # NOTE: run on lambda
            "URL": ssm.get_parameter(Name="/confluence/URL")["Parameter"]["Value"],
            "TOKEN": ssm.get_parameter(Name="/confluence/TOKEN")["Parameter"]["Value"],
            "USER": ssm.get_parameter(Name="/confluence/USER")["Parameter"]["Value"],
            "SPACE": ssm.get_parameter(Name="/confluence/SPACE")["Parameter"]["Value"],
            "PARENT_PAGE": ssm.get_parameter(Name="/confluence/PARENT_PAGE")[
                "Parameter"
            ]["Value"],
        }
    )
