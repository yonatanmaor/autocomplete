import json
import traceback

from flask import Blueprint, request

from rest_modules import rest_utils
from services import autocomplete_service

autocomplete_blueprint = Blueprint('autocomplete_api', __name__)


@autocomplete_blueprint.route('/options/<string:prefix>', methods=['GET'])
def get_autocomplete_options(prefix: str):
    username = rest_utils.get_authenticated_username()
    options_list = autocomplete_service.get_autocomplete_options(username=username,
                                                                 prefix=prefix)
    return json.dumps(options_list)


@autocomplete_blueprint.route('/add_text', methods=['POST'])
def add_text():
    """
    Adds all the words from the text to the database for autocomplete for the current user.
    If a word is already in the database, the score will be accumulated.
    """
    text = request.form.get('text')
    if not text:
        return json.dumps({"message", "No text provided"}), 400
    username = rest_utils.get_authenticated_username()
    try:
        autocomplete_service.add_text(username=username, text=text)
    except Exception as e:
        traceback.print_exc()
        return json.dumps({"message": "Failed to add text"}), 500
    return json.dumps({"message": "Success"})


@autocomplete_blueprint.route('/added_words', methods=['GET'])
def get_added_words():
    try:
        page = rest_utils.get_int_param(param_name='page', default=1)
        page_size = rest_utils.get_int_param(param_name='page_size', default=100)
    except KeyError:
        return json.dumps({"message": """Invalid parameters, please provide page (starting from 1) and page_size (up to 100) params"""}), 400
    if page_size > 100:
        page_size = 100
    username = rest_utils.get_authenticated_username()
    return json.dumps(autocomplete_service.get_user_word_scores(username=username,
                                                                page=page,
                                                                page_size=page_size))
