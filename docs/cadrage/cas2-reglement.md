# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Le système doit répondre aux questions des étudiants concernant le règlement interne de l'établissement en fournissant la référence exacte de l'article utilisé.

## Utilisateur final (obligatoire)

L'utilisateur final est l'étudiant qui souhaite obtenir rapidement une information sur le règlement interne.
## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'approche RAG est retenue car les réponses doivent être basées sur le contenu officiel du règlement et accompagnées d'une citation précise de l'article (a), tandis que le nombre de questions quotidiennes reste limité (d).

## Données nécessaires et leur origine (obligatoire)


Les données nécessaires sont les documents officiels du règlement interne de l'établissement, qui constituent la source de référence pour les réponses.

## Métrique de succès et seuil d'acceptation (obligatoire)
Le système doit fournir une réponse correcte accompagnée de la citation exacte de l'article correspondant sur un jeu de 20 questions de test.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)


Une réponse incorrecte peut induire un étudiant en erreur sur ses droits ou obligations ; les réponses importantes doivent donc pouvoir être vérifiées à partir du règlement officiel.

## Risques éthiques ou de confidentialité (obligatoire)

Le système doit éviter d'inventer des règles et doit uniquement utiliser les documents officiels disponibles comme sources de référence.
## Approche écartée et pourquoi (facultatif)

L'approche générative seule est rejetée car elle présente un risque d'hallucination et pourrait fournir une réponse non présente dans le règlement.
