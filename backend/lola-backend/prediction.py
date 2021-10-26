import json
import os
from http import HTTPStatus
from uuid import uuid4

from flask import Blueprint
from flask import current_app as app
from flask import request
from flask.wrappers import Response
from numpy import argmax, unique
from werkzeug import exceptions
from werkzeug.datastructures import FileStorage

from .audio import encode_audio
from .models import SingletonModels
from .utils import serialize_json

bp = Blueprint("prediction", __name__, url_prefix="/prediction")


def allowed_file(filename: str):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@bp.route("", methods=["POST"])
def predict():
    random_forest = SingletonModels().random_forest

    if "file" not in request.files:
        raise exceptions.BadRequest("No file sent")

    file: FileStorage = request.files["file"]

    if file and allowed_file(file.filename or ""):
        filename = f"{uuid4().hex}.mp3"
    else:
        raise exceptions.BadRequest("The file sent is not valid")

    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(audio_path)

    data = encode_audio(audio_path)

    os.unlink(audio_path)

    prediction = random_forest.predict(data)

    unique_vals, counts = unique(prediction, return_counts=True)

    probabilities = counts / prediction.shape[0]

    most_probable = argmax(probabilities)

    response = {"palo": "Other"}

    if probabilities[most_probable] > 0.3:
        response["palo"] = unique_vals[most_probable]

    return Response(
        json.dumps(response, default=serialize_json),
        HTTPStatus.OK,
        {"content-type": "application/json"},
    )
