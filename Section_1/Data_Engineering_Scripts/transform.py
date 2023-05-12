import pandas as pd 
from constants import *
from utils import process_dob, is_18_years_old, succesful_application

# obtain ingested data that was processed within the same hour 
raw_data = pd.read_csv(f'{INGEST_DIR}/{INGEST_FILE}')

# Standardise Datetime format

raw_data['date_of_birth'] = raw_data['date_of_birth'].apply(process_dob)
raw_data['above_18'] = raw_data['date_of_birth'].apply(is_18_years_old)
raw_data['succesful'] = raw_data.apply(succesful_application, axis=1)


print('Done')

