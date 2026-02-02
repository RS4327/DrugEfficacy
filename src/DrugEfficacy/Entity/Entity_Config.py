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


