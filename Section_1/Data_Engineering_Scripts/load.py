import pandas as pd 
from constants import *
from utils import enforce_data_types

succesful_applicants = pd.read_csv(f"{TRANSFORM_DIR}/{SUCESS_TRANSFORM_FILE}")
unsuccesful_applicants = pd.read_csv(f"{TRANSFORM_DIR}/{UNSUCESSFUL_TRANSFORM_FILE}")

column_data_types = {
    'membership_id':'str',
    'first_name':'str',
    'last_name': 'str',
    'email': 'str',
    'date_of_birth': 'str',
    'mobile_no': 'str',
    'above_18': 'bool'
}

succesful_applicants = enforce_data_types(succesful_applicants, column_data_types)
unsuccesful_applicants = enforce_data_types(unsuccesful_applicants, column_data_types)

succesful_applicants.to_csv(f"{SUCCESFUL_LOAD_DIR}/{SUCESS_LOAD_FILE}")
unsuccesful_applicants.to_csv(f"{UNSUCCESFUL_LOAD_DIR}/{UNSUCESSFUL_LOAD_FILE}")

print('done')