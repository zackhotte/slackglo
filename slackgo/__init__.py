import os

from flask import Flask, json
from werkzeug.exceptions import NotFound, MethodNotAllowed

from slackgo.slack import bp_slack


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(24)
    )

    try:
        os.makedirs(app.instance_path)
        config_file = open(app.instance_path + '/config.py', 'w')
        config_file.write('')
        config_file.close()
    except OSError:
        pass

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(bp_slack)

    @app.errorhandler(NotFound)
    def exception_handler(error):
        return json.jsonify({'error': error.description}), 404

    @app.errorhandler(MethodNotAllowed)
    def exception_handler(error):
        return json.jsonify({'error': error.description}), 405

    return app
