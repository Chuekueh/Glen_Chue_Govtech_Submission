import pandas as pd 
from constants import *
from utils import process_dob, is_18_years_old, succesful_application, generate_membership_id

# obtain ingested data that was processed within the same hour 
raw_data = pd.read_csv(f'{INGEST_DIR}/{INGEST_FILE}')

# Preprocessing Steps
raw_data['date_of_birth'] = raw_data['date_of_birth'].apply(process_dob)
raw_data['above_18'] = raw_data['date_of_birth'].apply(is_18_years_old)
raw_data['succesful'] = raw_data.apply(succesful_application, axis=1)
raw_data['first_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[0])
raw_data['last_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[1])

# Split into Successful and Unsuccesful appplicants 
succesful_applicants = raw_data[raw_data['succesful'] == True][['membership_id','first_name','last_name','email','date_of_birth',
                            'mobile_no','above_18']]
unsuccesful_applicants = raw_data[raw_data['succesful'] == False][['membership_id','first_name','last_name','email','date_of_birth',
                            'mobile_no','above_18']]

# Generate Membership ID for succesful applicants only
succesful_applicants['membership_id'] = succesful_applicants.apply(generate_membership_id, axis=1)

# Write to relevant folders
succesful_applicants.to_csv(f"{TRANSFORM_DIR}/{SUCESS_TRANSFORM_FILE}")
unsuccesful_applicants.to_csv(f"{TRANSFORM_DIR}/{UNSUCESSFUL_TRANSFORM_FILE}")

print('Done')

