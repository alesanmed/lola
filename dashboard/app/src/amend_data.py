import streamlit as st

from .classes import Page
from .data import check_auth, create_country


class AmendData(Page):
    def write(self):
        st.title("Data Management")

        st.session_state["api_key"] = st.text_input(
            "Enter your api key to continue", value=st.session_state.get("api_key", "")
        )

        if not st.session_state.get("api_key", ""):
            st.stop()
        else:
            api_key_valid = check_auth(st.session_state["api_key"])

            if not api_key_valid:
                st.error("API Key invalid")
                st.stop()
            else:
                st.success("API Key valid")

        st.subheader("Create country")

        if st.session_state.get("country_created", False):
            st.success("Country created successfully")
            st.session_state["country_created"] = False

        st.session_state["country_name"] = st.text_input(
            "Country name", value=st.session_state.get("country_name", "")
        )
        st.session_state["alpha2"] = st.text_input(
            "Alpha 2 Code", value=st.session_state.get("alpha2", "")
        )
        st.session_state["alpha3"] = st.text_input(
            "Alpha 3 Code", value=st.session_state.get("alpha3", "")
        )
        st.session_state["lat"] = st.number_input(
            "Latitude",
            value=st.session_state.get("lat", 0.0),
            min_value=-180.0,
            max_value=180.0,
            step=1e-7,
            format="%.7f",
        )
        st.session_state["lng"] = st.number_input(
            "Longitude",
            value=st.session_state.get("lng", 0.0),
            min_value=-180.0,
            max_value=180.0,
            step=1e-7,
            format="%.7f",
        )

        if st.button("Create country"):
            success = create_country(
                st.session_state["country_name"],
                st.session_state["alpha2"],
                st.session_state["alpha3"],
                float(st.session_state["lat"]),
                float(st.session_state["lng"]),
                st.session_state["api_key"],
            )

            if success:
                st.session_state["country_created"] = True

                del st.session_state["country_name"]
                del st.session_state["alpha2"]
                del st.session_state["alpha3"]
                del st.session_state["lat"]
                del st.session_state["lng"]

                st.experimental_rerun()
            else:
                st.session_state["country_create_error"] = True

            if st.session_state.get("country_create_error", False):
                st.error("Error creating country")
                del st.session_state["country_create_error"]
