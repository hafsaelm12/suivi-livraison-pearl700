import streamlit as st
from login import login_page
from module_selection import module_selection_page
from actions import actions_page
from views.derogations import derogations_page
from views.dashboard import dashboard_page
from views.suivi import suivi_page

st.set_page_config(page_title="Suivi Livraison Pearl 700", page_icon="✈️")

# Titre global affiché toujours en haut (tu peux le commenter si tu préfères qu'il soit sur certaines pages seulement)
st.markdown("<h1 style='text-align: center;'>Suivi Livraison Pearl 700</h1>", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'login'

if st.session_state.page == 'login':
    login_page()

elif st.session_state.page == 'module_selection':
    module_selection_page()

elif st.session_state.page == 'actions':
    actions_page()

elif st.session_state.page == 'derogations':
    derogations_page()

elif st.session_state.page == 'dashboard':
    dashboard_page()

elif st.session_state.page == 'suivi':
    suivi_page()
