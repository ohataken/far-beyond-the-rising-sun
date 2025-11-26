import json
import os


def get_summaries_host():
    return os.environ.get("SUMMARIES_HOST")


def get_summary_uri(dir, id):
    summaries_host = get_summaries_host()
    return f"https://{summaries_host}/{dir}/{id}.rdf"


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "This is summaries"})
    }
