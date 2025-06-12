import streamlit as st
import matplotlib.pyplot as plt
from utils import charger_fichier_excel

def dashboard_page():
    module = st.session_state.get('selected_module', '')
    st.title(f"Dashboard - Module {module}")

    filepath = f"data/suivi_{module}.xlsx"
    df = charger_fichier_excel(filepath)

    if df.empty:
        st.warning("Aucune donnée à afficher dans le fichier suivi.")
        return

    nb_ok = df[df['Statut'].str.upper() == 'OK'].shape[0]
    nb_nok = df[df['Statut'].str.upper() == 'NOK'].shape[0]

    st.write(f"Nombre de OK : {nb_ok}")
    st.write(f"Nombre de NOK : {nb_nok}")

    labels = ['OK', 'NOK']
    sizes = [nb_ok, nb_nok]
    colors = ['#00A859', '#EA2A2A']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    if st.button("⬅️ Retour aux actions"):
        st.session_state.page = 'actions'
        st.experimental_rerun()
