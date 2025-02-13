import os,sys

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from networksecurity.logging.logger import logging
from networksecurity.exceptions.exception import NetworkSecurityException

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            
            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)
            
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
        
        return report
            
    except Exception as e: 
        raise NetworkSecurityException(e, sys)