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
        config=self.config.data_preprocessing
        

        data_preprocessing_config=DataPreProcessingConfig(
            root_dir=config.root_dir,
            validation_path=config.valiation_path,
            cleaned_data_path=config.cleaned_data_path,
            allowed_missing_percentage=config.allowed_missing_percentage,
            allowed_outlier_std=config.allowed_outlier_std,
            encoding_strategy=config.encoding_strategy,
            scaling_strategy=config.scaling_strategy,
            imputation_strategy=config.imputation_strategy,
            handling_missing=config.handling_missing
        )
        return data_preprocessing_config

    


