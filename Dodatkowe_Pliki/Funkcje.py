# Tutaj będą tworzone funkcje

# Pierwsz funkcją jest funckja która wylicza scope completition :
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


def scope_completition(df, country=None, cluster=None, region=None):
    # Tworzymy filtry którę będą brały wartość z funkcji
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

    # Kolejnym krokiem jest utworznie data framu z zastosowanymi filtrami
    # filtered_df = df[filter_condition]

    # Liczymy sume wartości
    total_value = filtered_df["Value"].sum()

    # Liczymy liczbę wieszy
    num_rows = len(filtered_df)

    # Obliczamy stosunek sumy do ilości wierszy

    if num_rows > 0:
        percentage = round((total_value / num_rows), 2)
    else:
        percentage = 0

    return percentage


# Funckja która wylicza wartości harmonizacji


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

   # if scope_completition(df, country=country, cluster=cluster, region=region) == 0:
   #     return "Proces nie jest przejęty"

    # Analogicznie jak dla Scope Completition, czyli najpierw robimy filtracje
    filtered_df = df[filter_condition]

    # Liczymy sume wartości
    total_value = filtered_df["Value"].sum()

    # Liczymy liczbę wieszy
    num_rows = len(filtered_df)

    # Obliczamy stosunek sumy do ilości wierszy

    if num_rows > 0:
        percentage = round((total_value / num_rows), 2)
    else:
        percentage = 0

    return percentage


# A Tutaj sobie tworze funkcje co mi wykresy będzie plotować tak jak bym chciał miec nowej kolory
def BarChart(x, y, TextX=None, TextY=None, Title=None):
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
