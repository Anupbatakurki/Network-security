import sys,os
import os
import sys
import shap
import matplotlib.pyplot as plt
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class ModelExplainability:

    def __init__(self,model,X_train,X_test):
        try:
            self.model=model
            self.X_train=X_train
            self.X_test=X_test
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_model_explainability(self):
        try:
            logging.info("Starting SHAP explainability")

            explainer=shap.Explainer(
                self.model,
                self.X_train
            )

            shap_values=explainer(
                self.X_test
            )

            os.makedirs(
                "Artifacts/shap",
                exist_ok=True
            )

            plt.figure()

            shap.plots.bar(
                shap_values,
                show=False
            )

            plt.tight_layout()

            plt.savefig(
                "Artifacts/shap/shap_feature_importance.png",
                bbox_inches="tight"
            )

            plt.close()

            plt.figure()

            shap.plots.beeswarm(
                shap_values,
                show=False
            )

            plt.tight_layout()

            plt.savefig(
                "Artifacts/shap/shap_summary.png",
                bbox_inches="tight"
            )

            plt.close()

            logging.info(
                "SHAP explainability completed successfully"
            )

            return shap_values

        except Exception as e:
            raise NetworkSecurityException(e,sys)