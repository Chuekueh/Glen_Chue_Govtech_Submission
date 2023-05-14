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

data['buying'] = label_encoder.fit_transform(data['buying'])
data['maint'] = label_encoder.fit_transform(data['maint'])
data['doors'] = label_encoder.fit_transform(data['doors'])
data['persons'] = label_encoder.fit_transform(data['persons'])
data['lug_boot'] = label_encoder.fit_transform(data['lug_boot'])
data['safety'] = label_encoder.fit_transform(data['safety'])

Predicted_buying_price = predict_with_model(data, prediction_model)

print(f"The predicted buying price is {Predicted_buying_price}")