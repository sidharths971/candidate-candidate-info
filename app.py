from flask import Flask
import logging as logger

logger.basicConfig(level='DEBUG')

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/hi")
# def hello_world9():
#     return "<p>Hellow</p>"

if __name__ == '__main__':
    logger.debug('server started')
    from api import *

    app.run(
        host='0.0.0.0', port=8000, debug=True
    )
