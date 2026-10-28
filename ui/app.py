
"""Interface Streamlit du TP5 : le modèle est interrogé via l'API FastAPI."""

from pathlib import Path

import pandas as pd
import streamlit as st

import client

RACINE = Path(__file__).resolve().parents[1]

st.set_page_config(
    page_title="Analyse de sentiment",
    page_icon="💬",
    layout="wide",
)

st.title("Analyse de sentiment des avis clients")

# La page utilise uniquement le client HTTP : elle ne charge pas le modèle.
session = client.creer_session()
etat = client.sante(session)

if not etat.ok:
    st.error(etat.message)
    st.stop()

st.caption(f"API prête : {etat.message}")

onglet_avis, onglet_fichier, onglet_aide = st.tabs(
    ["Un avis", "Un fichier d'avis", "Comment ça marche"]
)

with onglet_avis:
    texte = st.text_area(
        "Avis à analyser",
        "Livraison rapide, produit conforme.",
        height=130,
    )

    if st.button("Analyser", type="primary"):
        resultat = client.predire(session, texte)

        if not resultat.ok:
            if resultat.message == client.REFUS:
                st.warning(resultat.message)
            else:
                st.error(resultat.message)
        else:
            verdict = resultat.label
            score = resultat.score

            if verdict == "POSITIVE":
                libelle = client.VERDICTS[verdict]
                st.success(libelle)
            elif verdict == "NEGATIVE":
                libelle = client.VERDICTS[verdict]
                st.error(libelle)
            else:
                libelle = client.VERDICTS.get(
                    verdict, "Je ne sais pas : à faire vérifier par un humain"
                )
                st.warning(libelle)
                st.info(
                    "La confiance est sous le seuil d'abstention : "
                    "un humain doit trancher."
                )

            st.metric(label=libelle, value=f"{score:.0%}")
            st.progress(float(score))

with onglet_fichier:
    st.write(
        "Importez un fichier CSV contenant une colonne d'avis "
        "(par exemple `text` ou `review`)."
    )

    fichier = st.file_uploader(
        "Choisir un fichier CSV",
        type=["csv"],
    )

    if fichier is not None:
        try:
            donnees = pd.read_csv(fichier)

            # Accepter les noms de colonnes courants.
            colonnes_possibles = ["text", "review", "avis", "texte"]
            colonne_avis = next(
                (nom for nom in colonnes_possibles if nom in donnees.columns),
                None,
            )

            if colonne_avis is None:
                st.error(
                    "Le CSV doit contenir une colonne nommée "
                    "`text`, `review`, `avis` ou `texte`."
                )
            elif donnees.empty:
                st.warning("Le fichier CSV ne contient aucun avis.")
            else:
                textes = donnees[colonne_avis].fillna("").astype(str).tolist()
                reponses = client.predire_lot(session, textes)

                resultats = donnees.copy()
                resultats["prediction"] = [
                    reponse.label if reponse.ok else "ERREUR"
                    for reponse in reponses
                ]
                resultats["confiance"] = [
                    reponse.score if reponse.ok else None
                    for reponse in reponses
                ]
                resultats["message"] = [
                    reponse.message if not reponse.ok else ""
                    for reponse in reponses
                ]

                st.subheader("Résultats des analyses")
                st.dataframe(resultats, use_container_width=True)

                resume = client.resumer(reponses)
                st.subheader("Résumé des verdicts")
                st.write(resume)

                st.download_button(
                    label="Télécharger les résultats",
                    data=resultats.to_csv(index=False).encode("utf-8-sig"),
                    file_name="resultats.csv",
                    mime="text/csv",
                )

        except (ValueError, pd.errors.ParserError, UnicodeDecodeError) as erreur:
            st.error(f"Impossible de lire le fichier CSV : {erreur}")

with onglet_aide:
    st.markdown(
        """
        **Fonctionnement**

        1. L'interface vérifie que l'API est disponible.
        2. Le client envoie chaque avis à l'endpoint `/predict`.
        3. L'API renvoie un verdict et un score de confiance.
        4. Les avis incertains sont signalés pour vérification humaine.

        **Gestion des erreurs**

        Les textes refusés, l'absence de modèle et les problèmes de connexion
        sont affichés à l'utilisateur au lieu de provoquer un plantage.
        """
    )
