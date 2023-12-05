from da import autocomplete_data_access
import nltk
from nltk.tokenize import word_tokenize


def get_autocomplete_options(username: str, prefix: str, limit=10):
    option_to_score = autocomplete_data_access.get_autocomplete_options(prefix=prefix, limit=limit)
    user_option_to_score = autocomplete_data_access.get_user_autocomplete_options(username=username, prefix=prefix, limit=10)
    remove_redundant_options(option_to_score, user_option_to_score)
    option_to_score.update(user_option_to_score)
    option_to_score = sorted(option_to_score.items(), key=lambda x: x[1], reverse=True)
    option_to_score = option_to_score[:limit]
    return [x[0] for x in option_to_score]


def remove_redundant_options(option_to_score, user_option_to_score):
    """
    removes the option with the lower score from one of the dicts in case of duplication
    """
    for option, score in option_to_score.items():
        if option in user_option_to_score.keys():
            if score > user_option_to_score[option]:
                del user_option_to_score[option]
            else:
                del option_to_score[option]


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
    add_text(username="testuser@gmail.com", text="the dog")