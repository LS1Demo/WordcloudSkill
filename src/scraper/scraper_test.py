import unittest

from src.scraper.scraper import Scraper


class ScraperBaseTest(unittest.TestCase):

    def test_scraper(self) -> None:
        text = Scraper.get_plain_text_from_url("https://en.wikipedia.org/wiki/Artificial_intelligence")
        self.assertTrue("Artificial Intelligence" in text)
