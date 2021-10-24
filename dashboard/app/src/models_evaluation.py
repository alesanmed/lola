from pickle import load
from typing import Dict, List

import altair as alt
import streamlit as st
from matplotlib.pyplot import subplots
from pandas import DataFrame, read_csv
from seaborn import heatmap
from sklearn.metrics import confusion_matrix
from streamlit.delta_generator import DeltaGenerator

from .classes import Page
from .config import STREAMLIT_STATIC_PATH


class ModelsEvaluation(Page):
    labels = ["bulerias", "alegrias", "sevillanas"]

    def write(self):
        title = "Models evaluation"
        st.title(title)

        st.header("Neural networks learning")

        model_full_history: Dict = load(
            open(STREAMLIT_STATIC_PATH / "data/history_conv_model_70_epochs.p", "rb")
        )

        cols: List[DeltaGenerator] = st.columns(2)

        cols[0].subheader("Model with full data")

        full_loss = (
            alt.Chart(DataFrame(model_full_history).reset_index())
            .transform_fold(["loss", "val_loss"])
            .mark_line()
            .encode(x="index:Q", y="value:Q", color="key:N")
        ).properties(width=600)

        cols[0].altair_chart(full_loss)

        model_partial_history: Dict = load(
            open(
                STREAMLIT_STATIC_PATH / "data/history_conv_model_only_mel_100_epochs.p",
                "rb",
            )
        )

        cols[1].subheader("Model with spectrogram data only")

        full_loss = (
            alt.Chart(DataFrame(model_partial_history).reset_index())
            .transform_fold(["loss", "val_loss"])
            .mark_line()
            .encode(x="index:Q", y="value:Q", color="key:N")
        ).properties(width=600)

        cols[1].altair_chart(full_loss)

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

        st.header("Prediction metrics")

        prediction_metrics = read_csv(STREAMLIT_STATIC_PATH / "data/metrics.csv")
        prediction_metrics: DataFrame

        selection = alt.selection_multi(fields=["metric_name"], bind="legend")

        bar_plot = (
            alt.Chart(prediction_metrics)
            .mark_bar(opacity=0.7)
            .encode(
                x="model:N",
                y=alt.Y("metric_val", stack=None),
                color=alt.Color(
                    "metric_name",
                ),
                opacity=alt.condition(selection, alt.value(1), alt.value(0)),
            )
            .add_selection(selection)
            .properties(width=900, height=600)
            .configure_axis(labelFontSize=16, titleFontSize=16)
        )

        st.altair_chart(bar_plot)

        st.header("Confusion matrices")

        confusion_data = read_csv(STREAMLIT_STATIC_PATH / "data/conf.csv")

        cols: List[DeltaGenerator] = st.columns(3)

        cols[0].subheader("Model with full data")

        y_true = confusion_data.loc[confusion_data["model"] == "full", "y_true"]
        y_pred = confusion_data.loc[confusion_data["model"] == "full", "y_pred"]

        confusion_matrix_full = confusion_matrix(y_true, y_pred)

        fig, ax = subplots()

        heatmap(confusion_matrix_full, ax=ax, annot=True, fmt="g")
        ax.xaxis.set_ticklabels(self.labels)
        ax.yaxis.set_ticklabels(self.labels)
        ax.tick_params(axis="x", colors="white", labelsize="large")
        ax.tick_params(axis="y", colors="white", labelsize="large")
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(colors="white", labelsize="large")

        cols[0].pyplot(fig, transparent=True)

        cols[1].subheader("Random forest")

        y_true = confusion_data.loc[confusion_data["model"] == "ml", "y_true"]
        y_pred = confusion_data.loc[confusion_data["model"] == "ml", "y_pred"]

        confusion_matrix_ml = confusion_matrix(y_true, y_pred)

        fig, ax = subplots()

        heatmap(confusion_matrix_ml, ax=ax, annot=True, fmt="g")
        ax.xaxis.set_ticklabels(self.labels)
        ax.yaxis.set_ticklabels(self.labels)
        ax.tick_params(axis="x", colors="white", labelsize="large")
        ax.tick_params(axis="y", colors="white", labelsize="large")
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(colors="white", labelsize="large")

        cols[1].pyplot(fig, transparent=True)

        cols[2].subheader("Model with only spectrograms")

        y_true = confusion_data.loc[confusion_data["model"] == "partial", "y_true"]
        y_pred = confusion_data.loc[confusion_data["model"] == "partial", "y_pred"]

        confusion_matrix_partial = confusion_matrix(y_true, y_pred)

        fig, ax = subplots()

        heatmap(confusion_matrix_partial, ax=ax, annot=True, fmt="g")
        ax.xaxis.set_ticklabels(self.labels)
        ax.yaxis.set_ticklabels(self.labels)
        ax.tick_params(axis="x", colors="white", labelsize="large")
        ax.tick_params(axis="y", colors="white", labelsize="large")
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(colors="white", labelsize="large")

        cols[2].pyplot(fig, transparent=True)
