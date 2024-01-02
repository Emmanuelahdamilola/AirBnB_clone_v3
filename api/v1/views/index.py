#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Return JSON status: OK

    This route handler is responsible for handling HTTP GET requests to the
    '/status' endpoint. returns a JSON response indicating the status as "OK".
    """
    return jsonify({"status": "OK"})
