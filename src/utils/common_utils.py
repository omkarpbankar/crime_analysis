import yaml 
import os
import shutil
import logging
import json 


def read_params(config_path:str) -> dict:
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    
    return config