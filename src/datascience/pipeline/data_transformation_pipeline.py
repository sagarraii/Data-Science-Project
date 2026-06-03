from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.logging.logger import logger
from pathlib import Path
STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
        
    def initiate_data_transformation(self):
        try:
            with open (Path("artifacts/data_validation/status.yaml"), "r") as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("data schema is not valid")
        except Exception as e:
                print(e)

'''
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.initiate_data_transformation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.info(e)
        raise e
        '''
