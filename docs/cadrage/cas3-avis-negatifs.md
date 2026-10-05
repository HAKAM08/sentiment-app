# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Le système doit identifier automatiquement les avis clients négatifs afin de permettre à l'équipe de les traiter en priorité.
## Utilisateur final (obligatoire)

Les utilisateurs finaux sont les membres de l'équipe du service client ou de l'équipe e-commerce chargés de traiter les avis.
## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'approche Machine Learning est retenue car les avis peuvent être associés à des labels à partir des notes disponibles (a), et le système doit traiter potentiellement des milliers d'avis par jour (d).

## Données nécessaires et leur origine (obligatoire)
Les données nécessaires sont les anciens avis clients accompagnés de leurs notes ou labels permettant d'identifier les avis positifs et négatifs.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale est le rappel de la classe négative avec un seuil cible de 0,90.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une erreur de classification peut faire passer un avis négatif au second plan, mais la conséquence reste limitée car un membre de l'équipe peut effectuer une vérification humaine.
## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des informations personnelles ; les données utilisées pour entraîner le modèle doivent donc être traitées avec précaution et les informations inutiles doivent être protégées.

## Approche écartée et pourquoi (facultatif)

