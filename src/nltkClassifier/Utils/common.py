import os 
from  box.exceptions import BoxValueError
import yaml
from nltkClassifier import logger
from pathlib import Path
from typing import Any
import json
import joblib
from ensure import ensure_annotations
from box import Box
from pathlib  import Path
from typing import  Any
import base64


class ConfigBox(Box):
    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"Key '{item}' not found in ConfigBox.")
        return super().__getattr__(item)
 
@ensure_annotations
def read_yaml(path_to_yaml:Path) ->ConfigBox:
    
    
    # print("Current Working Directory yaml:",path_to_yaml)
    # print("Current Directory:", os.getcwd())
    # print("Files:", os.listdir())
    # print("Config Folder Contents:", os.listdir("Config") if os.path.exists("Config") else "Config folder missing")

    try :  
        with open(Path(str(path_to_yaml).replace('\\', '/'))) as yaml_file:
            #print(f" {path_to_yaml} chekcing ")
            content=yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f" yamal file is empty {yaml_file}")
            if not isinstance(content,dict):
                raise ValueError(f"YAML content must be a Dictionay ,got{type(content)}")
            
            logger.info(f"yamal file : {path_to_yaml} loaded sucessfully")
            
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Read yaml : YAML File Content is invalid for Box")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        #print('path_to_directories ',path_to_directories)
        os.makedirs(path,exist_ok=True)

        if verbose:
            logger.info(f"Created Directory at : {path}")

# @ensure_annotations
# def save_json(path:Path,data:dict):
#     with open(path,'w') as f:
#         json.dump(data,f,indent=4)
#     logger.info(f"file save at :{path}")

# @ensure_annotations
# def load_json(path:Path) ->ConfigBox:

#     with open(path) as f:
#         content=json.load()
#     logger.info(f"Json file loaded successfully from :{path}")
#     return ConfigBox(content) 

# @ensure_annotations
# def save_bin(data:Any,path:Path):
#     joblib.dump(value=data,filename=path)
#     logger.info(f"Binary file saved at :{path}")


# @ensure_annotations
# def load_bin(path:Path) ->Any:
#     data=joblib.load(path)
#     logger.info(f"Binary file loadded from :{path}")
#     return data

@ensure_annotations
def get_size(path:Path) ->str:

    size_in_kb=round(os.path.getsize(path)/1024)

    return f"~{size_in_kb} KB"


