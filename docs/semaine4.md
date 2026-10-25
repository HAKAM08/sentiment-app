# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- **Avant (étape A) :** la couverture initiale n'a pas été conservée.
- **Lignes jamais exécutées au départ :** les numéros exacts des lignes manquantes ne sont pas disponibles dans les résultats enregistrés.
- **Comportements non vérifiés :** le démarrage réel de l'API, le comportement lorsque le modèle est absent ou non chargé, et la gestion des erreurs inattendues pendant une prédiction.
- **Après (étape D) :** 97 % de couverture totale.
- **Lignes non couvertes après les tests :** lignes 87 à 89 de `api/main.py`, correspondant au lancement direct de l'application avec `uvicorn`. Aucune exclusion de couverture n'a été ajoutée.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |

| Un texte constitué uniquement d'espaces était accepté par le schéma. | Tests paramétrés et tests de propriété dans `tests/test_limites.py`. | Ajout d'un validateur utilisant `strip()` pour refuser un texte vide. |
| Le modèle pouvait renvoyer une prédiction peu fiable sans verdict d'abstention. | Tests de prédiction et jeu d'or. | Ajout du seuil d'abstention de 0,60 et du verdict `INDETERMINE`. |
| Le démarrage devait échouer lorsque le fichier du modèle est absent. | `test_modele_absent_refuse_le_demarrage`. | Redirection du chemin du modèle vers un fichier inexistant et vérification de `FileNotFoundError`. |
| Un modèle non chargé ne doit pas permettre les prédictions. | Test d'intégration du modèle non chargé. | Vérification du retour HTTP 503 sur `/health` et `/predict`. |
| Une erreur inattendue du modèle pouvait être renvoyée comme une erreur 422. | `test_erreur_interne_retourne_500_sans_details`. | Les exceptions inattendues du classifieur renvoient HTTP 500 sans exposer le message interne. |

## 3. Seuil d'abstention

Le script `python src/courbe_seuil.py` a été exécuté sur un jeu de test de 58 avis de démonstration.

| Seuil | Avis classés | Part classée | Exactitude | Erreurs | Envoyés à un humain |
|---|---:|---:|---:|---:|---:|
| 0,50 | 58 | 100 % | 87,9 % | 7 | 0 |
| 0,60 | 42 | 72 % | 95,2 % | 2 | 16 |
| 0,70 | 37 | 64 % | 100 % | 0 | 21 |

Le seuil retenu est **0,60**. Il réduit les erreurs de 7 à 2 par rapport au seuil de 0,50, tout en conservant une classification pour 42 avis sur 58. Les 16 autres avis, soit environ 28 %, sont envoyés à un humain. Un seuil plus élevé de 0,70 élimine les erreurs sur ce jeu de test, mais nécessite une intervention humaine pour 21 avis. Le seuil de 0,60 représente donc un compromis entre fiabilité et couverture des prédictions.

## 4. Jeu d'or

Le résultat de `python src/bilan_jeu_or.py` sur 20 avis est le suivant :

- **Prédictions justes :** 5.
- **Abstentions (`INDETERMINE`) :** 14.
- **Erreurs franches déclarées :** 1.

Le modèle s'abstient sur 70 % des avis du jeu d'or. Il ne fournit donc une étiquette déterminée que pour 6 avis sur 20, dont 5 sont corrects et 1 correspond à une erreur connue déclarée. Cela montre que le seuil protège contre certaines prédictions incertaines, mais que le modèle reste limité sur des avis difficiles, notamment les formulations nuancées ou les négations. L'erreur connue est conservée et documentée plutôt que masquée.

## 5. Outils statiques

- **Ruff au départ :** 16 remarques signalées lors de la première vérification.
- **Ruff à la fin :** `ruff check .` — tous les contrôles passent.
- **Mypy à la fin :** `mypy api` — aucun problème détecté dans quatre fichiers source.
- **Mypy au départ :** [À compléter avec le résultat initial].
- **Défauts de la partie 2 signalés par Ruff et Mypy :** [À compléter après comparaison avec les résultats initiaux].
- **Conclusion :** les tests vérifient le comportement de l'API à l'exécution, tandis que Ruff et Mypy détectent certaines catégories de problèmes statiques. Ces outils sont complémentaires et ne remplacent pas les tests.

## Validation finale

La suite complète affiche **86 tests réussis, 1 échec attendu (`XFAIL`) et aucun test en échec**. La couverture totale de l'API est de 97 %. `ruff check .` et `mypy api` passent sans erreur. Le `XFAIL` correspond à une erreur de classification connue et documentée dans le jeu d'or.
