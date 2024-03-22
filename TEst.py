import streamlit as st
from pathlib import Path
from Dodatkowe_Pliki.Scope_Comp_web import Scope_page
from Dodatkowe_Pliki.Harmonization_page import Harmonization_page
from Dodatkowe_Pliki.Ladowanie_Tabel import przyklad_group
from Dodatkowe_Pliki.Funkcje import scope_completition, BarChart, harmonizacion
import streamlit as st

#print(harmonizacion(przyklad_group, country="Austria", process="Order Management"))

#print(przyklad_group["Process-Level3"])

# przyklad_group = przyklad_group[
#     przyklad_group["Country"] == "Austria"
# ].reset_index()
#
# przyklad_group = przyklad_group[
#     przyklad_group["Process-Level3"] == "Order Management"
# ].reset_index()
# print(przyklad_group)

print(harmonizacion(przyklad_group,country="Austria", process="Order Management"))

