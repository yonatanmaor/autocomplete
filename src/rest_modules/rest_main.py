import random
from flask import Flask
import sys

from rest_modules.autocomplete_rest import autocomplete_blueprint

print(sys.path)

app = Flask(__name__)
app.register_blueprint(autocomplete_blueprint, url_prefix='/autocomplete')


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return f"SUCCESS {random.randint(0,10000)}"


if __name__ == '__main__':
    app.run(port=1188, host="0.0.0.0")
