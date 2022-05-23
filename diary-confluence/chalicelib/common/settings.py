import os

import boto3


class Settings:

    def __init__(self, ssm: boto3.client):
        self.ssm = ssm
        self._env = os.environ.get("ENV", "local")
        if self._env == "local":
            self._confluence = {
                # NOTE: run locally
                "URL": os.environ["CONFLUENCE_URL"],
                "TOKEN": os.environ["CONFLUENCE_TOKEN"],
                "USER": os.environ["CONFLUENCE_USER"],
                "SPACE": os.environ["CONFLUENCE_SPACE"],
                "PARENT_PAGE": os.environ["CONFLUENCE_PARENT_PAGE"],
            }
        else:
            self._confluence = {
                "URL": self.ssm.get_parameter(Name="/automation/confluence/URL")["Parameter"]["Value"],
                "TOKEN": self.ssm.get_parameter(Name="/automation/confluence/TOKEN")["Parameter"]["Value"],
                "USER": self.ssm.get_parameter(Name="/automation/confluence/USER")["Parameter"]["Value"],
                "SPACE": self.ssm.get_parameter(Name="/automation/confluence/SPACE")["Parameter"]["Value"],
                "PARENT_PAGE": self.ssm.get_parameter(Name="/automation/confluence/PARENT_PAGE")[
                    "Parameter"
                ]["Value"],
            }

    
    @property
    def ENV(self):
        return self._env

    @property
    def CONFLUENCE(self):
        return self._confluence
