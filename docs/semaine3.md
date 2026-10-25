Question 1 — Pourquoi l'API refuse-t-elle de démarrer sans modèle plutôt que de répondre 503 ?

L’API charge le modèle au démarrage. Si le fichier `models/sentiment.joblib` est absent, une `FileNotFoundError` peut se produire, empêchant l’application de terminer son initialisation. Le serveur ne peut donc pas traiter les requêtes. Le code HTTP 503 serait plutôt utilisé si l’API était démarrée, mais que le service était temporairement indisponible.

Question 2 — Le texte vide est-il refusé deux fois de manière redondante ?
Les deux vérifications protègent des couches différentes. Pydantic valide les données reçues par l'API, tandis que predict() protège la fonction de prédiction lorsqu'elle est appelée directement ou depuis un autre composant. La validation peut sembler redondante dans le parcours HTTP normal, mais elle renforce la robustesse de la fonction. En revanche, les deux couches devraient idéalement produire un format d'erreur cohérent.