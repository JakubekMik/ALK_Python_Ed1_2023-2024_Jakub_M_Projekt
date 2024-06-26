from untilities.table_loader import exampl_table
import streamlit as st
from untilities.side_bar import side_bar_process
from untilities.define_function import (
    bar_char_and_download,
    unique_table_rows,
    unique,
    calculate_harmonizacion,
)
import datetime
import pandas as pd
import base64
import io

option_process = "All"

def harmonization_page():
    st.page_link("program.py", label="Home", icon="🏠")

    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.header("Illustrating the Level of Harmonization")

    option_process = side_bar_process(exampl_table["Process-Level3"])
    today = datetime.date.today().strftime("%Y-%m-%d")

    filtere_data = (
        exampl_table[exampl_table["Process-Level3"] == option_process]
        if option_process != "All"
        else exampl_table
    )

    if option_process != "All":
        st.write("Process Selected:", option_process)
    else:
        pass

    bar_char_and_download(
        unique(filtere_data["Region"]),
        unique_table_rows(
            filtere_data, filtere_data["Region"], unique(filtere_data["Region"])
        ),
        "Region",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option_process} process by region",
        highlight_index=None,
        filename=f"{today}_{option_process}_Harmonization_level_per_region.png",
    )

    bar_char_and_download(
        unique(filtere_data["Cluster"]),
        unique_table_rows(
            filtere_data, filtere_data["Cluster"], unique(filtere_data["Cluster"])
        ),
        "Cluster",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option_process} process by cluster",
        highlight_index=None,
        filename=f"{today}_{option_process}_Harmonization_level_per_cluster.png",
    )

    bar_char_and_download(
        unique(filtere_data["Country"]),
        unique_table_rows(
            filtere_data, filtere_data["Country"], unique(filtere_data["Country"])
        ),
        "Country",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option_process} process by country",
        highlight_index=None,
        filename=f"{today}_{option_process}_Harmonization_level_per_country.png",
    )

    bar_char_and_download(
        unique(exampl_table["Process-Level3"]),
        unique_table_rows(
            exampl_table,
            exampl_table["Process-Level3"],
            unique(exampl_table["Process-Level3"]),
        ),
        "Process",
        "Harmonization level",
        "Chart illustrating the Level of Harmonization by cluster",
        highlight_index=(
            list(exampl_table["Process-Level3"].unique()).index(option_process)
            if option_process != "All"
            else None
        ),
        filename=f"{today}_Harmonization_level_per_process.png",
    )


if __name__ == "__main__":
    harmonization_page()
