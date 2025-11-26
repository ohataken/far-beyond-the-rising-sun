import json
import os


def get_articles_host():
    return os.environ.get("ARTICLES_HOST")


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "This is articles"})
    }
