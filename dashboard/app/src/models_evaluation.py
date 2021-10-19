import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from .classes import Page


class ModelsEvaluation(Page):
    def write(self):
        title = "Models Evaluation"
        st.title(title)

        st.header("Convolutional Neural Network")
