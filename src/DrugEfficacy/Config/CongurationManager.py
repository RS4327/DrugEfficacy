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
    


