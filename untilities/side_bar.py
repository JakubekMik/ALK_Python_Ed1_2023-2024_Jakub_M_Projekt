import streamlit as st


def side_bar_country(tabela, region, cluster, country):
    option_region = st.sidebar.selectbox(
        "Please select Region",
        (["All"] + list(region.unique())),
    )

    if option_region != "All":
        if option_region == "All":
            option_cluster_selection = ["All"] + list(cluster.unique())
        else:
            option_cluster_selection = tabela[region == option_region]
            option_cluster_selection = ["All"] + list(
                option_cluster_selection["Cluster"].unique()
            )

        option_cluster = st.sidebar.selectbox(
            "Please select Cluster", option_cluster_selection
        )
    else:
        option_cluster = "All"

    if option_cluster != "All":
        if option_region == "All":
            option_country_selection = ["All"] + list(country.unique())
        elif option_cluster == "All":
            option_country_selection = tabela[region == option_region]
            option_country_selection = ["All"] + list(
                option_country_selection["Country"].unique()
            )
        else:
            option_country_selection = tabela[cluster == option_cluster]
            option_country_selection = ["All"] + list(
                option_country_selection["Country"].unique()
            )

        option_country = st.sidebar.selectbox(
            "Please select Country", option_country_selection
        )
    else:
        option_country = "All"

    return option_region, option_cluster, option_country


def side_bar_process(process):
    option_process = st.sidebar.selectbox(
        "Please select Process",
        (["All"] + list(process.unique())),
    )
    return option_process
