import pandas as pd 
import numpy as np
from datetime import datetime
from constants import *
from utils import add_in_cols
import os

def data_extraction ():
    #Loading in Input Data 
    input_data = pd.DataFrame(columns=['date_of_birth', 'mobile_no', 'name', 'email'])

    files = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]

    for file in files:
        try:
            data = pd.read_csv(file)
            input_data = pd.concat([input_data,data], ignore_index=True)

            #Creating Additional Column for preprocessing 
            processed_input_data = add_in_cols(input_data)

            #Standardise Order of Columns
            ingested_data = processed_input_data[['membership_id','first_name','last_name','name','email','date_of_birth',
                                        'mobile_no','above_18','is_succesful']]

            ingested_data.to_csv(f"{EXTRACT_DIR}/data_batch_{datetime.now().strftime('%Y%m%d%H')}.csv", index=False)

            print(f"{len(ingested_data)} data points sucessfully ingested at {datetime.now().strftime('%Y/%m/%d %H')} hrs")

            os.remove(file)
            print(f"Removed {file} as successfully extracted")

        except Exception as e: 
            print(e)

if __name__ == "__main__":
    data_extraction ()