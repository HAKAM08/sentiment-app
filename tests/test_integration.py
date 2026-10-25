
"""Tests d'intégration : démarrage de l'API et gestion des pannes (TP4)."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from api.main import app

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import predict as predict_module  # noqa: E402


MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"

pytestmark = pytest.mark.skipif(
    not MODELE.exists(),
    reason="modèle non produit : python src/train.py",
)


def test_demarrage_reel_charge_le_modele():
    """D.1 : le lifespan charge réellement le modèle."""
    with TestClient(app) as client:
        reponse = client.get("/health")

    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]



def test_modele_absent_refuse_le_demarrage(monkeypatch, tmp_path):
    """D.2 : l'API ne démarre pas si le fichier du modèle est absent."""
    chemin_absent = tmp_path / "modele_absent.joblib"

    monkeypatch.setattr(predict_module, "MODELE", chemin_absent)
    predict_module.charger_modele.cache_clear()

    with pytest.raises(FileNotFoundError):
        with TestClient(app):
            pass



def test_modele_non_charge_retourne_503(monkeypatch):
    """D.3 : /health et /predict répondent 503 sans classifier."""
    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier", raising=False)

        health = client.get("/health")
        predict = client.post("/predict", json={"text": "Très bon produit"})

    assert health.status_code == 503
    assert predict.status_code == 503


@pytest.mark.parametrize(
    "exception",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
)
def test_erreur_interne_retourne_500_sans_details(monkeypatch, exception):
    """D.4 : les erreurs inattendues sont masquées au client."""

    class FauxClassifier:
        model_name = "classifier de test"

        def predict(self, text):
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", FauxClassifier())
        reponse = client.post("/predict", json={"text": "Avis de test"})

    assert reponse.status_code == 500
    assert reponse.json()["detail"] == "Erreur interne du serveur"
    assert str(exception) not in reponse.text
