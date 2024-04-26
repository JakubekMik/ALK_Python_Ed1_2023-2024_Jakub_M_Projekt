import streamlit as st
from pages.scope_completition import scope_page
from pages.harmonization import harmonization_page
from pages.home_page import homepage


page = st.sidebar.selectbox(
    "Wybierz stronę", ("Strona startowa", "Scope", "Harmonization")
)

if page == "Strona startowa":
    homepage()
elif page == "Scope":
    scope_page()
elif page == "Harmonization":
    harmonization_page()
