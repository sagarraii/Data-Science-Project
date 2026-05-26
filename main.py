from src.datascience.logging.logger import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
        raise 


STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.initiate_data_validation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
        logger.info(e)
        raise e