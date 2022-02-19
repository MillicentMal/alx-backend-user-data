#!/usr/bin/env python3
"""
Route module for the API
"""
from flask_cors import (CORS, cross_origin)
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = os.getenv("API_HOST" or "0.0.0.0")
    port = os.getenv("API_PORT" or "5000")
    app.run(host=host, port=port)
