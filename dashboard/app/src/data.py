import os

import streamlit as st

from .types import Palo


@st.cache()
def get_audio(palo: Palo) -> bytes:
    """
    Returns the bytes of the audio

    Parameters
    ---------------------
    palo (~src.types.Palo): The palo (style) of the requested audio

    Returns
    ---------------------
    bytes The bytes of the audio file
    """
    return open(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "../../assets/audios",
                f"{palo.value}.mp3",
            )
        ),
        "rb",
    ).read()
