from datetime import datetime

ARCHIVE_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Archive'
INPUT_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Input_Data'
EXTRACT_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Extracted_Data'
TRANSFORM_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Transformed_data'
SUCCESFUL_LOAD_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Successful_Applications'
UNSUCCESFUL_LOAD_DIR = '~/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Unsuccessful_Applications'

EXTRACT_FILE = f"data_batch_{datetime.now().strftime('%Y%m%d%H')}.csv"

column_data_types = {
        'membership_id':'str',
        'first_name':'str',
        'last_name': 'str',
        'email': 'str',
        'date_of_birth': 'str',
        'mobile_no': 'str',
        'above_18': 'bool'
    }
