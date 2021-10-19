import os
from typing import List

import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from .classes import Page
from .components.juxtapose import juxtapose
from .data import get_audio
from .types import Palo


class DataExploration(Page):
    def write(self):
        st.title("Understanding the different *palos* (styles)")

        cols: List[DeltaGenerator] = st.columns(3)

        cols[0].header("Bulerias")
        cols[0].subheader("Hear it")
        cols[0].text("")
        cols[0].audio(get_audio(Palo.BULERIAS), format="audio/mp3")

        cols[1].header("Alegrias")
        cols[1].subheader("Hear it")
        cols[1].text("")
        cols[1].audio(get_audio(Palo.ALEGRIAS), format="audio/mp3")

        cols[2].header("Sevillanas")
        cols[2].subheader("Hear it")
        cols[2].text("")
        cols[2].audio(get_audio(Palo.SEVILLANAS), format="audio/mp3")

        st.markdown("***")

        st.header("Comparing spectrograms")

        st.markdown(
            "A spectrogram is a visual representation of the frequencies of the audio"
        )

        juxtapose(
            "img/spectrogram/sevillanas.png",
            "img/spectrogram/bulerias.png",
            height=600,
            img1_label="sevillanas",
            img2_label="bulerias",
        )

        st.text("")

        st.header("Comparing tempograms")

        st.markdown(
            (
                "A [tempogram]"
                "(http://resources.mpi-inf.mpg.de/MIR/"
                "tempogramtoolbox/2010_GroscheMuellerKurth_TempogramCyclic_ICASSP.pdf)"
                " is a representation of an  audio tempo variations"
            )
        )

        juxtapose(
            "img/tempogram/alegrias.png",
            "img/tempogram/bulerias.png",
            height=800,
            img1_label="alegrias",
            img2_label="bulerias",
        )

        st.header("Chromagrams")
        st.markdown(
            (
                "The [chroma features]"
                "(https://en.wikipedia.org/wiki/Chroma_feature)"
                " relates to the different notes."
            )
        )

        cols: List[DeltaGenerator] = st.columns(3)

        for i, palo in enumerate(Palo):
            cols[i].header(palo.value.capitalize())
            cols[i].image(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        f"../../assets/img/chromagram/{palo.value}.png",
                    )
                )
            )
