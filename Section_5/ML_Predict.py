import pandas as pd 
import json 
from ML_func import *
import numpy as np

# Read the contents of the JSON file
with open('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/model_results.json') as file:
    json_data = file.read()

model_metadata = json.loads(json_data)

# converting json dataset from dictionary to dataframe
available_models = pd.DataFrame.from_dict(model_metadata, orient='index')

# Select Best model Based on Prediction (Want to prioritize true positives)
prediction_model, label_encoder = select_model(available_models, 'precision')

# Define Input Data and Carry our prediction
input_data = {'maint': 'High',
              'doors': 4,
              'persons': 'missing',
              'lug_boot': 'big',
              'safety':'high',
              'class':'good'}

data = pd.DataFrame(input_data)

ML_input_data = encoder.transform(data)

Predicted_buying_price = predict_with_model(ML_input_data, prediction_model)

print(f"The predicted buying price is {Predicted_buying_price}")