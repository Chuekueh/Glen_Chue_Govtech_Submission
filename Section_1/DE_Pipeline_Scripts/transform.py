import os
import pandas as pd 
from constants import *
from utils import process_dob, is_18_years_old, succesful_application, generate_membership_id

def data_transform():
    # obtain ingested data that was processed within the same hour 
    
    files = [os.path.join(EXTRACT_DIR, f) for f in os.listdir(EXTRACT_DIR) if os.path.isfile(os.path.join(EXTRACT_DIR, f))]

    for file in files:
        try:
            print(f"Beginning Data Transformation for {file}")
            raw_data = pd.read_csv(file)
            # Preprocessing Steps
            print(f"Beginning date_of_birth Column Transformation")
            raw_data['date_of_birth'] = raw_data['date_of_birth'].apply(process_dob)

            print(f"Beginning above_18 Column Transformation")
            raw_data['above_18'] = raw_data['date_of_birth'].apply(is_18_years_old)

            print(f"Beginning succesful Column Transformation")
            raw_data['is_succesful'] = raw_data.apply(succesful_application, axis=1)

            print(f"Beginning first_name Column Transformation")
            raw_data['first_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[0])

            print(f"Beginning last_name Column Transformation")
            raw_data['last_name'] = raw_data['email'].apply(lambda x:x.split('@')[0].split('_')[1])

            # Split into Successful and Unsuccesful appplicants 
            print(f"Splitting Dataset into Succesful and Unsuccesful applicants")
            succesful_applicants = raw_data[raw_data['succesful'] == True][['membership_id','first_name','last_name','email','date_of_birth',
                                        'mobile_no','above_18']]
            print(f"There are a total of {len(succesful_applicants)} succesful applicants in this batch")
            unsuccesful_applicants = raw_data[raw_data['succesful'] == False][['membership_id','first_name','last_name','email','date_of_birth',
                                        'mobile_no','above_18']]
            print(f"There are a total of {len(unsuccesful_applicants)} unsuccesful applicants in this batch")

            # Generate Membership ID for succesful applicants only
            print(f"Generating Membership ID for Succesful Applicants")
            succesful_applicants['membership_id'] = succesful_applicants.apply(generate_membership_id, axis=1)

            # Write to relevant folders
            print(f"Saving transformed succesful applicants data to {TRANSFORM_DIR}/{os.path.basename(file)}_successful_applicants_transformed")
            succesful_applicants.to_csv(f"{TRANSFORM_DIR}/{os.path.basename(file)}_successful_applicants_transformed", index=False)
            print(f"Saving transformed unuccesful applicants to {TRANSFORM_DIR}/{os.path.basename(file)}_unsuccessful_applicants_transformed", index=False)
            unsuccesful_applicants.to_csv(f"{TRANSFORM_DIR}/{os.path.basename(file)}_unsuccessful_applicants_transformed")

            print('Data Batch Succesfully Transformed')

            os.remove(file)
            print(f"Removed {file} as successfully transformed")

        except Exception as e:
            return e

if __name__ == "__main__":
    data_transform ()

