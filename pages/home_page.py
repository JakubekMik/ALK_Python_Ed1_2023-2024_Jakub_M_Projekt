import streamlit as st
from untilities.function_streamlit import read_markdown_file

def homepage():

    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.caption("Welcome to home page")

    st.markdown('''

## Introduction to Process Harmonization Program

The Process Harmonization Program is a data analysis tool that enables the processing and analysis of information related to business processes. Below you will find a description of the tasks performed by this program:

- **Column Separation:**

The program automatically separates the column containing country names when there is more than one country name (separated by a comma or other delimiter). This operation facilitates the analysis of data related to multiple countries.

- **Data Conversion from Pivot to Database:**

The program allows the conversion of data provided in pivot form to database form. It reverses this process, allowing for better analysis and storage of data in a more traditional database form.

- **Assignment of Data to Corresponding Geographic Regions:**

Data is assigned to the appropriate geographic regions, enabling data analysis from a geographical perspective. This facilitates understanding of where specific business phenomena occur.

- **Calculation of Process Scope Completion:**

The program calculates whether for a given process level (level 4) there is a task performed at level 6 (value "Yes"). The process is considered adopted if such a task exists. Otherwise, if such a task is missing, the process is considered unadopted, with the possibility of "Local Exception" being skipped.

- **Calculation of Process Harmonization:**

The program calculates the process harmonization index, which is the ratio of the number of Standard Tasks performed (value Yes) to the total number of Standard Tasks in the process, taking into account any Local Exceptions. This index helps understand the degree of standardization and consistency in the processes being performed.

- **Graphical Presentation of Results:**

The program presents the analysis results graphically, making them easier to understand and interpret. Users have the option to limit the results to a specific region or process, enabling a more detailed analysis.
''')

   # intro_markdown = read_markdown_file("README.md")
   # st.markdown(intro_markdown, unsafe_allow_html=True)

    st.image("./picture/jakub_alk_main.jpg")
    st.image("./picture/jakub_alk_psc.jpg")

if __name__ == "__main__":
    homepage()
