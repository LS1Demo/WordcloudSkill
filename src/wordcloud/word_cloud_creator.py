import base64
from io import BytesIO

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class WordCloudCreator:

    @staticmethod
    def create_wordcloud(text: str) -> str:
        wordcloud = WordCloud().generate(text)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        wordcloud = WordCloud(max_font_size=40).generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        buf = BytesIO()
        plt.savefig(buf, format='jpg')
        buf.seek(0)
        wordcloud_image = base64.b64encode(buf.read()).decode('utf-8')

        return wordcloud_image