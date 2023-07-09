import os,sys
from src.logger import logging
from  src.exception import CustomException
from src.util.util import *

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("saved_models","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models ={
                "Logistic Regression":LogisticRegression(),
                "K Nearest Neighbours": KNeighborsClassifier(),
                "Support Vector Machine": SVC(),
                "Decision Tree":DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier()
                }
            
            #defining parameters for differant models
            params ={
                "Logistic Regression":{
                    'penalty':['none', 'l1', 'l2'],
                    'C':[ 1.0, 0.1, 0.01]
                },

                "K Nearest Neighbours":{ 
                    'n_neighbors' : [5,7,9,11,13,15],
                    'metric' : ['minkowski','euclidean','manhattan']
                },

                "Support Vector Machine":{
                    'kernel': ['rbf', 'linear', 'sigmoid'],
                    'C': [0.1,1, 10], 
                    'gamma': [1,0.1,0.01]
                },

                "Decision Tree":{
                    'max_depth':[3,5,7,9],
                    'criterion':['gini','entropy']
                },

                "Random Forest": {
                    'n_estimators': [25, 50, 100, 150],
                    'max_features': ['sqrt', 'log2', None],
                    'max_depth': [3,5,7, 9]
                }

            }
            

            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                models=models,param=params)

            #To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict
            best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("Model accuracy is low!")
            
            logging.info(f"Best model obtained on  both traininig and testing  dataset")

            preprocessing_obj = save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )


            predicted =best_model.predict(X_test)
            accuracy = accuracy_score(y_test,predicted)

            logging.info(f"model training completed and best model found is {best_model} with accuracy: {accuracy*100}%")
            return best_model,accuracy



        except Exception as e:
            raise CustomException(e,sys) from e 