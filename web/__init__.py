import os

from flask import Flask
from web.config import Config


def create_app(test_config=None):
    # Initialise the app, and the config.
    app = Flask(__name__)
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    # Create the instance directory if it doesn't exist.
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    # Add blueprints and modules.
    from flask_bootstrap import Bootstrap
    Bootstrap(app)

    from . import index
    app.register_blueprint(index.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
