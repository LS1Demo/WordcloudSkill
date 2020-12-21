import base64
import logging
from io import BytesIO
import numpy as np

from PIL import Image

from src.scraper.scraper import Scraper
from src.wordcloud.word_cloud_creator import WordCloudCreator

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    log.info("Wordcloud started!")

    text = ""
    if payload["text"]:
        text = base64.b64decode(payload["text"].encode('utf-8')).decode('utf-8')
    if payload["url"]:
        text = Scraper.get_plain_text_from_url(payload["url"])
    assert text, "text could not be set"

    if payload["mask"] == "":
        mask = None
    else:
        mask = np.array(Image.open(BytesIO(base64.b64decode(payload["mask"].encode('utf-8')))))

    image = WordCloudCreator.create_wordcloud(text=text, mask=mask, config=payload["config"])

    log.info("Wordcloud finished!")

    return {"image": image}


def on_started(context: dict):
    print("Wordcloud skill started!")


def on_stopped(context: dict):
    print("Wordcloud skill stopped!")


























#
