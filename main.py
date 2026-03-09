import sys
import os

print(os.getcwd())

# Add project paths
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(os.getcwd())

from DrugEfficacy import logger
from DrugEfficacy.Pipeline.Stage_D01_DataIngestoin import DataIngestionPipeline
from DrugEfficacy.Pipeline.Stage_D02_DataPreProcessing import DataPreProcessingPipeline
from DrugEfficacy.Pipeline.Stage_D03_DataFeatureEngineering import DataFeatureEngineeringPipeline
from DrugEfficacy.Pipeline.Stage_D04_DataModelTraining import DataModelTrainingPipeline


# ---------------- DATA INGESTION ----------------
Stage_Name = "Data Ingestion"

try:
    logger.info(f"<<<<<< Stage {Stage_Name} Started >>>>>>")

    obj = DataIngestionPipeline()
    df = obj.main()

    logger.info(f"DataFrame Shape after Data Ingestion: {df.shape}")

    logger.info(f"<<<<<< Stage {Stage_Name} Completed Successfully >>>>>>")

except Exception as e:
    logger.error("Error at Data Ingestion")
    logger.error(e)
    raise e


# ---------------- DATA PREPROCESSING ----------------
Stage_Name = "Data PreProcessing"

try:
    logger.info(f"<<<<<< Stage {Stage_Name} Started >>>>>>")

    obj = DataPreProcessingPipeline()
    df = obj.main(df)

    logger.info(f"DataFrame Shape after preprocessing: {df.shape}")

    logger.info(f"<<<<<< Stage {Stage_Name} Completed Successfully >>>>>>")

except Exception as e:
    logger.error(e)
    raise e


# ---------------- FEATURE ENGINEERING ----------------
Stage_Name = "Data Feature Engineering"

try:
    logger.info(f"<<<<<< Stage {Stage_Name} Started >>>>>>")

    obj = DataFeatureEngineeringPipeline()
    x, y = obj.main(df)

    logger.info(f"X Shape: {x.shape}")
    logger.info(f"Y Shape: {y.shape}")

    logger.info(f"<<<<<< Stage {Stage_Name} Completed Successfully >>>>>>")

except Exception as e:
    logger.error(e)
    raise e


# ---------------- MODEL TRAINING ----------------
Stage_Name = "Data Model Training"

try:
    logger.info(f"<<<<<< Stage {Stage_Name} Started >>>>>>")

    obj = DataModelTrainingPipeline()

    best_model_name, best_model, model_scores = obj.main(x, y)

    logger.info(f"Best Model Name: {best_model_name}")
    logger.info(f"Best Model: {best_model}")
    logger.info(f"Model Scores: {model_scores}")

    logger.info(f"<<<<<< Stage {Stage_Name} Completed Successfully >>>>>>")

except Exception as e:
    logger.error(e)
    raise e