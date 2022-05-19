import os


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
            "URL": os.environ["CONFLUENCE_URL"],
            "TOKEN": os.environ["CONFLUENCE_TOKEN"],
            "USER": os.environ["CONFLUENCE_USER"],
            "SPACE": os.environ["CONFLUENCE_SPACE"],
            "PARENT_PAGE": os.environ["CONFLUENCE_PARENT_PAGE"],
        }
    )
