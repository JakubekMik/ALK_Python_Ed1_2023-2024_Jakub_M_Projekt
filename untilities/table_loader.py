import pandas as pd

# Load the example table
exampl_table = pd.read_excel("./example/jakub_example.xlsx")

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
exampl_table = exampl_table.drop(columns=columns_to_remove)
exampl_table.rename(columns={"Process - Level 3": "Process-Level3"}, inplace=True)
exampl_table["Process-Level3"] = exampl_table["Process-Level3"].str.strip()

exampl_table = exampl_table.melt(
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

exampl_table["Value"] = exampl_table["Value"].astype(str)

#exampl_table = exampl_table[exampl_table["Value"] != "N/A"]
exampl_table = exampl_table[exampl_table["Value"].isin(["Yes", "No", "A", "B", "C"])]


exampl_table["Country"] = exampl_table["Country"].str.split(", ")
exampl_table = exampl_table.explode("Country")

mapping_values = {"Yes": 1, "No": 0, "N/A": 0 , "A": 2, "B": 3, "C": 4}
exampl_table["Value"] = exampl_table["Value"].map(mapping_values).fillna(0).astype(int)
exampl_table = exampl_table[pd.to_numeric(exampl_table["Value"], errors="coerce").notna()]

country_list = pd.read_excel("./example/jakub_example.xlsx", sheet_name="Country_List")
exampl_table = pd.merge(
    exampl_table,
    country_list,
    left_on="Country",
    right_on="Country_Description",
    how="inner",
)

exampl_table_standard = exampl_table[
    exampl_table["Standard/Local exception"] == "Standard"
].copy()
exampl_table_standard_group = (
    exampl_table_standard.groupby(
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
exampl_table_group = (
    exampl_table.groupby(
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
