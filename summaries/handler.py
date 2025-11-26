import json
import os


def get_summaries_host():
    return os.environ.get("SUMMARIES_HOST")


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "This is summaries"})
    }
