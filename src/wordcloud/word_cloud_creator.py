import base64
from io import BytesIO

from os import path
from PIL import Image
import numpy as np
import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class WordCloudCreator:

    @staticmethod
    def create_wordcloud(text: str, mask: np.ndarray = None) -> str:
        wordcloud = WordCloud(background_color="white", max_words=100, mask=mask, max_font_size=40, width=1920, height=1080).generate(text)

        plt.figure(figsize=[20, 20])
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        buf = BytesIO()
        plt.savefig(buf, format='jpg')
        buf.seek(0)
        wordcloud_image = base64.b64encode(buf.read()).decode('utf-8')

        return wordcloud_image
