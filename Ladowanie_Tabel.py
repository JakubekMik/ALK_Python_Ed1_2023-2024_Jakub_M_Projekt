# Ładowanie biblitek:

import pandas as pd
from Funkcje import scope_completition, harmonizacion

# Wczytanie danych z pliku Excel
# Docelowo ma to być pobierane bezpośrednie z sharpointa, więc będzie uzyta fukcja url oraz ograniczenie do tylko kokretnej zakładki
#url = "https://organizacja.sharepoint.com/sites/Location/file_name.xlsx"
#df = pd.read_excel(url, sheet_name="Table13454")

# W naszym przypadku będziemy pobierać dane z pliku "Jakub_Example"
przyklad = pd.read_excel('./Jakub_Example.xlsx')
#print(przyklad.head())

# Usuwanie zbędnych kolumn :

columns_to_remove = ["No_L1", "No_L2", "No_L3", "No_L4", "No_L5", "No_L6", "No_L7", "Level 7 (optional)", "System/Technology/Tool", "Department", "Team"]
przyklad = przyklad.drop(columns=columns_to_remove)
#print(przyklad.head())

# A teraz magia, czyli odpivotowanie danych
# https://pandas.pydata.org/docs/reference/api/pandas.melt.html

przyklad = przyklad.melt(id_vars=["Category - Level 1", "Process Group - Level 2", "Process - Level 3", "Subprocess - Level 4", "Activity - Level 5", "Task - Level 6", "Standard/Local exception"], var_name="Country", value_name="Value")
#print(przyklad.head())

# Kolejnym krokiem jest wydzielenie grupy krajów na oddzielne regmenty
# Czyli najpierw uzywany funckji assign aby dodać nową kolumne, gdzie wartości są podzielone ", "
# a następnie uzywamy funkcji Explode tak aby "Transform each element of a list-like to a row, replicating index values."
#  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html
przyklad = przyklad.assign(Country=przyklad["Country"].str.split(", ")).explode("Country")
#print(przyklad.head())

# Zamiana wartości z tesktu na liczby (Potrzebne do wyliczenia procentów)
# Najpierw tworzymy słownik który dla którego przypiszemy wartość słowną do wartości liczbowej
mapping_wartosci = {"Yes": 1, "No": 0, "N/A": 0, "A": 2, "B": 3, "C": 4}
przyklad["Value"] = przyklad["Value"].map(mapping_wartosci)
#print(przyklad.head())
# Sprawdzamy jaki jest typ kolumny
print((przyklad["Value"].dtype))
#print(przyklad["Value"].describe())
# Zamieniamy kolumne na wartosci :
przyklad["Value"] = pd.to_numeric(przyklad["Value"])

# Ładujemy teraz liste krajów wraz z podziałem na regiony/clustry
country_list = pd.read_excel('./Jakub_Example.xlsx', sheet_name='Country_List')
#print(country_list.head())

# Łączymy dane z przykładu z danymi z country list
przyklad = pd.merge(przyklad, country_list, left_on="Country", right_on="Country_Description", how="left")

#print(przyklad.head())

# Tworzymy tabele tylko i wyłacznie w standarowymi procesami

przyklad_standard = przyklad.copy()
przyklad_standard = przyklad_standard[przyklad_standard["Standard/Local exception"] == 'Standard'].reset_index()

#print(przyklad_standard)

# Kolejnym etapem jest po grupowanie do poziomu procesu :

przyklad_standard_group = przyklad_standard.groupby(["Category - Level 1", "Process Group - Level 2", "Process - Level 3", "Country", "Cluster", "Region"])["Value"].sum().reset_index()
# print(przyklad_standard_group)
# Kolejnym etapem jest zamiana wastości, tak aby jeśli jest suma > 0 to ma być 1 a w pozostałych przypadkach 0
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
przyklad_standard_group["Value"] = przyklad_standard_group["Value"].apply(lambda  x:0 if x == 0 else 1)

print(f' test {scope_completition(przyklad_standard, region="REU")*100}%')
print(f' test {scope_completition(przyklad_standard_group, region="REU")*100}%')

for x in przyklad_standard_group["Country"]:
    print(f' {x}  - {scope_completition(przyklad_standard, country=x)*100}%')

przyklad_group = przyklad.groupby(["Category - Level 1", "Process Group - Level 2", "Process - Level 3", "Country", "Cluster", "Region"])["Value"].sum().reset_index()
przyklad_group["Value"] = przyklad_group["Value"].apply(lambda  x:0 if x == 0 else 1)


for x in przyklad_standard_group["Country"]:
    print(f' {x}  - {harmonizacion(przyklad_standard, country=x)}')

