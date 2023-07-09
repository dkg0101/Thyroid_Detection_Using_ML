import os ,sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
import dill
 

from sklearn.metrics import (accuracy_score,roc_curve,roc_auc_score)
from sklearn.model_selection import GridSearchCV

from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info(f'created and saved preprocessed pickle object at: [{file_path}]')
    except Exception as e:
        raise CustomException(e,sys) from e
    


def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try: 
        report ={}

        for i in range(len(list(models))):
            model =list(models.values())[i]
            param_grid = param[list(models.keys())[i]]

            gs = GridSearchCV(model,param_grid,cv=3,verbose=3)

            logging.info(f"training model [{model}]...")
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            logging.info('Model training completed with best parameters')
            
            y_train_pred =model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = accuracy_score(y_train,y_train_pred) 

            test_model_score = accuracy_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report 

    except Exception as e:
        raise CustomException(e,sys) from e
    

 



