import base64
import logging
from io import BytesIO
import numpy as np

from PIL import Image

from src.wordcloud.word_cloud_creator import WordCloudCreator

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    log.info(f"Received payload: {payload}")
    log.info(f"Received context: {context}")

    log.info("Wordcloud started!")

    text = base64.b64decode(payload["text"].encode('utf-8')).decode('utf-8')
    if payload["mask"] == "":
        mask = None
    else:
        mask = np.array(Image.open(BytesIO(base64.b64decode(payload["mask"].encode('utf-8')))))

    image = WordCloudCreator.create_wordcloud(text, mask)

    log.info("Wordcloud finished!")

    return {"image": image}


def on_started(context: dict):
    print("Wordcloud skill started!")


def on_stopped(context: dict):
    print("Wordcloud skill stopped!")


























#
