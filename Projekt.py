# Ładowanie biblitek:

import pandas as pd


# Wczytanie danych z pliku Excel
# Docelowo ma to być pobierane bezpośrednie z sharpointa, więc będzie uzyta fukcja url oraz ograniczenie do tylko kokretnej zakładki
#url = "https://organizacja.sharepoint.com/sites/Location/file_name.xlsx"
#df = pd.read_excel(url, sheet_name="Table13454")

# W naszym przypadku będziemy pobierać dane z pliku "Jakub_Example"
przyklad = pd.read_excel('./Jakub_Example.xlsx')
print(przyklad.head())

# Usuwanie zbędnych kolumn :

columns_to_remove = ["No_L1", "No_L2", "No_L3", "No_L4", "No_L5", "No_L6", "No_L7", "Level 7 (optional)", "System/Technology/Tool", "Department", "Team"]
przyklad = przyklad.drop(columns=columns_to_remove)
print(przyklad.head())

# A teraz magia, czyli odpivotowanie danych
# https://pandas.pydata.org/docs/reference/api/pandas.melt.html

przyklad = przyklad.melt(id_vars=["Category - Level 1", "Process Group - Level 2", "Process - Level 3", "Subprocess - Level 4", "Activity - Level 5", "Task - Level 6", "Standard/Local exception"], var_name="Country", value_name="Value")
print(przyklad.head())

# Kolejnym krokiem jest wydzielenie grupy krajów na oddzielne regmenty
# Czyli najpierw uzywany funckji assign aby dodać nową kolumne, gdzie wartości są podzielone ", "
# a następnie uzywamy funkcji Explode tak aby "Transform each element of a list-like to a row, replicating index values."
#  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html
przyklad = przyklad.assign(Country=przyklad["Country"].str.split(", ")).explode("Country")
print(przyklad.head())

# Zamiana wartości z tesktu na liczby (Potrzebne do wyliczenia procentów)
# Najpierw tworzymy słownik który dla którego przypiszemy wartość słowną do wartości liczbowej
mapping_wartosci = {"Yes": 1, "No": 0, "N/A": 0, "A": 2, "B": 3, "C": 4}
przyklad["Value"] = przyklad["Value"].map(mapping_wartosci)
