import json
import os
import urllib.request


def get_articles_host():
    return os.environ.get("ARTICLES_HOST", "example.com")


def get_article_uri(id):
    articles_host = get_articles_host()
    return f"https://{articles_host}/articles/{id}.html?ref=rss"


def fetch_article(id):
    uri = get_article_uri(id)
    with urllib.request.urlopen(uri) as response:
        return response.read().decode('utf-8')


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "This is articles"})
    }
