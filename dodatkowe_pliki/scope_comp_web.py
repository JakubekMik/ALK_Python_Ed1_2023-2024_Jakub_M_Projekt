from dodatkowe_pliki.ladowanie_tabel import przyklad_standard_group
import streamlit as st
from dodatkowe_pliki.side_bar import side_bar
from dodatkowe_pliki.scope_chart import scope_bar1, scope_bar2, scope_bar3


def scope_page():
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.header(
        "Tutaj prezentowana jest poziom realizacji procesów względem zakresu geograficznego"
    )

    option1, option2, option3 = side_bar(
        przyklad_standard_group,
        przyklad_standard_group["Region"],
        przyklad_standard_group["Cluster"],
        przyklad_standard_group["Country"],
    )

    st.write("Region Scope:", option1) if option1 != "All" else None
    scope_bar1(option1)

    st.write("Cluster :", option2) if option2 != "All" else None
    scope_bar2(option1, option2)

    st.write("Country:", option3) if option3 != "All" else None
    scope_bar3(option1, option2, option3)
