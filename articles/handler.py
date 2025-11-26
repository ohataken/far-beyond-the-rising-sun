import json
import os


def get_articles_host():
    return os.environ.get("ARTICLES_HOST")


def get_article_uri(id):
    articles_host = get_articles_host()
    return f"https://{articles_host}/articles/{id}.html?ref=rss"


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "This is articles"})
    }
