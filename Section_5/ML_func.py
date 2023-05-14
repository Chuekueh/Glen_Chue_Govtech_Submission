import os
import pickle
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import f1_score, make_scorer, precision_score, recall_score, hamming_loss

def encode_categorical(X, y, label_encoder_path, mode):
    # Perform one-hot encoding on categorical columns
    if mode == 'train':
        label_encoder = LabelEncoder()
        X['buying'] = label_encoder.fit_transform(X['buying'])
        X['maint'] = label_encoder.fit_transform(X['maint'])
        X['doors'] = label_encoder.fit_transform(X['doors'])
        X['persons'] = label_encoder.fit_transform(X['persons'])
        X['lug_boot'] = label_encoder.fit_transform(X['lug_boot'])
        X['safety'] = label_encoder.fit_transform(X['safety'])
        
        # Encode the target variable
        y_encoded = label_encoder.fit_transform(y)
        y_encoded = np.reshape(y_encoded, (-1,))

        #Save Models
        with open(label_encoder_path, 'wb') as file:
            pickle.dump(label_encoder, file)

        return X, y_encoded
    
    else :
        # Open Encoders
    
        with open(label_encoder_path, 'rb') as file:
            label_encoder = pickle.load(file)
        
        X['buying'] = label_encoder.fit_transform(X['buying'])
        X['maint'] = label_encoder.fit_transform(X['maint'])
        X['doors'] = label_encoder.fit_transform(X['doors'])
        X['persons'] = label_encoder.fit_transform(X['persons'])
        X['lug_boot'] = label_encoder.fit_transform(X['lug_boot'])
        X['safety'] = label_encoder.fit_transform(X['safety'])

        y_encoded = label_encoder.transform(y)
        y_encoded = np.reshape(y_encoded, (-1,))
    
        return X, y_encoded
    
def find_best_random_forest(X, y, dir_path, seed):
    # Define the parameter grid for Random Forest
    param_grid = {
        'n_estimators': [100, 200, 300],  # Number of trees in the forest
        'max_depth': [2, 10, 15],       # Maximum depth of each tree
        'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split an internal node
        'min_samples_leaf': [1, 2, 4]     # Minimum number of samples required to be at a leaf node
    }
    
    # Create a Random Forest classifier with random seed for stability
    rf_classifier = RandomForestClassifier(random_state=seed)
    
    # Define the scoring metric (f1_score in this case)
    # Define the scoring metrics
    scoring_metrics = {
        make_scorer(recall_score, average='macro')
    }
    
    # Perform grid search to find the best configuration 
    grid_search = GridSearchCV(rf_classifier, param_grid, cv=3, scoring=scoring_metrics) ## CV = 3 to improve robustness of results
    grid_search.fit(X, y)
    
    # Get the best model and its parameters
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    #Write the Log of the Grid Search to a file called ML_training.log in the current dir 
    with open(f"{dir_path}/ML_training_RF_{seed}.log", "w") as file:
        file.write("Parameter Grid:\n")
        file.write(str(grid_search.param_grid) + "\n\n")
        file.write("CV Results:\n")
        results = grid_search.cv_results_
        for i, params in enumerate(results['params']):
            file.write(f"Parameters: {params}\n")
            file.write(f"Mean F1 Score: {results['mean_test_f1_score'][i]}\n")
            file.write(f"Mean Precision: {results['mean_test_precision'][i]}\n")
            file.write(f"Mean Recall: {results['mean_test_recall'][i]}\n")
            file.write(f"Mean Hamming Loss: {results['mean_test_hamming_loss'][i]}\n")
        
        file.write("Best Parameters:\n")
        file.write(str(best_params) + "\n")
        file.write("Best Score:\n")
        file.write(str(best_score))
    
    # Fit the best model on the entire dataset
    best_model.fit(X, y)
    
    # Print the best parameters
    print("Best Parameters:", best_params)

    return best_model, best_params, best_score

def find_best_svm_model(X, y, dir_path, seed):
    # Set the random seed
    np.random.seed(seed)

    # Define the SVM classifier
    svm = SVC()

    # Define the parameter grid
    param_grid = {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf'],
        'gamma': [0.1, 1, 10]
    }

    scoring_metrics = {
        make_scorer(recall_score, average='macro')
    }

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(svm, param_grid, cv=3, scoring=scoring_metrics)
    grid_search.fit(X, y)

    # Get the best SVM model
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    #Write the Log of the Grid Search to a file called ML_training.log in the current dir 
    with open(f"{dir_path}/ML_training_SVM_{seed}.log", "w") as file:
        file.write("Parameter Grid:\n")
        file.write(str(grid_search.param_grid) + "\n\n")
        file.write("CV Results:\n")
        results = grid_search.cv_results_
        for i, params in enumerate(results['params']):
            file.write(f"Parameters: {params}\n")
            file.write(f"Mean F1 Score: {results['mean_test_f1_score'][i]}\n")
            file.write(f"Mean Precision: {results['mean_test_precision'][i]}\n")
            file.write(f"Mean Recall: {results['mean_test_recall'][i]}\n")
            file.write(f"Mean Hamming Loss: {results['mean_test_hamming_loss'][i]}\n")
        
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

    with open(label_encoder_path, 'rb') as file:
        label_encoder = pickle.load(file)
    
    return model, label_encoder
