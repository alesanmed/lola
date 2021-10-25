from typing import List, Optional

import altair as alt
import pandas as pd
import streamlit as st
from altair.vegalite.v4.schema.core import UrlData


@st.cache(allow_output_mutation=True)
def evolution_by_type(source: pd.DataFrame) -> alt.Chart:
    selection = alt.selection_multi(fields=["type"], bind="legend")

    return (
        alt.Chart(source)
        .mark_line(point=False)
        .transform_aggregate(total_amount="sum(amount)", groupby=["date", "type"])
        .encode(
            x=alt.X("yearmonthdate(date):T", axis=alt.Axis(title="Date")),
            y=alt.Y("total_amount:Q", axis=alt.Axis(title="Cases amount", format="~s")),
            tooltip=["date:T", "total_amount:Q"],
            color=alt.Color(
                "type:N",
                scale=alt.Scale(
                    domain=["confirmed", "dead", "recovered"],
                    range=["orange", "red", "green"],
                ),
            ),
        )
        .transform_filter(selection)
        .add_selection(selection)
        .properties(height=500)
    )


@st.cache(allow_output_mutation=True)
def bar_rank(
    source: pd.DataFrame, place_type: str, height: Optional[int] = 900
) -> alt.Chart:
    chart: alt.Chart = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X(
                "amount:Q", axis=alt.Axis(format="~d", title="Total amount of cases")
            ),
            y=alt.Y(
                f"{place_type}:N",
                title=place_type.capitalize(),
                sort=alt.SortByEncoding("x", "descending"),
            ),
            tooltip=["amount:Q"],
            color=f"{place_type}:N",
        )
    )

    if height:
        chart.properties(height=height)

    return chart


@st.cache(allow_output_mutation=True)
def map_cases_contribution(
    geodata: UrlData,
    lookupdata: pd.DataFrame,
    tooltips: List[alt.Tooltip],
    lookup_property: str,
    lookup_key: str,
) -> alt.Chart:
    return (
        alt.Chart(geodata)
        .mark_geoshape()
        .encode(
            color="amount:Q",
            tooltip=tooltips,
        )
        .transform_lookup(
            lookup=lookup_property,
            from_=alt.LookupData(
                lookupdata,
                lookup_key,
                ["amount"],
            ),
        )
        .properties(height=600)
    )
