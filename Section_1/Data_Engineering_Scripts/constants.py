from datetime import datetime

INPUT_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Input_Data'
INGEST_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Ingested_Data'
LOAD_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Load_data'
TRANSFORM_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Transformed_data'


INGEST_FILE = f"data_batch_{datetime.now().strftime('%Y%m%d%H')}.csv"
SUCESS_TRANSFORM_FILE = f"transformed_data_batch_succesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
UNSUCESSFUL_TRANSFORM_FILE = f"transformed_data_batch_unsuccesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
