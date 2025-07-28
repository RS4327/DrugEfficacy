import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')


''' 
To automatically set up the basic folder and file structure of your project (nltkClassifier) 
so that you don’t have to manually create directories and boilerplate files every time.

This is especially helpful for:

Maintaining consistency across multiple projects

Ensuring all required files are present

Speeding up the setup for new team members or repositories

Setting up for tools like DVC, GitHub Actions, Jupyter, and templates

'''


ProjectName='nltkClassifier'

list_of_files=[
    ".gethug/workflows/.gitkeep",
    f"src/{ProjectName}/__init__.py",
    f"src/{ProjectName}/Components/__init__.py",
    f"src/{ProjectName}/Config/__init__.py",
    f"src/{ProjectName}/Constants/__init__.py",
    f"src/{ProjectName}/Entity/__init__.py",
    f"src/{ProjectName}/Pipeline/__init__.py",
    f"src/{ProjectName}/Utils/__init__.py",
    "Config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "Research/trails.ipynb",
    "Templates/index.html",
    "app.py"

]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating Directory : {filedir} for the file :{filename}')
    if (not os.path.exists(filepath) or (os.path.getsize)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating the Empty File : {filepath}")
    else:
        logging.info(f"{filename} is already exists")
