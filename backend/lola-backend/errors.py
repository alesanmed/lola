from http import HTTPStatus
from logging import getLogger

import flask
from flask import Response, json
from werkzeug.exceptions import HTTPException

bp = flask.Blueprint("error_handlers", __name__)


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""

    response = e.get_response()

    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@bp.app_errorhandler(Exception)
def handle_generic_exception(e):
    logger = getLogger("lola-backend")
    logger.error(e)
    data = json.dumps(
        {
            "code": 500,
            "name": HTTPStatus.INTERNAL_SERVER_ERROR,
            "description": "Internal server error",
        }
    )

    return Response(data, status=500, content_type="application/json")
