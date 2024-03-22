import streamlit as st
from pathlib import Path
from Scope_Comp_web import Scope_page

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Tworzymy sobie definicje strony startowej:
def homepage():
    st.title("Jakub Mikołajczyk - ALK Python Ed1 2023 - 2024")
    st.caption("Witaj na stronie startowej!")
    st.write("Wybierz jedną z opcji poniżej, aby przejść do innych stron:")

    # Odnośniki do innych stron
    st.header("Wybierz stronę:")
    col1, col2, col3 = st.columns(3)

    # Przycisk do strony 1
    with col1:
        if st.button("Strona 1"):
            st.write("Przechodzisz do Strony 1")

    # Przycisk do strony 2
    with col2:
        if st.button("Strona 2"):
            st.write("Przechodzisz do Strony 2")

    # Przycisk do strony 3
    with col3:
        if st.button("Strona 3"):
            st.write("Przechodzisz do Strony 3")

    intro_markdown = read_markdown_file("README.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    st.image("./Obrazy/Jakub ALK-Main.jpg")
    st.image("./Obrazy/Jakub ALK-PSC.jpg")
# Strona 1
def page1():
    st.title("Strona 1")
    st.write("To jest Strona 1")

# Strona 2
def page2():
    st.title("Strona 2")
    st.write("To jest Strona 2")

# Strona 3
def page3():
    st.title("Strona 3")
    st.write("To jest Strona 3")

# Wybór strony na podstawie odnośników na stronie startowej
page = st.sidebar.selectbox(
    'Wybierz stronę',
    ('Strona startowa', 'Strona 1', 'Strona 2', 'Strona 3')
)

# Wyświetlanie odpowiedniej strony na podstawie wyboru
if page == 'Strona startowa':
    homepage()
elif page == 'Strona 1':
    Scope_page()
elif page == 'Strona 2':
    page2()
elif page == 'Strona 3':
    page3()


