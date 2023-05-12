from datetime import datetime

INPUT_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Input_Data'
EXTRACT_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Extracted_Data'
TRANSFORM_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Transformed_data'
SUCCESFUL_LOAD_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Successful_Applications'
UNSUCCESFUL_LOAD_DIR = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Unuccessful_Applications'

EXTRACT_FILE = f"data_batch_{datetime.now().strftime('%Y%m%d%H')}.csv"
SUCESS_TRANSFORM_FILE = f"transformed_data_batch_succesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
UNSUCESSFUL_TRANSFORM_FILE = f"transformed_data_batch_unsuccesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
SUCESS_LOAD_FILE = f"final_data_batch_succesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
UNSUCESSFUL_LOAD_FILE = f"final_data_batch_unsuccesful_{datetime.now().strftime('%Y%m%d%H')}.csv"
