# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface utilise l'API FastAPI pour envoyer les avis et recevoir les résultats. Comme ça, elle ne charge pas directement le modèle et le code reste mieux organisé.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Quand le modèle hésite, l'interface affiche « Je ne sais pas » et demande une vérification humaine. C'est mieux parce qu'on évite de donner un résultat faux quand le modèle n'est pas sûr.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Quand l'API ne fonctionne plus, l'interface affiche un message indiquant qu'il faut lancer l'API. Dans le fichier CSV, un seul avis est envoyé vers un humain, car son résultat est indéterminé.
