import unittest
import os
from handler import get_summaries_host


class TestHandler(unittest.TestCase):
    def test_placeholder(self):
        pass

    def test_get_summaries_host_returns_env_value(self):
        os.environ["SUMMARIES_HOST"] = "http://summaries.example.com"
        self.assertEqual(get_summaries_host(), "http://summaries.example.com")
        del os.environ["SUMMARIES_HOST"]

    def test_get_summaries_host_returns_none_when_not_set(self):
        if "SUMMARIES_HOST" in os.environ:
            del os.environ["SUMMARIES_HOST"]
        self.assertIsNone(get_summaries_host())


if __name__ == "__main__":
    unittest.main()
