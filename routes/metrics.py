import random
from datetime import datetime
from fastapi import APIRouter
from models.schemas import MetricsResponse, FeatureDrift

router = APIRouter()

FEATURES = ["transaction_amt", "merchant_cat", "time_of_day", "device_type", "location_dist"]


def _jitter(value: float, spread: float = 0.03) -> float:
    return round(value + random.uniform(-spread, spread), 3)


def _status(psi: float) -> str:
    return "stable" if psi < 0.1 else "warning" if psi < 0.2 else "alert"


@router.get("/", response_model=MetricsResponse)
def get_metrics():
    psi = round(random.uniform(0.03, 0.13), 3)
    return MetricsResponse(
        timestamp=datetime.utcnow(),
        model_name="fraud_detection_v2",
        auc_roc=_jitter(0.94, 0.02),
        precision=_jitter(0.91, 0.02),
        recall=_jitter(0.87, 0.02),
        f1=_jitter(0.89, 0.02),
        psi_score=psi,
        predictions_per_hour=random.randint(1500, 2200),
        drift_status=_status(psi),
        feature_drift=[
            FeatureDrift(
                feature=f,
                psi=round(random.uniform(0.02, 0.18), 3),
                status=_status(round(random.uniform(0.02, 0.18), 3)),
            )
            for f in FEATURES
        ],
        volume_history=[random.randint(35, 95) for _ in range(15)],
    )


@router.get("/summary")
def get_summary():
    psi = round(random.uniform(0.03, 0.13), 3)
    return {
        "model": "fraud_detection_v2",
        "status": _status(psi),
        "auc_roc": _jitter(0.94, 0.02),
        "psi": psi,
        "timestamp": datetime.utcnow().isoformat(),
    }
