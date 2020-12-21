import base64
import unittest
from io import BytesIO

from src.handler import evaluate


class WordCloudBaseTest(unittest.TestCase):

    @staticmethod
    def test_wordcloud():
        with open('wordcloud_text_input', 'rb') as file:
            text_bytes = BytesIO(file.read())
            text_b64 = base64.b64encode(text_bytes.read()).decode('utf-8')

        image = evaluate({"text": text_b64}, {})
        print(image)

    @staticmethod
    @unittest.skip(reason="without file upload")
    def test_wordcloud():

        text = "The first AIOS wordcloud!"
        text_b64 = base64.b64encode(bytes(text, 'utf-8')).decode('utf-8')

        image = evaluate({"text": text_b64}, {})
        print(image)

    if __name__ == '__main__':
        unittest.main()
