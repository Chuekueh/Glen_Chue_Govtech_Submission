import os
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import f1_score, make_scorer, precision_score, recall_score

def encode_categorical(X,y, label_encoder_path, encoder_path):
    x_categorical_cols = ['maint','doors','persons','lug_boot','safety','class']
    # Perform one-hot encoding on categorical columns
    encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    X_encoded = pd.DataFrame(encoder.fit_transform(X[x_categorical_cols]))

    # Reassign the encoded categorical columns to the original DataFrame
    X_encoded.columns = encoder.get_feature_names(x_categorical_cols)
    
    # Encode the target variable
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    y_encoded = np.reshape(y_encoded, (-1,))

    #Save Models
    with open(encoder_path, 'wb') as file:
        pickle.dump(encoder, file)
    
    with open(label_encoder_path, 'wb') as file:
        pickle.dump(label_encoder, file)
    
    return X_encoded, y_encoded


def find_best_random_forest(X, y, dir_path):
    # Define the parameter grid for Random Forest
    param_grid = {
        'n_estimators': [100, 200, 300],  # Number of trees in the forest
        'max_depth': [None, 5, 10],       # Maximum depth of each tree
        'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split an internal node
        'min_samples_leaf': [1, 2, 4]     # Minimum number of samples required to be at a leaf node
    }
    
    # Create a Random Forest classifier with random seed for stability
    rf_classifier = RandomForestClassifier(random_state=42)
    
    # Define the scoring metric (f1_score in this case)
    # Define the scoring metrics
    scoring_metrics = {
        'precision': make_scorer(precision_score, average='weighted'),
        'recall': make_scorer(recall_score, average='weighted'),
        'f1_score': make_scorer(f1_score, average='weighted'),
    }
    
    # Perform grid search to find the best configuration 
    grid_search = GridSearchCV(rf_classifier, param_grid, cv=3, scoring=scoring_metrics, refit='f1_score') ## CV = 3 to improve robustness of results
    grid_search.fit(X, y)
    
    # Get the best model and its parameters
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    #Write the Log of the Grid Search to a file called ML_training.log in the current dir 
    with open(f"{dir_path}/ML.training_log", "w") as file:
        file.write("Parameter Grid:\n")
        file.write(str(grid_search.param_grid) + "\n\n")
        file.write("CV Results:\n")
        results = grid_search.cv_results_
        for i, params in enumerate(results['params']):
            file.write(f"Parameters: {params}\n")
            file.write(f"Mean F1 Score: {results['mean_test_f1_score'][i]}\n")
            file.write(f"Mean Precision: {results['mean_test_precision'][i]}\n")
            file.write(f"Mean Recall: {results['mean_test_recall'][i]}\n")
        
        file.write("Best Parameters:\n")
        file.write(str(best_params) + "\n")
        file.write("Best Score:\n")
        file.write(str(best_score))
    
    # Fit the best model on the entire dataset
    best_model.fit(X, y)
    
    # Print the best parameters
    print("Best Parameters:", best_params)

    return best_model, best_params, best_score

def evaluate_model(X_test, y_test, model):
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    return precision, recall, f1

def predict_with_model(X, model):
    # Make predictions using the best model
    predictions = model.predict(X)
    
    return predictions

def select_model(df, criteria):
    max_index = df[criteria].idxmax()

    model_path = df.loc[max_index].index
    encoder_path = df.loc[max_index].encoder
    label_encoder_path = df.loc[max_index].label_encoder

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    with open(encoder_path, 'rb') as file:
        encoder = pickle.load(file)

    with open(label_encoder_path, 'rb') as file:
        label_encoder = pickle.load(file)
    
    return model, encoder, label_encoder
