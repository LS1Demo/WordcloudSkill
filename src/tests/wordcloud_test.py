import base64
import unittest
from io import BytesIO
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from os import path

from PIL import Image

from src.handler import evaluate


class WordCloudBaseTest(unittest.TestCase):

    @staticmethod
    def test_wordcloud():
        mask = Image.open("wordcloud_logo.png")
        buf = BytesIO()
        mask.save(buf, format="png")
        buf.seek(0)
        mask_b64 = base64.b64encode(buf.read()).decode('utf-8')

        with open('documentation.txt', 'rb') as file:
            text_bytes = BytesIO(file.read())
            text_b64 = base64.b64encode(text_bytes.read()).decode('utf-8')

        url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        response = evaluate({"text": text_b64,
                             "mask": mask_b64,
                             "url": url,
                             "config": '{"max_words": 100, "max_font_size": 123, "height": 500, "width": 500}'},
                            {})

        # show word cloud image
        image_input = base64.b64decode(response["image"].encode('utf-8'))
        input_buf = BytesIO()
        input_buf.write(image_input)
        input_buf.seek(0)
        im = Image.open(input_buf)
        im.show()
        input_buf.close()
        im1 = im.save("wordcloud.jpg")

    @staticmethod
    @unittest.skip(reason="currently not needed")
    def test_wordcloud_mask_standalone():
        text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et " \
               "justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, " \
               "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd " \
               "gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
        mask = np.array(Image.open("wordcloud_logo.png"))

        wordcloud = WordCloud(background_color="white", max_words=100, mask=mask).generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    if __name__ == '__main__':
        unittest.main()
