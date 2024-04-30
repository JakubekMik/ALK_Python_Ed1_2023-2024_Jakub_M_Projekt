from untilities.table_loader import exampl_table_standard_group
import streamlit as st
from untilities.side_bar import side_bar_country
from untilities.define_function import bar_char_and_download, unique_table_rows, unique
import datetime

option_region  = "All"
option_cluster = "All"
option_country = "All"


def scope_page():
    today = datetime.date.today().strftime("%Y-%m-%d")
    st.page_link("program.py", label="Home", icon="🏠")
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.header("Illustrating the Level of Scope Completition")

    option_region, option_cluster, option_country = side_bar_country(
        exampl_table_standard_group,
        exampl_table_standard_group["Region"],
        exampl_table_standard_group["Cluster"],
        exampl_table_standard_group["Country"],
    )
    if option_region != "All":
        st.write("Region Scope:", option_region)
    else:
        pass

    bar_char_and_download(
        unique(exampl_table_standard_group["Region"]),
        unique_table_rows(
            exampl_table_standard_group,
            exampl_table_standard_group["Region"],
            unique(exampl_table_standard_group["Region"]),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by region",
        highlight_index=(
            list(exampl_table_standard_group["Region"].unique()).index(option_region)
            if option_region != "All"
            else None
        ),
        filename=f"{today}_Scope_Completition_level_per_region.png",
    )

    if option_cluster != "All":
        st.write("Cluster Scope:", option_cluster)
    else:
        pass

    if option_region != "All":
        unique_clusters = exampl_table_standard_group[
            exampl_table_standard_group["Region"] == option_region
        ]["Cluster"]
    else:
        unique_clusters = exampl_table_standard_group["Cluster"]

    bar_char_and_download(
        unique(unique_clusters),
        unique_table_rows(
            exampl_table_standard_group,
            exampl_table_standard_group["Cluster"],
            unique(unique_clusters),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by cluster",
        highlight_index=(
            list(unique_clusters.unique()).index(option_cluster)
            if option_cluster != "All"
            else None
        ),
        filename=f"{today}_Scope_Completition_level_per_cluster.png",
    )

    if option_country != "All":
        st.write("Country Scope:", option_country)
    else:
        pass

    if option_cluster != "All":
        unique_country = exampl_table_standard_group[
            exampl_table_standard_group["Cluster"] == option_cluster
        ]["Country"]
    elif option_region != "All":
        unique_country = exampl_table_standard_group[
            exampl_table_standard_group["Region"] == option_region
        ]["Country"]
    else:
        unique_country = exampl_table_standard_group["Country"]

    bar_char_and_download(
        unique(unique_country),
        unique_table_rows(
            exampl_table_standard_group,
            exampl_table_standard_group["Country"],
            unique(unique_country),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by cluster",
        highlight_index=(
            list(unique_country.unique()).index(option_country)
            if option_country != "All"
            else None
        ),
        filename=f"{today}_Scope_Completition_level_per_cluster.png",
    )


if __name__ == "__main__":
    scope_page()
