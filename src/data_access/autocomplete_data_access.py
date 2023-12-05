from data_access import sqlite_data_access


def get_autocomplete_options(username: str, prefix: str):
    pass


def update_corpus_words(word_rows: list[dict]):
    """
    inserts or updates the corpus words in the database
    """
    sqlite_data_access.upsert_bulk_records("word_scores", word_rows)


def clear_corpus_words():
    sqlite_data_access.truncate_table("word_scores")


if __name__ == '__main__':
    pass
    # clear_corpus_words()

