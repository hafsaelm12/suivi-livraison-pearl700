import pandas as pd
from utils import charger_fichier_excel, sauvegarder_fichier_excel

def appliquer_logique_vba(module):
    # Charger les fichiers Excel
    derogations_file = f"derogations_{module}.xlsx"
    suivi_file = f"suivi_{module}.xlsx"

    df_dero = charger_fichier_excel(derogations_file)
    df_suivi = charger_fichier_excel(suivi_file)

    # Initialisation: nettoyer colonnes ciblées dans suivi
    colonnes_a_nettoyer = ['Numéro de série', 'OF', 'Dérangements', 'Statut']
    for col in colonnes_a_nettoyer:
        if col in df_suivi.columns:
            df_suivi[col] = ""

    # Parcourir les dérogations
    for index, row in df_dero.iterrows():
        avis_numero = str(row.get('Avis Numero', '')).strip()
        avis_description = str(row.get('Avis Description', '')).strip()
        avis_statut = str(row.get('Avis Statut', '')).strip()
        of_value = str(row.get('OF', '')).strip()
        numero_serie = str(row.get('Numéro Série', '')).strip()

        if of_value == "":
            continue

        # Rechercher OF dans suivi
        if of_value in df_suivi['OF'].values:
            idx_suivi = df_suivi.index[df_suivi['OF'] == of_value][0]
        else:
            # Ajouter nouvelle ligne
            nouvelle_ligne = {'OF': of_value, 'Dérangements': '', 'Statut': 'OK', 'Numéro de série': ''}
            df_suivi = pd.concat([df_suivi, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
            idx_suivi = df_suivi.index[-1]

        # Vérifier avis
        if avis_numero.startswith(("30000", "40000", "70000")):
            if avis_description != "":
                dero_text = f"{avis_numero} {avis_description} ({avis_statut})"
                contenu_existant = df_suivi.at[idx_suivi, 'Dérangements']
                if dero_text not in contenu_existant:
                    if contenu_existant == "":
                        df_suivi.at[idx_suivi, 'Dérangements'] = dero_text
                    else:
                        df_suivi.at[idx_suivi, 'Dérangements'] = contenu_existant + "\n" + dero_text
                df_suivi.at[idx_suivi, 'Statut'] = "NOK"

        # Ajouter numéro de série sans doublon
        if numero_serie != "":
            num_serie_courant = df_suivi.at[idx_suivi, 'Numéro de série']
            nums = num_serie_courant.split('\n') if num_serie_courant else []
            if numero_serie not in nums:
                nums.append(numero_serie)
                df_suivi.at[idx_suivi, 'Numéro de série'] = "\n".join(nums)

    # Sauvegarder les données modifiées
    sauvegarder_fichier_excel(df_suivi, suivi_file)
