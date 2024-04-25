import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


def scope_completition(df, country=None, cluster=None, region=None):
    if country:
        filter_condition = df["Country"] == country
        filtered_df = df[filter_condition]
    elif cluster:
        filter_condition = df["Cluster"] == cluster
        filtered_df = df[filter_condition]
    elif region:
        filter_condition = df["Region"] == region
        filtered_df = df[filter_condition]
    else:
        filtered_df = df

    total_value = filtered_df["Value"].sum()

    num_rows = len(filtered_df)

    if num_rows > 0:
        percentage = round((total_value / num_rows), 2)
    else:
        percentage = 0

    return percentage


def harmonizacion(df, country=None, cluster=None, region=None, process=None):
    # Tutaj musimy trochę namieszać bo jest problem ze musimy mieć więcej niż jeden filtr :

    filter_condition = pd.Series(True, index=df.index)
    # Tworzymy filtry którę będą brały wartość z funkcji
    if country:
        filter_condition &= df["Country"] == country
    if cluster:
        filter_condition &= df["Cluster"] == cluster
    if region:
        filter_condition &= df["Region"] == region
    if process:
        filter_condition &= df["Process-Level3"] == process

    filtered_df = df[filter_condition]

    total_value = filtered_df["Value"].sum()

    num_rows = len(filtered_df)

    if num_rows > 0:
        percentage = round((total_value / num_rows), 2)
    else:
        percentage = 0

    return percentage


def bar_chart(x, y, TextX=None, TextY=None, Title=None):
    # Definicja rozmiaru :
    plt.figure(figsize=(10, 6))
    # Definicja koloru wykresu
    plt.bar(x, y, color="#05647e")
    plt.xlabel(TextX)
    plt.ylabel(TextY)
    plt.title(Title)
    # Jak mają wyświetlać się nazwy na wykresie
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return st.pyplot(plt)


def bar_chart_2(x, y, TextX=None, TextY=None, Title=None, highlight_index=None):
    # Definicja rozmiaru :
    plt.figure(figsize=(10, 6))

    # Domyślny kolor dla wszystkich słupków
    colors = ["#05647e"] * len(x)

    # Tutaj magia, czyli kod który powienien kiedy następuje podanie filtra kolorować wykres:
    if highlight_index is not None:
        colors[highlight_index] = (
            "#ff5733"  # Tutaj możesz ustawić inny kolor dla wyróżnionego słupka
        )

    # Definicja koloru wykresu
    plt.bar(x, y, color=colors)
    plt.xlabel(TextX)
    plt.ylabel(TextY)
    plt.title(Title)
    # Jak mają wyświetlać się nazwy na wykresie
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return st.pyplot(plt)
