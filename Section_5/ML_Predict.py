import pandas as pd 
import json 

model_metadata = json.loads('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/model_results.json')

# converting json dataset from dictionary to dataframe
available_models = pd.DataFrame.from_dict(model_metadata, orient='index')
available_models.reset_index(level=0, inplace=True)