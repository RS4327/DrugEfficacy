from nltkClassifier.Entity.config_entity import DataValidationConfig
from nltkClassifier.Components.data_validation import DataValidation
from nltkClassifier.Config.configuration import ConfigurationManager
from nltkClassifier import logger

Stage_Name ='Data Validation'


class DataValidationPipeLine:
    def __init__(self):
        pass
    def main(self):

        try :
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_cofig()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()

        except Exception as e:
            raise e
        


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataValidationPipeLine()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e
        
