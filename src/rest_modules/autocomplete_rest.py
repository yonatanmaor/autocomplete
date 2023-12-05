import json

from flask import Blueprint

from rest_modules import rest_utils
from services import autocomplete_service

autocomplete_blueprint = Blueprint('autocomplete_api', __name__)


@autocomplete_blueprint.route('/options/<string:prefix>', methods=['GET'])
def get_autocomplete_options(prefix: str):
    username = rest_utils.get_authenticated_username()
    options_list = autocomplete_service.get_autocomplete_options(username=username,
                                                                 prefix=prefix)
    return json.dumps(options_list)
