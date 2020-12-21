from bs4 import BeautifulSoup as bs
from urllib.request import (urlopen, urlretrieve)
import re


class Scraper:
    @staticmethod
    def get_plain_text_from_url(url: str) -> str:
        soup = bs(urlopen(url))
        text = soup.get_text().strip()
        text = re.sub(r'(\n\s*)+\n+', '\n\n', text)
        print(text)
        return text
