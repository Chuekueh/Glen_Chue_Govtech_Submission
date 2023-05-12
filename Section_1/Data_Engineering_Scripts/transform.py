import pandas as pd 
from constants import *
from utils import process_dob, is_18_years_old, succesful_application

# obtain ingested data that was processed within the same hour 
raw_data = pd.read_csv(f'{INGEST_DIR}/{INGEST_FILE}')

# Preprocessing Steps
raw_data['date_of_birth'] = raw_data['date_of_birth'].apply(process_dob)
raw_data['above_18'] = raw_data['date_of_birth'].apply(is_18_years_old)
raw_data['succesful'] = raw_data.apply(succesful_application, axis=1)
raw_data['first_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[0])
raw_data['last_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[1])

#Split into Successful and Unsuccesful appplicants 
succesful_applicants = raw_data[['membership_id','first_name','last_name','email','date_of_birth',
                            'mobile_no','above_18','succesful','processed_time']]

print('Done')

