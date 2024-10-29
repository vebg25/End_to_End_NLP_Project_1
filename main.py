from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME="DATA INGESTION PIPELINE"

try:
  logger.info(f"{STAGE_NAME} initiated")
  data_ingestion_training_pipeline=DataIngestionTrainingPipeline()
  data_ingestion_training_pipeline.initiate_data_ingestion()
  logger.info(f"Stage {STAGE_NAME} completed")

except Exception as e:
  raise e

STAGE_NAME="DATA TRANSFORMATION PIPELINE"

try:
  logger.info(f"{STAGE_NAME} initiated")
  data_transformation_training_pipeline=DataTransformationPipeline()
  data_transformation_training_pipeline.initiate_data_transformation()
  logger.info(f"Stage {STAGE_NAME} completed")

except Exception as e:
  raise e