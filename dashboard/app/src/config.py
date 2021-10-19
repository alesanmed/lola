import os
import pathlib

STREAMLIT_STATIC_PATH = pathlib.Path(os.environ.get("STREAMLIT_STATIC_PATH", ""))


class Config(object):
    BACK_URL: str = os.environ.get("BACK_URL", "")
