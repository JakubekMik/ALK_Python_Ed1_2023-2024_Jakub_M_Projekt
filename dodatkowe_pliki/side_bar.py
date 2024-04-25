import streamlit as st


def side_bar(tabela, region, cluster, country):
    option1 = st.sidebar.selectbox(
        "Please select Region",
        (["All"] + list(region.unique())),
    )

    if option1 != "All":
        if option1 == "All":
            option2_selection = ["All"] + list(cluster.unique())
        else:
            option2_selection = tabela[region == option1]
            option2_selection = ["All"] + list(option2_selection["Cluster"].unique())

        option2 = st.sidebar.selectbox("Please select Cluster", option2_selection)
    else:
        option2 = "All"

    if option2 != "All":
        if option1 == "All":
            option3_selection = ["All"] + list(country.unique())
        elif option2 == "All":
            option3_selection = tabela[region == option1]
            option3_selection = ["All"] + list(option3_selection["Country"].unique())
        else:
            option3_selection = tabela[cluster == option2]
            option3_selection = ["All"] + list(option3_selection["Country"].unique())

        option3 = st.sidebar.selectbox("Please select Country", option3_selection)
    else:
        option3 = "All"

    return option1, option2, option3
