import pandas as pd 
import numpy as np
from datetime import datetime
from constants import *
from utils import add_in_cols

def data_ingestion ():
    #Loading in Input Data 
    input_data = pd.read_csv(f'{INPUT_DIR}/applications_dataset_1.csv')

    #Creating Additional Column for preprocessing 
    processed_input_data = add_in_cols(input_data)

    #Standardise Order of Columns
    ingested_data = processed_input_data[['membership_id','first_name','last_name','name','email','date_of_birth',
                                'mobile_no','above_18','is_succesful',]]

    ingested_data.to_csv(f"{EXTRACT_DIR}/data_batch_{datetime.now().strftime('%Y%m%d%H')}.csv", index=False)

    print(f"{len(ingested_data)} data points sucessfully ingested at {datetime.now().strftime('%Y/%m/%d %H')} hrs")

if __name__ == "__main__":
    try:
        data_ingestion ()
    except Exception as e: 
        print ("WARNING Data not successfully ingested")
        print(e)
