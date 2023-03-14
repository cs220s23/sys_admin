
from flask import Flask
import json


app = Flask(__name__)


@app.route('/hello')
def greet():
    result = {'foo': 'bar',
              'value': 42}

    return json.dumps(result)


if __name__ == '__main__':
    app.run(port=8000)
