from dodatkowe_pliki.ladowanie_tabel import przyklad_standard_group
from dodatkowe_pliki.funkcje import scope_completition, bar_chart_2


def scope_bar1(option1):
    unique_regions = przyklad_standard_group["Region"].unique()
    scope_unique_regions = [
        scope_completition(
            przyklad_standard_group[przyklad_standard_group["Region"] == region]
        )
        for region in unique_regions
    ]

    highlighted_index = (
        list(unique_regions).index(option1) if option1 != "All" else None
    )
    chart_title = "Wykres ilustrujący Poziom realizacji procesów po Regionach"

    bar_chart_2(
        unique_regions,
        scope_unique_regions,
        "Region",
        "Scope Completition",
        chart_title,
        highlight_index=highlighted_index,
    )


def scope_bar2(option1, option2):
    unique_cluster = (
        przyklad_standard_group[przyklad_standard_group["Region"] == option1][
            "Cluster"
        ].unique()
        if option1 != "All"
        else przyklad_standard_group["Cluster"].unique()
    )
    scope_unique_cluster = [
        scope_completition(
            przyklad_standard_group[przyklad_standard_group["Cluster"] == cluster]
        )
        for cluster in unique_cluster
    ]

    highlighted_index = (
        list(unique_cluster).index(option2) if option2 != "All" else None
    )
    bar_chart_2(
        unique_cluster,
        scope_unique_cluster,
        "Cluster",
        "Scope Completition",
        "Wykres ilustrujący Poziom realizacji procesów po Clustrach",
        highlight_index=highlighted_index,
    )


def scope_bar3(option1, option2, option3):
    if option2 != "All":
        unique_country = przyklad_standard_group[
            przyklad_standard_group["Cluster"] == option2
        ]["Country"].unique()
    elif option1 != "All":
        unique_country = przyklad_standard_group[
            przyklad_standard_group["Region"] == option1
        ]["Country"].unique()
    else:
        unique_country = przyklad_standard_group["Country"].unique()

    scope_unique_country = [
        scope_completition(
            przyklad_standard_group[przyklad_standard_group["Country"] == country]
        )
        for country in unique_country
    ]

    highlighted_index = (
        list(unique_country).index(option3) if option3 != "All" else None
    )
    bar_chart_2(
        unique_country,
        scope_unique_country,
        "Country",
        "Scope Completition",
        "Wykres ilustrujący Poziom realizacji procesów po Krajach",
        highlight_index=highlighted_index,
    )
