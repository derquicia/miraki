import os


import streamlit as st
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Otro", "Documentation", "Examples", "Community", "About"])
st.write(page)


