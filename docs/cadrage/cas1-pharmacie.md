# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)


Le système doit détecter si une ordonnance est incomplète avant sa validation par le pharmacien.

## Utilisateur final (obligatoire)
L'utilisateur final est le pharmacien qui vérifie et valide les ordonnances.


## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'approche par règles métier est retenue car les critères permettant de vérifier une ordonnance sont connus et doivent être explicables (a), tandis qu'une erreur d'approbation peut avoir une conséquence importante (d).

## Données nécessaires et leur origine (obligatoire)
Le système utilise les informations présentes dans l'ordonnance afin de vérifier la présence des éléments obligatoires, avec une attention particulière aux données de santé.


## Métrique de succès et seuil d'acceptation (obligatoire)
Le système doit identifier correctement les ordonnances incomplètes et toutes les décisions doivent pouvoir être expliquées par une règle identifiable.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une fausse validation peut avoir une conséquence grave pour le patient ; la décision finale doit donc obligatoirement être vérifiée par un pharmacien.

## Risques éthiques ou de confidentialité (obligatoire)
Les ordonnances peuvent contenir des données de santé sensibles ; leur accès, leur stockage et leur traitement doivent donc être strictement contrôlés.

## Approche écartée et pourquoi (facultatif)
L'approche générative est rejetée car elle pourrait produire une décision difficile à expliquer et inadaptée à une situation où une erreur peut avoir de graves conséquences.

