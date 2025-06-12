import streamlit as st

def login_page():
    st.title("Connexion")

    st.write("Veuillez vous connecter")

    with st.form("login_form"):
        username = st.text_input("Identifiant")
        password = st.text_input("Mot de passe", type="password")
        submit = st.form_submit_button("Se connecter")

    if submit:
        if username == "admin" and password == "password":
            st.session_state.page = 'module_selection'
            st.experimental_rerun()
        else:
            st.error("Identifiant ou mot de passe incorrect")

    if st.button("ℹ️ Voir le logigramme"):
        st.image("images/logigramme.png", caption="Logigramme du processus")
