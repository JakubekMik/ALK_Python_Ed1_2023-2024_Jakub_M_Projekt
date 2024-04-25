import streamlit as st
from dodatkowe_pliki.scope_comp_web import scope_page
from dodatkowe_pliki.harmonization_page import harmonization_page
from dodatkowe_pliki.home_page import homepage

page = st.sidebar.selectbox(
    "Wybierz stronę", ("Strona startowa", "Scope", "Harmonization")
)

if page == "Strona startowa":
    homepage()
elif page == "Scope":
    scope_page()
elif page == "Harmonization":
    harmonization_page()
