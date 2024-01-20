import streamlit as st
from src.resume import show_resume

st.set_page_config(
    page_title="Shirleen Data Web App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Shirleen Web App"
    }
)

show_resume()
