import os
from src.datascience.logging.logger import logging
from sklearn.model_selection import train_test_split

from src.datascience.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logging.info("Splited data into train and test sets")
        logging.info(f"train data shape {train.shape}")
        logging.info(f"test data shape {test.shape}")
        
        print(train.shape)
        print(test.shape)