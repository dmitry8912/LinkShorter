import json

from flask import Flask, jsonify, g


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_json("config.json")

    # register api functions
    from . import api
    app.register_blueprint(api.bp)
    app.register_blueprint(api.redirect_bp)

    return app
