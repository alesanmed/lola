import requests
import streamlit as st
from streamlit.state.session_state import get_session_state

from .classes import Page
from .config import STREAMLIT_STATIC_PATH, Config
from .types import Palo


class IdentifyAudio(Page):
    def write(self):
        st.image(
            (STREAMLIT_STATIC_PATH / "img/logo_small.png").as_posix(),
            width=300,
        )

        st.title("Identifica tu audio")

        audio = st.file_uploader(
            "Sube tu audio de flamenco", "mp3", accept_multiple_files=False
        )

        if audio is not None:
            audio_bytes = audio.getvalue()

            URL = Config().BACK_URL

            full_url = f"{URL}/prediction"

            files = {"file": ("0.mp3", audio_bytes, "application/json")}

            response = requests.post(full_url, files=files)

            palo = response.json()["palo"]

            if palo != "other":
                st.markdown(f"Tu audio se corresponde con las {palo}")
            else:
                st.markdown("No se identificar tu palo.")
