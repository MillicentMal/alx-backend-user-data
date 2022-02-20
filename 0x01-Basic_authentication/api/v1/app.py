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
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")
if auth:
    from api.v1.auth.auth import Auth
    auth = Auth()
  
    

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request() ->  str:
    excluded_paths = ["/api/v1/status", "/api/v1/unauthorized/", "/api/v1/forbidden/"]
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
    elif auth is None:
        return 
    elif auth.require_auth(request.path, excluded_paths) is None:
        return
    
         




if __name__ == "__main__":
    host = os.getenv("API_HOST" or "0.0.0.0")
    port = os.getenv("API_PORT" or "5000")
    app.run(host=host, port=port)
