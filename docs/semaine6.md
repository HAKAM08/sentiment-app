# Semaine 6 : le paquet, notes du binôme

## 1. Pourquoi le modèle n'est-il pas dans la roue ? Comment le paquet le trouve-t-il ?

Le modèle n'est pas inclus dans la roue pour éviter d'alourdir le paquet et de mélanger le code avec les fichiers générés pendant l'entraînement. Le paquet recherche le modèle par défaut dans le dossier `models/sentiment.joblib`. Si le modèle se trouve ailleurs, on peut préciser son chemin avec la variable d'environnement `SENTIMENT_MODELE`. Nous avons vérifié cela en installant la roue dans un environnement indépendant du dépôt.

## 2. Qu'est-ce qui a changé dans api/model.py quand predict() est entré dans le paquet, et pourquoi est-ce mieux ?

Nous avons remplacé l'ancien import depuis `src/predict.py` par un import direct depuis `sentiment_app.predict`. Nous avons également supprimé la modification manuelle de `sys.path`. Cette solution est meilleure parce que l'API utilise directement le paquet Python, sans dépendre de l'organisation des anciens dossiers du projet.

## 3. La roue installée hors du dépôt : qu'a-t-il fallu lui fournir, et pourquoi scikit-learn est-il épinglé dans pyproject.toml ?

Après avoir installé la roue dans un environnement séparé, nous avons constaté que le modèle était absent. Nous avons donc fourni son chemin avec `SENTIMENT_MODELE` pour permettre à la prédiction de fonctionner. Scikit-learn est épinglé dans `pyproject.toml` pour garantir une version compatible avec celle utilisée pour entraîner et sauvegarder le modèle, et éviter les problèmes de compatibilité lors de son chargement.
