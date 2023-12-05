from da import sqlite_data_access


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


def get_user_word_scores(username: str, words: list[str] = None, page: int = None, page_size: int = None):
    query = """
    SELECT word, score FROM user_word_scores
    WHERE username = ?
    """
    params = [username]
    if words is not None:
        query += " AND word IN (?)"
        params += words
    query += " ORDER BY score DESC"
    if page is not None and page_size is not None:
        query += " LIMIT ? OFFSET ?"
        params += [page_size, (page - 1) * page_size]
    else:
        params = [username, ", ".join(words)]
    results = sqlite_data_access.execute_query(query, params=params)
    word_to_score = {x[0]: x[1] for x in results}
    return word_to_score


def update_user_word_score(username: str, word: str, score: int):
    sqlite_data_access.upsert_bulk_records("user_word_scores", [{
        "username": username,
        "word": word,
        "score": score
    }])


if __name__ == '__main__':
    # pass
    get_user_word_scores("testuser@gmail.com", ["test1", "test2"])
