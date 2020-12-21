from nltk.corpus import stopwords

if __name__ == '__main__':
    stopwords = stopwords.words('english') + stopwords.words('german')
    print(stopwords)