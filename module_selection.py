import streamlit as st
from PIL import Image
import os

def module_selection_page():
    st.header("Choisissez un module")  # titre secondaire ici

    col1, col2 = st.columns([2, 1])

    with col1:
        module = st.radio("Modules disponibles :", ["AFCD", "TR", "INLET"])

        if st.button("Valider le module"):
            st.session_state.selected_module = module
            st.session_state.page = 'actions'
            st.experimental_rerun()

    with col2:
        image_path = os.path.join('images', 'avion.png')
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, caption="Avion", use_container_width=True)
        else:
            st.warning("Image avion introuvable.")
