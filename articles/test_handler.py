import unittest
import os
from handler import get_articles_host


class TestHandler(unittest.TestCase):
    def test_placeholder(self):
        pass

    def test_get_articles_host_returns_env_value(self):
        os.environ["ARTICLES_HOST"] = "http://articles.example.com"
        self.assertEqual(get_articles_host(), "http://articles.example.com")
        del os.environ["ARTICLES_HOST"]

    def test_get_articles_host_returns_none_when_not_set(self):
        if "ARTICLES_HOST" in os.environ:
            del os.environ["ARTICLES_HOST"]
        self.assertIsNone(get_articles_host())


if __name__ == "__main__":
    unittest.main()
