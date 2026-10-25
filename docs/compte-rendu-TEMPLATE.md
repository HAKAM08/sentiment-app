# Compte rendu global des TP1 à TP3

**Binôme :** Mohamed Taha Hakam ([@HAKAM08]) et Chouaf Mohamed Amine ([@chouaf-mohamed-amine])  
**Dépôt :** [https://github.com/HAKAM08/sentiment-app]  
**Date :** 22/10/2026

## 1. Le besoin et son cadrage

Le projet vise à automatiser l’analyse des avis clients afin d’identifier les commentaires positifs et négatifs. Cette solution peut aider une équipe de relation client à repérer rapidement les avis négatifs et à traiter les situations nécessitant une attention particulière. Les prédictions incertaines doivent pouvoir être vérifiées par un agent humain.

Pour le cas 3, nous avons retenu une approche d’apprentissage supervisé avec un modèle de classification de sentiments.

Ce choix se justifie par les critères suivants :

- **(a) Données étiquetées :** les jeux de données contiennent des avis associés à des étiquettes positives ou négatives, ce qui permet d’entraîner un modèle supervisé.
- **(b) Vérifiabilité :** les prédictions peuvent être comparées aux étiquettes réelles à l’aide de métriques comme le F1 macro, l’exactitude et le rappel de la classe négative.
- **(d) Conséquence d’une erreur :** une mauvaise classification peut masquer un avis négatif important. Une vérification humaine est donc nécessaire pour les prédictions incertaines.

## 2. L’architecture du dépôt

Le dépôt est organisé en plusieurs dossiers :

- `src/` : entraînement du modèle, évaluation et préparation des données de démonstration.
- `data/` : jeux de données et exemples d’avis utilisés pour les tests.
- `models/` : métriques du modèle et modèle entraîné.
- `ui/` : interface utilisateur développée avec Streamlit.
- `api/` : API FastAPI permettant de tester le modèle à travers différents endpoints.
- `tests/` : tests automatisés du cadrage, du modèle, de l’interface et de l’API.
- `notebooks/` : notebooks utilisés pour les travaux pratiques.
- `docs/` : documentation et comptes rendus des séances.
- `scripts/` : scripts de vérification et d’aide à l’installation.

Les fichiers sources, la documentation, les tests et les métriques sont versionnés dans Git. Le modèle entraîné `models/sentiment.joblib` n’est pas versionné, car il s’agit d’un artefact généré qui peut être volumineux et être recréé à partir des données et du code.

À l’inverse, `models/metrics.json` est versionné car il contient des résultats légers, lisibles et utiles pour suivre les performances du modèle entre plusieurs exécutions.

## 3. Le modèle

Le pipeline utilise une représentation TF-IDF des textes et un classifieur Logistic Regression pour prédire le sentiment.

Les données sont divisées en 80 % pour l’entraînement et 20 % pour le test. Le découpage utilise une graine fixe et conserve la proportion des classes afin de rendre les expériences reproductibles.

### Résultats obtenus

| Jeu            | Avis  | Vocabulaire | F1 macro | Rappel négatif |
| Démonstration  | 290   | 316         | 0,879    | 0,931          |
| Allociné       | 20 000| 149 529     | 0,9205   | 0,9113         |

Sur le jeu de démonstration, 232 avis servent à l’entraînement et 58 au test. L’exactitude obtenue est de 87,9 %.

Sur Allociné, 16 000 avis servent à l’entraînement et 4 000 au test. L’exactitude obtenue est de 92,05 %.

### Matrice de confusion — jeu de démonstration

| Vérité \ Prédiction | Négatif | Positif |
| Négatif             | 27      | 2       |
| Positif             | 5       | 24      |

- **Ligne négative :** 27 avis négatifs sont correctement identifiés et 2 sont classés à tort comme positifs.
- **Ligne positive :** 24 avis positifs sont correctement identifiés et 5 sont classés à tort comme négatifs.

Le modèle commet 7 erreurs sur 58 avis de test.

### Matrice de confusion — Allociné

| Vérité \ Prédiction | Négatif | Positif |
|---|---:|---:|
| Négatif | 1 860 | 181 |
| Positif | 137 | 1 822 |

- **Ligne négative :** 1 860 avis négatifs sont correctement identifiés et 181 sont classés à tort comme positifs.
- **Ligne positive :** 1 822 avis positifs sont correctement identifiés et 137 sont classés à tort comme négatifs.

Le modèle commet 318 erreurs sur 4 000 avis de test. Les résultats montrent une bonne performance globale sur Allociné, avec un F1 macro de 92,05 %.

## 4. L’analyse des erreurs

Sur le jeu de démonstration, le modèle commet 7 erreurs : 2 avis négatifs sont classés positifs et 5 avis positifs sont classés négatifs.

Sur Allociné, il commet 318 erreurs : 181 faux positifs et 137 faux négatifs.

Une cause possible est la difficulté à interpréter les avis contenant des formulations contradictoires. Par exemple, un avis de démonstration contient l’expression « Taille trop petite et retour payant », mais mentionne ensuite que le produit est conforme. Le modèle peut donner trop d’importance à certains mots négatifs sans comprendre correctement le contexte global.

Le modèle TF-IDF représente essentiellement le texte à partir de ses termes et ne comprend pas pleinement les relations entre les phrases, l’ironie ou les nuances du langage.

Pour améliorer ces résultats, on pourrait enrichir les données d’entraînement, analyser davantage les erreurs et tester des modèles capables de mieux prendre en compte le contexte. Ces améliorations dépassent le périmètre des séances consacrées à la mise en place d’un premier pipeline fonctionnel.

## 5. L’interface et le seuil d’incertitude

L’interface Streamlit utilise un seuil de confiance de 60 %. Lorsqu’une prédiction n’atteint pas ce seuil, l’avis est présenté comme nécessitant une vérification humaine.

Ce mécanisme permet de limiter les décisions automatiques lorsque le modèle est incertain. Du point de vue de la relation client, ce compromis est utile : les agents peuvent se concentrer sur les avis ambigus au lieu de relire systématiquement tous les commentaires.

Le nombre exact d’avis envoyés à un agent sur le jeu de test doit être relevé lors d’une évaluation avec l’interface et le modèle correspondants : **[à compléter après vérification]**.

## 6. Ce qui a échoué

Plusieurs difficultés ont été rencontrées pendant les travaux pratiques.

Au début, certains tests de l’interface étaient ignorés parce que le fichier du modèle entraîné n’était pas encore présent. L’exécution du script d’entraînement a permis de générer `models/sentiment.joblib` et de vérifier les tests concernés.

Une autre difficulté a été de distinguer les résultats obtenus sur le jeu de démonstration de ceux obtenus sur Allociné. Le script d’évaluation utilise le jeu de démonstration par défaut ; il faut ajouter l’option `--allocine` pour évaluer Allociné. Il est également nécessaire d’utiliser le modèle entraîné sur le même jeu que celui utilisé pour l’évaluation.

Enfin, un avertissement de dépréciation provenant d’une dépendance a été observé pendant les tests. Malgré cet avertissement, les tests se sont terminés correctement.

Les vérifications finales ont donné **51 tests réussis et 1 avertissement**. L’interface Streamlit et l’API FastAPI ont également été lancées et testées.

## 7. Ce que nous ferions autrement

Avec davantage de temps, nous améliorerions la documentation des expériences et automatiserions la comparaison des résultats entre les jeux de démonstration et Allociné. Nous ajouterions également une analyse systématique des erreurs et un suivi du nombre d’avis transmis aux agents selon différents seuils de confiance.

Dans un contexte professionnel, nous surveillerions les performances sur de nouvelles données réelles afin de détecter une éventuelle baisse de qualité du modèle.

## 8. Répartition du travail


## 8. Répartition du travail

| Membre | Ce qu’il a pris en charge |
|---|---|
| Mohamed Taha Hakam (Membre A) | **TP1 :** Récupération du kit, création de l’environnement, création du dépôt GitHub privé, invitation du membre B et de l’enseignant, premier push avec `requirements.lock`. **TP2 :** Installation du kit, génération des données de démonstration, entraînement et évaluation du modèle, puis push des modifications. **TP3 :** Installation du kit, réentraînement du modèle, lancement des tests et push des modifications. |
| Chouaf Mohamed Amine (Membre B) | **TP1 :** Acceptation de l’invitation GitHub, clonage du dépôt, configuration de l’environnement, ajout et commit de ma ligne dans le `README.md`, vérification de l’installation et des tests. **TP2 :** Récupération des modifications, réentraînement du modèle sur mon poste et contrôle C5. **TP3 :** Récupération des modifications, réentraînement du modèle, tests de l’API FastAPI et participation à la rédaction des questions de `docs/semaine3.md`. |
## Outils d’aide à la rédaction

Un assistant d’IA a été utilisé pour aider à structurer et reformuler le compte rendu. Les commandes, les résultats des tests, les métriques et les matrices de confusion ont été vérifiés à partir des sorties réelles du projet.