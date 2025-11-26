import unittest
import os
from handler import get_articles_host, get_article_uri


class TestHandler(unittest.TestCase):
    def test_placeholder(self):
        pass

    def test_get_articles_host_returns_env_value(self):
        self.assertEqual(get_articles_host(), "example.com")

    def test_get_articles_host_returns_default_when_not_set(self):
        if "ARTICLES_HOST" in os.environ:
            del os.environ["ARTICLES_HOST"]
        self.assertEqual(get_articles_host(), "example.com")

    def test_get_article_uri_returns_correct_format(self):
        os.environ["ARTICLES_HOST"] = "articles.example.com"
        result = get_article_uri("12345")
        self.assertEqual(result, "https://articles.example.com/articles/12345.html?ref=rss")
        del os.environ["ARTICLES_HOST"]


if __name__ == "__main__":
    unittest.main()
