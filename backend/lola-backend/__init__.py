import logging
import os
import sys

import toml
from dotenv import load_dotenv
from flask import Flask

from .logger import init_logger, log_uncaught_exception
from .models import SingletonModels

load_dotenv()


def create_app(test_config=None):
    sys.excepthook = log_uncaught_exception

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    app.url_map.strict_slashes = False

    init_logger(
        os.path.join(os.path.dirname(__file__), "../logs/backend.log"), logging.INFO
    )

    logger = logging.getLogger("lola-backend")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object("lola-backend.config.Config")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "../tmp")
    app.config["ALLOWED_EXTENSIONS"] = {"mp3"}

    project_info = toml.load(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyproject.toml"))
    )

    app.config["VERSION"] = project_info["tool"]["poetry"]["version"]

    logger.info("Loading models")

    # Just load the models so the singleton is available in subsequent requests
    SingletonModels()

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    logger.info("Registering blueprints")

    from . import prediction

    app.register_blueprint(prediction.bp)

    from . import index

    app.register_blueprint(index.bp)

    from . import errors

    app.register_blueprint(errors.bp)

    logger.info("App ready")

    return app
