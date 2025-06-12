import pandas as pd
import os

def charger_fichier_excel(filepath):
    if not os.path.exists(filepath):
        # Créer un fichier vide avec colonnes si fichier inexistant (à adapter selon tes besoins)
        df = pd.DataFrame(columns=['ID', 'Statut', 'Autre'])  # exemple colonnes à adapter
        df.to_excel(filepath, index=False)
        return df
    try:
        return pd.read_excel(filepath)
    except Exception as e:
        print(f"Erreur chargement fichier {filepath} : {e}")
        return pd.DataFrame()

def sauvegarder_fichier_excel(df, filepath):
    try:
        df.to_excel(filepath, index=False)
    except Exception as e:
        print(f"Erreur sauvegarde fichier {filepath} : {e}")
