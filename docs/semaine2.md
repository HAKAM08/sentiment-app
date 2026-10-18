
# Semaine 2 — Entraînement et évaluation du modèle

Le modèle commet 7 erreurs sur les 58 avis du jeu de test : 2 avis négatifs sont classés à tort comme positifs et 5 avis positifs sont classés à tort comme négatifs. Le rappel de la classe négative est de 0,931, ce qui est important pour le cas 3.

Ces erreurs proviennent principalement des avis mitigés, car le modèle TF-IDF associé à la régression logistique ne tient pas suffisamment compte de l'ordre des mots ni des retournements de sens introduits par des expressions comme « mais finalement ».

Pour réduire ces erreurs, il faudrait utiliser des représentations prenant en compte le contexte et l'ordre des mots, comme des embeddings ou des modèles de langage plus avancés, puis réévaluer les performances en privilégiant le rappel de la classe négative conformément au cahier des charges.
