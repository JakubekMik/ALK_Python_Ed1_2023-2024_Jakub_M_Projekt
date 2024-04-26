import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import base64
import io


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


def bar_chart_2(x, y, TextX=None, TextY=None, Title=None, highlight_index=None):
    plt.figure(figsize=(10, 6))
    colors = ["#05647e"] * len(x)
    if highlight_index is not None:
        colors[highlight_index] = "#ff5733"
    plt.bar(x, y, color=colors)
    plt.xlabel(TextX)
    plt.ylabel(TextY)
    plt.title(Title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return st.pyplot(plt)


def bar_chart(x, y, TextX=None, TextY=None, Title=None, highlight_index=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    else:
        fig = ax.figure

    colors = ["#05647e"] * len(x)
    if highlight_index is not None:
        colors[highlight_index] = "#ff5733"

    ax.bar(x, y, color=colors)
    ax.set_xlabel(TextX)
    ax.set_ylabel(TextY)
    ax.set_title(Title)
    ax.set_xticklabels(x, rotation=45, ha="right")
    plt.tight_layout()

    return fig


def magic(fig, name):
    image_stream = io.BytesIO()
    fig.savefig(image_stream, format="png")
    image_stream.seek(0)
    base64_image = base64.b64encode(image_stream.getvalue()).decode("utf-8")
    return st.markdown(
        f'<a href="data:file/png;base64,{base64_image}" download={name}>Click here to download the upper graph</a>',
        unsafe_allow_html=True,
    )


def full_magic(
    x, y, TextX=None, TextY=None, Title=None, highlight_index=None, filename="chart.png"
):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#05647e"] * len(x)
    if highlight_index is not None:
        colors[highlight_index] = "#ff5733"
    ax.bar(x, y, color=colors)
    ax.set_xlabel(TextX)
    ax.set_ylabel(TextY)
    ax.set_title(Title)
    ax.set_xticklabels(x, rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)
    magic(fig, filename)


def unique_1(table, table_with_kolumn, unique_country):
    har_unique = [
        harmonizacion(table[table_with_kolumn == region]) for region in unique_country
    ]

    return har_unique


def unique_2(table):
    unique = table.unique()

    return unique
