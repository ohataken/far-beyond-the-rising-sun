import unittest
import os
from unittest.mock import patch
from handler import get_summaries_host, get_summary_uri


class TestHandler(unittest.TestCase):
    def test_placeholder(self):
        pass

    @patch.dict(os.environ, {"SUMMARIES_HOST": "http://summaries.example.com"})
    def test_get_summaries_host_returns_env_value(self):
        self.assertEqual(get_summaries_host(), "http://summaries.example.com")

    def test_get_summaries_host_returns_default_when_not_set(self):
        if "SUMMARIES_HOST" in os.environ:
            del os.environ["SUMMARIES_HOST"]
        self.assertEqual(get_summaries_host(), "example.com")

    @patch.dict(os.environ, {"SUMMARIES_HOST": "summaries.example.com"})
    def test_get_summary_uri_returns_correct_uri(self):
        result = get_summary_uri("articles", "12345")
        self.assertEqual(result, "https://summaries.example.com/articles/12345.rdf")


if __name__ == "__main__":
    unittest.main()
