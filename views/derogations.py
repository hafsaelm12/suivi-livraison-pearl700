import streamlit as st
from PIL import Image
import os
from utils import charger_fichier_excel

def derogations_page():
    module = st.session_state.get('selected_module', '')
    st.title(f"Dérogations - Module {module}")

    # Afficher le logigramme en haut
    image_path = os.path.join('images', 'logigramme.png')
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, caption="Logigramme", use_container_width=True)
    else:
        st.warning("Image logigramme introuvable.")

    filepath = f"data/derogations_{module}.xlsx"
    df = charger_fichier_excel(filepath)

    if df.empty:
        st.warning("Aucune donnée à afficher dans le fichier dérogations.")
        return

    st.dataframe(df)

    if st.button("⬅️ Retour aux actions"):
        st.session_state.page = 'actions'
        st.experimental_rerun()
