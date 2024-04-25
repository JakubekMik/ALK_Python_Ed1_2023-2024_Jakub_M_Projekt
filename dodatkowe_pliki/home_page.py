import streamlit as st
from dodatkowe_pliki.funckje_streamlit import read_markdown_file


def homepage():
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.caption("Witaj na stronie startowej!")

    intro_markdown = read_markdown_file("README.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    st.image("./obrazy/jakub_alk_main.jpg")
    st.image("./obrazy/jakub_alk_psc.jpg")