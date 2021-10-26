import json
from http import HTTPStatus

from flask import Blueprint
from flask import current_app as app
from flask.wrappers import Response

from .utils import serialize_json

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("", methods=["GET"])
def predict():
    return Response(
        json.dumps(
            {"name": "LOLA", "version": app.config["VERSION"], "status": "healthy"},
            default=serialize_json,
        ),
        HTTPStatus.OK,
        {"content-type": "application/json"},
    )
