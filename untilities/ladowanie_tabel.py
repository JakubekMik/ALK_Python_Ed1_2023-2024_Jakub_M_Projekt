import pandas as pd

przyklad = pd.read_excel("./example/jakub_example.xlsx")

columns_to_remove = [
    "No_L1",
    "No_L2",
    "No_L3",
    "No_L4",
    "No_L5",
    "No_L6",
    "No_L7",
    "Level 7 (optional)",
    "System/Technology/Tool",
    "Department",
    "Team",
]
przyklad = przyklad.drop(columns=columns_to_remove)
przyklad.rename(columns={"Process - Level 3": "Process-Level3"}, inplace=True)
przyklad["Process-Level3"] = przyklad["Process-Level3"].str.strip()

przyklad = przyklad.melt(
    id_vars=[
        "Category - Level 1",
        "Process Group - Level 2",
        "Process-Level3",
        "Subprocess - Level 4",
        "Activity - Level 5",
        "Task - Level 6",
        "Standard/Local exception",
    ],
    var_name="Country",
    value_name="Value",
)

przyklad["Country"] = przyklad["Country"].str.split(", ")
przyklad = przyklad.explode("Country")

mapping_values = {"Yes": 1, "No": 0, "N/A": 0, "A": 2, "B": 3, "C": 4}
przyklad["Value"] = przyklad["Value"].map(mapping_values).fillna(0).astype(int)

country_list = pd.read_excel("./example/jakub_example.xlsx", sheet_name="Country_List")
przyklad = pd.merge(
    przyklad,
    country_list,
    left_on="Country",
    right_on="Country_Description",
    how="left",
)

przyklad_standard = przyklad[przyklad["Standard/Local exception"] == "Standard"].copy()
przyklad_standard_group = (
    przyklad_standard.groupby(
        [
            "Category - Level 1",
            "Process Group - Level 2",
            "Process-Level3",
            "Country",
            "Cluster",
            "Region",
        ]
    )["Value"]
    .sum()
    .apply(lambda x: 0 if x == 0 else 1)
    .reset_index()
)
przyklad_group = (
    przyklad.groupby(
        [
            "Category - Level 1",
            "Process Group - Level 2",
            "Process-Level3",
            "Country",
            "Cluster",
            "Region",
        ]
    )["Value"]
    .sum()
    .apply(lambda x: 0 if x == 0 else 1)
    .reset_index()
)

print(przyklad_group.columns)
