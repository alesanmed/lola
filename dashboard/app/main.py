import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.config import STREAMLIT_STATIC_PATH, load_css


def main():
    from src.pages import PAGES

    st.set_page_config(
        layout="wide",
        page_title="LOLA",
        page_icon=(STREAMLIT_STATIC_PATH / "img/favicon.png").as_posix(),
    )

    load_css()

    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    Page = PAGES[page]

    Page().write()


if __name__ == "__main__":
    main()
