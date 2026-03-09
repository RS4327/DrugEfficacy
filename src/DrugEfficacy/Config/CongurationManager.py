from pathlib import Path
from DrugEfficacy import logger
from DrugEfficacy.Constant import *
from DrugEfficacy.Utils.common import *
from DrugEfficacy.Entity.Entity_Config import *



class ConfigurationManagerConfig:
    def __init__(self,
                 config_path=CONFIG_PATH,
                 params_path=PARAMS_PATH
                 ):
        self.config=Read_Yaml(Path(config_path))
        self.params=Read_Yaml(Path(params_path))
        
        create_directories([self.config.artifacts_root])
    
    def GetDataIngestionConfig(self)->DataIngestionConfig:
        config=self.config.Data_Ingestion

        Data_Ingestion_Config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_path=config.source_path
        )
        return Data_Ingestion_Config
    
    def getdatapreprocessing(self)->DataPreProcessingConfig:
        config=self.config.Data_Preprocessing


        data_preprocessing_config=DataPreProcessingConfig(
            root_dir=config.root_dir,
            validation_path=config.validation_path,
            cleaned_data_path=config.cleaned_data_path,
            allowed_missing_percentage=config.allowed_missing_percentage,
            allowed_outlier_std=config.allowed_outlier_std,
            encoding_strategy=config.encoding_strategy,
            scaling_strategy=config.scaling_strategy,
            imputation_strategy=config.imputation_strategy,
            handling_missing=config.handling_missing
        )
        return data_preprocessing_config

    def getdatafeatureengineering(self)->DataFeatureEngineeringConfig:
        config=self.config.Data_FeatureEngineering

        Data_FeatureEngineering_Config=DataFeatureEngineeringConfig(
            root_dir=config.root_dir,
            input_data_path=config.input_data_path,
            output_data_path=config.output_data_path,
            features_selection=config.features_selection,
            correlation_threshold=config.correlation_threshold
        )
        return Data_FeatureEngineering_Config

    def getdatamodeltraining(self)->DataModelTrainingCOnfig:
        config=self.config.Data_ModelTraining
        Data_ModelTraining_Config=DataModelTrainingCOnfig(
            root_dir=config.root_dir,
            model_dir=config.model_dir,
            reports_dir=config.reports_dir,
            logs_dir = config.logs_dir,
            test_size =config.test_size,
            random_state =config.random_state


        )
        return Data_ModelTraining_Config
        


