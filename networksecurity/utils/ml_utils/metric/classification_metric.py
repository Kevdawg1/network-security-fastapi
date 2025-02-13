import os, sys
from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from sklearn.metrics import f1_score, precision_score, recall_score

def get_classification_score(y_actual: object, y_pred: object) -> ClassificationMetricArtifact:
    try:
        f1 = f1_score(y_actual, y_pred)
        precision = precision_score(y_actual, y_pred)
        recall = recall_score(y_actual, y_pred)
        return ClassificationMetricArtifact(f1_score=f1, precision_score=precision, recall_score=recall)
    except Exception as e:
        raise NetworkSecurityException(e, sys)