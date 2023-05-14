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
input_data = {'maint': 'high',
              'doors': '4',
              'persons': 'missing',
              'lug_boot': 'big',
              'safety':'high',
              'class':'good'}

X = pd.DataFrame(input_data, index=[0])

X['class'] = X['class'].map({'unacc':0, 'acc':1, 'good':2, 'vgood':3})
X['maint'] = X['maint'].map({'low':0, 'med':1, 'high':2, 'vhigh':3})
X['doors'] = X['doors'].map({'2':0, '3':1, '4':2, '5more':3})
X['persons'] = X['persons'].map({'2':1, '4':2, 'more':3,'missing':0})
X['lug_boot'] = X['lug_boot'].map({'small':0, 'med':1, 'big':2})
X['safety'] = X['safety'].map({'low':0, 'med':1, 'high':2})

Predicted_buying_price = label_encoder.inverse_transform(predict_with_model(X, prediction_model))[0]

print(f"The predicted buying price is {Predicted_buying_price}.")