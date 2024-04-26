from untilities.ladowanie_tabel import przyklad_standard_group
import streamlit as st
from untilities.side_bar import side_bar
from untilities.funkcje import full_magic, unique_1, unique_2
import datetime


def scope_page():
    today = datetime.date.today().strftime("%Y-%m-%d")
    st.page_link("program.py", label="Home", icon="🏠")
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
    if option1 != "All":
        st.write("Region Scope:", option1)
    else:
        pass

    full_magic(
        unique_2(przyklad_standard_group["Region"]),
        unique_1(
            przyklad_standard_group,
            przyklad_standard_group["Region"],
            unique_2(przyklad_standard_group["Region"]),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by region",
        highlight_index=(
            list(przyklad_standard_group["Region"].unique()).index(option1)
            if option1 != "All"
            else None
        ),
        filename=f"{today}_Scope_Completition_level_per_region.png",
    )

    if option2 != "All":
        st.write("Cluster Scope:", option2)
    else:
        pass

    if option1 != "All":
        unique_clusters = przyklad_standard_group[
            przyklad_standard_group["Region"] == option1
        ]["Cluster"]
    else:
        unique_clusters = przyklad_standard_group["Cluster"]

    full_magic(
        unique_2(unique_clusters),
        unique_1(
            przyklad_standard_group,
            przyklad_standard_group["Cluster"],
            unique_2(unique_clusters),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by cluster",
        highlight_index=(
            list(unique_clusters.unique()).index(option2) if option2 != "All" else None
        ),
        filename=f"{today}_Scope_Completition_level_per_cluster.png",
    )

    if option3 != "All":
        st.write("Country Scope:", option3)
    else:
        pass

    if option2 != "All":
        unique_country = przyklad_standard_group[
            przyklad_standard_group["Cluster"] == option2
        ]["Country"]
    elif option1 != "All":
        unique_country = przyklad_standard_group[
            przyklad_standard_group["Region"] == option1
        ]["Country"]
    else:
        unique_country = przyklad_standard_group["Country"]

    full_magic(
        unique_2(unique_country),
        unique_1(
            przyklad_standard_group,
            przyklad_standard_group["Country"],
            unique_2(unique_country),
        ),
        "Region",
        "Scope Completition",
        f"Chart illustrating the Level of Scope Completition by cluster",
        highlight_index=(
            list(unique_country.unique()).index(option3) if option3 != "All" else None
        ),
        filename=f"{today}_Scope_Completition_level_per_cluster.png",
    )


if __name__ == "__main__":
    scope_page()
