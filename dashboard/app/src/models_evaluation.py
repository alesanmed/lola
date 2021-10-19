import altair as alt
import streamlit as st
from pandas import DataFrame, read_csv

from .classes import Page
from .config import STREAMLIT_STATIC_PATH


class ModelsEvaluation(Page):
    def write(self):
        title = "Models Evaluation"
        st.title(title)

        st.header("Prediction execution time")

        execution_times = read_csv(STREAMLIT_STATIC_PATH / "data/time_results.csv")
        execution_times: DataFrame

        boxplot = (
            (
                alt.Chart(execution_times)
                .mark_boxplot(size=50, extent=0.5)
                .encode(
                    x=alt.X("model:N", scale=alt.Scale(type="log")),
                    y=alt.Y("time:Q", scale=alt.Scale(zero=False)),
                    color=alt.Color("model", legend=None),
                )
            )
            .properties(width=900, height=600)
            .configure_axis(labelFontSize=16, titleFontSize=16)
        )

        st.altair_chart(boxplot)
