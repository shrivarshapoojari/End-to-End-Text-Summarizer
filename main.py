from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipline
logger.info("Welocome")
STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME}completed<<<<<<<<<<<<<")
except Exception as e:
   logger.exception(e)
   raise e

logger.info("Welocome")
STAGE_NAME="Data Validation stage"

try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<<")
    data_validation=DataValidationTrainingPipline()
    data_validation.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME}completed<<<<<<<<<<<<<")
except Exception as e:
   logger.exception(e)
   raise e