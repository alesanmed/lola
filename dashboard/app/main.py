import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def main():
    from src.pages import PAGES

    st.set_page_config(layout="wide", page_title="LOLA")

    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    Page = PAGES[page]

    Page().write()


if __name__ == "__main__":
    main()
