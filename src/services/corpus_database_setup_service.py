from data_access import autocomplete_data_access
from services.words_corpus_service import WordsCorpusService
from tqdm import tqdm


def add_corpus_words_to_db(bulk_size=100):
    """
    Assuming the existence of a unique constraint on words
    """
    service = WordsCorpusService()
    word_rows = []
    for word in tqdm(service.get_words()):
        word_rows.append({
            "word": word,
            "score": service.get_word_frequency(word),
        })
        if len(word_rows) >= bulk_size:
            autocomplete_data_access.update_corpus_words(word_rows)
            word_rows = []
    if len(word_rows) > 0:
        autocomplete_data_access.update_corpus_words(word_rows)


if __name__ == '__main__':
    add_corpus_words_to_db()
