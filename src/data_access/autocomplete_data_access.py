from data_access import sqlite_data_access


def get_autocomplete_options(username: str, prefix: str, limit: int):
    """
    return the most common words, up to 'limit' words, that start with 'prefix'
    sorted by their score (popularity of the word)
    """
    query = """
    SELECT word, score FROM word_scores
    WHERE word LIKE ?
    ORDER BY score DESC
    LIMIT ?
    """
    return sqlite_data_access.execute_query(query, params=[f"{prefix}%", limit])


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

