import base64
from io import BytesIO
import random

import numpy as np
from textblob import TextBlob

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

from src.wordcloud.grouped_color_func import GroupedColorFunc


class WordCloudCreator:

    @staticmethod
    def create_wordcloud(text: str, mask: np.ndarray = None) -> str:
        wordcloud = WordCloud(background_color="white", max_words=5000, mask=mask,
                              max_font_size=72,
                              width=1000, height=623,
                              stopwords=STOPWORDS).generate(text)

        color_to_words = WordCloudCreator.calculate_color_shades()

        tokens = text.split(sep=" ")
        for token in tokens:
            text_blob = TextBlob(token)
            if text_blob.polarity > 0.0:
                hex_value = WordCloudCreator.create_hex_value_from_polarity(text_blob)
                green_color = WordCloudCreator.create_green_color_shade(hex_value)
                color_to_words[green_color].add(token)
            elif text_blob.polarity < 0.0:
                hex_value = WordCloudCreator.create_hex_value_from_polarity(text_blob)
                red_color = WordCloudCreator.create_red_color_shade(hex_value)
                color_to_words[red_color].add(token)

        image_colors = GroupedColorFunc(color_to_words, default_color='grey')
        wordcloud_image = WordCloudCreator.create_wordcloud_imagee(image_colors, wordcloud)

        return wordcloud_image

    @staticmethod
    def create_hex_value_from_polarity(text_blob):
        return hex(abs(int(text_blob.polarity * 255)))[2:].zfill(2)

    @staticmethod
    def create_red_color_shade(hex_value):
        return "#" + hex_value + "0000"

        plt.figure(figsize=(10, 6))
    @staticmethod
    def create_green_color_shade(hex_value):
        return "#00" + hex_value + "00"

    @staticmethod
    def create_wordcloud_imagee(image_colors, wordcloud):
        plt.figure(figsize=[20, 20])
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=2)

        buf = BytesIO()
        plt.savefig(buf, format='jpg')
        buf.seek(0)
        wordcloud_image = base64.b64encode(buf.read()).decode('utf-8')

        return wordcloud_image

    @staticmethod
    def calculate_color_shades():
        color_to_words = {}
        for i in range(0, 256):
            hex_value = hex(i)[2:].zfill(2)
            green_color = WordCloudCreator.create_green_color_shade(hex_value)
            color_to_words[green_color] = set([])
            red_color = WordCloudCreator.create_red_color_shade(hex_value)
            color_to_words[red_color] = set([])
        return color_to_words
