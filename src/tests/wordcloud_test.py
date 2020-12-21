import unittest

from src.wordcloud.word_cloud_creator import WordCloudCreator


class WordCloudBaseTest(unittest.TestCase):

    @staticmethod
    def test_wordcloud():
        image = WordCloudCreator.create_wordcloud("My first wordcloud!")
        print(image)

    if __name__ == '__main__':
        unittest.main()
