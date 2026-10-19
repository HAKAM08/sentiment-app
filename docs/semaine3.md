Question 1 — Pourquoi l'API refuse-t-elle de démarrer sans modèle plutôt que de répondre 503 ?

Réponse possible, si elle correspond à ce que tu as observé :
L'API charge le modèle au démarrage. Si le fichier models/sentiment.joblib est absent, le chargement déclenche une FileNotFoundError. L'application ne termine donc pas son initialisation et le serveur ne peut pas traiter les requêtes. Un code HTTP 503 suppose qu'une application est démarrée et peut recevoir la requête, mais que le service est temporairement indisponible.

Question 2 — Le texte vide est-il refusé deux fois de manière redondante ?
Les deux vérifications protègent des couches différentes. Pydantic valide les données reçues par l'API, tandis que predict() protège la fonction de prédiction lorsqu'elle est appelée directement ou depuis un autre composant. La validation peut sembler redondante dans le parcours HTTP normal, mais elle renforce la robustesse de la fonction. En revanche, les deux couches devraient idéalement produire un format d'erreur cohérent.