"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele, predict as _predict  # noqa: E402


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec abstention si la confiance est faible."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"
    seuil_abstention = 0.60

    def __init__(self) -> None:
        charger_modele()

    def predict(self, text: str) -> dict:
        """Renvoie le sentiment ou INDETERMINE si la confiance est insuffisante."""
        r = _predict(text)
        score = r["score"]

        if score < self.seuil_abstention:
            label = "INDETERMINE"
        else:
            label = r["label"].upper()

        return {"label": label, "score": score, "text": text[:100]}



def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()
