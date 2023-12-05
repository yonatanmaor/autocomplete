import unittest
from unittest.mock import patch, call
from services import autocomplete_service


class TestAutocompleteService(unittest.TestCase):

    @patch('da.autocomplete_data_access.get_user_word_scores')
    @patch('da.autocomplete_data_access.update_user_word_score')
    def test_add_text(self, get_user_word_scores_mock, update_user_word_score_mock):
        with unittest.mock.patch("da.autocomplete_data_access.get_user_word_scores") as get_user_word_scores_mock:
            with unittest.mock.patch("da.autocomplete_data_access.update_user_word_score") as update_user_word_score_mock:
                get_user_word_scores_mock.return_value = {'word1': 4, 'word2': 3}
                update_user_word_score_mock.return_value = None
                autocomplete_service.add_text('testuser@gmail.com', 'Hey word1 word1 and word2')

                expected_calls = [call(username="testuser@gmail.com", word="hey", score=1),
                                  call(username="testuser@gmail.com", word="word1", score=6),
                                  call(username="testuser@gmail.com", word="and", score=1),
                                  call(username="testuser@gmail.com", word="word2", score=4)]
                update_user_word_score_mock.assert_has_calls(expected_calls, any_order=True)
