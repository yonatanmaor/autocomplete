from flask import request


def get_authenticated_username():
    """
    Returns the current authenticated user using flask.
    Since I didn't implement authentication - returning a fixed string
    """
    return "testuser@gmail.com"


def get_int_param(param_name: str, default: int = 1):
    value = request.args.get(param_name)
    if value is None:
        raise KeyError
    try:
        value = int(value)
    except ValueError:
        value = default
    return value
