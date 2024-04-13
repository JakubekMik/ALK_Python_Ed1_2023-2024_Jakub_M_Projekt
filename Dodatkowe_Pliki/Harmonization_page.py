from Dodatkowe_Pliki.Ladowanie_Tabel import przyklad_group
from Dodatkowe_Pliki.Funkcje import harmonizacion, BarChart, BarChart2
import streamlit as st


def Harmonization_page():

    # Dodajemy napis na górze
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")

    # Dodatkowy tekst
    st.header("Graficzna ilustracja procesu harmonizacji.")

    # A tutaj dodajemy sobie opcje wyboru odnośnie procesu
    option4 = st.sidebar.selectbox(
        "Please select Process",
        (["All"] + list(przyklad_group["Process-Level3"].unique())),
    )
    if option4 == "All":
        filtere_data   = przyklad_group
    else:
        filtere_data = przyklad_group[przyklad_group["Process-Level3"] == option4]

    unique_regions = filtere_data["Region"].unique()
    unique_cluster = filtere_data["Cluster"].unique()
    unique_country = filtere_data["Country"].unique()
    uniquer_process = filtere_data["Process-Level3"].unique()

    har_unique_regions = [harmonizacion(filtere_data[filtere_data["Region"] == region])
        for region in unique_regions]
    har_unique_cluster = [harmonizacion(filtere_data[filtere_data["Cluster"] == region])
        for region in unique_cluster]
    har_unique_country = [harmonizacion(filtere_data[filtere_data["Country"] == region])
        for region in unique_country]
    har_unique_process = [harmonizacion(filtere_data[filtere_data["Process-Level3"] == region])
        for region in uniquer_process]

    BarChart(unique_regions, har_unique_regions, "Region", "Harmonization level", "Wykres ilustrujący Poziom Harmonizacji po Regionach")
    BarChart(unique_cluster, har_unique_cluster, "Cluster", "Harmonization level", "Wykres ilustrujący Poziom Harmonizacji po Clustrach")
    BarChart(unique_country, har_unique_country, "Country", "Harmonization level", "Wykres ilustrujący Poziom Harmonizacji po Krajach")
    BarChart(uniquer_process, har_unique_process, "Process", "Harmonization level","Wykres ilustrujący Poziom Harmonizacji dla wybranego procesu")

    # Tworzymy sobie dodatkowe zmiene tak aby utworzyć wykres dla którego nie wpływa filtracja

    all_processes = przyklad_group["Process-Level3"].unique()
    all_harmonizations = [harmonizacion(przyklad_group[przyklad_group["Process-Level3"] == process])
        for process in all_processes]

    if option4 != "All":
        highlighted_index = list(uniquer_process).index(option4)
        BarChart2(all_processes, all_harmonizations, "Process", "Harmonization level", "Wykres ilustrujący Poziom Harmonizacji dla wybranego procesu", highlight_index=highlighted_index)
    else:
        BarChart(all_processes, all_harmonizations, "Process", "Harmonization level",
                 "Wykres ilustrujący Ogólny Poziom Harmonizacji dla wszystkich procesów")





