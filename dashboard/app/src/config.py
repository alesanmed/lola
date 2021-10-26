import os
import pathlib

import streamlit as st

STREAMLIT_STATIC_PATH = pathlib.Path(os.environ.get("STREAMLIT_STATIC_PATH", ""))


class Config(object):
    BACK_URL: str = os.environ.get("BACK_URL", "")


def load_css():
    css = """
    <style>
    .css-1kyxreq, .etr89bj0 {
        justify-content: center;
    }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
