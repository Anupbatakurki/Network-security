import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.main_utils.utils import save_object, load_object
from networksecurity.utils.main_utils.utils import load_numpy_array_data, evaluate_models
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)

import mlflow
import dagshub

dagshub.init(
    repo_owner='Anupbatakurki',
    repo_name='Network-security',
    mlflow=True
)

'''
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/krishnaik06/networksecurity.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="krishnaik06"
os.environ["MLFLOW_TRACKING_PASSWORD"]="7104284f1bb44ece21e0e2adb4e36a250ae3251"
'''


class ModelTrainer:

    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        data_transformation_artifact: DataTransformationArtifact
    ):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def track_mlflow(
        self,
        best_model,
        classificationmetric
    ):
        try:

            with mlflow.start_run():

                f1_score = classificationmetric.f1_score
                precision_score = classificationmetric.precision_score
                recall_score = classificationmetric.recall_score

                # Log metrics
                mlflow.log_metric(
                    "f1_score",
                    f1_score
                )

                mlflow.log_metric(
                    "precision",
                    precision_score
                )

                mlflow.log_metric(
                    "recall_score",
                    recall_score
                )

                # Log model
                mlflow.sklearn.log_model(
                    best_model,
                    name="model"
                )

                logging.info(
                    "Model and metrics logged successfully in MLflow."
                )

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def train_model(
        self,
        X_train,
        y_train,
        x_test,
        y_test
    ):

        models = {

            "Random Forest": RandomForestClassifier(
                verbose=1
            ),

            "Decision Tree": DecisionTreeClassifier(),

            "Gradient Boosting": GradientBoostingClassifier(
                verbose=1
            ),

            "Logistic Regression": LogisticRegression(
                verbose=1
            ),

            "AdaBoost": AdaBoostClassifier(),
        }


        params = {

            "Decision Tree": {
                'criterion': [
                    'gini',
                    'entropy',
                    'log_loss'
                ],

                # 'splitter':['best','random'],
                # 'max_features':['sqrt','log2'],
            },

            "Random Forest": {

                # 'criterion':['gini', 'entropy', 'log_loss'],
                # 'max_features':['sqrt','log2',None],

                'n_estimators': [
                    8,
                    16,
                    32,
                    128,
                    256
                ]
            },

            "Gradient Boosting": {

                # 'loss':['log_loss', 'exponential'],

                'learning_rate': [
                    .1,
                    .01,
                    .05,
                    .001
                ],

                'subsample': [
                    0.6,
                    0.7,
                    0.75,
                    0.85,
                    0.9
                ],

                # 'criterion':['squared_error', 'friedman_mse'],
                # 'max_features':['auto','sqrt','log2'],

                'n_estimators': [
                    8,
                    16,
                    32,
                    64,
                    128,
                    256
                ]
            },

            "Logistic Regression": {},

            "AdaBoost": {

                'learning_rate': [
                    .1,
                    .01,
                    .001
                ],

                'n_estimators': [
                    8,
                    16,
                    32,
                    64,
                    128,
                    256
                ]
            }

        }


        # Evaluate all models
        model_report: dict = evaluate_models(
            X_train=X_train,
            y_train=y_train,
            X_test=x_test,
            y_test=y_test,
            models=models,
            param=params
        )


        # Get best model score
        best_model_score = max(
            sorted(model_report.values())
        )


        # Get best model name
        best_model_name = list(
            model_report.keys()
        )[
            list(model_report.values()).index(
                best_model_score
            )
        ]


        # Get best model
        best_model = models[best_model_name]


        logging.info(
            f"Best model selected: {best_model_name}"
        )

        logging.info(
            f"Best model score: {best_model_score}"
        )


        # -----------------------------------------
        # Training Prediction
        # -----------------------------------------

        y_train_pred = best_model.predict(
            X_train
        )

        classification_train_metric = get_classification_score(
            y_true=y_train,
            y_pred=y_train_pred
        )


        # -----------------------------------------
        # Testing Prediction
        # -----------------------------------------

        y_test_pred = best_model.predict(
            x_test
        )

        classification_test_metric = get_classification_score(
            y_true=y_test,
            y_pred=y_test_pred
        )


        # -----------------------------------------
        # Track experiment with MLflow
        # -----------------------------------------

        self.track_mlflow(
            best_model,
            classification_train_metric
        )

        self.track_mlflow(
            best_model,
            classification_test_metric
        )


        # -----------------------------------------
        # Load Preprocessor
        # -----------------------------------------

        preprocessor = load_object(
            file_path=self.data_transformation_artifact.transformed_object_file_path
        )


        # -----------------------------------------
        # Create Model Directory
        # -----------------------------------------

        model_dir_path = os.path.dirname(
            self.model_trainer_config.trained_model_file_path
        )

        os.makedirs(
            model_dir_path,
            exist_ok=True
        )


        # -----------------------------------------
        # Create Complete Network Model
        # -----------------------------------------

        Network_Model = NetworkModel(
            preprocessor=preprocessor,
            model=best_model
        )


        # -----------------------------------------
        # Save Model in Artifacts
        # -----------------------------------------

        save_object(
            self.model_trainer_config.trained_model_file_path,
            obj=Network_Model
        )


        logging.info(
            f"Model saved at: "
            f"{self.model_trainer_config.trained_model_file_path}"
        )


        # -----------------------------------------
        # Model Pusher
        # -----------------------------------------

        final_model_dir = "final_model"

        os.makedirs(
            final_model_dir,
            exist_ok=True
        )


        final_model_path = os.path.join(
            final_model_dir,
            "model.pkl"
        )


        save_object(
            file_path=final_model_path,
            obj=Network_Model
        )


        logging.info(
            f"Final model saved at: "
            f"{final_model_path}"
        )


        # -----------------------------------------
        # Verify Final Model
        # -----------------------------------------

        if not os.path.exists(
            final_model_path
        ):
            raise Exception(
                f"Final model was not created at "
                f"{final_model_path}"
            )


        logging.info(
            "Final model verification successful."
        )


        # -----------------------------------------
        # Model Trainer Artifact
        # -----------------------------------------

        model_trainer_artifact = ModelTrainerArtifact(
            trained_model_file_path=(
                self.model_trainer_config.trained_model_file_path
            ),

            train_metric_artifact=(
                classification_train_metric
            ),

            test_metric_artifact=(
                classification_test_metric
            )
        )


        logging.info(
            f"Model trainer artifact: "
            f"{model_trainer_artifact}"
        )


        return model_trainer_artifact


    def initiate_model_trainer(
        self
    ) -> ModelTrainerArtifact:

        try:

            train_file_path = (
                self.data_transformation_artifact
                .transformed_train_file_path
            )

            test_file_path = (
                self.data_transformation_artifact
                .transformed_test_file_path
            )


            # Loading training array
            train_arr = load_numpy_array_data(
                train_file_path
            )


            # Loading testing array
            test_arr = load_numpy_array_data(
                test_file_path
            )


            # Split train and test data
            x_train, y_train, x_test, y_test = (

                train_arr[:, :-1],

                train_arr[:, -1],

                test_arr[:, :-1],

                test_arr[:, -1],

            )


            # Start model training
            model_trainer_artifact = self.train_model(
                x_train,
                y_train,
                x_test,
                y_test
            )


            return model_trainer_artifact


        except Exception as e:

            raise NetworkSecurityException(
                e,
                sys
            )