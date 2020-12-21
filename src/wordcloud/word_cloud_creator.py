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

        green = '#00ff00'
        red = '#ff0000'
        color_to_words = {green: set([]), red: set([])}
        tokens = text.split(sep=" ")
        for token in tokens:
            text_blob = TextBlob(token)
            if text_blob.polarity > 0.0:
                color_to_words[green].add(token)
            elif text_blob.polarity < 0.0:
                color_to_words[red].add(token)

        image_colors = GroupedColorFunc(color_to_words, default_color='grey')

        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=2)

        buf = BytesIO()
        plt.savefig(buf, format='jpg')
        buf.seek(0)
        wordcloud_image = base64.b64encode(buf.read()).decode('utf-8')

        return wordcloud_image
