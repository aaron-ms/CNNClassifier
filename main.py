from CNNClassifier.pipeline import DataIngestionTrainingPipeline
from CNNClassifier.pipeline import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline import ModelTrainingPipeline
from CNNClassifier.pipeline import EvaluationPipeline
from CNNClassifier import logger

STAGE_NAME = "Data Ingestion Stage."

try:
    logger.info(f">>>>> stage {STAGE_NAME} started. <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed. <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model."

try:
    logger.info(f"*******************************")
    logger.info(f">>>>> stage {STAGE_NAME} started. <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed. <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed. <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage {STAGE_NAME} Started. <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed. <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
