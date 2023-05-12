import pandas as pd 
from constants import *
from utils import enforce_data_types

print(f"Preparing data from {TRANSFORM_DIR}/{SUCESS_TRANSFORM_FILE} and {TRANSFORM_DIR}/{UNSUCESSFUL_TRANSFORM_FILE} for Loading")
succesful_applicants = pd.read_csv(f"{TRANSFORM_DIR}/{SUCESS_TRANSFORM_FILE}")
unsuccesful_applicants = pd.read_csv(f"{TRANSFORM_DIR}/{UNSUCESSFUL_TRANSFORM_FILE}")

print("Enforcing Datatypes")
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

print(f"Saving cleaned succesful applicants data to {SUCCESFUL_LOAD_DIR}/{SUCESS_LOAD_FILE}")
succesful_applicants.to_csv(f"{SUCCESFUL_LOAD_DIR}/{SUCESS_LOAD_FILE}")
print(f"Saving cleaned succesful applicants data to {UNSUCCESFUL_LOAD_DIR}/{UNSUCESSFUL_LOAD_FILE}")
unsuccesful_applicants.to_csv(f"{UNSUCCESFUL_LOAD_DIR}/{UNSUCESSFUL_LOAD_FILE}")

print('done')