import base64
import logging

from src.wordcloud.wordcloud import WordCloudCreator

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    log.info(f"Received payload: {payload}")
    log.info(f"Received context: {context}")

    log.info("Wordcloud started!")

    text = base64.b64decode(payload["text"].encode('utf-8'))

    image = WordCloudCreator.create_wordcloud(text)

    log.info("Wordcloud finished!")

    return {"image": base64.b64encode(image.encode("utf-8")).decode('utf-8')}


def on_started(context: dict):
    print("Wordcloud skill started!")


def on_stopped(context: dict):
    print("Wordcloud skill stopped!")


























#
