from data_access import autocomplete_data_access


def get_autocomplete_options(username: str, prefix: str):
    options = autocomplete_data_access.get_autocomplete_options(username=username, prefix=prefix, limit=10)
    result = [x[0] for x in options]
    return result

