from CNNClassifier.pipeline import DataIngestionTrainingPipeline
from CNNClassifier import logger

STAGE_NAME = "Data Ingestion stage."

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed. <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e