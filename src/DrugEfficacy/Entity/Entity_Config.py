from pathlib import Path
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    root_dir : str
    source_path : str

@dataclass
class DataPreProcessingConfig:
    root_dir : str
    validation_path : str
    cleaned_data_path : str
    allowed_missing_percentage : int
    allowed_outlier_std : int
    encoding_strategy : str
    scaling_strategy : str
    imputation_strategy : str
    handling_missing : bool

@dataclass
class DataFeatureEngineeringConfig:
  root_dir : str
  input_data_path : str
  output_data_path : str
  features_selection : bool
  correlation_threshold : float

@dataclass 
class RandomForestConfig:
   n_estimator : int 
   max_features : str 
   max_depth : int 
   min_samples_split : int 
   random_state : int 
@dataclass 
class XGBoostConfig:
   n_estimator  :int 
   learning_rate : float 
   max_depth : int
   subsmaple : float 
   colsample_bytree : float 
   random_state : int
@dataclass 
class DNNConfig: 
   layers : list
   activation : str
   batch_size : int
   dropout_rate : float
   epochs : int
   optimizer : str 
   loss : str
   metrics : list

@dataclass 
class ModelConfig:
   RandomForestConfig
   XGBoostConfig
   DNNConfig


@dataclass 
class DataModelTrainingCOnfig:
   root_dir : str
   model_dir : ModelConfig 
   reports_dir : Path
   logs_dir : Path
   test_size :  float
   random_state : int 

