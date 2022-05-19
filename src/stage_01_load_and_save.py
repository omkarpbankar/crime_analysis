import pandas as pd
import argparse 
from src.utils.common_utils import read_params
import logging

def get_data(config_path:str):
    config = read_params(config_path)
    print(config)
    return None


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default="params.yaml")
    parsed_args = args.parse_args()

    try:
        data = get_data(config_path=parsed_args.config)
    except Exception as e:
        raise e
