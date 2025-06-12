import streamlit as st
from PIL import Image
import os

def actions_page():
    module = st.session_state.get('selected_module', 'Non défini')
    st.title(f"Module sélectionné : {module}")

    col1, col2 = st.columns([1, 2])  # Image plus large à droite

    with col1:
        st.write("Choisissez une action :")

        if st.button("Dashboard"):
            st.session_state.page = 'dashboard'
            st.experimental_rerun()

        if st.button("Suivi"):
            st.session_state.page = 'suivi'
            st.experimental_rerun()

        if st.button("Dérogations"):
            st.session_state.page = 'derogations'
            st.experimental_rerun()

        if st.button("⬅️ Retour à la sélection du module"):
            st.session_state.page = 'module_selection'
            st.experimental_rerun()

    with col2:
        image_path = os.path.join('images', 'avion.png')
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, caption="Avion", use_container_width=True)
        else:
            st.warning("Image avion introuvable.")
