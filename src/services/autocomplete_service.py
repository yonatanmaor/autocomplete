from data_access import autocomplete_data_access
import nltk
from nltk.tokenize import word_tokenize


def get_autocomplete_options(username: str, prefix: str):
    options = autocomplete_data_access.get_autocomplete_options(username=username, prefix=prefix, limit=10)
    result = [x[0] for x in options]
    return result


def add_text(username, text):
    text = text.lower()
    words = word_tokenize(text)
    word_to_count = _count_words(words)
    existing_word_to_score = autocomplete_data_access.get_user_word_scores(username=username,
                                                                           words=list(word_to_count.keys()))
    for word in existing_word_to_score:
        word_to_count[word] += existing_word_to_score[word]

    for word, count in word_to_count.items():
        autocomplete_data_access.update_user_word_score(username=username, word=word, score=count)


def get_user_word_scores(username: str, page: int, page_size: int):
    return autocomplete_data_access.get_user_word_scores(username=username, page=page, page_size=page_size)


def _count_words(words):
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    return word_to_count


if __name__ == '__main__':
    add_text(username="testuser@gmail.com", text="the dog jumped over the lazy fox and then jumped on the other dog")