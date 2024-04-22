import streamlit as st
from pathlib import Path
from dodatkowe_pliki.scope_comp_web import Scope_page
from dodatkowe_pliki.harmonization_page import Harmonization_page
from dodatkowe_pliki.ladowanie_tabel import przyklad_group
from dodatkowe_pliki.funkcje import scope_completition, BarChart, harmonizacion
import streamlit as st

# print(harmonizacion(przyklad_group, country="Austria", process="Order Management"))

# print(przyklad_group["Process-Level3"])

# przyklad_group = przyklad_group[
#     przyklad_group["Country"] == "Austria"
# ].reset_index()
#
# przyklad_group = przyklad_group[
#     przyklad_group["Process-Level3"] == "Order Management"
# ].reset_index()
# print(przyklad_group)

print(harmonizacion(przyklad_group, country="Austria", process="Order Management"))
