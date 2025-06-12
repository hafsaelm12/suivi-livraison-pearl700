import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from utils import charger_fichier_excel, sauvegarder_fichier_excel

def suivi_page():
    module = st.session_state.get('selected_module', '')
    st.title(f"Suivi - Module {module}")

    filepath = f"data/suivi_{module}.xlsx"
    df = charger_fichier_excel(filepath)

    if df.empty:
        st.warning("Aucune donnée à afficher dans le fichier suivi.")
        return

    grid_response = AgGrid(
        df,
        editable=True,
        height=300,
        update_mode=GridUpdateMode.VALUE_CHANGED,
    )

    df_modifie = grid_response['data']

    if st.button("💾 Sauvegarder les modifications"):
        sauvegarder_fichier_excel(df_modifie, filepath)
        st.success("Modifications sauvegardées.")

    if st.button("⬅️ Retour aux actions"):
        st.session_state.page = 'actions'
        st.experimental_rerun()
