import numpy as np
import pandas as pd
from DrugEfficacy.Config.CongurationManager import ConfigurationManagerConfig
from DrugEfficacy.Components.Data_Model_Training import DataModelTraining
from DrugEfficacy import logger

Stage_Name='Data Model Training'

class DataModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self, x, y):

        try:

            logger.info("Starting Model Training Pipeline")

            config = ConfigurationManagerConfig()

            datamodeltraining = config.getdatamodeltraining()

            data_model = DataModelTraining(config=datamodeltraining)

            best_model_name, best_model, model_scores = data_model.TrainModel(x, y)

            logger.info(f"Best Model Name: {best_model_name}")
            logger.info(f"Model Scores: {model_scores}")

            return best_model_name, best_model, model_scores

        except Exception as e:

            logger.error("Error in Model Training Pipeline")
            logger.error(str(e))

            raise e

if __name__ =='__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} started >>>>>>>>>>>>>>>>>>>>>>")
        obj=DataModelTrainingPipeline()
        best_model_name, best_model, model_scores =obj.main()
        
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} Completed Successfully  >>>>>>>>>>>>>>>>>>>>>>")
    except  Exception as e:
        logger.info(e)
        raise e




