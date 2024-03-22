from Dodatkowe_Pliki.Ladowanie_Tabel import przyklad_group
from Dodatkowe_Pliki.Funkcje import harmonizacion, BarChart
import streamlit as st


def Harmonization_page():

    # Dodajemy napis na górze
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")

    # Dodatkowy tekst
    st.header("Graficzna ilustracja procesu harmonizacji.")

    # A tutaj dodajemy sobie opcje wyboru odnośnie procesu
    option4 = st.sidebar.selectbox(
        "Please select Region",
        (["All"] + list(przyklad_group["Process-Level3"].unique())),
    )
    if option4 == "All":
        unique_regions = przyklad_group["Region"].unique()
        unique_cluster = przyklad_group["Cluster"].unique()
        unique_country = przyklad_group["Country"].unique()
        filtere_data   = przyklad_group
    else:
        filtere_data = przyklad_group[przyklad_group["Process-Level3"] == option4]
        unique_cluster = filtere_data["Cluster"].unique()
        unique_country = filtere_data["Country"].unique()
        unique_regions = filtere_data["Region"].unique()
    uniquer_process = przyklad_group["Process-Level3"].unique()

    st.write("Tudaj powinna byc wartosc dla Austri i Order Managementu: ")
    st.write(harmonizacion(przyklad_group, country="Austria", process="Oder Management"))


    scope_unique_regions = [harmonizacion(filtere_data[filtere_data["Region"] == region])
        for region in unique_regions]
    scope_unique_cluster = [harmonizacion(filtere_data[filtere_data["Cluster"] == region])
        for region in unique_cluster]
    scope_unique_country = [harmonizacion(filtere_data[filtere_data["Country"] == region])
        for region in unique_country]
    scope_unique_process = [harmonizacion(filtere_data[filtere_data["Process-Level3"] == region])
        for region in uniquer_process]

    BarChart(unique_regions, scope_unique_regions, "Region", "Harmonization level")
    BarChart(unique_cluster, scope_unique_cluster, "Cluster", "Harmonization level")
    BarChart(unique_country, scope_unique_country, "Country", "Harmonization level")
    BarChart(uniquer_process, scope_unique_process, "Process", "Harmonization level")


