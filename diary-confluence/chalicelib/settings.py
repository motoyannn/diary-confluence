import os


class Settings:

    CONFLUENCE = {
        "URL": os.environ["CONFLUENCE_URL"],
        "TOKEN": os.environ["CONFLUENCE_TOKEN"],
        "USER": os.environ["CONFLUENCE_USER"],
        "SPACE": os.environ["CONFLUENCE_SPACE"],
    }
