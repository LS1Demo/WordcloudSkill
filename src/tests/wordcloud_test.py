import base64
import unittest

from src.handler import evaluate
from src.wordcloud.word_cloud_creator import WordCloudCreator


class WordCloudBaseTest(unittest.TestCase):

    # @staticmethod
    # def test_wordcloud():
    #     image = WordCloudCreator.create_wordcloud("My first wordcloud!")
    #     print(image)

    @staticmethod
    def test_wordcloud():
        text = "The first AIOS wordcloud!"
        text_b64 = base64.b64encode(bytes(text, 'utf-8')).decode('utf-8')

        image = evaluate({"text": text_b64}, {})
        print(image)

    if __name__ == '__main__':
        unittest.main()
