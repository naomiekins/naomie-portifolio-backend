from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime


class FeatureDrift(BaseModel):
    feature: str
    psi: float
    status: str


class MetricsResponse(BaseModel):
    timestamp: datetime
    model_name: str
    auc_roc: float
    precision: float
    recall: float
    f1: float
    psi_score: float
    predictions_per_hour: int
    drift_status: str
    feature_drift: List[FeatureDrift]
    volume_history: List[int]


class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


class ContactResponse(BaseModel):
    success: bool
    message: str
