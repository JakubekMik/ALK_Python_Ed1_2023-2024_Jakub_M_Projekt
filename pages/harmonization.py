from untilities.ladowanie_tabel import przyklad_group
import streamlit as st
from untilities.side_bar import side_bar_2
from untilities.funkcje import full_magic, unique_1, unique_2
import datetime


def harmonization_page():
    st.page_link("program.py", label="Home", icon="🏠")

    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.header("Graficzna ilustracja procesu harmonizacji.")

    option4 = side_bar_2(przyklad_group["Process-Level3"])
    today = datetime.date.today().strftime("%Y-%m-%d")
    st.write("Process Selected:", option4) if option4 != "All" else None

    filtere_data = (
        przyklad_group[przyklad_group["Process-Level3"] == option4]
        if option4 != "All"
        else przyklad_group
    )

    full_magic(
        unique_2(filtere_data["Region"]),
        unique_1(
            filtere_data, filtere_data["Region"], unique_2(filtere_data["Region"])
        ),
        "Region",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option4} process by region",
        highlight_index=None,
        filename=f"{today}_{option4}_Harmonization_level_per_region.png",
    )

    full_magic(
        unique_2(filtere_data["Cluster"]),
        unique_1(
            filtere_data, filtere_data["Cluster"], unique_2(filtere_data["Cluster"])
        ),
        "Cluster",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option4} process by cluster",
        highlight_index=None,
        filename=f"{today}_{option4}_Harmonization_level_per_cluster.png",
    )

    full_magic(
        unique_2(filtere_data["Country"]),
        unique_1(
            filtere_data, filtere_data["Country"], unique_2(filtere_data["Country"])
        ),
        "Country",
        "Harmonization level",
        f"Chart illustrating the Level of Harmonization {option4} process by country",
        highlight_index=None,
        filename=f"{today}_{option4}_Harmonization_level_per_country.png",
    )

    full_magic(
        unique_2(przyklad_group["Process-Level3"]),
        unique_1(
            przyklad_group,
            przyklad_group["Process-Level3"],
            unique_2(przyklad_group["Process-Level3"]),
        ),
        "Process",
        "Harmonization level",
        "Chart illustrating the Level of Harmonization by cluster",
        highlight_index=(
            list(przyklad_group["Process-Level3"].unique()).index(option4)
            if option4 != "All"
            else None
        ),
        filename=f"{today}_Harmonization_level_per_process.png",
    )


if __name__ == "__main__":
    harmonization_page()
