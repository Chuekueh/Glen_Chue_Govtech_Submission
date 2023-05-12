import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelBinarizer


car_data = pd.read_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/car_data.csv', names = 
                       ['buying','maint','doors','persons','lug_boot','safety','class'])

#Set Index to preserve order of rows:
car_data['row_num'] = np.arange(len(car_data))
car_data['row_num'] = car_data.reset_index().index

# Non-dummified Dataset 
non_dummy = car_data
non_dummy.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/non_dummy.csv', header=True)

#Create Dummified Dataset for Experimentation 
## Pandas get dummies 
pandas_dummy = pd.get_dummies(car_data,
                     columns = ['maint','doors','persons','lug_boot','safety','class',])
pandas_dummy.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/pandas_dummy.csv', header=True)

print('done')

