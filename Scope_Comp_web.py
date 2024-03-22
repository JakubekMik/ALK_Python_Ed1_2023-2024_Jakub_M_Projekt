from Ladowanie_Tabel import przyklad_standard_group
from Funkcje import scope_completition, harmonizacion, BarChart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def Scope_page():

    # Dodajemy napis na górze
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")

    # Dodatkowy tekst
    st.header("To jest dodatkowy tekst.")

    # A tutaj dodajemy sobie opcje wyboru odnośnie regionu
    option1 = st.sidebar.selectbox(
        'Please select Region',
        ( ["All"] +list(przyklad_standard_group["Region"].unique()))
    )

    # Lista rozwijana numer 2
    if option1 == "All":
        option2_selection = ( ["All"] +list(przyklad_standard_group["Cluster"].unique()))
    else:
        option2_selection = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
        option2_selection =  ( ["All"] +list(option2_selection["Cluster"].unique()))

    option2 = st.sidebar.selectbox(
        'Please select Cluster',
        option2_selection
    )


    # Lista rozwijana 3

    if option1 == "All":
        option3_selection = ( ["All"] +list(przyklad_standard_group["Country"].unique()))
    elif option2 == "All":
        option3_selection = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
        option3_selection =  ( ["All"] +list(option3_selection["Country"].unique()))
    else:
        option3_selection = przyklad_standard_group[przyklad_standard_group["Cluster"] == option2]
        option3_selection =  ( ["All"] +list(option3_selection["Country"].unique()))

    option3 = st.sidebar.selectbox(
        'Please select Country',
        option3_selection
    )

    #Teraz sobie robimy zmienne tak aby uzyć je potem do filtracji
    if option1 == "All":
        option1_value  = None
        a = scope_completition(przyklad_standard_group)

    else:
        option1_value = option1
        a = scope_completition(przyklad_standard_group, region=option1_value)

    if option2 == "All":
        option2_value  = None
        if option1 == "All":
            b = scope_completition(przyklad_standard_group)
            unique_cluster = przyklad_standard_group["Cluster"].unique()

        else:
            option1_value = option1
            b = scope_completition(przyklad_standard_group, region=option1_value)
            unique_cluster = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
            unique_cluster = unique_cluster["Cluster"].unique()
    else:
        option2_value = option2
        b = scope_completition(przyklad_standard_group, cluster=option2_value)
        if option1 == "All":
            unique_cluster = przyklad_standard_group["Cluster"].unique()
        else:
            unique_cluster = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
            unique_cluster = unique_cluster["Cluster"].unique()


    if option3 == "All":
        option3_value  = None
        if option1 == "All":
            unique_country = przyklad_standard_group["Country"].unique()
        else:
            if option2 == "All":
                unique_country = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
                unique_country = unique_country["Country"].unique()
            else:
                unique_country = przyklad_standard_group[przyklad_standard_group["Cluster"] == option2]
                unique_country = unique_country["Country"].unique()

    else:
        option3_value = option3
        if option1 == "All" and option2 == "All":
            unique_country = przyklad_standard_group["Country"].unique()
        elif option1 == "All" and option2 != "All":
            unique_country = przyklad_standard_group[przyklad_standard_group["Cluster"] == option2]
            unique_country = unique_country["Country"].unique()
        elif option1 != "All" and option2 == "All":
            unique_country = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
            unique_country = unique_country["Country"].unique()
        else:
            unique_country = przyklad_standard_group[przyklad_standard_group["Region"] == option1]
            unique_country = unique_country[unique_country["Cluster"] == option2]
            unique_country = unique_country["Country"].unique()


    # Tutaj możemy wpisywać jakie teksty
    st.write('Region Scope:', option1_value)
    st.write('Cluster :', option2_value)
    st.write('Country:', option3_value)


    # a teraz wykresiki:
    unique_regions = przyklad_standard_group["Region"].unique()
    scope_unique_regions = [scope_completition(przyklad_standard_group[przyklad_standard_group["Region"] == region]) for region in unique_regions]
    scope_unique_cluster = [scope_completition(przyklad_standard_group[przyklad_standard_group["Cluster"] == cluster]) for cluster in unique_cluster]
    scope_unique_country = [scope_completition(przyklad_standard_group[przyklad_standard_group["Country"] == country]) for country in unique_country]

    BarChart(unique_regions,scope_unique_regions,'Region','Scope Completition')
    BarChart(unique_cluster,scope_unique_cluster,'Cluster','Scope Completition')
    BarChart(unique_country,scope_unique_country,'Country','Scope Completition')
