import unittest

from src.scraper.scraper import Scraper


class ScraperBaseTest(unittest.TestCase):

    @staticmethod
    def test_scraper() -> None:
        text = Scraper.get_plain_text_from_url("https://en.wikipedia.org/wiki/Artificial_intelligence")
        print(text)
