#!/usr/bin/python3

import os
from flask import Flask
from models import storage
from api.v1.views import app_views

# Create an instance of the Flask application
app = Flask(__name__)
# Register the app_views Blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown App Context

    This function is registered to be called when the application context
    is torn down. It ensures that the storage connection is properly closed.
    """
    storage.close()


if __name__ == "__main__":
    # Define the host and port based on environment variables
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
