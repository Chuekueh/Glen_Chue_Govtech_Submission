import pandas as pd 
import numpy as np
from datetime import datetime

#Loading in Input Data 
input_data = pd.read_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/Input Data/applications_dataset_1.csv')

#Creating Additional Column for preprocessing 
input_data['first_name'] = ""
input_data['last_name'] = ""
input_data['above_18'] = False 
input_data['membership_id'] = ""
input_data['succesful'] = False
input_data['processed_time'] = datetime.now().strftime('%y%m%d%H')

#Standardise Order of Columns
ingested_data = input_data[['membership_id','first_name','last_name','name','email','date_of_birth',
                            'mobile_no','above_18','succesful','processed_time']]

ingested_data.to_csv(f"/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_1/DE_Pipeline_Data/Ingested_Data/data_batch_{datetime.now().strftime('%Y%m%d%H')}")
print("Done")