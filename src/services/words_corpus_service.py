import nltk
from nltk.corpus import brown


class WordsCorpusService:

    def __init__(self):
        self.corpus = brown
        self.words = self.get_words()
        self.words_frequency = nltk.FreqDist(self.get_words())

    def get_categories(self):
        return self.corpus.categories()

    def get_words(self):
        return self.corpus.words()

    def get_word_frequency(self, word: str):
        return self.words_frequency[word]


if __name__ == '__main__':
    service = WordsCorpusService()
    for word in service.get_words():
        print(word, service.get_word_frequency(word))


